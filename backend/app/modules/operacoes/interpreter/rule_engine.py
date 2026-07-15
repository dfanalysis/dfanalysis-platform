from app.modules.operacoes.interpreter.base import (
    InterpreterEngine,
    InterpreterResult,
)
from app.modules.operacoes.inbox.models import InboxMessage


class RuleEngine(InterpreterEngine):
    """
    Estratégia baseada em regras determinísticas.
    """

    def interpret(
        self,
        message: InboxMessage,
    ) -> InterpreterResult:

        payload: dict = {}

        assunto = message.assunto.lower()

        if "oncologia" in assunto:
            payload["tipo_processo"] = "REPASSE_ONCOLOGIA"

        elif "retaguarda" in assunto:
            payload["tipo_processo"] = "RETAGUARDA_PA"

        elif "visitas" in assunto:
            payload["tipo_processo"] = "VISITAS"

        else:
            return InterpreterResult(
                success=False,
                confidence=0.0,
                payload={},
            )

        return InterpreterResult(
            success=True,
            confidence=0.95,
            payload=payload,
        )
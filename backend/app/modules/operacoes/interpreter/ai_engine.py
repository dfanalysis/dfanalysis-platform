from app.modules.operacoes.interpreter.base import (
    InterpreterEngine,
    InterpreterResult,
)
from app.modules.operacoes.inbox.models import InboxMessage


class AIEngine(InterpreterEngine):
    """
    Placeholder para interpretação baseada em IA.
    """

    def interpret(
        self,
        message: InboxMessage,
    ) -> InterpreterResult:

        return InterpreterResult(
            success=False,
            confidence=0.0,
            payload={},
        )
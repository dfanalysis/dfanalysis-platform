from app.modules.operacoes.interpreter.ai_engine import AIEngine
from app.modules.operacoes.interpreter.base import (
    InterpreterResult,
)
from app.modules.operacoes.interpreter.rule_engine import (
    RuleEngine,
)
from app.modules.operacoes.inbox.models import InboxMessage


class CommunicationInterpreter:
    """
    Orquestra os mecanismos de interpretação da plataforma.
    """

    def __init__(self) -> None:
        self.rule_engine = RuleEngine()
        self.ai_engine = AIEngine()

    def interpret(
        self,
        message: InboxMessage,
    ) -> InterpreterResult:

        result = self.rule_engine.interpret(message)

        if result.success:
            return result

        return self.ai_engine.interpret(message)
from sqlalchemy.orm import Session

from app.modules.operacoes.interpreter.enums import (
    MetodoInterpretacao,
    StatusInterpretacao,
)
from app.modules.operacoes.interpreter.models import (
    CommunicationInterpretation,
)
from app.modules.operacoes.interpreter.repository import (
    CommunicationInterpretationRepository,
)
from app.modules.operacoes.interpreter.service import (
    CommunicationInterpreter,
)
from app.modules.operacoes.inbox.models import InboxMessage


class InterpretCommunication:
    """
    Executa a interpretação de uma comunicação e persiste o resultado.
    """

    def __init__(self, db: Session) -> None:
        self.db = db
        self.repository = CommunicationInterpretationRepository(db)
        self.interpreter = CommunicationInterpreter()

    def execute(
        self,
        message: InboxMessage,
    ) -> CommunicationInterpretation:

        result = self.interpreter.interpret(message)

        interpretation = CommunicationInterpretation(
            message_id=message.id,
            metodo=(
                MetodoInterpretacao.REGRA
                if result.success
                else MetodoInterpretacao.IA
            ),
            status=(
                StatusInterpretacao.GERADA
                if result.success
                else StatusInterpretacao.AGUARDANDO_REVISAO
            ),
            confianca=result.confidence,
            necessita_revisao=not result.success,
            resultado=result.payload,
            engine=(
                "RuleEngine"
                if result.success
                else "AIEngine"
            ),
            sequencia=self.repository.get_next_sequence(
                message.id,
            ),
            interpretado_em=message.recebido_em,
        )

        return self.repository.add(
            interpretation,
        )
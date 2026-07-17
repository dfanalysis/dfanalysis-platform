from sqlalchemy.orm import Session

from app.modules.operacoes.cases.enums import (
    StatusOperationalCase,
    TipoOperationalCase,
)
from app.modules.operacoes.cases.models import OperationalCase
from app.modules.operacoes.cases.repository import (
    OperationalCaseRepository,
)
from app.modules.operacoes.interpreter.models import (
    CommunicationInterpretation,
)


class OpenOperationalCase:
    """
    Abre oficialmente um processo operacional.

    Um Case nasce sempre a partir de uma
    CommunicationInterpretation.
    """

    def __init__(
        self,
        db: Session,
    ) -> None:
        self.db = db
        self.repository = OperationalCaseRepository(db)

    def execute(
        self,
        interpretation: CommunicationInterpretation,
        numero: str,
        tipo: TipoOperationalCase,
    ) -> OperationalCase:

        case = OperationalCase(
            numero=numero,
            tipo=tipo,
            status=StatusOperationalCase.ABERTO,
            communication_id=interpretation.message_id,
        )

        return self.repository.add(case)
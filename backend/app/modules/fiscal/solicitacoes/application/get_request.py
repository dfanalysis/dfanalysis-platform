from uuid import UUID

from sqlalchemy.orm import Session

from app.modules.fiscal.solicitacoes.models import SolicitacaoEmissao
from app.modules.fiscal.solicitacoes.repository import (
    SolicitacaoEmissaoRepository,
)


class GetEmissionRequest:
    """
    Recupera uma solicitação de emissão pelo seu identificador.
    """

    def __init__(
        self,
        db: Session,
        repository: SolicitacaoEmissaoRepository | None = None,
    ) -> None:
        self.repository = (
            repository
            if repository is not None
            else SolicitacaoEmissaoRepository(db)
        )

    def execute(
        self,
        solicitacao_id: UUID,
    ) -> SolicitacaoEmissao | None:
        return self.repository.get_by_id(
            solicitacao_id,
        )
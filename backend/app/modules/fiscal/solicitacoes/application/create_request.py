from sqlalchemy.orm import Session

from app.modules.empresas.repository import EmpresaRepository
from app.modules.fiscal.solicitacoes.domain.services import (
    FiscalDomainService,
)
from app.modules.fiscal.solicitacoes.models import SolicitacaoEmissao
from app.modules.fiscal.solicitacoes.repository import (
    SolicitacaoEmissaoRepository,
)
from app.modules.fiscal.solicitacoes.schemas import (
    SolicitacaoEmissaoCreate,
)


class CreateEmissionRequest:
    """Caso de uso responsável por criar uma solicitação de emissão."""

    def __init__(self, db: Session) -> None:
        self.db = db
        self.empresa_repository = EmpresaRepository(db)
        self.solicitacao_repository = SolicitacaoEmissaoRepository(db)

    def execute(
        self,
        payload: SolicitacaoEmissaoCreate,
    ) -> tuple[SolicitacaoEmissao, bool]:
        """
        Cria uma solicitação de emissão.

        Lança uma exceção quando a chave de idempotência já tiver sido utilizada.
        """

        empresa = self.empresa_repository.get_by_id(
            payload.empresa_id,
        )

        FiscalDomainService.validar_empresa(empresa)

        if payload.idempotency_key:
            existing_request = (
                self.solicitacao_repository.get_by_idempotency_key(
                    payload.idempotency_key,
                )
            )

            FiscalDomainService.verificar_idempotencia(
                existing_request,
            )

        solicitacao = SolicitacaoEmissao(
            empresa_id=payload.empresa_id,
            origem=payload.origem,
            referencia_externa=payload.referencia_externa,
            idempotency_key=payload.idempotency_key,
            competencia=payload.competencia,
            descricao_servico=payload.descricao_servico,
            valor_servico=payload.valor_servico,
        )

        return self.solicitacao_repository.add(solicitacao), True
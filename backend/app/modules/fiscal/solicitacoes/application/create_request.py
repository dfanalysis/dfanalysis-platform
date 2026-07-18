from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.modules.empresas.repository import EmpresaRepository
from app.modules.fiscal.solicitacoes.application.factory import (
    SolicitacaoFactory,
)
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

    def __init__(
        self,
        db: Session,
        empresa_repository: EmpresaRepository | None = None,
        solicitacao_repository: SolicitacaoEmissaoRepository | None = None,
        factory: SolicitacaoFactory | None = None,
    ) -> None:
        self.db = db

        self.empresa_repository = (
            empresa_repository
            if empresa_repository is not None
            else EmpresaRepository(db)
        )

        self.solicitacao_repository = (
            solicitacao_repository
            if solicitacao_repository is not None
            else SolicitacaoEmissaoRepository(db)
        )

        self.factory = (
            factory
            if factory is not None
            else SolicitacaoFactory()
        )

    def execute(
        self,
        payload: SolicitacaoEmissaoCreate,
    ) -> tuple[SolicitacaoEmissao, bool]:
        """
        Cria e persiste uma solicitação de emissão.

        Retorna:
            tuple[SolicitacaoEmissao, bool]:
                A solicitação criada e o indicador de criação.

        Lança:
            Exceções de domínio quando a empresa ou os dados forem inválidos.
            SQLAlchemyError quando ocorrer falha de persistência.
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

        solicitacao = self.factory.create(payload)

        try:
            solicitacao = self.solicitacao_repository.add(
                solicitacao,
            )

            self.db.commit()
            self.db.refresh(solicitacao)

            return solicitacao, True

        except SQLAlchemyError:
            self.db.rollback()
            raise
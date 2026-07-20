from uuid import UUID

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.modules.fiscal.enums import StatusSolicitacao
from app.modules.fiscal.solicitacoes.domain.services import (
    FiscalDomainService,
)
from app.modules.fiscal.solicitacoes.exceptions import (
    CompetenciaInvalidaError,
    DescricaoServicoInvalidaError,
    SolicitacaoNaoEncontradaError,
    ValorServicoInvalidoError,
)
from app.modules.fiscal.solicitacoes.models import SolicitacaoEmissao
from app.modules.fiscal.solicitacoes.repository import (
    SolicitacaoEmissaoRepository,
)


class ValidateEmissionRequest:
    """
    Caso de uso responsável por validar uma solicitação de emissão
    já persistida e movimentá-la no ciclo de vida fiscal.
    """

    def __init__(
        self,
        db: Session,
        repository: SolicitacaoEmissaoRepository | None = None,
    ) -> None:
        self.db = db

        self.repository = (
            repository
            if repository is not None
            else SolicitacaoEmissaoRepository(db)
        )

    def execute(
        self,
        solicitacao_id: UUID,
    ) -> SolicitacaoEmissao:
        """
        Valida uma solicitação existente.

        Fluxo de sucesso:
            RECEBIDA -> EM_VALIDACAO -> VALIDADA

        Fluxo de rejeição:
            RECEBIDA -> EM_VALIDACAO -> REJEITADA
        """

        solicitacao = self.repository.get_by_id(
            solicitacao_id,
        )

        if solicitacao is None:
            raise SolicitacaoNaoEncontradaError(
                "Solicitação de emissão não encontrada.",
            )

        FiscalDomainService.alterar_status(
            solicitacao,
            StatusSolicitacao.EM_VALIDACAO,
        )

        try:
            FiscalDomainService.validar_competencia(
                solicitacao.competencia,
            )

            FiscalDomainService.validar_valor(
                solicitacao.valor_servico,
            )

            solicitacao.descricao_servico = (
                FiscalDomainService.validar_descricao(
                    solicitacao.descricao_servico,
                )
            )

        except (
            CompetenciaInvalidaError,
            ValorServicoInvalidoError,
            DescricaoServicoInvalidaError,
        ):
            FiscalDomainService.alterar_status(
                solicitacao,
                StatusSolicitacao.REJEITADA,
            )

            self._persistir(solicitacao)
            raise

        FiscalDomainService.alterar_status(
            solicitacao,
            StatusSolicitacao.VALIDADA,
        )

        self._persistir(solicitacao)

        return solicitacao

    def _persistir(
        self,
        solicitacao: SolicitacaoEmissao,
    ) -> None:
        """Persiste a alteração de estado em uma única transação."""

        try:
            self.repository.update(solicitacao)
            self.db.commit()
            self.db.refresh(solicitacao)

        except SQLAlchemyError:
            self.db.rollback()
            raise
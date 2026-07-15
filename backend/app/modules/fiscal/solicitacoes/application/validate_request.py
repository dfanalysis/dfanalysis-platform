from app.modules.fiscal.solicitacoes.domain.services import (
    FiscalDomainService,
)
from app.modules.fiscal.solicitacoes.schemas import (
    SolicitacaoEmissaoCreate,
)


class ValidateEmissionRequest:
    """
    Caso de uso responsável por validar uma solicitação de emissão
    antes que ela siga para as próximas etapas do fluxo fiscal.
    """

    @staticmethod
    def execute(
        payload: SolicitacaoEmissaoCreate,
    ) -> SolicitacaoEmissaoCreate:
        """
        Executa as validações do domínio fiscal.

        Neste estágio da plataforma são realizadas apenas validações
        independentes de integrações externas.

        Futuramente este caso de uso incorporará validações de
        instituições, contratos operacionais, documentos,
        estabelecimentos, regras tributárias e demais políticas
        do domínio.
        """

        FiscalDomainService.validar_competencia(
            payload.competencia,
        )

        FiscalDomainService.validar_valor(
            payload.valor_servico,
        )

        FiscalDomainService.validar_descricao(
            payload.descricao_servico,
        )

        return payload
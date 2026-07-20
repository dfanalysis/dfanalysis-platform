class SolicitacaoEmissaoError(Exception):
    """Exceção base do módulo de solicitações de emissão."""


class SolicitacaoNaoEncontradaError(SolicitacaoEmissaoError):
    """A solicitação de emissão não foi encontrada."""


class EmpresaNaoEncontradaError(SolicitacaoEmissaoError):
    """Empresa informada não foi encontrada."""


class EmpresaInativaError(SolicitacaoEmissaoError):
    """Empresa informada está inativa ou excluída."""


class TransicaoStatusInvalidaError(SolicitacaoEmissaoError):
    """A transição solicitada não é permitida pelo ciclo de vida."""


class IdempotencyConflictError(SolicitacaoEmissaoError):
    """A chave de idempotência já foi utilizada."""


class CompetenciaInvalidaError(SolicitacaoEmissaoError):
    """A competência informada não é válida para emissão."""


class ValorServicoInvalidoError(SolicitacaoEmissaoError):
    """O valor do serviço informado não é válido."""


class DescricaoServicoInvalidaError(SolicitacaoEmissaoError):
    """A descrição do serviço informada não é válida."""
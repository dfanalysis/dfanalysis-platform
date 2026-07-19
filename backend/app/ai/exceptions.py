class AIError(Exception):
    """Exceção base da infraestrutura de Inteligência Artificial."""


class AIConfigurationError(AIError):
    """Configuração obrigatória do provedor ausente ou inválida."""


class AIConnectionError(AIError):
    """Falha de comunicação com o provedor de IA."""


class AITimeoutError(AIError):
    """Tempo limite excedido durante a chamada ao provedor."""


class AIInvalidResponseError(AIError):
    """Resposta do provedor ausente, inválida ou fora do contrato."""


class PromptNotFoundError(AIError):
    """Prompt solicitado não foi encontrado."""

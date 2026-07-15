class InboxError(Exception):
    """Exceção base do domínio de Inbox."""


class TransicaoStatusInboxInvalidaError(InboxError):
    """A transição de status da mensagem não é permitida."""
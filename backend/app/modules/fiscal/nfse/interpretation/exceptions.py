class NFSeInterpretationError(Exception):
    """
    Exceção base da camada de interpretação da NFS-e.
    """


class InvalidNFSeDocumentError(NFSeInterpretationError):
    """
    Indica que o documento recebido não possui os dados mínimos
    necessários para ser interpretado como uma NFS-e.
    """


class UnsupportedNFSeDocumentError(NFSeInterpretationError):
    """
    Indica que o documento possui uma característica ainda não
    suportada pela camada de interpretação.
    """

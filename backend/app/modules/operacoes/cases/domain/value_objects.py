from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Competencia:
    """
    Representa a competência operacional do processo.
    """

    referencia: date


@dataclass(frozen=True)
class NumeroCase:
    """
    Identificador funcional do processo.
    """

    valor: str


@dataclass(frozen=True)
class OrigemCase:
    """
    Origem do processo operacional.
    """

    valor: str


@dataclass(frozen=True)
class ReferenciaExterna:
    """
    Identificador fornecido pelo sistema de origem.

    Exemplos:
    - Message-ID do e-mail
    - Número da fatura hospitalar
    - Código do ERP
    """

    valor: str
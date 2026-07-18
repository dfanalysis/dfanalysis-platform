from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class BusinessValidationResult:
    """
    Resultado de uma validação de domínio.

    A camada de domínio nunca retorna apenas True ou False.

    Ela informa também os motivos que impediram
    o processamento do documento.
    """

    valid: bool = True

    errors: list[str] = field(default_factory=list)

    def add_error(self, message: str) -> None:
        """
        Adiciona um erro de validação.

        Ao adicionar um erro, o resultado passa
        automaticamente a ser inválido.
        """
        self.valid = False
        self.errors.append(message)

    @property
    def has_errors(self) -> bool:
        return bool(self.errors)
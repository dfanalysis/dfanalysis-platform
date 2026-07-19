from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class LLMProvider(ABC):
    """
    Contrato comum para provedores de modelos de linguagem.

    Nenhuma regra de negócio deve ser implementada nesta camada.
    """

    @abstractmethod
    def generate_json(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
    ) -> dict[str, Any]:
        """
        Solicita ao modelo uma resposta JSON e devolve
        um dicionário Python validável pela aplicação.
        """
        raise NotImplementedError

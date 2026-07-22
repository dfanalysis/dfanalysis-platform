from __future__ import annotations

import uuid
from abc import ABC, abstractmethod

from app.modules.fiscal.rps.models import Rps


class RpsRepository(ABC):
    """Contrato de persistência do aggregate RPS."""

    @abstractmethod
    def add(self, rps: Rps) -> Rps:
        """Adiciona um novo RPS à unidade de trabalho."""
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, rps_id: uuid.UUID) -> Rps | None:
        """Busca um RPS pelo identificador único."""
        raise NotImplementedError

    @abstractmethod
    def get_by_solicitacao_id(
        self,
        solicitacao_id: uuid.UUID,
    ) -> Rps | None:
        """Busca o RPS vinculado a uma solicitação de emissão."""
        raise NotImplementedError

    @abstractmethod
    def exists_by_solicitacao_id(
        self,
        solicitacao_id: uuid.UUID,
    ) -> bool:
        """Verifica se já existe RPS para a solicitação."""
        raise NotImplementedError
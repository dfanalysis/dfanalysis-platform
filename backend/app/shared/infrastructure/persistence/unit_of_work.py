from __future__ import annotations

from abc import ABC, abstractmethod


class AbstractUnitOfWork(ABC):
    """
    Contrato base para gerenciamento transacional.
    """

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc:
            self.rollback()
        else:
            self.commit()

    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError
from __future__ import annotations

from abc import ABC, abstractmethod

from app.modules.operacoes.inbox.models import InboxMessage


class InterpreterResult:
    """
    Resultado produzido por um mecanismo de interpretação.
    """

    def __init__(
        self,
        *,
        success: bool,
        confidence: float,
        payload: dict,
    ) -> None:
        self.success = success
        self.confidence = confidence
        self.payload = payload


class InterpreterEngine(ABC):
    """
    Interface base para mecanismos de interpretação.
    """

    @abstractmethod
    def interpret(
        self,
        message: InboxMessage,
    ) -> InterpreterResult:
        """
        Interpreta uma comunicação.
        """
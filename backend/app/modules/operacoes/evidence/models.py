from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from uuid import UUID

from app.modules.operacoes.evidence.enums import (
    SeveridadeAviso,
    StatusProcessamentoEvidencia,
    TipoEvidencia,
)
from app.modules.operacoes.inbox.models import (
    InboxAttachment,
    InboxMessage,
)


@dataclass(frozen=True)
class ProcessingWarning:
    """Advertência produzida durante o processamento."""

    codigo: str
    mensagem: str
    severidade: SeveridadeAviso
    evidence_id: UUID | None = None


@dataclass
class ParsedDocument:
    """Resultado técnico produzido pelo parser de uma evidência."""

    evidence_id: UUID
    tipo: TipoEvidencia
    status: StatusProcessamentoEvidencia
    parser: str
    parser_version: str | None = None
    conteudo: dict[str, Any] = field(default_factory=dict)
    texto_extraido: str | None = None
    processado_em: datetime | None = None
    warnings: list[ProcessingWarning] = field(
        default_factory=list,
    )


@dataclass
class EvidenceBundle:
    """
    Conjunto completo de evidências vinculadas a uma comunicação.

    É o objeto de entrada do Communication Interpretation Pipeline.
    """

    message: InboxMessage
    attachments: list[InboxAttachment] = field(
        default_factory=list,
    )
    parsed_documents: list[ParsedDocument] = field(
        default_factory=list,
    )
    warnings: list[ProcessingWarning] = field(
        default_factory=list,
    )
    metadata: dict[str, Any] = field(
        default_factory=dict,
    )

    @property
    def correlation_id(self) -> UUID:
        """Retorna o correlation ID da comunicação de origem."""

        return self.message.correlation_id

    @property
    def has_attachments(self) -> bool:
        """Informa se o Bundle possui anexos."""

        return bool(self.attachments)

    @property
    def has_critical_warnings(self) -> bool:
        """Informa se existe advertência crítica."""

        return any(
            warning.severidade == SeveridadeAviso.CRITICO
            for warning in self.warnings
        )

    def add_parsed_document(
        self,
        document: ParsedDocument,
    ) -> None:
        """Adiciona um documento processado ao Bundle."""

        self.parsed_documents.append(document)

    def add_warning(
        self,
        warning: ProcessingWarning,
    ) -> None:
        """Adiciona uma advertência ao Bundle."""

        self.warnings.append(warning)
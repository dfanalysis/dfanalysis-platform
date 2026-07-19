from __future__ import annotations

from app.ai.schemas import (
    AICommunicationContext,
    AIDocumentContext,
    AIWarningContext,
)
from app.modules.operacoes.evidence.models import (
    EvidenceBundle,
)


class AIContextBuilder:
    """
    Constrói o contexto controlado enviado ao mecanismo de IA.
    """

    def build(
        self,
        bundle: EvidenceBundle,
    ) -> AICommunicationContext:
        message_metadata = bundle.metadata.get(
            "message",
            {},
        )

        operation_type = bundle.metadata.get(
            "operation_type",
        )

        if hasattr(operation_type, "value"):
            operation_type = operation_type.value

        documents = [
            AIDocumentContext(
                evidence_id=document.evidence_id,
                tipo=document.tipo.value,
                status=document.status.value,
                parser=document.parser,
                parser_version=document.parser_version,
                conteudo=document.conteudo,
                texto_extraido=document.texto_extraido,
            )
            for document in bundle.parsed_documents
        ]

        warnings = [
            AIWarningContext(
                codigo=warning.codigo,
                mensagem=warning.mensagem,
                severidade=warning.severidade.value,
                evidence_id=warning.evidence_id,
            )
            for warning in bundle.warnings
        ]

        return AICommunicationContext(
            correlation_id=bundle.correlation_id,
            canal=bundle.metadata.get("canal"),
            origem=bundle.metadata.get("origem"),
            assunto=message_metadata.get("assunto"),
            corpo=message_metadata.get("corpo"),
            remetente=message_metadata.get("remetente"),
            recebido_em=message_metadata.get("recebido_em"),
            operation_type=operation_type,
            consolidated=dict(
                bundle.metadata.get(
                    "consolidated",
                    {},
                )
            ),
            documents=documents,
            warnings=warnings,
        )

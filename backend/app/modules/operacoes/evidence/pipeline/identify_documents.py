from app.modules.operacoes.evidence.enums import (
    StatusProcessamentoEvidencia,
    TipoEvidencia,
)
from app.modules.operacoes.evidence.models import (
    EvidenceBundle,
    ParsedDocument,
)


class IdentifyDocuments:
    """
    Identifica o tipo técnico de cada anexo
    presente no EvidenceBundle.
    """

    MIME_MAPPING = {
        "application/pdf": TipoEvidencia.PDF_TEXTUAL,
        "application/xml": TipoEvidencia.XML,
        "text/xml": TipoEvidencia.XML,
        "application/vnd.ms-excel": TipoEvidencia.EXCEL,
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": TipoEvidencia.EXCEL,
        "text/csv": TipoEvidencia.CSV,
        "image/png": TipoEvidencia.IMAGEM,
        "image/jpeg": TipoEvidencia.IMAGEM,
        "application/zip": TipoEvidencia.ZIP,
    }

    def execute(
        self,
        bundle: EvidenceBundle,
    ) -> EvidenceBundle:
        """
        Identifica os anexos sem processar
        seu conteúdo.
        """

        for attachment in bundle.attachments:

            tipo = self.MIME_MAPPING.get(
                attachment.mime_type,
                TipoEvidencia.DESCONHECIDO,
            )

            bundle.add_parsed_document(
                ParsedDocument(
                    evidence_id=attachment.id,
                    tipo=tipo,
                    status=StatusProcessamentoEvidencia.IDENTIFICADA,
                    parser="DocumentIdentifier",
                )
            )

        return bundle
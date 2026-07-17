from app.modules.operacoes.evidence.enums import (
    StatusProcessamentoEvidencia,
    TipoEvidencia,
)
from app.modules.operacoes.evidence.models import (
    EvidenceBundle,
)


class ParseDocuments:
    """
    Executa o parser apropriado para cada
    documento identificado.
    """

    def execute(
        self,
        bundle: EvidenceBundle,
    ) -> EvidenceBundle:

        for document in bundle.parsed_documents:

            if (
                document.status
                != StatusProcessamentoEvidencia.IDENTIFICADA
            ):
                continue

            if document.tipo == TipoEvidencia.XML:
                self._parse_xml(document)

            elif document.tipo == TipoEvidencia.PDF_TEXTUAL:
                self._parse_pdf(document)

            elif document.tipo == TipoEvidencia.EXCEL:
                self._parse_excel(document)

            else:
                document.status = (
                    StatusProcessamentoEvidencia.COM_ADVERTENCIA
                )

        return bundle

    def _parse_xml(
        self,
        document,
    ) -> None:
        """
        Placeholder para parser XML.
        """

        document.parser = "XMLParser"

        document.status = (
            StatusProcessamentoEvidencia.PROCESSADA
        )

    def _parse_pdf(
        self,
        document,
    ) -> None:
        """
        Placeholder para parser PDF.
        """

        document.parser = "PDFParser"

        document.status = (
            StatusProcessamentoEvidencia.PROCESSADA
        )

    def _parse_excel(
        self,
        document,
    ) -> None:
        """
        Placeholder para parser Excel.
        """

        document.parser = "ExcelParser"

        document.status = (
            StatusProcessamentoEvidencia.PROCESSADA
        )
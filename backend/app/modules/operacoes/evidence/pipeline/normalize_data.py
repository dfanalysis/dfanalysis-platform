from app.modules.operacoes.evidence.models import (
    EvidenceBundle,
)


class NormalizeData:
    """
    Padroniza todas as informações extraídas
    pelos parsers.
    """

    def execute(
        self,
        bundle: EvidenceBundle,
    ) -> EvidenceBundle:

        for document in bundle.parsed_documents:

            self._normalize_document(document)

        return bundle

    def _normalize_document(
        self,
        document,
    ) -> None:

        if not document.conteudo:
            return

        for key, value in document.conteudo.items():

            if isinstance(value, str):

                document.conteudo[key] = value.strip()
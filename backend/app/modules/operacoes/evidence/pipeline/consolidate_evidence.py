from app.modules.operacoes.evidence.models import (
    EvidenceBundle,
)


class ConsolidateEvidence:
    """
    Consolida as informações extraídas pelos
    diferentes documentos do Bundle.
    """

    def execute(
        self,
        bundle: EvidenceBundle,
    ) -> EvidenceBundle:
        consolidated = dict(
            bundle.metadata.get(
                "consolidated",
                {},
            )
        )

        for document in bundle.parsed_documents:
            if not document.conteudo:
                continue

            for key, value in document.conteudo.items():
                if value in (None, "", [], {}):
                    continue

                if key not in consolidated:
                    consolidated[key] = value

        bundle.metadata["consolidated"] = consolidated

        return bundle
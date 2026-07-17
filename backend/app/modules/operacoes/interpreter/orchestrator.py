from app.modules.operacoes.evidence.application.build_bundle import (
    BuildEvidenceBundle,
)
from app.modules.operacoes.evidence.pipeline.ai_enrichment import (
    AIEnrichment,
)
from app.modules.operacoes.evidence.pipeline.classify_operation import (
    ClassifyOperation,
)
from app.modules.operacoes.evidence.pipeline.consolidate_evidence import (
    ConsolidateEvidence,
)
from app.modules.operacoes.evidence.pipeline.identify_documents import (
    IdentifyDocuments,
)
from app.modules.operacoes.evidence.pipeline.normalize_data import (
    NormalizeData,
)
from app.modules.operacoes.evidence.pipeline.parse_documents import (
    ParseDocuments,
)
from app.modules.operacoes.inbox.models import InboxMessage
from app.modules.operacoes.interpreter.analysis import (
    OperationalAnalysis,
)
from app.modules.operacoes.interpreter.result import (
    InterpreterResult,
)
from app.modules.operacoes.interpreter.schemas import (
    BusinessExtraction,
)


class InterpreterOrchestrator:
    """
    Executa todo o Communication Pipeline.
    """

    def __init__(self) -> None:

        self.build_bundle = BuildEvidenceBundle()

        self.identify_documents = IdentifyDocuments()

        self.parse_documents = ParseDocuments()

        self.normalize_data = NormalizeData()

        self.consolidate = ConsolidateEvidence()

        self.classify = ClassifyOperation()

        self.ai = AIEnrichment()

    def execute(
        self,
        message: InboxMessage,
    ) -> InterpreterResult:

        bundle = self.build_bundle.execute(
            message,
        )

        bundle = self.identify_documents.execute(
            bundle,
        )

        bundle = self.parse_documents.execute(
            bundle,
        )

        bundle = self.normalize_data.execute(
            bundle,
        )

        bundle = self.consolidate.execute(
            bundle,
        )

        bundle = self.classify.execute(
            bundle,
        )

        bundle = self.ai.execute(
            bundle,
        )

        extraction = BusinessExtraction()

        analysis = OperationalAnalysis()

        return InterpreterResult(
            extraction=extraction,
            analysis=analysis,
        )
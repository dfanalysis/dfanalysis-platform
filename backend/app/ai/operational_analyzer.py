from __future__ import annotations

from pydantic import ValidationError

from app.ai.context_builder import AIContextBuilder
from app.ai.contracts import LLMProvider
from app.ai.exceptions import AIInvalidResponseError
from app.ai.prompt_manager import PromptManager
from app.ai.schemas import AIOperationalResponse
from app.modules.operacoes.evidence.models import (
    EvidenceBundle,
)


class OperationalAIAnalyzer:
    """
    Coordena a análise operacional por IA.

    Esta camada:
    - constrói o contexto;
    - carrega o prompt versionado;
    - chama o provider;
    - valida a resposta.
    """

    PROMPT_PATH = (
        "operacoes/analyze_communication_v1.md"
    )

    def __init__(
        self,
        *,
        provider: LLMProvider,
        prompt_manager: PromptManager | None = None,
        context_builder: AIContextBuilder | None = None,
    ) -> None:
        self.provider = provider
        self.prompt_manager = (
            prompt_manager or PromptManager()
        )
        self.context_builder = (
            context_builder or AIContextBuilder()
        )

    def analyze(
        self,
        bundle: EvidenceBundle,
    ) -> AIOperationalResponse:
        context = self.context_builder.build(
            bundle,
        )

        system_prompt = self.prompt_manager.load(
            self.PROMPT_PATH,
        )

        user_prompt = context.model_dump_json(
            indent=2,
        )

        raw_response = self.provider.generate_json(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        try:
            return AIOperationalResponse.model_validate(
                raw_response,
            )

        except ValidationError as exc:
            raise AIInvalidResponseError(
                "A resposta da IA não atende ao contrato operacional.",
            ) from exc

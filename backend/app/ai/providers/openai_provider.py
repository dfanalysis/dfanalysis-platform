from __future__ import annotations

import json
from typing import Any

from openai import (
    APIConnectionError,
    APIError,
    APITimeoutError,
    OpenAI,
)

from app.ai.contracts import LLMProvider
from app.ai.exceptions import (
    AIConfigurationError,
    AIConnectionError,
    AIInvalidResponseError,
    AITimeoutError,
)
from app.core.config import settings


class OpenAIProvider(LLMProvider):
    """
    Implementação do LLMProvider utilizando a OpenAI.

    Esta classe é responsável somente pela comunicação técnica
    com o provedor. Regras de negócio não devem ser implementadas
    nesta camada.
    """

    def __init__(
        self,
        *,
        client: OpenAI | None = None,
        api_key: str | None = None,
        model: str | None = None,
    ) -> None:
        self.model = model or settings.OPENAI_MODEL

        if client is not None:
            self.client = client
            return

        resolved_api_key = api_key or settings.OPENAI_API_KEY

        if not resolved_api_key:
            raise AIConfigurationError(
                "A variável OPENAI_API_KEY não está configurada.",
            )

        self.client = OpenAI(
            api_key=resolved_api_key,
            timeout=settings.OPENAI_TIMEOUT_SECONDS,
            max_retries=settings.OPENAI_MAX_RETRIES,
        )

    def generate_json(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
    ) -> dict[str, Any]:
        """
        Executa uma solicitação ao modelo e converte
        a resposta JSON em um dicionário Python.
        """

        if not system_prompt.strip():
            raise ValueError(
                "O system_prompt não pode estar vazio.",
            )

        if not user_prompt.strip():
            raise ValueError(
                "O user_prompt não pode estar vazio.",
            )

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": user_prompt,
                    },
                ],
                response_format={
                    "type": "json_object",
                },
                temperature=0,
            )

        except APITimeoutError as exc:
            raise AITimeoutError(
                "A chamada ao provedor de IA excedeu o tempo limite.",
            ) from exc

        except APIConnectionError as exc:
            raise AIConnectionError(
                "Não foi possível conectar ao provedor de IA.",
            ) from exc

        except APIError as exc:
            raise AIConnectionError(
                "O provedor de IA retornou uma falha durante a requisição.",
            ) from exc

        content = response.choices[0].message.content

        if not content:
            raise AIInvalidResponseError(
                "O provedor retornou uma resposta vazia.",
            )

        try:
            result = json.loads(content)

        except json.JSONDecodeError as exc:
            raise AIInvalidResponseError(
                "O provedor retornou um JSON inválido.",
            ) from exc

        if not isinstance(result, dict):
            raise AIInvalidResponseError(
                "A resposta da IA deve ser um objeto JSON.",
            )

        return result

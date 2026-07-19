from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from app.ai.exceptions import (
    AIConfigurationError,
    AIInvalidResponseError,
)
from app.ai.providers.openai_provider import OpenAIProvider


def build_mock_client(
    content: str | None,
) -> Mock:
    client = Mock()

    client.chat.completions.create.return_value = (
        SimpleNamespace(
            choices=[
                SimpleNamespace(
                    message=SimpleNamespace(
                        content=content,
                    ),
                )
            ],
        )
    )

    return client


def test_generate_json_returns_dictionary() -> None:
    client = build_mock_client(
        '{"tipo_processo": "FATURAMENTO_HOSPITALAR"}',
    )

    provider = OpenAIProvider(
        client=client,
        model="test-model",
    )

    result = provider.generate_json(
        system_prompt="Responda somente em JSON.",
        user_prompt="Analise esta comunicação.",
    )

    assert result == {
        "tipo_processo": "FATURAMENTO_HOSPITALAR",
    }

    client.chat.completions.create.assert_called_once()


def test_generate_json_sends_expected_parameters() -> None:
    client = build_mock_client(
        '{"success": true}',
    )

    provider = OpenAIProvider(
        client=client,
        model="test-model",
    )

    provider.generate_json(
        system_prompt="System prompt.",
        user_prompt="User prompt.",
    )

    client.chat.completions.create.assert_called_once_with(
        model="test-model",
        messages=[
            {
                "role": "system",
                "content": "System prompt.",
            },
            {
                "role": "user",
                "content": "User prompt.",
            },
        ],
        response_format={
            "type": "json_object",
        },
        temperature=0,
    )


def test_reject_empty_response() -> None:
    client = build_mock_client(
        None,
    )

    provider = OpenAIProvider(
        client=client,
    )

    with pytest.raises(AIInvalidResponseError):
        provider.generate_json(
            system_prompt="System prompt.",
            user_prompt="User prompt.",
        )


def test_reject_invalid_json() -> None:
    client = build_mock_client(
        "resposta inválida",
    )

    provider = OpenAIProvider(
        client=client,
    )

    with pytest.raises(AIInvalidResponseError):
        provider.generate_json(
            system_prompt="System prompt.",
            user_prompt="User prompt.",
        )


def test_reject_json_array() -> None:
    client = build_mock_client(
        '["item"]',
    )

    provider = OpenAIProvider(
        client=client,
    )

    with pytest.raises(AIInvalidResponseError):
        provider.generate_json(
            system_prompt="System prompt.",
            user_prompt="User prompt.",
        )


def test_reject_empty_system_prompt() -> None:
    client = build_mock_client(
        '{"success": true}',
    )

    provider = OpenAIProvider(
        client=client,
    )

    with pytest.raises(ValueError):
        provider.generate_json(
            system_prompt=" ",
            user_prompt="User prompt.",
        )


def test_reject_empty_user_prompt() -> None:
    client = build_mock_client(
        '{"success": true}',
    )

    provider = OpenAIProvider(
        client=client,
    )

    with pytest.raises(ValueError):
        provider.generate_json(
            system_prompt="System prompt.",
            user_prompt=" ",
        )


def test_requires_api_key_without_injected_client(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.ai.providers.openai_provider.settings.OPENAI_API_KEY",
        "",
    )

    with pytest.raises(AIConfigurationError):
        OpenAIProvider()

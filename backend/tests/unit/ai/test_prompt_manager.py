from pathlib import Path

import pytest

from app.ai.exceptions import PromptNotFoundError
from app.ai.prompt_manager import PromptManager


def test_load_existing_prompt(
    tmp_path: Path,
) -> None:
    prompt_file = tmp_path / "prompt_v1.md"
    prompt_file.write_text(
        "Analise o documento.",
        encoding="utf-8",
    )

    manager = PromptManager(
        base_path=tmp_path,
    )

    result = manager.load(
        "prompt_v1.md",
    )

    assert result == "Analise o documento."


def test_reject_missing_prompt(
    tmp_path: Path,
) -> None:
    manager = PromptManager(
        base_path=tmp_path,
    )

    with pytest.raises(PromptNotFoundError):
        manager.load(
            "inexistente.md",
        )


def test_reject_empty_prompt(
    tmp_path: Path,
) -> None:
    prompt_file = tmp_path / "empty.md"
    prompt_file.write_text(
        "   ",
        encoding="utf-8",
    )

    manager = PromptManager(
        base_path=tmp_path,
    )

    with pytest.raises(PromptNotFoundError):
        manager.load(
            "empty.md",
        )


def test_reject_path_outside_prompt_directory(
    tmp_path: Path,
) -> None:
    manager = PromptManager(
        base_path=tmp_path,
    )

    with pytest.raises(PromptNotFoundError):
        manager.load(
            "../secret.txt",
        )

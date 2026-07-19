from pathlib import Path

from app.ai.exceptions import PromptNotFoundError


class PromptManager:
    """
    Carrega prompts versionados armazenados como arquivos de texto.
    """

    def __init__(
        self,
        base_path: Path | None = None,
    ) -> None:
        self.base_path = base_path or Path(__file__).parent / "prompts"

    def load(
        self,
        prompt_path: str,
    ) -> str:
        """
        Carrega um prompt relativo ao diretório app/ai/prompts.
        """

        file_path = (self.base_path / prompt_path).resolve()
        base_path = self.base_path.resolve()

        if base_path not in file_path.parents:
            raise PromptNotFoundError(
                "O caminho informado está fora do diretório de prompts.",
            )

        if not file_path.is_file():
            raise PromptNotFoundError(
                f"Prompt não encontrado: {prompt_path}",
            )

        content = file_path.read_text(
            encoding="utf-8",
        ).strip()

        if not content:
            raise PromptNotFoundError(
                f"O prompt está vazio: {prompt_path}",
            )

        return content

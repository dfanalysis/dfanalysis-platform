from __future__ import annotations

from app.modules.fiscal.rps.application.commands.create_rps import (
    CreateRpsCommand,
)
from app.modules.fiscal.rps.application.interfaces.rps_repository import (
    RpsRepository,
)


class CreateRpsHandler:

    def __init__(
        self,
        repository: RpsRepository,
    ) -> None:
        self._repository = repository

    def execute(
        self,
        command: CreateRpsCommand,
    ):
        raise NotImplementedError
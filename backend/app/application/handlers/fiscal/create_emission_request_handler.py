from app.application.commands.fiscal.create_emission_request import (
    CreateEmissionRequestCommand,
)
from app.application.dto.fiscal.emission_request_response import (
    EmissionRequestResponse,
)
from app.application.interfaces.emission_request_repository import (
    EmissionRequestRepository,
)


class CreateEmissionRequestHandler:

    def __init__(self, repository: EmissionRequestRepository):
        self.repository = repository

    async def handle(
        self,
        command: CreateEmissionRequestCommand,
    ) -> EmissionRequestResponse:

        # implementação virá no próximo passo

        raise NotImplementedError
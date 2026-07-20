from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class EmissionRequestResponse:
    id: UUID
    status: str
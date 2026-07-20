from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class CreateEmissionRequestCommand:
    empresa_id: UUID
    solicitante_id: UUID
    evidence_bundle_id: UUID
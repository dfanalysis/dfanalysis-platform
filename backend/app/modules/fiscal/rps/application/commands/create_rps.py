from __future__ import annotations

import uuid
from dataclasses import dataclass


@dataclass(slots=True)
class CreateRpsCommand:
    solicitacao_id: uuid.UUID
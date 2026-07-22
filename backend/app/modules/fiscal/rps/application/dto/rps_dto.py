from __future__ import annotations

import uuid
from dataclasses import dataclass
from datetime import date
from decimal import Decimal

from app.modules.fiscal.rps.enums import StatusRps


@dataclass(slots=True)
class RpsDTO:
    id: uuid.UUID
    empresa_id: uuid.UUID
    solicitacao_id: uuid.UUID
    numero: int
    serie: str
    competencia: date
    status: StatusRps
    valor: Decimal
    descricao: str
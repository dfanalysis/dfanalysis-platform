from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.empresas.models import Empresa


class EmpresaRepository:
    """Operações de persistência do módulo de empresas."""

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_by_id(self, empresa_id: UUID) -> Empresa | None:
        statement = select(Empresa).where(Empresa.id == empresa_id)
        return self.db.scalar(statement)

    def get_by_cnpj(self, cnpj: str) -> Empresa | None:
        statement = select(Empresa).where(Empresa.cnpj == cnpj)
        return self.db.scalar(statement)

    def add(self, empresa: Empresa) -> Empresa:
        self.db.add(empresa)
        self.db.flush()
        return empresa
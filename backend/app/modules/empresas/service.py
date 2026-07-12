from sqlalchemy.orm import Session

from app.modules.empresas.models import Empresa
from app.modules.empresas.repository import EmpresaRepository


class EmpresaService:
    """Regras de negócio para criação e consulta de empresas."""

    def __init__(self, db: Session) -> None:
        self.db = db
        self.repository = EmpresaRepository(db)

    def get_or_create(
        self,
        *,
        razao_social: str,
        cnpj: str,
        nome_fantasia: str | None = None,
        inscricao_municipal: str | None = None,
        inscricao_estadual: str | None = None,
        email: str | None = None,
        telefone: str | None = None,
    ) -> tuple[Empresa, bool]:
        """
        Retorna a empresa existente ou cria uma nova.

        O segundo item da tupla informa se o registro foi criado.
        """

        normalized_cnpj = "".join(character for character in cnpj if character.isdigit())

        if len(normalized_cnpj) != 14:
            raise ValueError("O CNPJ deve conter exatamente 14 dígitos.")

        existing_company = self.repository.get_by_cnpj(normalized_cnpj)

        if existing_company:
            return existing_company, False

        company = Empresa(
            razao_social=razao_social.strip(),
            nome_fantasia=nome_fantasia.strip() if nome_fantasia else None,
            cnpj=normalized_cnpj,
            inscricao_municipal=(
                inscricao_municipal.strip()
                if inscricao_municipal
                else None
            ),
            inscricao_estadual=(
                inscricao_estadual.strip()
                if inscricao_estadual
                else None
            ),
            email=email.strip().lower() if email else None,
            telefone=telefone.strip() if telefone else None,
        )

        return self.repository.add(company), True
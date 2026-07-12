from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.modules.auth.models import Perfil
from app.modules.empresas.service import EmpresaService
from app.modules.usuarios.service import UsuarioService
from app.shared.constants import (
    DEFAULT_ADMIN_EMAIL,
    DEFAULT_ADMIN_NAME,
    DEFAULT_COMPANY_CNPJ,
    DEFAULT_COMPANY_LEGAL_NAME,
    DEFAULT_COMPANY_TRADE_NAME,
    SUPER_ADMIN_PROFILE_CODE,
)


def seed_development(db: Session) -> dict[str, bool]:
    """
    Cria os dados mínimos do ambiente de desenvolvimento.

    O processo é idempotente: pode ser executado várias vezes
    sem duplicar empresa ou usuário.
    """

    if not settings.DEVELOPMENT_ADMIN_PASSWORD:
        raise RuntimeError(
            "DEVELOPMENT_ADMIN_PASSWORD não está configurado no arquivo .env."
        )

    profile = db.scalar(
        select(Perfil).where(
            Perfil.codigo == SUPER_ADMIN_PROFILE_CODE
        )
    )

    if profile is None:
        raise RuntimeError(
            "O perfil super_admin não foi encontrado. "
            "Execute o Platform Seed antes do Development Seed."
        )

    company_service = EmpresaService(db)

    company, company_created = company_service.get_or_create(
        razao_social=DEFAULT_COMPANY_LEGAL_NAME,
        nome_fantasia=DEFAULT_COMPANY_TRADE_NAME,
        cnpj=DEFAULT_COMPANY_CNPJ,
        email=DEFAULT_ADMIN_EMAIL,
    )

    user_service = UsuarioService(db)

    user, user_created = user_service.get_or_create(
        empresa_id=company.id,
        nome=DEFAULT_ADMIN_NAME,
        email=DEFAULT_ADMIN_EMAIL,
        password=settings.DEVELOPMENT_ADMIN_PASSWORD,
        profiles=[profile],
    )

    profile_link_created = False

    if profile not in user.perfis:
        user.perfis.append(profile)
        db.flush()
        profile_link_created = True

    return {
        "company_created": company_created,
        "user_created": user_created,
        "profile_link_created": profile_link_created,
    }
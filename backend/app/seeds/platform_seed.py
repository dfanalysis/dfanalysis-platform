from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.auth.models import Perfil, Permissao


PROFILES = [
    {
        "codigo": "super_admin",
        "nome": "Super Administrador",
        "descricao": "Administrador global da Plataforma DF Analysis IA.",
        "is_system": True,
    },
    {
        "codigo": "administrador",
        "nome": "Administrador",
        "descricao": "Administrador da empresa vinculada.",
        "is_system": True,
    },
    {
        "codigo": "fiscal",
        "nome": "Fiscal",
        "descricao": "Responsável pelas operações fiscais.",
        "is_system": True,
    },
    {
        "codigo": "financeiro",
        "nome": "Financeiro",
        "descricao": "Responsável pelas rotinas financeiras.",
        "is_system": True,
    },
    {
        "codigo": "comercial",
        "nome": "Comercial",
        "descricao": "Responsável pelo CRM e processos comerciais.",
        "is_system": True,
    },
    {
        "codigo": "operador",
        "nome": "Operador",
        "descricao": "Usuário responsável por rotinas operacionais.",
        "is_system": True,
    },
    {
        "codigo": "ia_agent",
        "nome": "Agente de IA",
        "descricao": "Conta técnica utilizada por agentes de IA.",
        "is_system": True,
    },
    {
        "codigo": "api",
        "nome": "API",
        "descricao": "Conta técnica utilizada por integrações externas.",
        "is_system": True,
    },
]


PERMISSIONS = [
    ("usuarios.read", "Consultar usuários"),
    ("usuarios.create", "Criar usuários"),
    ("usuarios.update", "Alterar usuários"),
    ("usuarios.delete", "Excluir usuários"),
    ("empresas.read", "Consultar empresas"),
    ("empresas.create", "Criar empresas"),
    ("empresas.update", "Alterar empresas"),
    ("empresas.delete", "Excluir empresas"),
    ("fiscal.emitir", "Emitir documentos fiscais"),
    ("fiscal.cancelar", "Cancelar documentos fiscais"),
    ("fiscal.consultar", "Consultar documentos fiscais"),
    ("workflow.execute", "Executar workflows"),
    ("workflow.update", "Alterar workflows"),
    ("ia.execute", "Executar agentes de IA"),
    ("ia.configure", "Configurar agentes de IA"),
    ("auditoria.read", "Consultar auditoria"),
    ("configuracoes.update", "Alterar configurações"),
]


def seed_platform(db: Session) -> dict[str, int]:
    """
    Cria perfis e permissões estruturais da plataforma.

    O processo é idempotente: pode ser executado diversas vezes sem
    duplicar registros.
    """

    created_profiles = 0
    created_permissions = 0

    profiles_by_code: dict[str, Perfil] = {}

    for profile_data in PROFILES:
        profile = db.scalar(
            select(Perfil).where(
                Perfil.codigo == profile_data["codigo"]
            )
        )

        if profile is None:
            profile = Perfil(**profile_data)
            db.add(profile)
            db.flush()
            created_profiles += 1

        profiles_by_code[profile.codigo] = profile

    permissions: list[Permissao] = []

    for permission_code, permission_name in PERMISSIONS:
        permission = db.scalar(
            select(Permissao).where(
                Permissao.codigo == permission_code
            )
        )

        if permission is None:
            permission = Permissao(
                codigo=permission_code,
                nome=permission_name,
                descricao=None,
            )
            db.add(permission)
            db.flush()
            created_permissions += 1

        permissions.append(permission)

    super_admin = profiles_by_code["super_admin"]

    existing_permission_ids = {
        permission.id
        for permission in super_admin.permissoes
    }

    for permission in permissions:
        if permission.id not in existing_permission_ids:
            super_admin.permissoes.append(permission)

    db.flush()

    return {
        "created_profiles": created_profiles,
        "created_permissions": created_permissions,
    }
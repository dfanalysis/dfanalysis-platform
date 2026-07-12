import argparse
import sys

from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.seeds.development_seed import seed_development
from app.seeds.platform_seed import seed_platform


SUPPORTED_ENVIRONMENTS = {
    "development",
}


def run_seed(environment: str) -> None:
    """
    Executa os seeds da plataforma na ordem correta.

    Ordem:
    1. Platform Seed
    2. Seed específico do ambiente
    """

    if environment not in SUPPORTED_ENVIRONMENTS:
        supported = ", ".join(sorted(SUPPORTED_ENVIRONMENTS))
        raise ValueError(
            f"Ambiente inválido: {environment}. "
            f"Ambientes suportados: {supported}."
        )

    db: Session = SessionLocal()

    try:
        print("")
        print("DF Analysis IA Platform")
        print("Inicialização de dados")
        print("-" * 40)

        platform_result = seed_platform(db)

        print(
            "Platform Seed executado:"
            f" {platform_result['created_profiles']} perfil(is) criado(s),"
            f" {platform_result['created_permissions']} permissão(ões) criada(s)."
        )

        if environment == "development":
            development_result = seed_development(db)

            print(
                "Development Seed executado:"
                f" empresa_criada={development_result['company_created']},"
                f" usuario_criado={development_result['user_created']},"
                " perfil_vinculado="
                f"{development_result['profile_link_created']}."
            )

        db.commit()

        print("-" * 40)
        print("Seeds concluídos com sucesso.")

    except Exception as error:
        db.rollback()

        print("-" * 40)
        print("Falha durante a execução dos seeds.")
        print(f"Erro: {error}")

        raise

    finally:
        db.close()


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Executa os seeds da DF Analysis IA Platform."
    )

    parser.add_argument(
        "environment",
        choices=sorted(SUPPORTED_ENVIRONMENTS),
        help="Ambiente de execução dos seeds.",
    )

    return parser.parse_args()


def main() -> None:
    arguments = parse_arguments()

    try:
        run_seed(arguments.environment)
    except Exception:
        sys.exit(1)


if __name__ == "__main__":
    main()
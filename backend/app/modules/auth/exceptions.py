class InvalidCredentialsError(Exception):
    """
    Falha genérica de autenticação.

    A mensagem deve ser deliberadamente genérica para não revelar
    se determinado e-mail existe ou se o usuário está inativo.
    """


class AuthenticatedUserNotFoundError(Exception):
    """Usuário associado a um token válido não está mais disponível."""

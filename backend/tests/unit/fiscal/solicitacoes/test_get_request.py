from types import SimpleNamespace
from unittest.mock import MagicMock
from uuid import uuid4

from app.modules.fiscal.solicitacoes.application.get_request import (
    GetEmissionRequest,
)


def test_busca_solicitacao_por_id():
    solicitacao_id = uuid4()

    repository = MagicMock()

    solicitacao = SimpleNamespace(
        id=solicitacao_id,
    )

    repository.get_by_id.return_value = solicitacao

    use_case = GetEmissionRequest(
        db=MagicMock(),
        repository=repository,
    )

    result = use_case.execute(
        solicitacao_id,
    )

    repository.get_by_id.assert_called_once_with(
        solicitacao_id,
    )

    assert result is solicitacao


def test_retorna_none_quando_nao_encontra():
    solicitacao_id = uuid4()

    repository = MagicMock()

    repository.get_by_id.return_value = None

    use_case = GetEmissionRequest(
        db=MagicMock(),
        repository=repository,
    )

    result = use_case.execute(
        solicitacao_id,
    )

    repository.get_by_id.assert_called_once_with(
        solicitacao_id,
    )

    assert result is None
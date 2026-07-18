from types import SimpleNamespace
from unittest.mock import MagicMock
from uuid import uuid4

from app.modules.fiscal.enums import StatusSolicitacao
from app.modules.fiscal.solicitacoes.application.list_requests import (
    ListEmissionRequests,
)


def test_lista_solicitacoes_da_empresa():
    empresa_id = uuid4()

    repository = MagicMock()

    solicitacoes = [
        SimpleNamespace(id=uuid4()),
        SimpleNamespace(id=uuid4()),
    ]

    repository.list_by_empresa.return_value = solicitacoes

    use_case = ListEmissionRequests(
        db=MagicMock(),
        repository=repository,
    )

    result = use_case.execute(
        empresa_id,
    )

    repository.list_by_empresa.assert_called_once_with(
        empresa_id=empresa_id,
        status=None,
    )

    assert result == solicitacoes


def test_lista_filtrando_por_status():
    empresa_id = uuid4()

    repository = MagicMock()
    repository.list_by_empresa.return_value = []

    use_case = ListEmissionRequests(
        db=MagicMock(),
        repository=repository,
    )

    result = use_case.execute(
        empresa_id,
        status=StatusSolicitacao.RECEBIDA,
    )

    repository.list_by_empresa.assert_called_once_with(
        empresa_id=empresa_id,
        status=StatusSolicitacao.RECEBIDA,
    )

    assert result == []
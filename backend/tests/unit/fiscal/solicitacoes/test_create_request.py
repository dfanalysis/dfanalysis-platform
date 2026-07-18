from datetime import date
from decimal import Decimal
from types import SimpleNamespace
from unittest.mock import MagicMock
from uuid import uuid4

import pytest

from app.modules.fiscal.enums import OrigemSolicitacao
from app.modules.fiscal.solicitacoes.application.create_request import (
    CreateEmissionRequest,
)
from app.modules.fiscal.solicitacoes.exceptions import (
    EmpresaNaoEncontradaError,
    IdempotencyConflictError,
)
from app.modules.fiscal.solicitacoes.schemas import (
    SolicitacaoEmissaoCreate,
)


def make_payload(
    *,
    idempotency_key: str | None = "nfse-6044",
) -> SolicitacaoEmissaoCreate:
    return SolicitacaoEmissaoCreate(
        empresa_id=uuid4(),
        origem=OrigemSolicitacao.EMAIL,
        referencia_externa="6044",
        idempotency_key=idempotency_key,
        competencia=date(2026, 6, 12),
        descricao_servico="Serviços médicos prestados.",
        valor_servico=Decimal("202699.00"),
    )


def make_empresa():
    return SimpleNamespace(
        id=uuid4(),
        is_active=True,
        deleted_at=None,
    )


@pytest.fixture
def empresa_repository():
    repository = MagicMock()
    repository.get_by_id.return_value = make_empresa()
    return repository


@pytest.fixture
def solicitacao_repository():
    repository = MagicMock()
    repository.get_by_idempotency_key.return_value = None
    return repository


@pytest.fixture
def factory():
    factory_mock = MagicMock()
    factory_mock.create.return_value = SimpleNamespace(
        id=uuid4(),
        status="PENDENTE",
    )
    return factory_mock


@pytest.fixture
def use_case(
    empresa_repository,
    solicitacao_repository,
    factory,
):
    return CreateEmissionRequest(
        db=MagicMock(),
        empresa_repository=empresa_repository,
        solicitacao_repository=solicitacao_repository,
        factory=factory,
    )


def test_cria_solicitacao_com_sucesso(
    use_case,
    empresa_repository,
    solicitacao_repository,
    factory,
):
    payload = make_payload()
    solicitacao_criada = factory.create.return_value
    solicitacao_repository.add.return_value = solicitacao_criada

    result, created = use_case.execute(payload)

    empresa_repository.get_by_id.assert_called_once_with(
        payload.empresa_id,
    )
    solicitacao_repository.get_by_idempotency_key.assert_called_once_with(
        payload.idempotency_key,
    )
    factory.create.assert_called_once_with(payload)
    solicitacao_repository.add.assert_called_once_with(
        solicitacao_criada,
    )

    assert result is solicitacao_criada
    assert created is True


def test_empresa_inexistente_interrompe_fluxo(
    use_case,
    empresa_repository,
    solicitacao_repository,
    factory,
):
    payload = make_payload()
    empresa_repository.get_by_id.return_value = None

    with pytest.raises(EmpresaNaoEncontradaError):
        use_case.execute(payload)

    solicitacao_repository.get_by_idempotency_key.assert_not_called()
    factory.create.assert_not_called()
    solicitacao_repository.add.assert_not_called()


def test_idempotencia_duplicada_interrompe_fluxo(
    use_case,
    solicitacao_repository,
    factory,
):
    payload = make_payload()
    solicitacao_repository.get_by_idempotency_key.return_value = (
        SimpleNamespace(id=uuid4())
    )

    with pytest.raises(IdempotencyConflictError):
        use_case.execute(payload)

    factory.create.assert_not_called()
    solicitacao_repository.add.assert_not_called()


def test_sem_idempotency_key_nao_consulta_repositorio(
    use_case,
    solicitacao_repository,
    factory,
):
    payload = make_payload(idempotency_key=None)
    solicitacao_criada = factory.create.return_value
    solicitacao_repository.add.return_value = solicitacao_criada

    result, created = use_case.execute(payload)

    solicitacao_repository.get_by_idempotency_key.assert_not_called()
    factory.create.assert_called_once_with(payload)
    solicitacao_repository.add.assert_called_once_with(
        solicitacao_criada,
    )

    assert result is solicitacao_criada
    assert created is True


def test_retorna_objeto_persistido_pelo_repositorio(
    use_case,
    solicitacao_repository,
    factory,
):
    payload = make_payload()

    objeto_da_factory = factory.create.return_value
    objeto_persistido = SimpleNamespace(
        id=uuid4(),
        status="PENDENTE",
    )
    solicitacao_repository.add.return_value = objeto_persistido

    result, created = use_case.execute(payload)

    solicitacao_repository.add.assert_called_once_with(
        objeto_da_factory,
    )

    assert result is objeto_persistido
    assert created is True
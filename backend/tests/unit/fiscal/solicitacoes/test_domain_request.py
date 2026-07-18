from datetime import date, timedelta
from decimal import Decimal
from types import SimpleNamespace
from typing import Any, cast

import pytest

from app.modules.fiscal.enums import StatusSolicitacao
from app.modules.fiscal.solicitacoes.domain.services import (
    FiscalDomainService,
)
from app.modules.fiscal.solicitacoes.exceptions import (
    CompetenciaInvalidaError,
    DescricaoServicoInvalidaError,
    EmpresaInativaError,
    EmpresaNaoEncontradaError,
    IdempotencyConflictError,
    TransicaoStatusInvalidaError,
    ValorServicoInvalidoError,
)
from app.modules.fiscal.solicitacoes.models import SolicitacaoEmissao


def make_empresa(
    *,
    is_active: bool = True,
    deleted_at: object | None = None,
) -> Any:
    """
    Cria um objeto mínimo com os atributos utilizados pelo serviço.

    Não acessamos banco de dados nestes testes unitários.
    """

    return SimpleNamespace(
        is_active=is_active,
        deleted_at=deleted_at,
    )


def make_solicitacao(
    status: StatusSolicitacao,
) -> SolicitacaoEmissao:
    """
    Cria uma solicitação mínima para testar a máquina de estados.
    """

    solicitacao = SimpleNamespace(status=status)

    return cast(SolicitacaoEmissao, solicitacao)


# ---------------------------------------------------------------------------
# validar_empresa
# ---------------------------------------------------------------------------


def test_validar_empresa_rejeita_empresa_inexistente() -> None:
    with pytest.raises(
        EmpresaNaoEncontradaError,
        match="Empresa não encontrada",
    ):
        FiscalDomainService.validar_empresa(None)


def test_validar_empresa_rejeita_empresa_inativa() -> None:
    empresa = make_empresa(is_active=False)

    with pytest.raises(
        EmpresaInativaError,
        match="inativa ou excluída",
    ):
        FiscalDomainService.validar_empresa(empresa)


def test_validar_empresa_rejeita_empresa_excluida() -> None:
    empresa = make_empresa(
        is_active=True,
        deleted_at=object(),
    )

    with pytest.raises(
        EmpresaInativaError,
        match="inativa ou excluída",
    ):
        FiscalDomainService.validar_empresa(empresa)


def test_validar_empresa_retorna_empresa_valida() -> None:
    empresa = make_empresa()

    result = FiscalDomainService.validar_empresa(empresa)

    assert result is empresa


# ---------------------------------------------------------------------------
# validar_competencia
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "competencia",
    [
        date.today(),
        date.today() - timedelta(days=1),
        date.today() - timedelta(days=365),
    ],
)
def test_validar_competencia_aceita_data_atual_ou_passada(
    competencia: date,
) -> None:
    result = FiscalDomainService.validar_competencia(competencia)

    assert result == competencia


def test_validar_competencia_rejeita_data_futura() -> None:
    competencia_futura = date.today() + timedelta(days=1)

    with pytest.raises(
        CompetenciaInvalidaError,
        match="não pode ser uma data futura",
    ):
        FiscalDomainService.validar_competencia(
            competencia_futura,
        )


# ---------------------------------------------------------------------------
# validar_valor
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "valor_invalido",
    [
        Decimal("0"),
        Decimal("-0.01"),
        Decimal("-1000.00"),
    ],
)
def test_validar_valor_rejeita_valor_nao_positivo(
    valor_invalido: Decimal,
) -> None:
    with pytest.raises(
        ValorServicoInvalidoError,
        match="maior que zero",
    ):
        FiscalDomainService.validar_valor(valor_invalido)


@pytest.mark.parametrize(
    "valor_valido",
    [
        Decimal("0.01"),
        Decimal("1000.00"),
        Decimal("999999.99"),
    ],
)
def test_validar_valor_aceita_valor_positivo(
    valor_valido: Decimal,
) -> None:
    result = FiscalDomainService.validar_valor(valor_valido)

    assert result == valor_valido


# ---------------------------------------------------------------------------
# validar_descricao
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "descricao_invalida",
    [
        "",
        " ",
        "ab",
        " a ",
    ],
)
def test_validar_descricao_rejeita_texto_com_menos_de_tres_caracteres(
    descricao_invalida: str,
) -> None:
    with pytest.raises(
        DescricaoServicoInvalidaError,
        match="ao menos 3 caracteres",
    ):
        FiscalDomainService.validar_descricao(
            descricao_invalida,
        )


def test_validar_descricao_normaliza_espacos_externos() -> None:
    descricao = "  Serviços médicos hospitalares  "

    result = FiscalDomainService.validar_descricao(descricao)

    assert result == "Serviços médicos hospitalares"


def test_validar_descricao_retorna_texto_valido() -> None:
    descricao = "Consulta médica"

    result = FiscalDomainService.validar_descricao(descricao)

    assert result == descricao


# ---------------------------------------------------------------------------
# verificar_idempotencia
# ---------------------------------------------------------------------------


def test_verificar_idempotencia_aceita_quando_nao_existe_solicitacao() -> None:
    result = FiscalDomainService.verificar_idempotencia(None)

    assert result is None


def test_verificar_idempotencia_rejeita_solicitacao_existente() -> None:
    solicitacao_existente = make_solicitacao(
        StatusSolicitacao.RECEBIDA,
    )

    with pytest.raises(
        IdempotencyConflictError,
        match="Já existe uma solicitação",
    ):
        FiscalDomainService.verificar_idempotencia(
            solicitacao_existente,
        )


# ---------------------------------------------------------------------------
# alterar_status
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("status_atual", "novo_status"),
    [
        (
            StatusSolicitacao.RECEBIDA,
            StatusSolicitacao.EM_VALIDACAO,
        ),
        (
            StatusSolicitacao.RECEBIDA,
            StatusSolicitacao.CANCELADA,
        ),
        (
            StatusSolicitacao.EM_VALIDACAO,
            StatusSolicitacao.VALIDADA,
        ),
        (
            StatusSolicitacao.VALIDADA,
            StatusSolicitacao.AGUARDANDO_PROCESSAMENTO,
        ),
        (
            StatusSolicitacao.AGUARDANDO_PROCESSAMENTO,
            StatusSolicitacao.PROCESSANDO,
        ),
        (
            StatusSolicitacao.PROCESSANDO,
            StatusSolicitacao.EMITIDA,
        ),
        (
            StatusSolicitacao.REJEITADA,
            StatusSolicitacao.EM_VALIDACAO,
        ),
        (
            StatusSolicitacao.FALHA,
            StatusSolicitacao.AGUARDANDO_PROCESSAMENTO,
        ),
    ],
)
def test_alterar_status_aceita_transicoes_permitidas(
    status_atual: StatusSolicitacao,
    novo_status: StatusSolicitacao,
) -> None:
    solicitacao = make_solicitacao(status_atual)

    result = FiscalDomainService.alterar_status(
        solicitacao,
        novo_status,
    )

    assert result is solicitacao
    assert result.status == novo_status


@pytest.mark.parametrize(
    ("status_atual", "novo_status"),
    [
        (
            StatusSolicitacao.RECEBIDA,
            StatusSolicitacao.EMITIDA,
        ),
        (
            StatusSolicitacao.EM_VALIDACAO,
            StatusSolicitacao.PROCESSANDO,
        ),
        (
            StatusSolicitacao.VALIDADA,
            StatusSolicitacao.EMITIDA,
        ),
        (
            StatusSolicitacao.EMITIDA,
            StatusSolicitacao.CANCELADA,
        ),
        (
            StatusSolicitacao.CANCELADA,
            StatusSolicitacao.RECEBIDA,
        ),
    ],
)
def test_alterar_status_rejeita_transicoes_nao_permitidas(
    status_atual: StatusSolicitacao,
    novo_status: StatusSolicitacao,
) -> None:
    solicitacao = make_solicitacao(status_atual)

    with pytest.raises(
        TransicaoStatusInvalidaError,
        match="Transição de",
    ):
        FiscalDomainService.alterar_status(
            solicitacao,
            novo_status,
        )

    assert solicitacao.status == status_atual


def test_alterar_status_rejeita_repeticao_do_status_atual() -> None:
    solicitacao = make_solicitacao(
        StatusSolicitacao.RECEBIDA,
    )

    with pytest.raises(TransicaoStatusInvalidaError):
        FiscalDomainService.alterar_status(
            solicitacao,
            StatusSolicitacao.RECEBIDA,
        )

    assert solicitacao.status == StatusSolicitacao.RECEBIDA
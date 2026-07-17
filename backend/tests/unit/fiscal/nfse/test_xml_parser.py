from __future__ import annotations

from datetime import date
from decimal import Decimal
from pathlib import Path

import pytest

from app.modules.fiscal.nfse.xml.parser import (
    NFSeXMLParser,
)


FIXTURES_DIR = Path(
    "tests/fixtures/nfse/hospital"
)


def parse_fixture(
    filename: str,
):
    parser = NFSeXMLParser()

    return parser.parse(
        FIXTURES_DIR / filename
    )


def test_parser_reads_nfse_number():
    document = parse_fixture(
        "nfse_6138.xml"
    )

    assert document.numero_nfse == "6138"


def test_parser_reads_service_value():
    document = parse_fixture(
        "nfse_6138.xml"
    )

    assert (
        document.valores.valor_servico
        == Decimal("234950.39")
    )


def test_parser_reads_provider():
    document = parse_fixture(
        "nfse_6138.xml"
    )

    provider = document.prestador

    assert provider.tipo_documento == "CNPJ"
    assert provider.documento == "12971279000130"
    assert provider.inscricao_municipal == "0766024100100"
    assert (
        provider.nome
        == "PRIME HEALTH SERVICOS MEDICO-HOSPITALARES "
        "E PARTICIPACOES LTDA"
    )


def test_parser_reads_recipient():
    document = parse_fixture(
        "nfse_6138.xml"
    )

    recipient = document.tomador

    assert recipient.tipo_documento == "CNPJ"
    assert recipient.documento == "61590410000558"
    assert recipient.inscricao_municipal == "0757742800286"
    assert (
        recipient.nome
        == "SOCIEDADE BENEFICENTE DE SENHORAS "
        "- HOSPITAL SIRIO LIBANES"
    )
    assert recipient.email == "ouvidoria@hsl.org.br"
    assert recipient.telefone == "6121414000"


def test_parser_reads_national_tax_code():
    document = parse_fixture(
        "nfse_6138.xml"
    )

    assert (
        document.servico.codigo_tributacao_nacional
        == "040101"
    )


def test_parser_reads_municipal_tax_code():
    document = parse_fixture(
        "nfse_6138.xml"
    )

    assert (
        document.servico.codigo_tributacao_municipal
        == "401"
    )


def test_parser_reads_nbs_code():
    document = parse_fixture(
        "nfse_6138.xml"
    )

    assert document.servico.codigo_nbs == "123012200"


@pytest.mark.parametrize(
    (
        "filename",
        "numero_nfse",
        "valor_servico",
        "valor_liquido",
    ),
    [
        (
            "nfse_6044.xml",
            "6044",
            Decimal("202699.00"),
            Decimal("186179.03"),
        ),
        (
            "nfse_6123.xml",
            "6123",
            Decimal("2.00"),
            Decimal("2.00"),
        ),
    ],
)
def test_parser_reads_identification_and_values(
    filename: str,
    numero_nfse: str,
    valor_servico: Decimal,
    valor_liquido: Decimal,
):
    document = parse_fixture(
        filename
    )

    assert document.numero_nfse == numero_nfse
    assert document.valores.valor_servico == valor_servico
    assert document.valores.valor_liquido == valor_liquido


@pytest.mark.parametrize(
    (
        "filename",
        "valor_iss",
        "valor_irrf",
        "valor_csll",
        "valor_total_retencoes",
        "iss_retido",
        "pis_cofins_retidos",
    ),
    [
        (
            "nfse_6044.xml",
            Decimal("4053.98"),
            Decimal("3040.49"),
            Decimal("9425.50"),
            Decimal("16519.97"),
            True,
            True,
        ),
        (
            "nfse_6123.xml",
            Decimal("0.04"),
            Decimal("0"),
            Decimal("0"),
            Decimal("0"),
            False,
            False,
        ),
    ],
)
def test_parser_reads_taxes(
    filename: str,
    valor_iss: Decimal,
    valor_irrf: Decimal,
    valor_csll: Decimal,
    valor_total_retencoes: Decimal,
    iss_retido: bool,
    pis_cofins_retidos: bool,
):
    document = parse_fixture(
        filename
    )

    taxes = document.tributos

    assert taxes.aliquota_iss == Decimal("2.00")
    assert taxes.valor_iss == valor_iss
    assert taxes.valor_irrf == valor_irrf
    assert taxes.valor_csll == valor_csll
    assert (
        taxes.valor_total_retencoes
        == valor_total_retencoes
    )
    assert taxes.iss_retido is iss_retido
    assert (
        taxes.pis_cofins_retidos
        is pis_cofins_retidos
    )


@pytest.mark.parametrize(
    (
        "filename",
        "numero_dps",
        "versao_aplicacao",
        "competencia",
    ),
    [
        (
            "nfse_6044.xml",
            "6044",
            "ISSNET v7.6.2.0",
            date(2026, 6, 12),
        ),
        (
            "nfse_6123.xml",
            "6123",
            "ISSNET v7.7.1.0",
            date(2026, 7, 9),
        ),
    ],
)
def test_parser_reads_metadata(
    filename: str,
    numero_dps: str,
    versao_aplicacao: str,
    competencia: date,
):
    document = parse_fixture(
        filename
    )

    assert document.numero_dps == numero_dps
    assert document.serie_dps == "70001"
    assert document.versao_aplicacao == versao_aplicacao
    assert document.ambiente == "1"
    assert document.status == "100"
    assert document.competencia == competencia
    assert document.local_emissao == "Brasília"
    assert document.local_prestacao == "Brasília"
    assert document.local_incidencia == "Brasília"


def test_parser_identifies_individual_recipient():
    document = parse_fixture(
        "nfse_6123.xml"
    )

    recipient = document.tomador

    assert recipient.tipo_documento == "CPF"
    assert recipient.documento == "04786760935"


@pytest.mark.parametrize(
    "filename",
    [
        "nfse_6044.xml",
        "nfse_6123.xml",
    ],
)
def test_parser_reads_service_classification(
    filename: str,
):
    document = parse_fixture(
        filename
    )

    service = document.servico

    assert service.codigo_tributacao_nacional == "040101"
    assert service.codigo_tributacao_municipal == "401"
    assert service.codigo_nbs == "123012200"
    assert service.local_prestacao == "5300108"
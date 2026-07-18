from datetime import date, datetime
from decimal import Decimal

import pytest

from app.modules.fiscal.nfse.interpretation import (
    InvalidNFSeDocumentError,
    NFSeBusinessDocument,
    NFSeInterpreter,
)
from app.modules.fiscal.nfse.xml.schemas import (
    NFSeParty,
    NFSeService,
    NFSeTaxes,
    NFSeValues,
    NFSeXMLDocument,
)


def make_xml_document(
    *,
    numero_nfse: str = "6044",
    prestador_documento: str = "07660241000100",
    tomador_documento: str = "12345678000190",
) -> NFSeXMLDocument:
    """
    Cria um documento XML controlado para os testes do interpreter.

    O objetivo desta fixture local é testar somente a transformação
    entre o modelo técnico XML e o modelo de negócio.
    """
    return NFSeXMLDocument(
        numero_nfse=numero_nfse,
        numero_dps="98765",
        serie_dps="1",
        versao_nfse="1.01",
        versao_dps="1.00",
        versao_aplicacao="ISSNET-DF",
        ambiente="PRODUCAO",
        status="EMITIDA",
        data_processamento=datetime(2026, 7, 17, 10, 35, 0),
        data_emissao=datetime(2026, 7, 17, 10, 30, 0),
        competencia=date(2026, 7, 1),
        local_emissao="Brasília/DF",
        local_prestacao="Brasília/DF",
        local_incidencia="Brasília/DF",
        prestador=NFSeParty(
            tipo_documento="CNPJ",
            documento=prestador_documento,
            inscricao_municipal="12345678",
            nome="DF Analysis Serviços Médicos Ltda.",
            nome_fantasia="DF Analysis",
            email="fiscal@dfanalysis.com.br",
            telefone="61999999999",
        ),
        tomador=NFSeParty(
            tipo_documento="CNPJ",
            documento=tomador_documento,
            inscricao_municipal="87654321",
            nome="Hospital Exemplo S.A.",
            nome_fantasia="Hospital Exemplo",
            email="financeiro@hospitalexemplo.com.br",
            telefone="6133333333",
        ),
        servico=NFSeService(
            codigo_tributacao_nacional="04.01",
            codigo_tributacao_municipal="0401",
            codigo_nbs="123456789",
            descricao="Prestação de serviços médicos.",
            informacoes_complementares="Serviços referentes à competência 07/2026.",
            local_prestacao="Brasília/DF",
        ),
        tributos=NFSeTaxes(
            aliquota_iss=Decimal("0.02"),
            iss_retido=True,
            pis_cofins_retidos=False,
            valor_iss=Decimal("200.00"),
            valor_irrf=Decimal("150.00"),
            valor_csll=Decimal("100.00"),
            valor_total_retencoes=Decimal("450.00"),
        ),
        valores=NFSeValues(
            valor_servico=Decimal("10000.00"),
            base_calculo=Decimal("10000.00"),
            valor_liquido=Decimal("9550.00"),
        ),
        observacoes=[
            "Documento processado pelo ISSNET.",
            "NFS-e emitida em ambiente de produção.",
        ],
    )


@pytest.fixture
def xml_document() -> NFSeXMLDocument:
    return make_xml_document()


@pytest.fixture
def business_document(
    xml_document: NFSeXMLDocument,
) -> NFSeBusinessDocument:
    return NFSeInterpreter().interpret(xml_document)


def test_interpreter_returns_business_document(
    business_document: NFSeBusinessDocument,
) -> None:
    assert isinstance(business_document, NFSeBusinessDocument)


def test_interpreter_preserves_identification(
    business_document: NFSeBusinessDocument,
) -> None:
    identification = business_document.identificacao

    assert identification.numero_nfse == "6044"
    assert identification.numero_dps == "98765"
    assert identification.serie_dps == "1"
    assert identification.data_emissao == datetime(2026, 7, 17, 10, 30, 0)
    assert identification.competencia == date(2026, 7, 1)
    assert identification.ambiente == "PRODUCAO"
    assert identification.status == "EMITIDA"


def test_interpreter_preserves_parties(
    business_document: NFSeBusinessDocument,
) -> None:
    prestador = business_document.prestador
    tomador = business_document.tomador

    assert prestador.tipo_documento == "CNPJ"
    assert prestador.documento == "07660241000100"
    assert prestador.inscricao_municipal == "12345678"
    assert prestador.nome == "DF Analysis Serviços Médicos Ltda."

    assert tomador.tipo_documento == "CNPJ"
    assert tomador.documento == "12345678000190"
    assert tomador.inscricao_municipal == "87654321"
    assert tomador.nome == "Hospital Exemplo S.A."


def test_interpreter_preserves_service(
    business_document: NFSeBusinessDocument,
) -> None:
    service = business_document.servico

    assert service.codigo_tributacao_nacional == "04.01"
    assert service.codigo_tributacao_municipal == "0401"
    assert service.codigo_nbs == "123456789"
    assert service.descricao == "Prestação de serviços médicos."
    assert service.local_prestacao == "Brasília/DF"


def test_interpreter_preserves_values_and_taxes(
    business_document: NFSeBusinessDocument,
) -> None:
    values = business_document.valores
    taxes = business_document.tributos

    assert values.valor_servico == Decimal("10000.00")
    assert values.base_calculo == Decimal("10000.00")
    assert values.valor_liquido == Decimal("9550.00")

    assert taxes.aliquota_iss == Decimal("0.02")
    assert taxes.iss_retido is True
    assert taxes.pis_cofins_retidos is False
    assert taxes.valor_iss == Decimal("200.00")
    assert taxes.valor_irrf == Decimal("150.00")
    assert taxes.valor_csll == Decimal("100.00")
    assert taxes.valor_total_retencoes == Decimal("450.00")


def test_interpreter_preserves_metadata(
    business_document: NFSeBusinessDocument,
) -> None:
    metadata = business_document.metadados

    assert metadata.versao_nfse == "1.01"
    assert metadata.versao_dps == "1.00"
    assert metadata.versao_aplicacao == "ISSNET-DF"
    assert metadata.data_processamento == datetime(2026, 7, 17, 10, 35, 0)
    assert metadata.local_emissao == "Brasília/DF"
    assert metadata.local_prestacao == "Brasília/DF"
    assert metadata.local_incidencia == "Brasília/DF"
    assert metadata.observacoes == (
        "Documento processado pelo ISSNET.",
        "NFS-e emitida em ambiente de produção.",
    )


@pytest.mark.parametrize(
    ("document", "expected_message"),
    [
        (
            make_xml_document(numero_nfse=""),
            "Número da NFS-e não informado.",
        ),
        (
            make_xml_document(prestador_documento=""),
            "Documento do prestador não informado.",
        ),
        (
            make_xml_document(tomador_documento=""),
            "Documento do tomador não informado.",
        ),
    ],
)
def test_interpreter_rejects_invalid_document(
    document: NFSeXMLDocument,
    expected_message: str,
) -> None:
    interpreter = NFSeInterpreter()

    with pytest.raises(
        InvalidNFSeDocumentError,
        match=expected_message,
    ):
        interpreter.interpret(document)
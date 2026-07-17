from pathlib import Path

from app.modules.fiscal.nfse.xml.parser import (
    NFSeXMLParser,
)


def test_parser_reads_nfse_number():
    parser = NFSeXMLParser()

    document = parser.parse(
        Path(
            "tests/fixtures/nfse/hospital/nfse_6138.xml"
        )
    )

    assert document.numero_nfse == "6138"


def test_parser_reads_service_value():
    parser = NFSeXMLParser()

    document = parser.parse(
        Path(
            "tests/fixtures/nfse/hospital/nfse_6138.xml"
        )
    )

    assert float(
        document.valores.valor_servico
    ) == 234950.39


def test_parser_reads_provider():
    parser = NFSeXMLParser()

    document = parser.parse(
        Path(
            "tests/fixtures/nfse/hospital/nfse_6138.xml"
        )
    )

    provider = document.prestador

    assert provider.tipo_documento == "CNPJ"
    assert provider.documento == "12971279000130"
    assert provider.inscricao_municipal == "0766024100100"
    assert (
        provider.nome
        == "PRIME HEALTH SERVICOS MEDICO-HOSPITALARES E PARTICIPACOES LTDA"
    )

def test_parser_reads_recipient():
    parser = NFSeXMLParser()

    document = parser.parse(
        Path(
            "tests/fixtures/nfse/hospital/nfse_6138.xml"
        )
    )

    recipient = document.tomador

    assert recipient.tipo_documento == "CNPJ"
    assert recipient.documento == "61590410000558"
    assert recipient.inscricao_municipal == "0757742800286"
    assert (
        recipient.nome
        == "SOCIEDADE BENEFICENTE DE SENHORAS - HOSPITAL SIRIO LIBANES"
    )
    assert recipient.email == "ouvidoria@hsl.org.br"
    assert recipient.telefone == "6121414000"

def test_parser_reads_national_tax_code():
    parser = NFSeXMLParser()

    document = parser.parse(
        Path("tests/fixtures/nfse/hospital/nfse_6138.xml")
    )

    assert document.servico.codigo_tributacao_nacional == "040101"

def test_parser_reads_municipal_tax_code():
    parser = NFSeXMLParser()

    document = parser.parse(
        Path("tests/fixtures/nfse/hospital/nfse_6138.xml")
    )

    assert document.servico.codigo_tributacao_municipal == "401"

def test_parser_reads_nbs_code():
    parser = NFSeXMLParser()

    document = parser.parse(
        Path("tests/fixtures/nfse/hospital/nfse_6138.xml")
    )

    assert document.servico.codigo_nbs == "123012200"
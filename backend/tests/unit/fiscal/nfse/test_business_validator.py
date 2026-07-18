from dataclasses import replace
from decimal import Decimal

import pytest

from app.modules.fiscal.nfse.domain.models import BusinessValidationResult
from app.modules.fiscal.nfse.domain.validator import BusinessValidator
from app.modules.fiscal.nfse.interpretation.models import (
    NFSeBusinessDocument,
    NFSeIdentification,
    NFSeMetadata,
    NFSeParty,
    NFSeService,
    NFSeTaxes,
    NFSeValues,
)


@pytest.fixture
def valid_business_document() -> NFSeBusinessDocument:
    return NFSeBusinessDocument(
        identificacao=NFSeIdentification(
            numero_nfse="6044",
            numero_dps="98765",
            serie_dps="1",
            ambiente="PRODUCAO",
            status="EMITIDA",
        ),
        prestador=NFSeParty(
            tipo_documento="CNPJ",
            documento="07660241000100",
            inscricao_municipal="12345678",
            nome="DF Analysis Serviços Médicos Ltda.",
        ),
        tomador=NFSeParty(
            tipo_documento="CNPJ",
            documento="12345678000190",
            inscricao_municipal="87654321",
            nome="Hospital Exemplo S.A.",
        ),
        servico=NFSeService(
            codigo_tributacao_nacional="04.01",
            codigo_tributacao_municipal="0401",
            descricao="Prestação de serviços médicos.",
            local_prestacao="Brasília/DF",
        ),
        valores=NFSeValues(
            valor_servico=Decimal("10000.00"),
            base_calculo=Decimal("10000.00"),
            valor_liquido=Decimal("9550.00"),
        ),
        tributos=NFSeTaxes(
            aliquota_iss=Decimal("0.02"),
            iss_retido=True,
            valor_iss=Decimal("200.00"),
        ),
        metadados=NFSeMetadata(
            versao_nfse="1.01",
            versao_aplicacao="ISSNET-DF",
            local_emissao="Brasília/DF",
        ),
    )


@pytest.fixture
def validator() -> BusinessValidator:
    return BusinessValidator()


def test_validator_accepts_valid_document(
    validator: BusinessValidator,
    valid_business_document: NFSeBusinessDocument,
) -> None:
    result = validator.validate(valid_business_document)

    assert isinstance(result, BusinessValidationResult)
    assert result.valid is True
    assert result.has_errors is False
    assert result.errors == []


def test_validator_rejects_missing_nfse_number(
    validator: BusinessValidator,
    valid_business_document: NFSeBusinessDocument,
) -> None:
    invalid_identification = replace(
        valid_business_document.identificacao,
        numero_nfse="",
    )

    invalid_document = replace(
        valid_business_document,
        identificacao=invalid_identification,
    )

    result = validator.validate(invalid_document)

    assert result.valid is False
    assert result.has_errors is True
    assert "Número da NFS-e não informado." in result.errors


def test_validator_rejects_missing_provider_document(
    validator: BusinessValidator,
    valid_business_document: NFSeBusinessDocument,
) -> None:
    invalid_provider = replace(
        valid_business_document.prestador,
        documento="",
    )

    invalid_document = replace(
        valid_business_document,
        prestador=invalid_provider,
    )

    result = validator.validate(invalid_document)

    assert result.valid is False
    assert "Documento do prestador não informado." in result.errors


def test_validator_rejects_missing_customer_document(
    validator: BusinessValidator,
    valid_business_document: NFSeBusinessDocument,
) -> None:
    invalid_customer = replace(
        valid_business_document.tomador,
        documento="",
    )

    invalid_document = replace(
        valid_business_document,
        tomador=invalid_customer,
    )

    result = validator.validate(invalid_document)

    assert result.valid is False
    assert "Documento do tomador não informado." in result.errors


@pytest.mark.parametrize(
    "description",
    [
        None,
        "",
        "   ",
    ],
)
def test_validator_rejects_missing_service_description(
    validator: BusinessValidator,
    valid_business_document: NFSeBusinessDocument,
    description: str | None,
) -> None:
    invalid_service = replace(
        valid_business_document.servico,
        descricao=description,
    )

    invalid_document = replace(
        valid_business_document,
        servico=invalid_service,
    )

    result = validator.validate(invalid_document)

    assert result.valid is False
    assert "Descrição do serviço não informada." in result.errors


@pytest.mark.parametrize(
    "service_value",
    [
        Decimal("0"),
        Decimal("-1.00"),
    ],
)
def test_validator_rejects_non_positive_service_value(
    validator: BusinessValidator,
    valid_business_document: NFSeBusinessDocument,
    service_value: Decimal,
) -> None:
    invalid_values = replace(
        valid_business_document.valores,
        valor_servico=service_value,
    )

    invalid_document = replace(
        valid_business_document,
        valores=invalid_values,
    )

    result = validator.validate(invalid_document)

    assert result.valid is False
    assert "Valor do serviço deve ser maior que zero." in result.errors


def test_validator_accumulates_multiple_errors(
    validator: BusinessValidator,
    valid_business_document: NFSeBusinessDocument,
) -> None:
    invalid_identification = replace(
        valid_business_document.identificacao,
        numero_nfse="",
    )

    invalid_provider = replace(
        valid_business_document.prestador,
        documento="",
    )

    invalid_customer = replace(
        valid_business_document.tomador,
        documento="",
    )

    invalid_service = replace(
        valid_business_document.servico,
        descricao="",
    )

    invalid_values = replace(
        valid_business_document.valores,
        valor_servico=Decimal("0"),
    )

    invalid_document = replace(
        valid_business_document,
        identificacao=invalid_identification,
        prestador=invalid_provider,
        tomador=invalid_customer,
        servico=invalid_service,
        valores=invalid_values,
    )

    result = validator.validate(invalid_document)

    assert result.valid is False
    assert result.has_errors is True
    assert len(result.errors) == 5

    assert result.errors == [
        "Número da NFS-e não informado.",
        "Documento do prestador não informado.",
        "Documento do tomador não informado.",
        "Descrição do serviço não informada.",
        "Valor do serviço deve ser maior que zero.",
    ]
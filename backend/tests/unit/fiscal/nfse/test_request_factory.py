from decimal import Decimal
from uuid import uuid4
from datetime import date

import pytest

from app.modules.fiscal.enums import OrigemSolicitacao
from app.modules.fiscal.nfse.application import EmissionRequestFactory
from app.modules.fiscal.nfse.interpretation.models import (
    NFSeBusinessDocument,
    NFSeIdentification,
    NFSeMetadata,
    NFSeParty,
    NFSeService,
    NFSeTaxes,
    NFSeValues,
)
from app.modules.fiscal.solicitacoes.schemas import (
    SolicitacaoEmissaoCreate,
)


@pytest.fixture
def business_document() -> NFSeBusinessDocument:
    return NFSeBusinessDocument(
        identificacao=NFSeIdentification(
            numero_nfse="6044",
            numero_dps="123",
            serie_dps="1",
            competencia=date(2026, 7, 1),
            ambiente="PRODUCAO",
            status="EMITIDA",
        ),
        prestador=NFSeParty(
            tipo_documento="CNPJ",
            documento="07660241000100",
            inscricao_municipal="123",
            nome="Prestador",
        ),
        tomador=NFSeParty(
            tipo_documento="CNPJ",
            documento="11111111000199",
            inscricao_municipal="456",
            nome="Hospital",
        ),
        servico=NFSeService(
            codigo_tributacao_nacional="4.01",
            codigo_tributacao_municipal="401",
            descricao="Serviços médicos",
            local_prestacao="Brasília",
        ),
        valores=NFSeValues(
            valor_servico=Decimal("1000.00"),
            base_calculo=Decimal("1000.00"),
            valor_liquido=Decimal("980.00"),
        ),
        tributos=NFSeTaxes(
            aliquota_iss=Decimal("0.02"),
            iss_retido=True,
            valor_iss=Decimal("20.00"),
        ),
        metadados=NFSeMetadata(
        versao_nfse="1.0",
        versao_aplicacao="ISSNET",
        local_emissao="Brasília",
        ),
    )


@pytest.fixture
def factory() -> EmissionRequestFactory:
    return EmissionRequestFactory()


def test_factory_returns_request_schema(
    factory: EmissionRequestFactory,
    business_document: NFSeBusinessDocument,
):
    empresa_id = uuid4()

    request = factory.from_business_document(
        document=business_document,
        empresa_id=empresa_id,
        origem=OrigemSolicitacao.EMAIL,
    )

    assert isinstance(request, SolicitacaoEmissaoCreate)


def test_factory_maps_all_fields(
    factory: EmissionRequestFactory,
    business_document: NFSeBusinessDocument,
):
    empresa_id = uuid4()

    request = factory.from_business_document(
        document=business_document,
        empresa_id=empresa_id,
        origem=OrigemSolicitacao.EMAIL,
        idempotency_key="abc123",
    )

    assert request.empresa_id == empresa_id
    assert request.origem == OrigemSolicitacao.EMAIL
    assert request.referencia_externa == "6044"
    assert request.idempotency_key == "abc123"
    assert request.competencia == date(2026, 7, 1)
    assert request.descricao_servico == "Serviços médicos"
    assert request.valor_servico == Decimal("1000.00")


def test_factory_accepts_missing_idempotency_key(
    factory: EmissionRequestFactory,
    business_document: NFSeBusinessDocument,
):
    request = factory.from_business_document(
        document=business_document,
        empresa_id=uuid4(),
        origem=OrigemSolicitacao.EMAIL,
    )

    assert request.idempotency_key is None
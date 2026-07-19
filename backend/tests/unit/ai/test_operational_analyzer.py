from types import SimpleNamespace
from unittest.mock import Mock
from uuid import uuid4

import pytest

from app.ai.exceptions import AIInvalidResponseError
from app.ai.operational_analyzer import (
    OperationalAIAnalyzer,
)
from app.modules.operacoes.evidence.models import (
    EvidenceBundle,
)


def build_bundle() -> EvidenceBundle:
    message = SimpleNamespace(
        correlation_id=uuid4(),
    )

    return EvidenceBundle(
        message=message,
        metadata={
            "canal": "EMAIL",
            "origem": "GMAIL",
            "message": {
                "assunto": "Solicitação de NFS-e",
                "corpo": "Favor emitir a nota.",
                "remetente": "hospital@example.com",
                "recebido_em": None,
            },
            "consolidated": {
                "valor": "1000.00",
            },
        },
    )


def test_analyze_returns_validated_response() -> None:
    provider = Mock()

    provider.generate_json.return_value = {
        "tipo_processo": "FATURAMENTO_HOSPITALAR",
        "necessita_faturamento": True,
        "necessita_emissao_nfse": True,
        "confianca": 0.91,
        "observacoes": [],
    }

    prompt_manager = Mock()
    prompt_manager.load.return_value = (
        "Analise a comunicação."
    )

    analyzer = OperationalAIAnalyzer(
        provider=provider,
        prompt_manager=prompt_manager,
    )

    result = analyzer.analyze(
        build_bundle(),
    )

    assert (
        result.tipo_processo
        == "FATURAMENTO_HOSPITALAR"
    )
    assert result.necessita_faturamento is True
    assert result.necessita_emissao_nfse is True
    assert result.confianca == 0.91

    prompt_manager.load.assert_called_once_with(
        "operacoes/analyze_communication_v1.md",
    )

    provider.generate_json.assert_called_once()


def test_analyze_rejects_invalid_operational_response() -> None:
    provider = Mock()

    provider.generate_json.return_value = {
        "confianca": 2.5,
    }

    prompt_manager = Mock()
    prompt_manager.load.return_value = (
        "Analise a comunicação."
    )

    analyzer = OperationalAIAnalyzer(
        provider=provider,
        prompt_manager=prompt_manager,
    )

    with pytest.raises(AIInvalidResponseError):
        analyzer.analyze(
            build_bundle(),
        )

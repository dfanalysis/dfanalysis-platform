from datetime import UTC, datetime
from types import SimpleNamespace
from uuid import uuid4

from app.ai.context_builder import AIContextBuilder
from app.modules.operacoes.evidence.models import (
    EvidenceBundle,
)


def build_message():
    return SimpleNamespace(
        correlation_id=uuid4(),
    )


def test_build_context_from_bundle() -> None:
    message = build_message()

    recebido_em = datetime(
        2026,
        7,
        19,
        10,
        30,
        tzinfo=UTC,
    )

    bundle = EvidenceBundle(
        message=message,
        metadata={
            "canal": "EMAIL",
            "origem": "GMAIL",
            "message": {
                "assunto": "Emissão de NFS-e",
                "corpo": "Favor emitir a nota fiscal.",
                "remetente": "hospital@example.com",
                "recebido_em": recebido_em,
            },
            "operation_type": "FATURAMENTO_HOSPITALAR",
            "consolidated": {
                "valor": "1500.00",
            },
        },
    )

    context = AIContextBuilder().build(
        bundle,
    )

    assert context.correlation_id == message.correlation_id
    assert context.canal == "EMAIL"
    assert context.origem == "GMAIL"
    assert context.assunto == "Emissão de NFS-e"
    assert context.corpo == "Favor emitir a nota fiscal."
    assert context.remetente == "hospital@example.com"
    assert context.recebido_em == recebido_em
    assert (
        context.operation_type
        == "FATURAMENTO_HOSPITALAR"
    )
    assert context.consolidated == {
        "valor": "1500.00",
    }
    assert context.documents == []
    assert context.warnings == []


def test_build_context_does_not_expose_message_object() -> None:
    message = build_message()

    bundle = EvidenceBundle(
        message=message,
        metadata={
            "message": {
                "assunto": "Teste",
            },
        },
    )

    context = AIContextBuilder().build(
        bundle,
    )

    serialized = context.model_dump()

    assert "message" not in serialized
    assert "attachments" not in serialized

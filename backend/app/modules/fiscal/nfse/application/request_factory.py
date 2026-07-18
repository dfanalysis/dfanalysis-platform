from __future__ import annotations

from uuid import UUID

from app.modules.fiscal.enums import OrigemSolicitacao
from app.modules.fiscal.nfse.interpretation.models import (
    NFSeBusinessDocument,
)
from app.modules.fiscal.solicitacoes.schemas import (
    SolicitacaoEmissaoCreate,
)


class EmissionRequestFactory:
    """
    Converte um documento de domínio da NFS-e em um comando de
    criação de Solicitação de Emissão.

    Não executa validações de negócio nem persistência.
    """

    def from_business_document(
        self,
        *,
        document: NFSeBusinessDocument,
        empresa_id: UUID,
        origem: OrigemSolicitacao,
        idempotency_key: str | None = None,
    ) -> SolicitacaoEmissaoCreate:

        return SolicitacaoEmissaoCreate(
            empresa_id=empresa_id,
            origem=origem,
            referencia_externa=document.identificacao.numero_nfse,
            idempotency_key=idempotency_key,
            competencia=document.identificacao.competencia,
            descricao_servico=document.servico.descricao,
            valor_servico=document.valores.valor_servico,
        )
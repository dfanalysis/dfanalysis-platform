from __future__ import annotations

from app.modules.fiscal.solicitacoes.models import (
    SolicitacaoEmissao,
)
from app.modules.fiscal.solicitacoes.schemas import (
    SolicitacaoEmissaoCreate,
)


class SolicitacaoFactory:
    """
    Factory responsável por criar o Aggregate Root
    SolicitacaoEmissao a partir de um comando da aplicação.

    Não realiza validações de negócio nem persistência.
    """

    def create(
        self,
        payload: SolicitacaoEmissaoCreate,
    ) -> SolicitacaoEmissao:

        return SolicitacaoEmissao(
            empresa_id=payload.empresa_id,
            origem=payload.origem,
            referencia_externa=payload.referencia_externa,
            idempotency_key=payload.idempotency_key,
            competencia=payload.competencia,
            descricao_servico=payload.descricao_servico,
            valor_servico=payload.valor_servico,
        )
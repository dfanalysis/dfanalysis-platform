from datetime import date
from decimal import Decimal

from app.modules.empresas.models import Empresa
from app.modules.fiscal.enums import StatusSolicitacao
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


class FiscalDomainService:
    """Regras centrais do domínio fiscal."""

    @staticmethod
    def validar_empresa(empresa: Empresa | None) -> Empresa:
        """Valida se a empresa pode participar do processo fiscal."""

        if empresa is None:
            raise EmpresaNaoEncontradaError(
                "Empresa não encontrada.",
            )

        if empresa.deleted_at is not None or not empresa.is_active:
            raise EmpresaInativaError(
                "A empresa está inativa ou excluída.",
            )

        return empresa

    @staticmethod
    def validar_competencia(competencia: date) -> date:
        """Valida a competência informada para a solicitação."""

        if competencia > date.today():
            raise CompetenciaInvalidaError(
                "A competência não pode ser uma data futura.",
            )

        return competencia

    @staticmethod
    def validar_valor(valor_servico: Decimal) -> Decimal:
        """Valida o valor bruto solicitado para faturamento."""

        if valor_servico <= Decimal("0"):
            raise ValorServicoInvalidoError(
                "O valor do serviço deve ser maior que zero.",
            )

        return valor_servico

    @staticmethod
    def validar_descricao(descricao_servico: str) -> str:
        """Valida e normaliza a descrição fiscal do serviço."""

        descricao_normalizada = descricao_servico.strip()

        if len(descricao_normalizada) < 3:
            raise DescricaoServicoInvalidaError(
                "A descrição do serviço deve possuir ao menos 3 caracteres.",
            )

        return descricao_normalizada

    @staticmethod
    def alterar_status(
        solicitacao: SolicitacaoEmissao,
        novo_status: StatusSolicitacao,
    ) -> SolicitacaoEmissao:
        """Altera o status respeitando as transições permitidas."""

        transicoes_permitidas = {
            StatusSolicitacao.RECEBIDA: {
                StatusSolicitacao.EM_VALIDACAO,
                StatusSolicitacao.CANCELADA,
            },
            StatusSolicitacao.EM_VALIDACAO: {
                StatusSolicitacao.VALIDADA,
                StatusSolicitacao.REJEITADA,
                StatusSolicitacao.FALHA,
            },
            StatusSolicitacao.VALIDADA: {
                StatusSolicitacao.AGUARDANDO_PROCESSAMENTO,
                StatusSolicitacao.CANCELADA,
            },
            StatusSolicitacao.AGUARDANDO_PROCESSAMENTO: {
                StatusSolicitacao.PROCESSANDO,
                StatusSolicitacao.CANCELADA,
                StatusSolicitacao.FALHA,
            },
            StatusSolicitacao.PROCESSANDO: {
                StatusSolicitacao.EMITIDA,
                StatusSolicitacao.REJEITADA,
                StatusSolicitacao.FALHA,
            },
            StatusSolicitacao.REJEITADA: {
                StatusSolicitacao.EM_VALIDACAO,
                StatusSolicitacao.CANCELADA,
            },
            StatusSolicitacao.FALHA: {
                StatusSolicitacao.AGUARDANDO_PROCESSAMENTO,
                StatusSolicitacao.CANCELADA,
            },
            StatusSolicitacao.EMITIDA: set(),
            StatusSolicitacao.CANCELADA: set(),
        }

        status_permitidos = transicoes_permitidas[
            solicitacao.status
        ]

        if novo_status not in status_permitidos:
            raise TransicaoStatusInvalidaError(
                f"Transição de '{solicitacao.status.value}' "
                f"para '{novo_status.value}' não permitida.",
            )

        solicitacao.status = novo_status
        return solicitacao

    @staticmethod
    def verificar_idempotencia(
        solicitacao_existente: SolicitacaoEmissao | None,
    ) -> None:
        """Garante que a chave de idempotência ainda não foi utilizada."""

        if solicitacao_existente is not None:
            raise IdempotencyConflictError(
                "Já existe uma solicitação para esta chave de idempotência.",
            )
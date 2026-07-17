from app.modules.operacoes.cases.enums import (
    EtapaOperationalCase,
    StatusOperationalCase,
)
from app.modules.operacoes.cases.models import OperationalCase


class OperationalCaseDomainService:
    """Regras centrais do ciclo de vida do OperationalCase."""

    @staticmethod
    def send_to_analysis(
        case: OperationalCase,
    ) -> OperationalCase:
        """Encaminha o processo para análise e conferência."""

        if case.status in {
            StatusOperationalCase.CONCLUIDO,
            StatusOperationalCase.CANCELADO,
        }:
            raise ValueError(
                "Um processo concluído ou cancelado não pode voltar para análise.",
            )

        case.status = StatusOperationalCase.EM_ANALISE
        case.etapa = EtapaOperationalCase.CONFERENCIA

        return case

    @staticmethod
    def start_execution(
        case: OperationalCase,
    ) -> OperationalCase:
        """Inicia oficialmente a execução operacional."""

        if case.status not in {
            StatusOperationalCase.ABERTO,
            StatusOperationalCase.EM_ANALISE,
            StatusOperationalCase.AGUARDANDO_TERCEIROS,
        }:
            raise ValueError(
                "O processo não pode entrar em execução no estado atual.",
            )

        case.status = StatusOperationalCase.EM_EXECUCAO
        case.etapa = EtapaOperationalCase.CONFERENCIA

        return case

    @staticmethod
    def wait_for_third_party(
        case: OperationalCase,
        etapa: EtapaOperationalCase,
    ) -> OperationalCase:
        """Registra que o processo depende de uma ação externa."""

        if case.status != StatusOperationalCase.EM_EXECUCAO:
            raise ValueError(
                "Somente processos em execução podem aguardar terceiros.",
            )

        case.status = StatusOperationalCase.AGUARDANDO_TERCEIROS
        case.etapa = etapa

        return case

    @staticmethod
    def advance_to(
        case: OperationalCase,
        etapa: EtapaOperationalCase,
    ) -> OperationalCase:
        """Altera a etapa atual sem encerrar o processo."""

        if case.status in {
            StatusOperationalCase.CONCLUIDO,
            StatusOperationalCase.CANCELADO,
        }:
            raise ValueError(
                "Não é possível avançar um processo concluído ou cancelado.",
            )

        case.status = StatusOperationalCase.EM_EXECUCAO
        case.etapa = etapa

        return case

    @staticmethod
    def can_be_completed(
        case: OperationalCase,
    ) -> bool:
        """Verifica se o processo pode ser concluído."""

        return (
            case.status == StatusOperationalCase.EM_EXECUCAO
            and case.etapa
            in {
                EtapaOperationalCase.DEMONSTRATIVO,
                EtapaOperationalCase.ENCERRAMENTO,
            }
        )

    @staticmethod
    def complete(
        case: OperationalCase,
    ) -> OperationalCase:
        """Encerra oficialmente o processo operacional."""

        if not OperationalCaseDomainService.can_be_completed(case):
            raise ValueError(
                "O processo ainda não atingiu uma etapa que permita sua conclusão.",
            )

        case.status = StatusOperationalCase.CONCLUIDO
        case.etapa = EtapaOperationalCase.ENCERRAMENTO

        return case

    @staticmethod
    def cancel(
        case: OperationalCase,
    ) -> OperationalCase:
        """Cancela um processo operacional ainda ativo."""

        if case.status == StatusOperationalCase.CONCLUIDO:
            raise ValueError(
                "Um processo concluído não pode ser cancelado.",
            )

        case.status = StatusOperationalCase.CANCELADO
        case.etapa = EtapaOperationalCase.ENCERRAMENTO

        return case
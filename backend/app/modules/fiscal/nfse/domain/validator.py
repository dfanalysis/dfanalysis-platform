from __future__ import annotations

from app.modules.fiscal.nfse.domain.models import BusinessValidationResult
from app.modules.fiscal.nfse.interpretation.models import NFSeBusinessDocument


class BusinessValidator:
    """
    Executa validações de domínio sobre um documento NFS-e.

    Esta classe não possui dependências externas e não realiza
    acesso a banco de dados, APIs ou infraestrutura.
    """

    def validate(
        self,
        document: NFSeBusinessDocument,
    ) -> BusinessValidationResult:

        result = BusinessValidationResult()

        self._validate_identification(document, result)
        self._validate_parties(document, result)
        self._validate_service(document, result)
        self._validate_values(document, result)

        return result

    def _validate_identification(
        self,
        document: NFSeBusinessDocument,
        result: BusinessValidationResult,
    ) -> None:

        if not document.identificacao.numero_nfse:
            result.add_error("Número da NFS-e não informado.")

    def _validate_parties(
        self,
        document: NFSeBusinessDocument,
        result: BusinessValidationResult,
    ) -> None:

        if not document.prestador.documento:
            result.add_error("Documento do prestador não informado.")

        if not document.tomador.documento:
            result.add_error("Documento do tomador não informado.")

    def _validate_service(
        self,
        document: NFSeBusinessDocument,
        result: BusinessValidationResult,
    ) -> None:

        descricao = (document.servico.descricao or "").strip()

        if not descricao:
            result.add_error("Descrição do serviço não informada.")

    def _validate_values(
        self,
        document: NFSeBusinessDocument,
        result: BusinessValidationResult,
    ) -> None:

        if document.valores.valor_servico <= 0:
            result.add_error("Valor do serviço deve ser maior que zero.")
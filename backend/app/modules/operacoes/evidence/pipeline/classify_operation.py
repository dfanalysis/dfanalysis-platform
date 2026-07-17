from app.modules.operacoes.cases.enums import (
    TipoOperationalCase,
)
from app.modules.operacoes.evidence.models import (
    EvidenceBundle,
)


class ClassifyOperation:
    """
    Classifica qual processo operacional
    deverá ser iniciado.
    """

    def execute(
        self,
        bundle: EvidenceBundle,
    ) -> EvidenceBundle:
        consolidated = bundle.metadata.get(
            "consolidated",
            {},
        )

        operation = self._classify(
            consolidated,
        )

        bundle.metadata["operation_type"] = operation

        return bundle

    def _classify(
        self,
        data: dict,
    ) -> TipoOperationalCase:
        descricao = (
            str(data.get("descricao", ""))
            .lower()
            .strip()
        )

        assunto = (
            str(data.get("assunto", ""))
            .lower()
            .strip()
        )

        texto = f"{descricao} {assunto}"

        if (
            "nota fiscal" in texto
            or "nfse" in texto
            or "nfs-e" in texto
            or "faturamento" in texto
        ):
            return TipoOperationalCase.FATURAMENTO_HOSPITALAR

        if "repasse" in texto:
            return TipoOperationalCase.REPASSE_MEDICO

        if (
            "recebimento" in texto
            or "pagamento" in texto
            or "conciliação" in texto
            or "conciliacao" in texto
        ):
            return TipoOperationalCase.RECEBIMENTO_FINANCEIRO

        if (
            "contrato" in texto
            or "aditivo" in texto
        ):
            return TipoOperationalCase.CONTRATO

        if (
            "credenciamento" in texto
            or "credenciar" in texto
        ):
            return TipoOperationalCase.CREDENCIAMENTO

        if (
            "cadastro" in texto
            or "cadastral" in texto
        ):
            return TipoOperationalCase.CADASTRO

        return TipoOperationalCase.FATURAMENTO_HOSPITALAR
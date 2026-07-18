from __future__ import annotations

from app.modules.fiscal.nfse.interpretation.exceptions import (
    InvalidNFSeDocumentError,
)
from app.modules.fiscal.nfse.interpretation.models import (
    NFSeBusinessDocument,
    NFSeIdentification,
    NFSeMetadata,
    NFSeParty,
    NFSeService,
    NFSeTaxes,
    NFSeValues,
)
from app.modules.fiscal.nfse.xml.schemas import (
    NFSeParty as XMLParty,
)
from app.modules.fiscal.nfse.xml.schemas import (
    NFSeXMLDocument,
)


class NFSeInterpreter:
    """
    Traduz um NFSeXMLDocument para um
    NFSeBusinessDocument.

    Esta camada representa a interpretação
    do documento fiscal.

    Não conhece banco de dados.

    Não conhece FastAPI.

    Não conhece ISSNET.

    Não conhece SQLAlchemy.

    Apenas interpreta o documento.
    """

    def interpret(
        self,
        document: NFSeXMLDocument,
    ) -> NFSeBusinessDocument:
        """
        Interpreta um documento fiscal.

        Parameters
        ----------
        document:
            Documento produzido pelo parser XML.

        Returns
        -------
        NFSeBusinessDocument
        """

        self._validate(document)

        return NFSeBusinessDocument(
            identificacao=self._identification(document),
            prestador=self._party(document.prestador),
            tomador=self._party(document.tomador),
            servico=self._service(document),
            valores=self._values(document),
            tributos=self._taxes(document),
            metadados=self._metadata(document),
        )

    def _validate(
        self,
        document: NFSeXMLDocument,
    ) -> None:

        if not document.numero_nfse:
            raise InvalidNFSeDocumentError(
                "Número da NFS-e não informado."
            )

        if not document.prestador.documento:
            raise InvalidNFSeDocumentError(
                "Documento do prestador não informado."
            )

        if not document.tomador.documento:
            raise InvalidNFSeDocumentError(
                "Documento do tomador não informado."
            )

    def _identification(
        self,
        document: NFSeXMLDocument,
    ) -> NFSeIdentification:

        return NFSeIdentification(
            numero_nfse=document.numero_nfse,
            numero_dps=document.numero_dps,
            serie_dps=document.serie_dps,
            data_emissao=document.data_emissao,
            competencia=document.competencia,
            ambiente=document.ambiente,
            status=document.status,
        )

    def _party(
        self,
        party: XMLParty,
    ) -> NFSeParty:

        return NFSeParty(
            tipo_documento=party.tipo_documento,
            documento=party.documento,
            inscricao_municipal=party.inscricao_municipal,
            nome=party.nome,
            nome_fantasia=party.nome_fantasia,
            email=party.email,
            telefone=party.telefone,
        )

    def _service(
        self,
        document: NFSeXMLDocument,
    ) -> NFSeService:

        return NFSeService(
            codigo_tributacao_nacional=document.servico.codigo_tributacao_nacional,
            codigo_tributacao_municipal=document.servico.codigo_tributacao_municipal,
            codigo_nbs=document.servico.codigo_nbs,
            descricao=document.servico.descricao,
            informacoes_complementares=document.servico.informacoes_complementares,
            local_prestacao=document.servico.local_prestacao,
        )

    def _values(
        self,
        document: NFSeXMLDocument,
    ) -> NFSeValues:

        return NFSeValues(
            valor_servico=document.valores.valor_servico,
            base_calculo=document.valores.base_calculo,
            valor_liquido=document.valores.valor_liquido,
        )

    def _taxes(
        self,
        document: NFSeXMLDocument,
    ) -> NFSeTaxes:

        return NFSeTaxes(
            aliquota_iss=document.tributos.aliquota_iss,
            iss_retido=document.tributos.iss_retido,
            pis_cofins_retidos=document.tributos.pis_cofins_retidos,
            valor_iss=document.tributos.valor_iss,
            valor_irrf=document.tributos.valor_irrf,
            valor_csll=document.tributos.valor_csll,
            valor_total_retencoes=document.tributos.valor_total_retencoes,
        )

    def _metadata(
        self,
        document: NFSeXMLDocument,
    ) -> NFSeMetadata:

        return NFSeMetadata(
            versao_nfse=document.versao_nfse,
            versao_dps=document.versao_dps,
            versao_aplicacao=document.versao_aplicacao,
            data_processamento=document.data_processamento,
            local_emissao=document.local_emissao,
            local_prestacao=document.local_prestacao,
            local_incidencia=document.local_incidencia,
            observacoes=tuple(document.observacoes),
        )
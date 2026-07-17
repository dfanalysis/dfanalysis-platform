from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from pathlib import Path
import xml.etree.ElementTree as ET

from app.modules.fiscal.nfse.xml.schemas import (
    NFSeParty,
    NFSeService,
    NFSeTaxes,
    NFSeValues,
    NFSeXMLDocument,
)


class NFSeXMLParser:
    """
    Parser da NFS-e em XML.

    Extrai:
    - identificação da NFS-e e da DPS;
    - versões e ambiente;
    - datas e competência;
    - locais relacionados à prestação;
    - dados do prestador;
    - dados do tomador;
    - dados do serviço;
    - valores financeiros;
    - tributos e retenções.
    """

    def parse(
        self,
        xml_path: Path,
    ) -> NFSeXMLDocument:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        nfse_xml = self._find(
            root,
            "NFSe",
        )

        dps_xml = self._find(
            root,
            "DPS",
        )

        emit = self._find(
            root,
            "emit",
        )

        toma = self._find(
            root,
            "toma",
        )

        servico_xml = self._find(
            root,
            "serv",
        )

        valores_servico_xml = self._find(
            root,
            "vServPrest",
        )

        valores_nfse_xml = self._find(
            root,
            "valores",
        )

        tributos_municipais_xml = self._find(
            dps_xml,
            "tribMun",
        )

        tributos_federais_xml = self._find(
            dps_xml,
            "tribFed",
        )

        return NFSeXMLDocument(
            numero_nfse=self._text(
                root,
                "nNFSe",
            ),
            numero_dps=self._optional_text(
                dps_xml,
                "nDPS",
            ),
            serie_dps=self._optional_text(
                dps_xml,
                "serie",
            ),
            versao_nfse=self._attribute(
                nfse_xml,
                "versao",
            ),
            versao_dps=self._attribute(
                dps_xml,
                "versao",
            ),
            versao_aplicacao=self._optional_text(
                root,
                "verAplic",
            ),
            ambiente=self._optional_text(
                dps_xml,
                "tpAmb",
            ),
            status=self._optional_text(
                root,
                "cStat",
            ),
            data_processamento=self._parse_datetime(
                self._optional_text(
                    root,
                    "dhProc",
                )
            ),
            data_emissao=self._parse_datetime(
                self._optional_text(
                    dps_xml,
                    "dhEmi",
                )
            ),
            competencia=self._parse_date(
                self._optional_text(
                    dps_xml,
                    "dCompet",
                )
            ),
            local_emissao=self._optional_text(
                root,
                "xLocEmi",
            ),
            local_prestacao=self._optional_text(
                root,
                "xLocPrestacao",
            ),
            local_incidencia=self._optional_text(
                root,
                "xLocIncid",
            ),
            prestador=self._parse_party(
                emit,
            ),
            tomador=self._parse_party(
                toma,
            ),
            servico=self._parse_service(
                servico_xml,
            ),
            tributos=self._parse_taxes(
                nfse_values_element=valores_nfse_xml,
                municipal_tax_element=tributos_municipais_xml,
                federal_tax_element=tributos_federais_xml,
            ),
            valores=self._parse_values(
                valores_servico_xml,
                valores_nfse_xml,
            ),
        )

    def _parse_party(
        self,
        element: ET.Element | None,
        tipo_documento: str = "CNPJ",
    ) -> NFSeParty:
        documento_cnpj = self._text(
            element,
            "CNPJ",
        )

        documento_cpf = self._text(
            element,
            "CPF",
        )

        if documento_cnpj:
            documento = documento_cnpj
            tipo_documento_identificado = "CNPJ"
        elif documento_cpf:
            documento = documento_cpf
            tipo_documento_identificado = "CPF"
        else:
            documento = ""
            tipo_documento_identificado = tipo_documento

        return NFSeParty(
            tipo_documento=tipo_documento_identificado,
            documento=documento,
            inscricao_municipal=self._optional_text(
                element,
                "IM",
            ),
            nome=self._optional_text(
                element,
                "xNome",
            ),
            nome_fantasia=self._optional_text(
                element,
                "xFant",
            ),
            email=self._optional_text(
                element,
                "email",
            ),
            telefone=self._optional_text(
                element,
                "fone",
            ),
        )

    def _parse_service(
        self,
        element: ET.Element | None,
    ) -> NFSeService:
        return NFSeService(
            codigo_tributacao_nacional=self._optional_text(
                element,
                "cTribNac",
            ),
            codigo_tributacao_municipal=self._optional_text(
                element,
                "cTribMun",
            ),
            codigo_nbs=self._optional_text(
                element,
                "cNBS",
            ),
            descricao=self._optional_text(
                element,
                "xDescServ",
            ),
            informacoes_complementares=self._optional_text(
                element,
                "xInfComp",
            ),
            local_prestacao=self._optional_text(
                element,
                "cLocPrestacao",
            ),
        )

    def _parse_values(
        self,
        servico_values_element: ET.Element | None,
        nfse_values_element: ET.Element | None,
    ) -> NFSeValues:
        return NFSeValues(
            valor_servico=Decimal(
                self._text(
                    servico_values_element,
                    "vServ",
                    "0",
                )
            ),
            base_calculo=Decimal(
                self._text(
                    nfse_values_element,
                    "vBC",
                    "0",
                )
            ),
            valor_liquido=Decimal(
                self._text(
                    nfse_values_element,
                    "vLiq",
                    "0",
                )
            ),
        )

    def _parse_taxes(
        self,
        nfse_values_element: ET.Element | None,
        municipal_tax_element: ET.Element | None,
        federal_tax_element: ET.Element | None,
    ) -> NFSeTaxes:
        """
        Extrai os tributos dos diferentes blocos do XML da NFS-e.

        Estrutura observada no padrão nacional utilizado pelo ISSNET:

        - infNFSe/valores:
            - vISSQN
            - vTotalRet

        - DPS/infDPS/valores/trib/tribMun:
            - pAliq
            - tpRetISSQN

        - DPS/infDPS/valores/trib/tribFed:
            - tpRetPisCofins
            - vRetIRRF
            - vRetCSLL
        """
        tipo_retencao_iss = self._text(
            municipal_tax_element,
            "tpRetISSQN",
            "1",
        )

        tipo_retencao_pis_cofins = self._text(
            federal_tax_element,
            "tpRetPisCofins",
            "0",
        )

        return NFSeTaxes(
            aliquota_iss=Decimal(
                self._text(
                    municipal_tax_element,
                    "pAliq",
                    "0",
                )
            ),
            valor_iss=Decimal(
                self._text(
                    nfse_values_element,
                    "vISSQN",
                    "0",
                )
            ),
            valor_irrf=Decimal(
                self._text(
                    federal_tax_element,
                    "vRetIRRF",
                    "0",
                )
            ),
            valor_csll=Decimal(
                self._text(
                    federal_tax_element,
                    "vRetCSLL",
                    "0",
                )
            ),
            valor_total_retencoes=Decimal(
                self._text(
                    nfse_values_element,
                    "vTotalRet",
                    "0",
                )
            ),
            iss_retido=tipo_retencao_iss in {"2", "3"},
            pis_cofins_retidos=tipo_retencao_pis_cofins != "0",
        )

    @staticmethod
    def _parse_datetime(
        value: str | None,
    ) -> datetime | None:
        if not value:
            return None

        return datetime.fromisoformat(value)

    @staticmethod
    def _parse_date(
        value: str | None,
    ) -> date | None:
        if not value:
            return None

        return date.fromisoformat(value)

    @staticmethod
    def _attribute(
        element: ET.Element | None,
        attribute: str,
    ) -> str | None:
        if element is None:
            return None

        value = element.attrib.get(attribute)

        if value is None:
            return None

        normalized_value = value.strip()

        return normalized_value or None

    @staticmethod
    def _find(
        root: ET.Element | None,
        tag: str,
    ) -> ET.Element | None:
        if root is None:
            return None

        for element in root.iter():
            local_name = element.tag.rsplit("}", 1)[-1]

            if local_name == tag:
                return element

        return None

    @classmethod
    def _optional_text(
        cls,
        root: ET.Element | None,
        tag: str,
    ) -> str | None:
        value = cls._text(
            root,
            tag,
        )

        return value or None

    @staticmethod
    def _text(
        root: ET.Element | None,
        tag: str,
        default: str = "",
    ) -> str:
        if root is None:
            return default

        for element in root.iter():
            local_name = element.tag.rsplit("}", 1)[-1]

            if local_name == tag:
                return (element.text or default).strip()

        return default
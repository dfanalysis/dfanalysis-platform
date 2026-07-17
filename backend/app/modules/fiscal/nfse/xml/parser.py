from __future__ import annotations

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
    - número da NFS-e;
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

        return NFSeXMLDocument(
            numero_nfse=self._text(
                root,
                "nNFSe",
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
                valores_nfse_xml,
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
        return NFSeParty(
            tipo_documento=tipo_documento,
            documento=self._text(
                element,
                "CNPJ",
            ),
            inscricao_municipal=self._text(
                element,
                "IM",
            ),
            nome=self._text(
                element,
                "xNome",
            ),
            nome_fantasia=self._text(
                element,
                "xFant",
            ),
            email=self._text(
                element,
                "email",
            ),
            telefone=self._text(
                element,
                "fone",
            ),
        )

    def _parse_service(
        self,
        element: ET.Element | None,
    ) -> NFSeService:
        return NFSeService(
            codigo_tributacao_nacional=self._text(
                element,
                "cTribNac",
            ),
            codigo_tributacao_municipal=self._text(
                element,
                "cTribMun",
            ),
            codigo_nbs=self._text(
                element,
                "cNBS",
            ),
            descricao=self._text(
                element,
                "xDescServ",
            ),
            informacoes_complementares=self._text(
                element,
                "xInfComp",
            ),
            local_prestacao=self._text(
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
        element: ET.Element | None,
    ) -> NFSeTaxes:
        return NFSeTaxes(
            aliquota_iss=Decimal(
                self._text(
                    element,
                    "pAliq",
                    "0",
                )
            ),
            valor_iss=Decimal(
                self._text(
                    element,
                    "vISSQN",
                    "0",
                )
            ),
            valor_irrf=Decimal(
                self._text(
                    element,
                    "vRetIRRF",
                    "0",
                )
            ),
            valor_csll=Decimal(
                self._text(
                    element,
                    "vRetCSLL",
                    "0",
                )
            ),
            valor_total_retencoes=Decimal(
                self._text(
                    element,
                    "vTotalRet",
                    "0",
                )
            ),
            iss_retido=self._text(
                element,
                "tpRetISSQN",
                "1",
            )
            in {"2", "3"},
            pis_cofins_retidos=self._text(
                element,
                "tpRetPisCofins",
                "0",
            )
            != "0",
        )

    @staticmethod
    def _find(
        root: ET.Element,
        tag: str,
    ) -> ET.Element | None:
        for element in root.iter():
            local_name = element.tag.rsplit("}", 1)[-1]

            if local_name == tag:
                return element

        return None

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
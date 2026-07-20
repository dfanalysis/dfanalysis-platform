# Médico Executante

## Objetivo

Representa o papel exercido pelo Médico responsável pela execução efetiva do serviço médico relacionado a uma produção, solicitação, repasse ou NFS-e.

O Médico Executante não é necessariamente o emissor do documento fiscal. A emissão normalmente é realizada pela Empresa Médica à qual ele está vinculado.

## Quem pode assumir este papel

* Médico

## Responsabilidades

* Executar o atendimento ou procedimento médico.
* Ser identificado na produção correspondente.
* Permitir a vinculação entre serviço executado, Empresa Médica e Tomador.
* Compor a base de cálculo de repasses e demonstrativos individualizados.

## Relacionamentos

O Médico Executante:

* pode estar vinculado a uma ou mais Empresas Médicas;
* pode atuar em diferentes Hospitais e Clínicas;
* pode executar diversos procedimentos;
* pode constar em relatórios de produção;
* pode ser identificado na descrição de uma NFS-e;
* pode participar de processos de faturamento, conferência, cobrança e repasse.

## Regras de Negócio

* Deve possuir identificação profissional válida.
* Deve possuir CRM e UF de registro quando aplicável.
* Deve estar vinculado à Empresa Médica responsável pelo faturamento no período correspondente.
* Pode executar serviços para diferentes Tomadores.
* Pode possuir mais de um vínculo ativo simultaneamente.
* A identificação do Médico Executante não substitui a identificação fiscal do Prestador.
* Um processo pode envolver um ou vários Médicos Executantes.
* Uma NFS-e pode consolidar serviços executados por vários médicos, conforme o modelo operacional e as regras do Tomador.

## Informações relevantes

O vínculo do Médico Executante com uma produção pode conter:

* competência;
* período de execução;
* Hospital ou Clínica;
* procedimento;
* código TUSS;
* quantidade;
* valor bruto;
* descontos;
* tributos;
* taxa administrativa;
* valor de repasse;
* origem da informação;
* evidência documental.

## Observações

A separação entre Médico Executante e Prestador é essencial.

Exemplo:

* Médico Executante: profissional que realizou o atendimento;
* Prestador: Empresa Médica que emite a NFS-e;
* Tomador: Hospital ou Clínica que contratou o serviço;
* Solicitante: pessoa ou organização que encaminhou o pedido de emissão.

Essa distinção permitirá reutilizar o mesmo modelo nos módulos Fiscal, Faturamento Médico, Repasse, Cobrança, Credenciamento e Contratos.

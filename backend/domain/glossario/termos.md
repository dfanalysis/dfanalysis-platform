---

id: DOMAIN-GL-001
titulo: Glossário do Domínio
versao: 1.0.0
status: Em elaboração
ultima_atualizacao: 2026-07-19
responsavel: DF Analysis
------------------------

# Glossário do Domínio

## 1. Objetivo

Este documento estabelece a linguagem oficial utilizada no domínio da Plataforma DF Analysis IA.

As definições aqui registradas deverão orientar:

* documentação;
* código;
* banco de dados;
* APIs;
* prompts;
* agentes de Inteligência Artificial;
* integrações;
* comunicação entre áreas;
* testes funcionais.

Sempre que um termo possuir mais de um significado possível, deverá prevalecer a definição estabelecida neste glossário dentro do contexto correspondente.

---

# 2. Termos gerais

## Agente de Inteligência Artificial

Componente especializado da plataforma responsável por interpretar informações, aplicar conhecimento de domínio, recomendar decisões e participar da execução de processos.

Um agente não deve depender exclusivamente de respostas probabilísticas. Suas decisões devem combinar contexto, regras determinísticas, validações, permissões e auditoria.

---

## Automação

Execução total ou parcial de uma atividade por software, integração, workflow ou agente de Inteligência Artificial, com redução de intervenção manual.

---

## Contexto de negócio

Limite funcional dentro do qual termos, regras, entidades e processos possuem significado específico.

Exemplos:

* Faturamento;
* Fiscal;
* Financeiro;
* Administrativo;
* Comercial;
* Faturamento Assistencial.

---

## Empresa atendida

Pessoa jurídica que utiliza os serviços da DF Analysis ou da Plataforma DF Analysis IA.

Uma empresa atendida poderá possuir usuários, configurações, integrações, documentos, processos e regras próprias.

---

## Empresa médica

Pessoa jurídica constituída para prestação de serviços médicos.

A empresa médica poderá emitir documentos fiscais, receber honorários, realizar pagamentos, distribuir resultados e se relacionar com hospitais, clínicas, pacientes, cooperativas e outras empresas.

---

## Usuário

Pessoa autorizada a acessar a plataforma e executar ações conforme seus perfis e permissões.

---

## Processo

Conjunto ordenado de atividades destinadas a produzir um resultado de negócio.

---

## Macroprocesso

Agrupamento de processos relacionados a uma finalidade ampla.

Exemplo:

```text
Macroprocesso: Faturamento

Processos relacionados:
- recebimento da solicitação;
- validação;
- emissão;
- armazenamento;
- notificação.
```

---

## Regra de negócio

Condição, restrição, cálculo, decisão ou comportamento que representa uma exigência operacional, contratual, fiscal ou administrativa.

---

## Evidência

Informação utilizada para comprovar, fundamentar ou validar uma decisão da plataforma.

Exemplos:

* e-mail;
* mensagem;
* anexo;
* PDF;
* XML;
* planilha;
* imagem;
* protocolo;
* resposta de uma API.

---

## Rastreabilidade

Capacidade de identificar a origem, as alterações, as decisões, os responsáveis e os resultados de uma operação.

---

## Auditoria

Registro estruturado das ações executadas por usuários, sistemas, integrações e agentes de IA.

---

# 3. Termos do contexto de Faturamento

## Faturamento

Processo de emissão de documento fiscal pela empresa médica para formalização e recebimento dos serviços prestados.

No contexto da plataforma, Faturamento não significa o processamento de guias médicas perante operadoras de planos de saúde.

---

## Faturamento Assistencial

Processo realizado por clínicas, hospitais ou prestadores de saúde para cobrança de atendimentos perante operadoras de planos de saúde.

Pode envolver:

* guias;
* padrão TISS;
* XML TISS;
* lotes;
* protocolos;
* auditoria;
* glosas;
* recursos;
* pagamentos.

É um contexto independente do Faturamento de NFS-e.

---

## Produção médica

Conjunto de serviços, procedimentos, atendimentos, plantões ou atividades realizadas por um médico ou empresa médica durante determinado período.

A produção médica poderá ser utilizada como base para apuração de honorários e solicitação de emissão de NFS-e.

---

## Produção hospitalar

No contexto de emissão de NFS-e, representa a produção médica apurada por um hospital e utilizada para calcular os honorários devidos à empresa médica.

Não deve ser confundida com faturamento hospitalar de guias perante operadoras.

---

## Atendimento particular

Serviço prestado diretamente ao paciente, sem que o pagamento do honorário dependa da apuração de um hospital ou clínica.

A NFS-e poderá ser emitida diretamente para o CPF do paciente.

---

## Plantão médico

Período de trabalho médico prestado para hospital, clínica, empresa ou outra instituição contratante.

O plantão poderá gerar remuneração e posterior solicitação de emissão de NFS-e.

---

## Honorário médico

Valor devido pela prestação de serviço médico.

O honorário poderá ser apurado por atendimento, procedimento, plantão, produção, contrato, percentual ou outra regra previamente definida.

---

## Solicitação de emissão

Registro que representa o pedido de emissão de um documento fiscal.

A solicitação deverá possuir vínculo com a comunicação de origem, evidências, prestador, tomador, valor, competência e demais informações necessárias.

---

## Solicitante

Pessoa, empresa, instituição ou sistema que encaminha uma solicitação de emissão.

O solicitante não é necessariamente o tomador do serviço.

---

## Prestador

Pessoa jurídica responsável pela prestação do serviço e pela emissão da NFS-e.

No escopo inicial, o prestador será normalmente uma empresa médica.

---

## Tomador

Pessoa física ou jurídica que recebe o serviço e consta como destinatária da NFS-e.

Exemplos:

* hospital;
* clínica;
* paciente;
* cooperativa;
* empresa contratante.

---

## Competência

Período ao qual o serviço prestado se refere.

A competência não deve ser confundida automaticamente com:

* data de emissão;
* data de pagamento;
* data de recebimento da solicitação;
* data de envio do documento.

---

## Valor do serviço

Montante financeiro correspondente ao serviço que será documentado na NFS-e.

Deverá ser identificado e validado com base nas evidências disponíveis.

---

## Descrição do serviço

Texto inserido no documento fiscal para representar a natureza, o período e as características do serviço prestado.

Poderá conter:

* tipo de serviço;
* competência;
* médico executante;
* hospital ou clínica;
* unidade;
* referência contratual;
* outras informações exigidas.

---

## Modalidade de faturamento

Classificação da origem e da natureza operacional da emissão.

Exemplos:

* produção médica apurada por hospital;
* produção médica apurada por clínica;
* atendimento particular;
* plantão;
* prestação de serviços para empresa;
* cooperativa;
* convênio direto.

---

# 4. Termos fiscais

## NFS-e

Nota Fiscal de Serviços Eletrônica.

Documento fiscal eletrônico utilizado para registrar prestação de serviços sujeita às regras do município competente.

---

## RPS

Recibo Provisório de Serviços.

Documento utilizado para registrar provisoriamente uma prestação de serviço, podendo posteriormente ser convertido em NFS-e.

---

## ISS

Imposto Sobre Serviços de Qualquer Natureza.

Tributo municipal incidente sobre determinadas prestações de serviços.

---

## ISSNET

Sistema utilizado por municípios para gestão e emissão de documentos fiscais relacionados ao ISS.

No escopo inicial da plataforma, será utilizado para integração com o Distrito Federal.

---

## Sistema Nacional da NFS-e

Ambiente nacional destinado à emissão e gestão padronizada de NFS-e conforme adesão dos municípios.

---

## Código do serviço

Identificador da atividade ou serviço utilizado para emissão fiscal conforme regras do município e do provedor.

---

## Alíquota

Percentual utilizado para cálculo de determinado tributo.

---

## Retenção

Situação em que o tomador ou outro responsável realiza o recolhimento de determinado tributo em vez do prestador.

---

## Natureza da operação

Classificação fiscal utilizada para determinar características tributárias da prestação de serviços.

---

## Exigibilidade

Condição que define se o tributo é devido, suspenso, isento, imune ou sujeito a outro tratamento fiscal.

---

## CNAE

Classificação Nacional de Atividades Econômicas.

Identifica as atividades econômicas exercidas por uma empresa.

O CNAE não deve ser confundido automaticamente com o código de serviço municipal.

---

## Protocolo

Identificador gerado por um sistema externo ou interno para comprovar o envio, recebimento ou processamento de uma operação.

---

## Código de verificação

Código associado à NFS-e que permite validar sua autenticidade.

---

# 5. Termos financeiros

## Conta a receber

Registro financeiro que representa um valor devido à empresa.

A emissão de uma NFS-e poderá originar uma conta a receber, conforme as regras do contexto Financeiro.

---

## Recebimento

Entrada financeira correspondente à liquidação total ou parcial de um valor devido.

---

## Conciliação

Processo de comparação entre registros internos e movimentações financeiras externas, como extratos bancários ou relatórios de pagamento.

---

## Repasse médico

Transferência de valores devidos a médicos, sócios ou prestadores após aplicação das regras financeiras, contratuais e societárias.

---

## Inadimplência

Situação em que um valor devido não foi recebido até a data esperada.

---

# 6. Termos do Faturamento Assistencial

## Guia

Documento utilizado para registrar e solicitar autorização ou cobrança de um atendimento de saúde.

---

## TISS

Padrão de Troca de Informações na Saúde Suplementar.

Define estruturas, conceitos e formatos utilizados na comunicação entre prestadores e operadoras.

---

## XML TISS

Arquivo XML estruturado conforme o padrão TISS para envio de informações assistenciais às operadoras.

---

## Operadora

Pessoa jurídica responsável pela gestão de planos privados de assistência à saúde.

---

## Beneficiário

Pessoa vinculada a um plano de saúde que recebe atendimento assistencial.

---

## Lote

Agrupamento de guias ou contas assistenciais enviado para processamento por uma operadora.

---

## Glosa

Recusa total ou parcial de um valor faturado por uma operadora.

A glosa poderá decorrer de inconsistências cadastrais, técnicas, contratuais, documentais ou operacionais.

---

## Recurso de glosa

Processo de contestação de uma glosa com apresentação de justificativas e documentos.

---

## KonsistMed

Sistema utilizado para lançamento, processamento e geração de informações relacionadas ao faturamento assistencial.

---

# 7. Termos técnicos da plataforma

## Comunicação

Mensagem recebida ou enviada pela plataforma.

Pode ter origem em:

* e-mail;
* WhatsApp;
* API;
* webhook;
* sistema externo;
* lançamento manual.

---

## InboxMessage

Representação técnica de uma comunicação recebida pela plataforma.

---

## InboxAttachment

Representação técnica de um arquivo anexado a uma comunicação.

---

## EvidenceBundle

Conjunto organizado de evidências relacionadas a uma comunicação ou processo.

---

## Documento identificado

Arquivo cuja natureza foi classificada pela plataforma.

Exemplos:

* NFS-e;
* relatório de produção;
* solicitação;
* XML;
* planilha;
* comprovante;
* documento cadastral.

---

## Extração de dados

Processo de leitura e transformação de informações presentes em documentos ou mensagens em dados estruturados.

---

## Enriquecimento por IA

Uso de Inteligência Artificial para complementar a interpretação de uma comunicação ou conjunto de evidências.

---

## Regra determinística

Regra que produz resultado previsível a partir de condições objetivas.

Exemplos:

* validação de CPF ou CNPJ;
* comparação de valores;
* verificação de campos obrigatórios;
* prevenção de duplicidade;
* controle de permissões.

---

## Revisão humana

Intervenção de uma pessoa autorizada para validar, corrigir ou decidir sobre uma situação que não deve ser processada automaticamente.

---

## Integração

Comunicação estruturada entre a plataforma e um sistema externo.

---

## Provider

Componente responsável pela comunicação com um serviço externo específico.

Exemplos:

* provedor de IA;
* provedor municipal de NFS-e;
* provedor de e-mail;
* provedor de WhatsApp.

---

# 8. Regras de utilização do glossário

1. Um termo deverá possuir definição única dentro de cada contexto.

2. Quando o mesmo termo tiver significados distintos, o contexto deverá ser informado.

3. Novos termos deverão ser incluídos antes de serem utilizados de forma recorrente no código ou na documentação.

4. Termos técnicos não deverão substituir a linguagem operacional sem necessidade.

5. Abreviações deverão ser definidas em sua primeira utilização.

6. Nomes de classes, entidades, eventos e endpoints deverão refletir, sempre que possível, o vocabulário oficial do domínio.

---

# 9. Termos pendentes de detalhamento

Os seguintes conceitos deverão ser aprofundados em versões posteriores:

* produção;
* médico executante;
* unidade de atendimento;
* contrato;
* convênio direto;
* cooperativa;
* retenção tributária;
* município de incidência;
* cancelamento de NFS-e;
* substituição de NFS-e;
* duplicidade;
* autorização de emissão;
* credencial fiscal;
* evento financeiro;
* pendência operacional.

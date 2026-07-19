---

id: DOMAIN-MP-001
titulo: Macroprocesso de Faturamento
contexto: Faturamento
versao: 1.0.0
status: Em elaboração
ultima_atualizacao: 2026-07-19
responsavel: DF Analysis
------------------------

# Macroprocesso de Faturamento

## 1. Objetivo

O macroprocesso de Faturamento compreende as atividades necessárias para emitir documentos fiscais destinados ao recebimento pelos serviços prestados por empresas médicas.

Seu objetivo é transformar uma solicitação de faturamento válida em uma Nota Fiscal de Serviços Eletrônica — NFS-e — emitida, registrada, armazenada e encaminhada ao destinatário correto.

---

## 2. Definição

No domínio da Plataforma DF Analysis IA, o termo **Faturamento** representa o processo de emissão de documento fiscal pela empresa médica para cobrança ou formalização dos serviços prestados.

Esse processo pode ter como origem:

* produção médica apurada por hospital;
* produção médica apurada por clínica;
* atendimento particular;
* plantão médico;
* prestação de serviços para empresas;
* cooperativa;
* convênio direto;
* outra relação de prestação de serviços.

---

## 3. Limites do macroprocesso

### 3.1 Início

O processo inicia quando a plataforma recebe uma solicitação de emissão de documento fiscal.

A solicitação poderá ser recebida por:

* e-mail;
* WhatsApp;
* API;
* webhook;
* ERP;
* portal de hospital ou clínica;
* lançamento manual;
* integração com outro sistema.

### 3.2 Término

O processo é considerado concluído quando:

* a NFS-e foi emitida com sucesso;
* os documentos gerados foram armazenados;
* o protocolo e os dados da emissão foram registrados;
* o solicitante foi notificado;
* os eventos necessários foram disponibilizados aos demais contextos.

---

## 4. Fora do escopo

Este macroprocesso não contempla o faturamento assistencial realizado por clínicas ou hospitais perante operadoras de planos de saúde.

O faturamento assistencial envolve, entre outros elementos:

* guias de atendimento;
* padrão TISS;
* XML TISS;
* lotes;
* auditoria;
* glosas;
* reapresentações;
* portais de operadoras;
* pagamento de contas assistenciais.

Esse processo pertence ao contexto independente de **Faturamento Assistencial**.

---

## 5. Participantes

### 5.1 Empresa prestadora

Empresa médica responsável pela prestação do serviço e pela emissão da NFS-e.

### 5.2 Tomador do serviço

Pessoa física ou jurídica para quem a NFS-e será emitida.

Pode ser:

* hospital;
* clínica;
* paciente;
* empresa;
* cooperativa;
* instituição contratante.

### 5.3 Solicitante

Pessoa, empresa ou sistema que encaminha a solicitação de faturamento.

O solicitante pode ou não ser o tomador do serviço.

### 5.4 DF Analysis

Responsável pela gestão operacional, validação das informações, emissão fiscal, armazenamento dos documentos e acompanhamento do processo.

### 5.5 Plataforma DF Analysis IA

Responsável por receber, interpretar, validar, classificar, processar, registrar e acompanhar a solicitação.

---

## 6. Modalidades de faturamento

### 6.1 Produção médica apurada por hospital

O hospital apura os honorários devidos à empresa médica e solicita a emissão da NFS-e.

Fluxo simplificado:

```text
Hospital apura a produção médica
        ↓
Hospital envia a solicitação
        ↓
DF Analysis valida os dados
        ↓
Empresa médica emite a NFS-e
        ↓
Hospital realiza o pagamento
```

### 6.2 Produção médica apurada por clínica

A clínica apura os serviços ou honorários médicos e solicita a emissão da NFS-e.

Fluxo simplificado:

```text
Clínica apura os serviços
        ↓
Clínica envia a solicitação
        ↓
DF Analysis valida os dados
        ↓
Empresa médica emite a NFS-e
        ↓
Clínica realiza o pagamento
```

### 6.3 Atendimento particular

A empresa médica emite a NFS-e diretamente para o paciente atendido.

Fluxo simplificado:

```text
Paciente recebe o atendimento
        ↓
Dados fiscais são coletados
        ↓
Empresa médica emite a NFS-e
        ↓
Documento é enviado ao paciente
```

### 6.4 Plantão médico

A instituição contratante apura os plantões realizados e solicita a emissão da NFS-e pela empresa médica.

### 6.5 Prestação de serviços para empresa

A empresa médica presta serviços para uma pessoa jurídica e emite a NFS-e conforme contrato, competência ou medição.

### 6.6 Cooperativa ou convênio direto

A cooperativa ou entidade contratante solicita documento fiscal referente aos serviços prestados pela empresa médica.

---

## 7. Entradas

O macroprocesso pode receber:

* texto da solicitação;
* remetente;
* destinatários;
* assunto da comunicação;
* anexos;
* planilhas;
* PDFs;
* XMLs;
* imagens;
* relatórios de produção;
* demonstrativos;
* dados do prestador;
* dados do tomador;
* valor do serviço;
* competência;
* descrição solicitada;
* instruções específicas;
* dados contratuais.

---

## 8. Dados mínimos necessários

Antes da emissão, a plataforma deverá identificar ou obter:

* empresa prestadora;
* CNPJ do prestador;
* tomador do serviço;
* CPF ou CNPJ do tomador;
* município aplicável;
* valor do serviço;
* competência;
* descrição do serviço;
* código ou atividade do serviço;
* regras tributárias aplicáveis;
* origem da solicitação;
* documentos comprobatórios.

A obrigatoriedade exata de cada dado poderá variar conforme município, modalidade e regra fiscal.

---

## 9. Fluxo principal

```text
Recebimento da solicitação
        ↓
Registro da comunicação
        ↓
Armazenamento dos anexos
        ↓
Organização das evidências
        ↓
Identificação dos documentos
        ↓
Extração das informações
        ↓
Identificação da modalidade
        ↓
Identificação do prestador
        ↓
Identificação do tomador
        ↓
Validação dos dados
        ↓
Aplicação das regras fiscais
        ↓
Definição da competência
        ↓
Formação da descrição
        ↓
Emissão da NFS-e
        ↓
Validação do retorno
        ↓
Armazenamento de PDF, XML e protocolo
        ↓
Notificação do solicitante
        ↓
Disponibilização dos eventos financeiros e gerenciais
```

---

## 10. Etapas do processo

### 10.1 Receber a solicitação

A plataforma deverá registrar a comunicação recebida e preservar seu conteúdo original.

### 10.2 Armazenar evidências

Todos os anexos e documentos relacionados deverão ser armazenados com integridade, rastreabilidade e vínculo com a solicitação.

### 10.3 Interpretar a comunicação

A plataforma deverá identificar:

* intenção do solicitante;
* empresa médica envolvida;
* modalidade de faturamento;
* tomador;
* valor;
* competência;
* documentos presentes;
* informações ausentes;
* instruções relevantes.

### 10.4 Validar o prestador

A empresa médica deverá estar:

* cadastrada;
* ativa;
* autorizada para emissão;
* vinculada ao usuário ou operação;
* com credenciais e configurações válidas.

### 10.5 Validar o tomador

Os dados do tomador deverão ser conferidos conforme o cadastro existente, os documentos recebidos e as exigências fiscais aplicáveis.

### 10.6 Validar o valor

O valor da emissão deverá ser identificado de forma inequívoca e comparado com os documentos comprobatórios.

### 10.7 Definir a competência

A competência deverá representar o período ao qual os serviços prestados se referem.

Ela não deve ser confundida automaticamente com a data de emissão ou com a data de recebimento da solicitação.

### 10.8 Formar a descrição do serviço

A descrição deverá refletir corretamente:

* natureza do serviço;
* período ou competência;
* profissional executante, quando aplicável;
* unidade ou instituição relacionada, quando necessário;
* informações exigidas pelo tomador;
* regras fiscais e contratuais.

### 10.9 Aplicar regras fiscais

O contexto de Faturamento deverá consultar o contexto Fiscal para obter:

* código do serviço;
* alíquota;
* retenções;
* incidência do ISS;
* exigibilidade;
* natureza da operação;
* regras municipais;
* demais parâmetros necessários.

### 10.10 Emitir a NFS-e

A emissão deverá ocorrer por integração com o provedor municipal ou nacional aplicável.

Inicialmente, a prioridade será o ISSNET do Distrito Federal.

### 10.11 Validar o retorno

A plataforma deverá verificar:

* sucesso ou falha;
* número da NFS-e;
* código de verificação;
* protocolo;
* mensagens do provedor;
* PDF;
* XML;
* divergências entre a solicitação e a nota emitida.

### 10.12 Registrar e notificar

O resultado deverá ser registrado e o solicitante deverá receber a resposta adequada.

---

## 11. Validações obrigatórias

Antes da emissão, a plataforma deverá validar:

* existência da empresa prestadora;
* situação ativa do prestador;
* autorização para emissão;
* identificação do tomador;
* CPF ou CNPJ válido;
* valor maior que zero;
* competência identificada;
* descrição disponível;
* atividade fiscal configurada;
* município e provedor definidos;
* ausência de duplicidade;
* disponibilidade das credenciais;
* consistência entre solicitação e documentos.

---

## 12. Duplicidade

A plataforma deverá evitar emissão duplicada.

A análise de duplicidade poderá considerar:

* prestador;
* tomador;
* valor;
* competência;
* descrição;
* documento de origem;
* número de solicitação;
* protocolo externo;
* emissão já existente.

Quando houver suspeita de duplicidade, o processo deverá ser interrompido para validação.

---

## 13. Tratamento de inconsistências

A plataforma não deverá emitir automaticamente quando houver inconsistência relevante.

Exemplos:

* prestador não identificado;
* tomador divergente;
* valor divergente;
* competência ausente;
* múltiplos valores possíveis;
* documentos ilegíveis;
* ausência de configuração fiscal;
* credencial inválida;
* suspeita de duplicidade;
* solicitação incompatível com os anexos.

Nesses casos, a solicitação deverá ser classificada para revisão humana ou complementação de dados.

---

## 14. Estados do processo

A solicitação poderá assumir estados como:

* recebida;
* em processamento;
* aguardando documentos;
* aguardando validação;
* validada;
* pronta para emissão;
* em emissão;
* emitida;
* falha na emissão;
* cancelada;
* rejeitada;
* duplicidade identificada;
* revisão humana necessária.

Os estados oficiais deverão ser compatibilizados com o ciclo de vida já implementado no módulo fiscal.

---

## 15. Saídas

O macroprocesso poderá gerar:

* NFS-e emitida;
* PDF;
* XML;
* número da nota;
* código de verificação;
* protocolo;
* registro de auditoria;
* log de processamento;
* notificação;
* evento de conta a receber;
* evento para Business Intelligence;
* pendência de validação;
* relatório de erro.

---

## 16. Sistemas envolvidos

Dependendo do município e da modalidade:

* ISSNET;
* Sistema Nacional da NFS-e;
* ERP da empresa;
* sistemas hospitalares;
* sistemas clínicos;
* e-mail;
* WhatsApp;
* Google Workspace;
* Microsoft 365;
* n8n;
* APIs;
* PostgreSQL;
* armazenamento de arquivos.

---

## 17. Papel da Inteligência Artificial

A IA poderá apoiar:

* interpretação de e-mails e mensagens;
* classificação da solicitação;
* identificação da modalidade;
* leitura de documentos;
* extração de dados;
* identificação de informações ausentes;
* sugestão de competência;
* sugestão de descrição;
* comparação entre documentos;
* detecção de inconsistências;
* recomendação da próxima ação.

A IA não deverá substituir validações determinísticas, fiscais ou cadastrais que possam ser executadas por regras objetivas.

Decisões críticas deverão combinar:

```text
Conhecimento do domínio
        +
Regras determinísticas
        +
Inteligência Artificial
        +
Auditoria
```

---

## 18. Integração com outros contextos

### Fiscal

Fornece as regras tributárias necessárias à emissão.

### Financeiro

Recebe os eventos relacionados ao valor faturado e à expectativa de recebimento.

### Administrativo

Fornece cadastros, documentos, certificados e credenciais.

### Núcleo da Plataforma

Fornece autenticação, autorização, auditoria, IA, integrações e processamento de comunicações.

### Business Intelligence

Recebe dados consolidados para indicadores, relatórios e análises.

---

## 19. Regras que deverão possuir documentos próprios

As seguintes regras serão detalhadas separadamente:

* definição da competência;
* identificação do prestador;
* identificação do tomador;
* validação do valor;
* formação da descrição;
* prevenção de duplicidade;
* emissão no ISSNET;
* armazenamento de documentos;
* tratamento de falhas;
* revisão humana;
* cancelamento e substituição de NFS-e.

---

## 20. Critério de sucesso

O macroprocesso será considerado automatizado quando a plataforma conseguir:

1. receber uma solicitação real;
2. interpretar seus documentos;
3. identificar os dados necessários;
4. aplicar as regras de negócio;
5. emitir a NFS-e;
6. validar o retorno;
7. armazenar os documentos;
8. registrar a auditoria;
9. notificar o solicitante;
10. tratar exceções sem perda de rastreabilidade.

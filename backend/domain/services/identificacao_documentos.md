# Domain Service — Identificação de Documentos

## Objetivo

O Domain Service de Identificação de Documentos é responsável por reconhecer, classificar e organizar os documentos recebidos pela Plataforma DF Analysis IA.

Seu objetivo é transformar um conjunto heterogêneo de arquivos em informações estruturadas que possam ser utilizadas pelos demais processos do domínio.

---

# Motivação

Na operação da DF Analysis, uma solicitação pode chegar contendo diversos arquivos em formatos distintos.

Exemplos:

* PDF;
* XML;
* XLSX;
* CSV;
* DOCX;
* imagens;
* arquivos compactados;
* e-mails.

Antes de qualquer processamento, a plataforma precisa identificar o que cada documento representa.

---

# Responsabilidades

O serviço é responsável por:

* identificar o tipo de documento;
* classificar documentos;
* reconhecer layouts conhecidos;
* identificar município de origem;
* identificar competência;
* identificar Prestador;
* identificar Tomador;
* identificar Médico Executante;
* identificar períodos;
* identificar documentos duplicados;
* organizar os documentos em um Evidence Bundle.

---

# Entradas

O serviço recebe:

* arquivos;
* anexos de e-mail;
* documentos enviados via portal;
* documentos enviados via API;
* documentos enviados via WhatsApp;
* metadados da Solicitação de Emissão.

---

# Saídas

O serviço produz:

* documentos classificados;
* metadados extraídos;
* tipos documentais;
* vínculos com Aggregates;
* eventos de domínio.

---

# Tipos de documentos reconhecidos

Entre outros:

* NFS-e (PDF);
* NFS-e (XML);
* RPS;
* Relatório de Produção;
* Planilha Financeira;
* Demonstrativo Hospitalar;
* Contrato;
* Documento de Identificação;
* Comprovante;
* Arquivo Desconhecido.

---

# Regras de Negócio

O serviço deve:

* preservar os arquivos originais;
* nunca alterar documentos recebidos;
* permitir múltiplas versões;
* registrar nível de confiança da classificação;
* registrar a origem do documento;
* permitir reclassificação posterior.

---

# Fluxo conceitual

1. Receber documentos.
2. Identificar formato.
3. Identificar tipo documental.
4. Extrair metadados.
5. Classificar.
6. Agrupar documentos relacionados.
7. Produzir Evidence Bundle.
8. Publicar eventos.

---

# Eventos produzidos

* Documento Recebido;
* Documento Classificado;
* Documento Desconhecido;
* Evidence Bundle Criado.

---

# Dependências

Este serviço pode utilizar:

* Aggregate Solicitação de Emissão;
* Aggregate Relatório de Produção;
* Aggregate NFS-e;
* Policies de classificação;
* Serviços de OCR;
* Serviços de IA;
* Modelos de Machine Learning.

---

# Limites

Este Domain Service não:

* altera arquivos;
* valida regras fiscais;
* emite NFS-e;
* calcula tributos;
* grava diretamente em banco de dados.

Essas responsabilidades pertencem a outros componentes do domínio e da infraestrutura.

---

# Observações

A identificação documental representa a porta de entrada da inteligência da plataforma.

Ao separar essa responsabilidade em um Domain Service independente, a Plataforma DF Analysis IA poderá evoluir continuamente seus modelos de classificação, OCR e Inteligência Artificial sem alterar os Aggregates ou os fluxos de negócio.

Isso torna o domínio mais estável, modular e preparado para incorporar novas tecnologias de IA ao longo do tempo.

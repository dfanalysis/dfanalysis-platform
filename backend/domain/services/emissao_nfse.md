# Domain Service — Emissão de NFS-e

## Objetivo

O Domain Service de Emissão de NFS-e é responsável por coordenar todas as regras de negócio necessárias para transformar uma Solicitação de Emissão validada em uma Nota Fiscal de Serviços Eletrônica autorizada pelo município.

Esse serviço encapsula o comportamento do domínio relacionado à emissão fiscal, sem depender de detalhes técnicos da integração com provedores externos.

---

# Motivação

A emissão da NFS-e não é responsabilidade de um único Aggregate.

Ela envolve simultaneamente:

* Solicitação de Emissão;
* Prestador;
* Tomador;
* Competência;
* Valores;
* Tributos;
* Regras municipais;
* Integrações externas.

Como o comportamento ultrapassa os limites de um Aggregate, ele deve ser representado por um Domain Service.

---

# Responsabilidades

O serviço é responsável por:

* validar se a Solicitação está apta para emissão;
* validar informações obrigatórias;
* validar Prestador;
* validar Tomador;
* validar competência;
* validar documentos necessários;
* montar os dados fiscais;
* solicitar a emissão ao serviço de infraestrutura;
* interpretar o retorno do município;
* atualizar os Aggregates envolvidos;
* produzir eventos de domínio.

---

# Entradas

O serviço recebe, entre outras informações:

* Solicitação de Emissão;
* Prestador;
* Tomador;
* Competência;
* Dados fiscais;
* Configuração municipal.

---

# Saídas

O serviço pode produzir:

* NFS-e emitida;
* rejeição;
* pendência;
* erro de negócio;
* eventos de domínio.

---

# Regras de Negócio

Antes da emissão, o serviço deve garantir que:

* a Solicitação esteja validada;
* exista um Prestador ativo;
* exista um Tomador válido;
* todos os campos obrigatórios estejam preenchidos;
* os valores sejam consistentes;
* as regras municipais sejam respeitadas.

Caso qualquer validação falhe, a emissão não deve prosseguir.

---

# Fluxo conceitual

1. Receber Solicitação.
2. Validar regras de negócio.
3. Preparar os dados fiscais.
4. Solicitar emissão ao serviço de infraestrutura.
5. Receber retorno do município.
6. Criar ou atualizar o Aggregate NFS-e.
7. Atualizar a Solicitação de Emissão.
8. Publicar eventos de domínio.

---

# Eventos produzidos

* Emissão Iniciada;
* NFS-e Emitida;
* Emissão Rejeitada;
* Erro de Emissão.

---

# Dependências

Este Domain Service pode utilizar:

* Aggregate Solicitação de Emissão;
* Aggregate NFS-e;
* Policies de emissão;
* Repositories;
* Serviços de infraestrutura responsáveis pela comunicação com o município.

---

# Limites

Este Domain Service **não**:

* acessa diretamente banco de dados;
* implementa chamadas HTTP;
* monta XML específico de provedores;
* executa autenticação no portal municipal.

Essas responsabilidades pertencem à camada de Infraestrutura.

---

# Observações

Este serviço representa a regra de negócio da emissão fiscal.

A integração com ISSNET, padrão nacional da NFS-e ou qualquer outro provedor deve ser tratada como um detalhe de infraestrutura, preservando o domínio independente de tecnologias e fornecedores.

Essa separação permitirá reutilizar o mesmo modelo de negócio para diferentes municípios e provedores fiscais, alterando apenas os adaptadores de infraestrutura.

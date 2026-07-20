# Integration Event — XML Recebido

## Objetivo

O evento **XML Recebido** representa o momento em que o XML oficial da Nota Fiscal de Serviços Eletrônica é disponibilizado pelo provedor de NFS-e e recebido pela Plataforma DF Analysis IA.

Este evento registra a disponibilidade do documento fiscal eletrônico em seu formato estruturado e oficial.

---

# Motivação

O XML é o principal artefato fiscal produzido pelo processo de emissão.

Ele será utilizado por diversos componentes da plataforma, incluindo:

- armazenamento permanente;
- auditoria;
- integração com ERP;
- extração de dados;
- geração de relatórios;
- validações futuras;
- reconstrução histórica do processo.

Ao registrar sua chegada por meio de um Integration Event, a plataforma desacopla a recepção do documento de seu processamento posterior.

---

# Quando ocorre

O evento deve ser publicado quando:

- o XML oficial for recebido do provedor;
- sua integridade mínima puder ser confirmada;
- ele estiver disponível para armazenamento e processamento.

---

# Dados do evento

O evento pode conter:

- identificador da NFS-e;
- identificador da Solicitação de Emissão;
- identificador do XML;
- provedor;
- município;
- versão do layout;
- data e hora do recebimento;
- hash do arquivo;
- tamanho do arquivo;
- identificador de correlação.

O conteúdo completo do XML não deve ser publicado no evento.

---

# Possíveis consumidores

O evento pode ser consumido por:

- Storage Service;
- Parser XML;
- Auditoria;
- ERP;
- Backup;
- Monitoramento;
- Serviços de IA para extração de informações.

---

# Relação com o domínio

Este evento representa exclusivamente a disponibilização do XML pelo sistema externo.

Ele não confirma a validade do conteúdo nem altera diretamente o estado do domínio.

---

# Auditoria

Devem ser registrados:

- identificador do XML;
- hash;
- provedor;
- versão do layout;
- data e hora;
- origem do recebimento.

---

# Segurança

O XML deve ser armazenado de forma íntegra e imutável.

Qualquer processamento posterior deverá utilizar cópias ou representações derivadas, preservando sempre o documento original.

---

# Observações

O evento **XML Recebido** representa a entrada do principal artefato fiscal da emissão dentro da Plataforma DF Analysis IA, permitindo que diversos módulos iniciem seus próprios processos sem depender diretamente da integração com o provedor.
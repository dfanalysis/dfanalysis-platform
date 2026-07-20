# Integration Event — E-mail Recebido

## Objetivo

O evento **E-mail Recebido** representa a confirmação de que um novo e-mail foi capturado por um mecanismo de integração da Plataforma DF Analysis IA e disponibilizado para processamento.

Este evento marca a entrada de informações provenientes de um sistema externo no ecossistema da plataforma.

---

# Motivação

Grande parte dos processos administrativos da DF Analysis inicia-se com o recebimento de um e-mail contendo solicitações de emissão, documentos fiscais, relatórios ou demais evidências necessárias ao processamento.

Ao registrar esse fato por meio de um Integration Event, a plataforma desacopla o mecanismo de captura do processamento de negócio.

---

# Quando ocorre

O evento deve ser publicado quando:

- um novo e-mail for recebido;
- sua captura for concluída com sucesso;
- seus metadados estiverem disponíveis para processamento.

---

# Dados do evento

O evento pode conter:

- identificador do e-mail;
- Message-ID;
- remetente;
- destinatários;
- assunto;
- data de recebimento;
- quantidade de anexos;
- identificador da caixa postal;
- identificador de correlação.

O conteúdo completo da mensagem deve permanecer armazenado na infraestrutura apropriada.

---

# Possíveis consumidores

O evento pode ser consumido por:

- Inbox Service;
- Identify Documents;
- Auditoria;
- Monitoramento;
- Serviços de IA responsáveis pela classificação inicial.

Cada consumidor decide independentemente como reagir ao evento.

---

# Relação com o domínio

Este evento não representa uma decisão de negócio.

Ele apenas informa que um sistema externo entregou um novo e-mail para processamento.

A partir desse momento poderão surgir Business Events, como:

- Solicitação de Emissão Criada;
- Documento Identificado;
- Documento Não Identificado.

---

# Auditoria

Devem ser registrados:

- origem do e-mail;
- data e hora;
- caixa postal;
- identificador de correlação;
- mecanismo responsável pela captura.

---

# Observações

O evento **E-mail Recebido** representa a principal porta de entrada da Plataforma DF Analysis IA.

Ele estabelece o ponto de integração entre sistemas externos de comunicação e o núcleo do domínio, permitindo que diferentes mecanismos de captura sejam substituídos sem impacto nas regras de negócio.
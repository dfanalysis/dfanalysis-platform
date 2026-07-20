# Domain Event — Notificação Solicitada

## Objetivo

O evento **Notificação Solicitada** representa o momento em que o domínio determina que uma comunicação deve ser realizada em decorrência de um fato relevante do negócio.

Esse evento não representa o envio da mensagem, mas sim a intenção formal do domínio de comunicar uma informação a um ou mais destinatários.

---

# Motivação

Diversos acontecimentos do domínio exigem comunicação com usuários, clientes, médicos ou sistemas externos.

Exemplos:

* NFS-e emitida;
* emissão bloqueada;
* repasse apurado;
* competência encerrada;
* documento rejeitado;
* aprovação pendente;
* inconsistências identificadas.

Ao invés de enviar mensagens diretamente, o domínio publica este evento para que outros componentes executem a comunicação.

---

# Quando ocorre

O evento deve ser publicado sempre que uma regra de negócio determinar que uma comunicação é necessária.

A necessidade da comunicação pertence ao domínio.

A forma de comunicação pertence à infraestrutura.

---

# Dados do evento

O evento pode conter:

* identificador da notificação;
* identificador do Processo Administrativo;
* identificador da Solicitação de Emissão, quando aplicável;
* fato gerador da notificação;
* categoria da notificação;
* nível de prioridade;
* nível de criticidade;
* destinatários previstos;
* canais sugeridos;
* idioma;
* data e hora da solicitação;
* identificador de correlação.

O evento deve transportar apenas as informações necessárias para que os consumidores possam decidir como realizar a comunicação.

---

# Possíveis consumidores

O evento pode ser consumido por:

* módulo de Notificações;
* integração com WhatsApp;
* integração com E-mail;
* integração com Microsoft Teams;
* integração com Google Workspace;
* Portal do Cliente;
* Portal Administrativo;
* aplicativo móvel;
* agentes especializados em comunicação.

Cada consumidor decide autonomamente como processar o evento.

---

# Regras de Negócio

O evento deve ser publicado quando:

* existir uma necessidade legítima de comunicação;
* houver destinatários definidos ou determináveis;
* a comunicação representar um fato relevante para o negócio.

A publicação do evento não garante que a mensagem será enviada.

Ela apenas representa a intenção do domínio.

---

# Relação com o Domain Service de Notificação

O Domain Service de Notificação é responsável por determinar:

* quando comunicar;
* quem deve ser comunicado;
* qual o nível de prioridade;
* qual o conteúdo semântico da comunicação.

Após essa decisão, o Domain Service publica o evento **Notificação Solicitada**.

A execução do envio pertence às camadas de Aplicação e Infraestrutura.

---

# Imutabilidade

Após publicado, o evento é imutável.

Caso seja necessária uma nova comunicação, um novo evento deverá ser publicado, preservando o histórico das solicitações.

---

# Auditoria

Devem ser registrados:

* identificador da notificação;
* fato gerador;
* prioridade;
* destinatários previstos;
* canais sugeridos;
* data e hora;
* origem da solicitação;
* identificador de correlação com o processo administrativo.

---

# Relação com o domínio

Este evento representa exclusivamente a intenção de comunicação do domínio.

Ele não confirma:

* envio;
* entrega;
* leitura;
* falha;
* reenvio.

Esses fatos pertencem às integrações externas e poderão ser representados por Integration Events específicos.

---

# Relação com integrações

Após a publicação deste evento, diferentes integrações podem executar ações como:

* envio de e-mail;
* envio de mensagem via WhatsApp;
* criação de tarefa;
* geração de alerta interno;
* envio de push notification;
* criação de ticket;
* atualização de portal.

Cada integração é responsável por sua própria execução e por publicar seus respectivos Integration Events.

---

# Observações

O evento **Notificação Solicitada** encerra o fluxo principal de sucesso do processo de emissão da Plataforma DF Analysis IA.

Ele representa a transição entre a decisão do domínio e a comunicação efetiva com usuários e sistemas externos, mantendo o núcleo do domínio desacoplado das tecnologias utilizadas para entrega das mensagens e permitindo que novos canais sejam incorporados sem alterações nas regras de negócio.

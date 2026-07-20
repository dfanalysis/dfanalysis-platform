# Integration Event — Requisição de Emissão Enviada

## Objetivo

O evento **Requisição de Emissão Enviada** representa o momento em que a Plataforma DF Analysis IA encaminha ao provedor de NFS-e uma solicitação formal para emissão de uma Nota Fiscal de Serviços Eletrônica.

Este evento registra que a comunicação foi iniciada com sucesso pela infraestrutura, independentemente do resultado que será retornado pelo provedor.

---

# Motivação

Após a publicação do Business Event **Emissão Autorizada**, a camada de Aplicação solicita à infraestrutura que execute a integração com o provedor responsável.

Quando a requisição é transmitida com sucesso, este evento é publicado para registrar que o pedido deixou a plataforma e foi encaminhado ao sistema externo.

Este evento não representa sucesso na emissão da nota.

Ele representa apenas o sucesso da transmissão da requisição.

---

# Quando ocorre

O evento deve ser publicado quando:

- a requisição HTTP/SOAP for enviada ao provedor;
- o payload for transmitido integralmente;
- a infraestrutura confirmar o envio da solicitação.

Caso a comunicação não possa ser realizada, deverá ser publicado um Integration Event específico para falha de comunicação.

---

# Dados do evento

O evento pode conter:

- identificador da Solicitação de Emissão;
- identificador da requisição;
- provedor;
- município;
- ambiente (produção ou homologação);
- operação executada;
- data e hora do envio;
- identificador de correlação;
- versão do layout utilizado.

O payload completo da requisição não deve ser publicado no evento.

---

# Possíveis consumidores

O evento pode ser consumido por:

- monitoramento operacional;
- auditoria;
- observabilidade;
- métricas;
- tracing distribuído;
- mecanismos de timeout;
- mecanismos de retry.

---

# Relação com o domínio

Este evento não representa qualquer decisão de negócio.

Ele apenas informa que a infraestrutura iniciou a comunicação com o sistema externo.

A confirmação da emissão dependerá da resposta do provedor.

---

# Auditoria

Devem ser registrados:

- data e hora;
- provedor;
- operação executada;
- ambiente;
- identificador da requisição;
- identificador de correlação;
- mecanismo responsável pelo envio.

---

# Segurança

O evento não deve conter:

- XML completo;
- credenciais;
- tokens;
- certificados digitais;
- dados sensíveis protegidos.

Essas informações pertencem exclusivamente à camada de infraestrutura.

---

# Observações

O evento **Requisição de Emissão Enviada** representa o início da comunicação efetiva entre a Plataforma DF Analysis IA e o provedor de NFS-e.

Sua existência permite monitorar tempos de resposta, detectar falhas de comunicação, implementar mecanismos de retry e separar claramente o momento do envio da confirmação da emissão.
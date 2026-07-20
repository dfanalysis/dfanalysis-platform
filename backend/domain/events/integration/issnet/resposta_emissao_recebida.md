# Integration Event — Resposta de Emissão Recebida

## Objetivo

O evento **Resposta de Emissão Recebida** representa o momento em que a Plataforma DF Analysis IA recebe uma resposta do provedor de NFS-e referente a uma solicitação previamente enviada.

Este evento registra exclusivamente o recebimento da resposta técnica, sem interpretar seu conteúdo ou produzir conclusões de negócio.

---

# Motivação

Após o envio da solicitação de emissão, o provedor poderá retornar diferentes resultados.

Exemplos:

- emissão autorizada;
- emissão rejeitada;
- processamento assíncrono;
- erro de validação;
- indisisponibilidade temporária;
- erro interno;
- timeout;
- lote recebido.

A responsabilidade deste evento é apenas registrar que uma resposta foi recebida.

A interpretação dessa resposta pertence à camada de Aplicação.

---

# Quando ocorre

O evento deve ser publicado quando:

- uma resposta válida for recebida do provedor;
- a infraestrutura concluir a comunicação;
- o conteúdo estiver disponível para interpretação.

---

# Dados do evento

O evento pode conter:

- identificador da requisição;
- identificador da resposta;
- provedor;
- município;
- ambiente;
- código HTTP, quando aplicável;
- protocolo retornado;
- data e hora da resposta;
- identificador de correlação;
- tempo total da operação.

O conteúdo integral do XML ou da resposta não deve ser publicado no evento.

---

# Possíveis consumidores

O evento pode ser consumido por:

- camada de Aplicação;
- monitoramento;
- auditoria;
- observabilidade;
- métricas;
- tracing distribuído;
- mecanismos de retry;
- mecanismos de timeout.

---

# Relação com o domínio

Este evento não representa qualquer fato de negócio.

Ele informa apenas que uma resposta técnica foi recebida do sistema externo.

A partir da interpretação dessa resposta poderão surgir:

- Business Events;
- Exception Events;
- novos Integration Events.

---

# Auditoria

Devem ser registrados:

- provedor;
- data e hora;
- tempo de resposta;
- protocolo;
- identificador da requisição;
- identificador da resposta;
- ambiente.

---

# Segurança

O evento não deve conter:

- XML completo;
- credenciais;
- certificados;
- tokens;
- informações sensíveis protegidas.

Esses dados pertencem exclusivamente à infraestrutura.

---

# Observações

O evento **Resposta de Emissão Recebida** separa claramente o recebimento técnico da resposta da interpretação de seu significado para o negócio.

Essa distinção permite que a Plataforma DF Analysis IA permaneça desacoplada dos diferentes comportamentos dos provedores de NFS-e, facilitando futuras integrações com ISSNET, ABRASF, padrão nacional e outros municípios.
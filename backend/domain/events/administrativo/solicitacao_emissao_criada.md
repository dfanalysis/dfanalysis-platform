# Domain Event — Solicitação de Emissão Criada

## Objetivo

O evento **Solicitação de Emissão Criada** representa o momento em que uma nova Solicitação de Emissão passa a existir no domínio da Plataforma DF Analysis IA.

Esse é o evento que inicia o ciclo de vida do processo administrativo relacionado à emissão de uma NFS-e.

---

# Motivação

Uma Solicitação de Emissão é o ponto de entrada do processo de negócio.

A partir dela, diversos componentes do domínio poderão executar comportamentos independentes.

Esse evento comunica aos demais componentes que uma nova solicitação foi criada e está disponível para processamento.

---

# Quando ocorre

O evento deve ser publicado quando:

* uma nova Solicitação de Emissão for criada com sucesso;
* o Aggregate estiver consistente;
* todos os requisitos mínimos para existência da solicitação forem atendidos.

---

# Dados do evento

O evento pode conter:

* identificador da Solicitação;
* identificador da Empresa Médica;
* Competência;
* data e hora da criação;
* origem da solicitação;
* usuário responsável;
* identificador do Processo Administrativo;
* versão do Aggregate.

O evento deve transportar apenas as informações necessárias para que outros componentes iniciem seu processamento.

---

# Possíveis consumidores

O evento pode ser consumido por:

* Domain Service de Identificação de Documentos;
* Domain Service de Auditoria;
* Domain Service de Notificação;
* módulo de monitoramento;
* módulo gerencial;
* futuras integrações.

Cada consumidor decide independentemente como reagir ao evento.

---

# Regras de Negócio

O evento somente deve ser publicado quando:

* o Aggregate estiver válido;
* a criação da Solicitação tiver sido concluída com sucesso;
* não houver inconsistências impeditivas.

Caso a criação seja cancelada ou revertida, o evento não deve ser publicado.

---

# Imutabilidade

Após publicado, o evento é imutável.

Correções posteriores devem resultar na publicação de novos eventos, nunca na alteração do evento original.

---

# Auditoria

Devem ser preservados:

* data e hora da publicação;
* origem da solicitação;
* usuário responsável;
* versão do Aggregate;
* identificador do evento;
* correlação com o Processo Administrativo.

---

# Relação com o domínio

Este evento marca o início do ciclo operacional da Plataforma DF Analysis IA.

A partir dele, outros componentes poderão identificar documentos, validar informações, calcular tributos, emitir NFS-e, apurar repasses e gerar notificações, sempre de forma desacoplada.

---

# Observações

O evento **Solicitação de Emissão Criada** é o primeiro marco temporal do processo de emissão dentro do domínio.

Sua existência permite que a plataforma evolua para arquiteturas orientadas a eventos, processamento assíncrono, filas, mensageria e cooperação entre múltiplos agentes de IA, preservando o baixo acoplamento entre os componentes do sistema.

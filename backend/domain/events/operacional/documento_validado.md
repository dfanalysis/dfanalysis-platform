# Domain Event — Documento Validado

## Objetivo

O evento **Documento Validado** representa o momento em que um documento identificado foi submetido às regras de validação da Plataforma DF Analysis IA e considerado apto para utilização no processo de negócio.

Esse evento marca a conclusão da etapa de validação documental e autoriza a continuidade do fluxo operacional.

---

# Motivação

Após a identificação, todo documento deve ser validado quanto à sua integridade, consistência e conformidade com as regras do domínio.

A validação pode envolver:

* estrutura do documento;
* consistência dos dados;
* obrigatoriedade;
* competência;
* informações cadastrais;
* coerência com outros documentos;
* requisitos fiscais.

Quando essa etapa é concluída, o domínio publica este evento.

---

# Quando ocorre

O evento deve ser publicado quando:

* todas as validações obrigatórias forem concluídas;
* o documento for considerado válido;
* o resultado da validação permitir a continuidade do processo.

Documentos reprovados não produzem este evento, devendo gerar eventos específicos de rejeição ou pendência.

---

# Dados do evento

O evento pode conter:

* identificador do documento;
* identificador da Solicitação de Emissão;
* identificador do Evidence Bundle;
* tipo documental;
* resultado da validação;
* data e hora;
* versão das regras aplicadas;
* responsável pela validação;
* mecanismo utilizado.

O evento deve transportar apenas as informações necessárias para seus consumidores.

---

# Possíveis consumidores

O evento pode ser consumido por:

* Domain Service de Cálculo Tributário;
* Domain Service de Emissão de NFS-e;
* Domain Service de Auditoria;
* Domain Service de Notificação;
* módulos gerenciais;
* futuros agentes especializados.

Cada consumidor decide independentemente como reagir ao evento.

---

# Regras de Negócio

O evento somente deve ser publicado quando:

* o documento estiver identificado;
* todas as validações obrigatórias forem executadas;
* não existirem divergências impeditivas;
* o documento puder ser utilizado pelo domínio.

---

# Imutabilidade

Após publicado, o evento é imutável.

Caso novas validações sejam realizadas posteriormente, novos eventos deverão ser publicados, preservando o histórico completo.

---

# Auditoria

Devem ser registrados:

* identificador do documento;
* resultado da validação;
* regras utilizadas;
* data e hora;
* executor;
* mecanismo utilizado;
* nível de confiança, quando houver IA;
* correlação com a Solicitação de Emissão.

---

# Relação com o domínio

Este evento representa a conclusão da etapa de validação documental.

A partir dele, o domínio pode prosseguir para validações de competência, decisões tributárias, emissão da NFS-e ou outros processos dependentes da documentação aprovada.

---

# Observações

O evento **Documento Validado** confirma que um documento atende aos requisitos definidos pelas Policies e pelos Domain Services da Plataforma DF Analysis IA.

Sua publicação garante que os componentes posteriores trabalhem apenas com informações consideradas confiáveis pelo domínio, preservando a consistência e a rastreabilidade de todo o processo.

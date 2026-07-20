# Domain Event — Documento Duplicado

## Objetivo

O evento **Documento Duplicado** representa a identificação de que um documento já foi anteriormente recebido ou processado pela Plataforma DF Analysis IA.

---

# Motivação

Documentos duplicados podem ocorrer devido a:

- reenvio de e-mails;
- uploads repetidos;
- reprocessamentos;
- integração duplicada;
- falhas operacionais.

A identificação precoce evita processamento redundante e inconsistências.

---

# Quando ocorre

O evento deve ser publicado quando:

- o documento possuir hash idêntico;
- existir documento equivalente já associado ao processo;
- houver duplicidade confirmada pelas regras do domínio.

---

# Dados do evento

Pode conter:

- documento atual;
- documento original;
- hash;
- origem;
- data do primeiro processamento;
- Processo Administrativo.

---

# Possíveis consumidores

- Auditoria;
- Notificações;
- monitoramento;
- fila administrativa.

---

# Regras de Negócio

A duplicidade deve ser confirmada conforme os critérios definidos pela Política de Documentos.

Nem toda duplicidade implica descarte automático.

---

# Imutabilidade

O evento é imutável.

Caso a duplicidade seja posteriormente descartada, novo evento deverá representar esse fato.

---

# Auditoria

Registrar:

- hash;
- documentos relacionados;
- data;
- origem;
- Processo Administrativo.

---

# Relação com o domínio

Este evento representa um fato operacional que protege a integridade do processo administrativo e evita retrabalho.

---

# Relação com políticas

A confirmação da duplicidade deve respeitar os critérios definidos pela Política de Documentos.

---

# Observações

A existência deste evento facilita a implementação de mecanismos de idempotência e deduplicação em futuros agentes da plataforma.
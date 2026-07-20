# Domain Event — Documento Rejeitado

## Objetivo

O evento **Documento Rejeitado** representa o momento em que um documento previamente identificado não atende aos critérios mínimos de validação definidos pelo domínio e, por esse motivo, não pode ser utilizado no processo administrativo correspondente.

Esse evento comunica que o documento foi analisado, compreendido quanto à sua natureza, porém rejeitado por apresentar inconsistências ou não conformidades que impedem sua utilização.

---

# Motivação

Nem todo documento identificado é necessariamente válido.

Durante o processo de validação podem ser encontradas situações como:

- documento ilegível;
- informações obrigatórias ausentes;
- assinatura inválida;
- arquivo incompleto;
- conteúdo incompatível;
- documento expirado;
- layout incompatível;
- campos obrigatórios inválidos.

Quando qualquer uma dessas condições impedir sua utilização, este evento deverá ser publicado.

---

# Quando ocorre

O evento deve ser publicado quando:

- o documento já tiver sido identificado;
- a validação indicar impossibilidade de utilização;
- não existir regra que permita aprovação com ressalvas.

---

# Dados do evento

O evento pode conter:

- identificador do documento;
- tipo documental;
- identificador do Evidence Bundle;
- motivo da rejeição;
- regra violada;
- severidade;
- data e hora;
- identificador do Processo Administrativo.

---

# Possíveis consumidores

O evento pode ser consumido por:

- Domain Service de Auditoria;
- Domain Service de Notificação;
- módulo Administrativo;
- fila de tratamento manual;
- monitoramento operacional;
- dashboards gerenciais.

---

# Regras de Negócio

O evento deve ser publicado somente quando a rejeição impedir a continuidade automática do processo.

Caso a inconsistência seja considerada não impeditiva, o documento poderá ser aprovado com ressalvas, conforme definido pela Política de Validação.

---

# Imutabilidade

Após publicado, o evento é imutável.

Caso um novo documento substitua o anterior ou a rejeição seja sanada, um novo evento deverá representar essa alteração.

---

# Auditoria

Devem ser registrados:

- documento rejeitado;
- regra violada;
- motivo;
- severidade;
- responsável pela validação;
- data e hora;
- identificador do Processo Administrativo.

---

# Relação com o domínio

Este evento representa um fato operacional decorrente da aplicação das regras de validação documental.

Ele não representa falha técnica da plataforma, mas sim uma decisão de negócio baseada nas políticas estabelecidas.

---

# Relação com políticas

A decisão de rejeitar um documento deve respeitar os critérios definidos pela Política de Validação e pela Política de Documentos.

---

# Observações

O evento **Documento Rejeitado** interrompe exclusivamente o fluxo relacionado ao documento afetado, preservando os demais elementos do processo sempre que possível.
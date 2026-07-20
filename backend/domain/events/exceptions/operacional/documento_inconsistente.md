# Domain Event — Documento Inconsistente

## Objetivo

O evento **Documento Inconsistente** representa a identificação de divergências entre um documento e outras evidências pertencentes ao mesmo Processo Administrativo.

Diferentemente da rejeição, a inconsistência indica que o documento pode ser estruturalmente válido, porém apresenta informações incompatíveis com o restante do processo.

---

# Motivação

Em processos administrativos complexos é comum comparar informações provenientes de diferentes documentos.

Exemplos:

- CNPJ divergente;
- competência diferente;
- valores incompatíveis;
- médico executante diferente;
- tomador divergente;
- datas incompatíveis;
- descrição incompatível.

Quando essas divergências ultrapassarem os limites definidos pelas regras do domínio, este evento deverá ser publicado.

---

# Quando ocorre

O evento deve ser publicado quando:

- houver conflito entre documentos relacionados;
- a inconsistência impedir a continuidade automática;
- a divergência exigir análise manual.

---

# Dados do evento

O evento pode conter:

- documento envolvido;
- documentos relacionados;
- tipo da inconsistência;
- regra violada;
- severidade;
- data e hora;
- Processo Administrativo.

---

# Possíveis consumidores

- Auditoria;
- Notificações;
- módulo Administrativo;
- fila de análise manual;
- dashboards.

---

# Regras de Negócio

A inconsistência deve ser registrada mesmo quando o documento permanecer armazenado.

O tratamento dependerá da severidade definida pelas políticas do domínio.

---

# Imutabilidade

O evento é imutável.

Nova análise deverá produzir novo evento.

---

# Auditoria

Registrar:

- inconsistência encontrada;
- documentos comparados;
- regra aplicada;
- data;
- responsável.

---

# Relação com políticas

As regras para identificação das inconsistências pertencem à Política de Validação.

---

# Observações

Nem toda inconsistência implica rejeição do documento. Algumas podem ser resolvidas por confirmação manual ou reprocessamento automático.
# Use Case — Criar Solicitação de Emissão

## Objetivo

Criar uma nova Solicitação de Emissão a partir de uma entrada válida (e-mail, API ou integração).

---

## Entrada

- Empresa
- Solicitante
- Origem
- Evidence Bundle

---

## Validações

- Empresa existente
- Solicitante autorizado
- Evidence Bundle existente

---

## Fluxo

1. Validar entrada.
2. Criar Aggregate Solicitação de Emissão.
3. Persistir Aggregate.
4. Publicar Business Event:
   - Solicitação de Emissão Criada.

---

## Saída

- ID da Solicitação
- Status inicial

---

## Erros possíveis

- Empresa inexistente
- Solicitante inválido
- Evidence Bundle inexistente
# Catálogo de Perfis e Permissões

Versão: 1.0

---

# Objetivo

Este documento define o catálogo oficial de perfis e permissões da Plataforma DF Analysis IA.

Toda autorização da plataforma deverá ser baseada neste catálogo.

---

# Modelo

Usuário

↓

Perfil

↓

Permissões

---

# Perfis da Plataforma

## SUPER_ADMIN

Administrador global da plataforma.

Possui acesso irrestrito.

---

## ADMINISTRADOR

Administrador da empresa (Tenant).

Gerencia usuários, configurações e módulos da própria empresa.

---

## FISCAL

Responsável pelas operações fiscais.

Exemplo:

- emissão de NFS-e
- cancelamentos
- consultas
- RPS

---

## FINANCEIRO

Responsável pelas rotinas financeiras.

---

## COMERCIAL

Responsável pelo CRM e vendas.

---

## OPERADOR

Usuário operacional.

Possui acesso apenas às funcionalidades necessárias.

---

## IA_AGENT

Conta utilizada pelos Agentes de IA.

Não representa uma pessoa física.

---

## API

Conta técnica utilizada por integrações externas.

---

# Convenção das Permissões

As permissões seguirão o padrão:

```
modulo.acao
```

Exemplos:

```
usuarios.read
usuarios.create
usuarios.update
usuarios.delete

empresas.read
empresas.create
empresas.update
empresas.delete

fiscal.emitir
fiscal.cancelar
fiscal.consultar

workflow.execute
workflow.update

ia.execute
ia.configure

auditoria.read

configuracoes.update
```

---

# Regras

Permissões nunca serão atribuídas diretamente ao usuário.

Sempre serão atribuídas ao Perfil.

Usuários poderão possuir múltiplos perfis.

---

# MVP

Na primeira versão serão criados automaticamente:

- SUPER_ADMIN
- ADMINISTRADOR
- FISCAL
- FINANCEIRO
- COMERCIAL
- OPERADOR
- IA_AGENT
- API
# Convenções SQL da Plataforma DF Analysis IA

**Versão:** 1.0

---

# Objetivo

Este documento define os padrões oficiais para desenvolvimento, manutenção e evolução do banco de dados PostgreSQL da Plataforma DF Analysis IA.

Todas as migrations, tabelas, funções, índices e objetos do banco deverão seguir estas convenções.

---

# Banco de Dados

Banco oficial:

PostgreSQL 16+

Todo desenvolvimento deverá utilizar PostgreSQL.

Não serão suportadas adaptações para outros bancos relacionais.

---

# Organização por Schemas

A plataforma será organizada por domínios de negócio.

Schemas oficiais:

- core
- fiscal
- financeiro
- comercial
- workflow
- auditoria
- integracao

Novos schemas somente poderão ser criados mediante decisão arquitetural documentada (ADR).

---

# Convenções de Nomenclatura

## Schemas

Sempre em letras minúsculas.

Exemplo:

core

fiscal

workflow

---

## Tabelas

Sempre no singular.

Sempre em snake_case.

Exemplos:

empresa

usuario

perfil

usuario_perfil

prestador

tomador

nfse

---

## Colunas

Sempre em snake_case.

Nunca utilizar espaços.

Nunca utilizar caracteres especiais.

Exemplos:

empresa_id

created_at

updated_by

numero_rps

data_emissao

---

## Constraints

PRIMARY KEY

pk_<tabela>

Exemplo:

pk_empresa

---

FOREIGN KEY

fk_<tabela>_<referencia>

Exemplo:

fk_nfse_empresa

---

UNIQUE

uk_<tabela>_<campo>

CHECK

ck_<tabela>_<campo>

INDEX

idx_<tabela>_<campo>

---

# Chaves Primárias

Todas as tabelas deverão utilizar:

UUID

Exemplo:

id UUID PRIMARY KEY

Não utilizar SERIAL ou BIGSERIAL em entidades de negócio.

---

# Chaves Estrangeiras

Toda chave estrangeira deverá:

- possuir índice;
- possuir constraint;
- possuir nome padronizado.

Exemplo:

empresa_id UUID NOT NULL

---

# Auditoria

Sempre que aplicável:

created_at

updated_at

created_by

updated_by

---

# Exclusão Lógica

Sempre que houver necessidade de exclusão:

deleted_at

deleted_by

Evitar DELETE físico.

---

# Datas

Utilizar sempre:

TIMESTAMP WITH TIME ZONE

Nunca utilizar DATE para registros transacionais quando houver necessidade de rastreabilidade temporal.

---

# Valores Monetários

Utilizar:

NUMERIC(15,2)

Nunca utilizar FLOAT.

---

# Texto

TEXT

quando o tamanho for variável.

VARCHAR apenas quando houver limite funcional conhecido.

---

# Booleanos

Utilizar BOOLEAN.

Nunca utilizar CHAR(1).

---

# JSON

Sempre utilizar:

JSONB

quando houver necessidade de armazenamento semiestruturado.

---

# Índices

Criar índices para:

- Foreign Keys;
- Campos de pesquisa;
- Campos utilizados em filtros;
- Campos utilizados em ORDER BY;
- Campos utilizados em JOIN.

Evitar índices desnecessários.

---

# Constraints

Toda validação estrutural deverá ser realizada no banco.

Utilizar:

NOT NULL

CHECK

UNIQUE

FOREIGN KEY

Sempre que possível.

---

# Triggers

Triggers deverão ser reutilizáveis.

Exemplo:

fn_update_updated_at()

Evitar funções duplicadas.

---

# Funções

Sempre utilizar prefixo:

fn_

Exemplos:

fn_update_updated_at

fn_generate_rps

fn_validate_cnpj

---

# Views

Sempre utilizar prefixo:

vw_

Exemplos:

vw_nfse_emitidas

vw_fluxo_caixa

---

# Migrations

Todas as alterações estruturais deverão ocorrer exclusivamente através de migrations.

Nunca alterar o banco manualmente em ambientes compartilhados.

Padrão:

001_create_extensions.sql

002_create_schemas.sql

003_create_functions.sql

...

---

# Seeds

Os dados iniciais deverão permanecer separados das migrations.

Exemplos:

empresa padrão

perfis

parâmetros

configurações

---

# Performance

Evitar:

SELECT *

Preferir:

SELECT campo1, campo2

Utilizar EXPLAIN ANALYZE sempre que necessário para otimização.

---

# Integridade

Nunca remover uma constraint para "fazer funcionar".

A modelagem deverá refletir as regras de negócio.

---

# Comentários

Toda tabela deverá possuir comentário.

Toda coluna crítica deverá possuir comentário.

Utilizar:

COMMENT ON TABLE

COMMENT ON COLUMN

---

# Padrão Geral

Toda nova migration deverá responder às seguintes perguntas:

- Está normalizada?
- Possui índices?
- Possui auditoria?
- Possui integridade referencial?
- Está documentada?
- É compatível com multiempresa?
- Segue as convenções desta plataforma?
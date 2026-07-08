-- ==========================================================
-- Plataforma DF Analysis IA
-- Migration: 009_create_parametro.sql
-- Versão: 1.0.0
-- Objetivo:
-- Criar a tabela de parâmetros da plataforma.
-- ==========================================================

BEGIN;

CREATE TABLE IF NOT EXISTS core.parametro (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    categoria VARCHAR(50) NOT NULL,

    chave VARCHAR(100) NOT NULL,

    valor TEXT,

    tipo VARCHAR(20) NOT NULL DEFAULT 'STRING',

    descricao TEXT,

    ativo BOOLEAN NOT NULL DEFAULT TRUE,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT uk_parametro UNIQUE (categoria, chave)

);

COMMENT ON TABLE core.parametro IS
'Tabela de parâmetros globais da plataforma.';

COMMENT ON COLUMN core.parametro.categoria IS
'Categoria do parâmetro (GERAL, OPENAI, ISSNET, SMTP, etc.).';

COMMENT ON COLUMN core.parametro.chave IS
'Nome único do parâmetro dentro da categoria.';

COMMENT ON COLUMN core.parametro.valor IS
'Valor armazenado.';

COMMENT ON COLUMN core.parametro.tipo IS
'Tipo do valor: STRING, INTEGER, BOOLEAN, JSON.';

CREATE INDEX IF NOT EXISTS idx_parametro_categoria
ON core.parametro(categoria);

CREATE TRIGGER trg_parametro_updated_at

BEFORE UPDATE
ON core.parametro

FOR EACH ROW

EXECUTE FUNCTION core.fn_update_updated_at();

COMMIT;
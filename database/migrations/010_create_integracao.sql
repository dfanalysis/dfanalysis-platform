-- ==========================================================
-- Plataforma DF Analysis IA
-- Migration: 010_create_integracao.sql
-- Versão: 1.0.0
-- Objetivo:
-- Cadastro das integrações utilizadas pela plataforma.
-- ==========================================================

BEGIN;

CREATE TABLE IF NOT EXISTS core.integracao (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    nome VARCHAR(100) NOT NULL,

    tipo VARCHAR(50) NOT NULL,

    fabricante VARCHAR(100),

    versao VARCHAR(30),

    descricao TEXT,

    ativo BOOLEAN NOT NULL DEFAULT TRUE,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT uk_integracao_nome UNIQUE (nome)

);

COMMENT ON TABLE core.integracao IS
'Tabela de integrações disponíveis na plataforma.';

CREATE INDEX IF NOT EXISTS idx_integracao_tipo
ON core.integracao(tipo);

CREATE TRIGGER trg_integracao_updated_at

BEFORE UPDATE
ON core.integracao

FOR EACH ROW

EXECUTE FUNCTION core.fn_update_updated_at();

COMMIT;
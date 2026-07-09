-- ==========================================================
-- Plataforma DF Analysis IA
-- Migration: 011_create_credencial.sql
-- Versão: 1.0.0
-- Objetivo:
-- Cadastro das credenciais das integrações.
-- ==========================================================

BEGIN;

CREATE TABLE IF NOT EXISTS core.credencial (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    integracao_id UUID NOT NULL,

    nome VARCHAR(100) NOT NULL,

    tipo_autenticacao VARCHAR(30) NOT NULL,

    configuracao JSONB NOT NULL,

    observacao TEXT,

    ativo BOOLEAN NOT NULL DEFAULT TRUE,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_credencial_integracao
        FOREIGN KEY (integracao_id)
        REFERENCES core.integracao(id)
        ON DELETE CASCADE,

    CONSTRAINT uk_credencial
        UNIQUE (integracao_id, nome)

);

COMMENT ON TABLE core.credencial IS
'Tabela de credenciais das integrações da plataforma.';

COMMENT ON COLUMN core.credencial.tipo_autenticacao IS
'API_KEY, BASIC, OAUTH2, CERTIFICATE, TOKEN, JWT, etc.';

COMMENT ON COLUMN core.credencial.configuracao IS
'Configuração específica da autenticação armazenada em JSONB.';

CREATE INDEX IF NOT EXISTS idx_credencial_integracao
ON core.credencial(integracao_id);

CREATE TRIGGER trg_credencial_updated_at

BEFORE UPDATE
ON core.credencial

FOR EACH ROW

EXECUTE FUNCTION core.fn_update_updated_at();

COMMIT;
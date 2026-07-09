-- ==========================================================
-- Plataforma DF Analysis IA
-- Migration: 013_create_certificado.sql
-- Versão: 1.0.0
-- Objetivo:
-- Cadastro de certificados digitais utilizados nas integrações.
-- ==========================================================

BEGIN;

CREATE TABLE IF NOT EXISTS core.certificado (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    empresa_id UUID NOT NULL,

    nome VARCHAR(150) NOT NULL,

    tipo VARCHAR(10) NOT NULL DEFAULT 'A1',

    arquivo VARCHAR(500),

    senha TEXT,

    validade DATE NOT NULL,

    emissor VARCHAR(200),

    numero_serie VARCHAR(200),

    ativo BOOLEAN NOT NULL DEFAULT TRUE,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_certificado_empresa
        FOREIGN KEY (empresa_id)
        REFERENCES core.empresa(id)
        ON DELETE CASCADE

);

COMMENT ON TABLE core.certificado IS
'Certificados digitais utilizados para autenticação em integrações e emissão de NFS-e.';

CREATE INDEX IF NOT EXISTS idx_certificado_empresa
ON core.certificado (empresa_id);

CREATE INDEX IF NOT EXISTS idx_certificado_validade
ON core.certificado (validade);

CREATE TRIGGER trg_certificado_updated_at

BEFORE UPDATE
ON core.certificado

FOR EACH ROW

EXECUTE FUNCTION core.fn_update_updated_at();

COMMIT;
-- ==========================================================
-- Plataforma DF Analysis IA
-- Migration: 017_create_servico.sql
-- Objetivo:
-- Cadastro dos serviços prestados.
-- ==========================================================

BEGIN;

CREATE TABLE IF NOT EXISTS fiscal.servico (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    empresa_id UUID NOT NULL,

    codigo VARCHAR(50) NOT NULL,

    descricao VARCHAR(500) NOT NULL,

    item_lista_servico VARCHAR(20) NOT NULL,

    cnae VARCHAR(20),

    aliquota NUMERIC(5,2) NOT NULL,

    codigo_tributacao_municipio VARCHAR(50),

    exige_iss_retido BOOLEAN NOT NULL DEFAULT FALSE,

    permite_deducao BOOLEAN NOT NULL DEFAULT FALSE,

    ativo BOOLEAN NOT NULL DEFAULT TRUE,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_servico_empresa
        FOREIGN KEY (empresa_id)
        REFERENCES core.empresa(id)
        ON DELETE CASCADE,

    CONSTRAINT uk_servico_empresa_codigo
        UNIQUE (empresa_id, codigo)

);

COMMENT ON TABLE fiscal.servico IS
'Cadastro de serviços fiscais utilizados na emissão de NFS-e.';

CREATE INDEX IF NOT EXISTS idx_servico_empresa
ON fiscal.servico (empresa_id);

CREATE INDEX IF NOT EXISTS idx_servico_codigo
ON fiscal.servico (codigo);

CREATE INDEX IF NOT EXISTS idx_servico_item_lista
ON fiscal.servico (item_lista_servico);

CREATE TRIGGER trg_servico_updated_at

BEFORE UPDATE
ON fiscal.servico

FOR EACH ROW

EXECUTE FUNCTION core.fn_update_updated_at();

COMMIT;
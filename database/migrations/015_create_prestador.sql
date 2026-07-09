-- ==========================================================
-- Plataforma DF Analysis IA
-- Migration: 015_create_prestador.sql
-- Objetivo:
-- Cadastro dos prestadores de serviços.
-- ==========================================================

BEGIN;

CREATE TABLE IF NOT EXISTS fiscal.prestador (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    empresa_id UUID NOT NULL,

    codigo VARCHAR(50),

    nome VARCHAR(200) NOT NULL,

    nome_fantasia VARCHAR(200),

    cpf_cnpj VARCHAR(20) NOT NULL,

    inscricao_municipal VARCHAR(50),

    inscricao_estadual VARCHAR(50),

    cnae VARCHAR(20),

    regime_tributario VARCHAR(50),

    simples_nacional BOOLEAN NOT NULL DEFAULT FALSE,

    email VARCHAR(200),

    telefone VARCHAR(30),

    ativo BOOLEAN NOT NULL DEFAULT TRUE,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_prestador_empresa
        FOREIGN KEY (empresa_id)
        REFERENCES core.empresa(id)
        ON DELETE CASCADE,

    CONSTRAINT uk_prestador_cpf_cnpj
        UNIQUE (cpf_cnpj)

);

COMMENT ON TABLE fiscal.prestador IS
'Cadastro de prestadores de serviços.';

CREATE INDEX IF NOT EXISTS idx_prestador_empresa
ON fiscal.prestador (empresa_id);

CREATE INDEX IF NOT EXISTS idx_prestador_nome
ON fiscal.prestador (nome);

CREATE INDEX IF NOT EXISTS idx_prestador_documento
ON fiscal.prestador (cpf_cnpj);

CREATE TRIGGER trg_prestador_updated_at

BEFORE UPDATE
ON fiscal.prestador

FOR EACH ROW

EXECUTE FUNCTION core.fn_update_updated_at();

COMMIT;
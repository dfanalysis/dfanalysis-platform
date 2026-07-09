-- ==========================================================
-- Plataforma DF Analysis IA
-- Migration: 016_create_tomador.sql
-- Objetivo:
-- Cadastro dos tomadores de serviços.
-- ==========================================================

BEGIN;

CREATE TABLE IF NOT EXISTS fiscal.tomador (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    empresa_id UUID NOT NULL,

    codigo VARCHAR(50),

    nome VARCHAR(200) NOT NULL,

    cpf_cnpj VARCHAR(20) NOT NULL,

    inscricao_municipal VARCHAR(50),

    inscricao_estadual VARCHAR(50),

    email VARCHAR(200),

    telefone VARCHAR(30),

    cep VARCHAR(10),

    logradouro VARCHAR(200),

    numero VARCHAR(20),

    complemento VARCHAR(100),

    bairro VARCHAR(100),

    cidade VARCHAR(100),

    uf CHAR(2),

    pais VARCHAR(100) DEFAULT 'Brasil',

    ativo BOOLEAN NOT NULL DEFAULT TRUE,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_tomador_empresa
        FOREIGN KEY (empresa_id)
        REFERENCES core.empresa(id)
        ON DELETE CASCADE,

    CONSTRAINT uk_tomador_empresa_documento
        UNIQUE (empresa_id, cpf_cnpj)

);

COMMENT ON TABLE fiscal.tomador IS
'Cadastro de tomadores de serviços.';

CREATE INDEX IF NOT EXISTS idx_tomador_empresa
ON fiscal.tomador (empresa_id);

CREATE INDEX IF NOT EXISTS idx_tomador_nome
ON fiscal.tomador (nome);

CREATE INDEX IF NOT EXISTS idx_tomador_documento
ON fiscal.tomador (cpf_cnpj);

CREATE TRIGGER trg_tomador_updated_at

BEFORE UPDATE
ON fiscal.tomador

FOR EACH ROW

EXECUTE FUNCTION core.fn_update_updated_at();

COMMIT;
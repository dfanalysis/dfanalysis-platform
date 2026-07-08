-- ==========================================================
-- Plataforma DF Analysis IA
-- Migration: 003_create_empresa.sql
-- Objetivo: Criar tabela de empresas.
-- ==========================================================

BEGIN;

CREATE TABLE IF NOT EXISTS core.empresa (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    razao_social VARCHAR(200) NOT NULL,

    nome_fantasia VARCHAR(200),

    cnpj VARCHAR(14) NOT NULL UNIQUE,

    inscricao_municipal VARCHAR(30),

    inscricao_estadual VARCHAR(30),

    email VARCHAR(200),

    telefone VARCHAR(30),

    ativo BOOLEAN NOT NULL DEFAULT TRUE,

    created_at TIMESTAMP NOT NULL DEFAULT NOW(),

    updated_at TIMESTAMP NOT NULL DEFAULT NOW()

);

COMMENT ON TABLE core.empresa IS
'Empresas cadastradas na Plataforma DF Analysis IA.';

COMMENT ON COLUMN core.empresa.id IS 'Identificador único da empresa.';
COMMENT ON COLUMN core.empresa.razao_social IS 'Razão Social.';
COMMENT ON COLUMN core.empresa.nome_fantasia IS 'Nome Fantasia.';
COMMENT ON COLUMN core.empresa.cnpj IS 'CNPJ sem máscara.';
COMMENT ON COLUMN core.empresa.ativo IS 'Empresa ativa.';
COMMENT ON COLUMN core.empresa.created_at IS 'Data de criação.';
COMMENT ON COLUMN core.empresa.updated_at IS 'Última atualização.';

CREATE INDEX idx_empresa_cnpj
ON core.empresa(cnpj);

CREATE INDEX idx_empresa_ativo
ON core.empresa(ativo);

COMMIT;
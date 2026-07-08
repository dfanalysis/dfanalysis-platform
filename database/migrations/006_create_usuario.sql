-- =====================================================
-- Plataforma DF Analysis IA
-- Migration: 006_create_usuario.sql
-- Objetivo:
-- Criação da tabela de usuários.
-- =====================================================

BEGIN;

CREATE TABLE IF NOT EXISTS core.usuario (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    empresa_id UUID NOT NULL,

    nome VARCHAR(150) NOT NULL,

    email VARCHAR(200) NOT NULL UNIQUE,

    senha_hash TEXT NOT NULL,

    ativo BOOLEAN NOT NULL DEFAULT TRUE,

    ultimo_login TIMESTAMP,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_usuario_empresa
        FOREIGN KEY (empresa_id)
        REFERENCES core.empresa(id)

);

COMMENT ON TABLE core.usuario IS
'Tabela de usuários da plataforma.';

COMMENT ON COLUMN core.usuario.nome IS
'Nome completo do usuário.';

COMMENT ON COLUMN core.usuario.email IS
'E-mail utilizado para autenticação.';

COMMENT ON COLUMN core.usuario.senha_hash IS
'Hash criptográfico da senha.';

CREATE INDEX idx_usuario_empresa
ON core.usuario (empresa_id);

CREATE INDEX idx_usuario_email
ON core.usuario (email);

CREATE TRIGGER trg_usuario_updated_at

BEFORE UPDATE ON core.usuario

FOR EACH ROW

EXECUTE FUNCTION core.fn_update_updated_at();

COMMIT;
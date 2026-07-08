-- ==========================================================
-- Plataforma DF Analysis IA
-- Migration: 008_create_usuario_perfil.sql
-- Versão : 1.0.0
-- Objetivo:
-- Relacionar usuários aos perfis de acesso.
-- ==========================================================

BEGIN;

CREATE TABLE IF NOT EXISTS core.usuario_perfil (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    usuario_id UUID NOT NULL,

    perfil_id UUID NOT NULL,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_usuario_perfil_usuario
        FOREIGN KEY (usuario_id)
        REFERENCES core.usuario(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_usuario_perfil_perfil
        FOREIGN KEY (perfil_id)
        REFERENCES core.perfil(id)
        ON DELETE CASCADE,

    CONSTRAINT uk_usuario_perfil
        UNIQUE (usuario_id, perfil_id)

);

COMMENT ON TABLE core.usuario_perfil IS
'Tabela de relacionamento entre usuários e perfis da plataforma.';

COMMENT ON COLUMN core.usuario_perfil.usuario_id IS
'Usuário vinculado ao perfil.';

COMMENT ON COLUMN core.usuario_perfil.perfil_id IS
'Perfil associado ao usuário.';

CREATE INDEX idx_usuario_perfil_usuario
ON core.usuario_perfil (usuario_id);

CREATE INDEX idx_usuario_perfil_perfil
ON core.usuario_perfil (perfil_id);

COMMIT;
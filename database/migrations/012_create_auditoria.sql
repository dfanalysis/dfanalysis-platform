-- ==========================================================
-- Plataforma DF Analysis IA
-- Migration: 012_create_auditoria.sql
-- Versão: 1.0.0
-- Objetivo:
-- Criar a tabela de auditoria da plataforma.
-- ==========================================================

BEGIN;

CREATE TABLE IF NOT EXISTS auditoria.log (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    tabela VARCHAR(100) NOT NULL,

    registro_id UUID,

    acao VARCHAR(20) NOT NULL,

    usuario_id UUID,

    dados_anteriores JSONB,

    dados_novos JSONB,

    ip VARCHAR(45),

    user_agent TEXT,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_auditoria_usuario
        FOREIGN KEY (usuario_id)
        REFERENCES core.usuario(id)
        ON DELETE SET NULL

);

COMMENT ON TABLE auditoria.log IS
'Tabela de auditoria da plataforma.';

COMMENT ON COLUMN auditoria.log.acao IS
'INSERT, UPDATE, DELETE, LOGIN, LOGOUT, EXECUTION, ERROR, etc.';

COMMENT ON COLUMN auditoria.log.dados_anteriores IS
'Estado anterior do registro.';

COMMENT ON COLUMN auditoria.log.dados_novos IS
'Estado posterior do registro.';

CREATE INDEX IF NOT EXISTS idx_log_tabela
ON auditoria.log(tabela);

CREATE INDEX IF NOT EXISTS idx_log_registro
ON auditoria.log(registro_id);

CREATE INDEX IF NOT EXISTS idx_log_usuario
ON auditoria.log(usuario_id);

CREATE INDEX IF NOT EXISTS idx_log_created_at
ON auditoria.log(created_at);

COMMIT;
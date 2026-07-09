-- ==========================================================
-- Plataforma DF Analysis IA
-- Migration: 014_create_schema_migrations.sql
-- Versão: 1.0.0
-- Objetivo:
-- Controle das migrations executadas.
-- ==========================================================

BEGIN;

CREATE TABLE IF NOT EXISTS core.schema_migrations (

    version VARCHAR(20) PRIMARY KEY,

    description VARCHAR(255) NOT NULL,

    executed_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    executed_by VARCHAR(100) NOT NULL DEFAULT CURRENT_USER

);

COMMENT ON TABLE core.schema_migrations IS
'Histórico das migrations executadas na plataforma.';

COMMIT;
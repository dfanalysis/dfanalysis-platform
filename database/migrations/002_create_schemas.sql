-- ==========================================================
-- Plataforma DF Analysis IA
-- Migration: 002_create_schemas.sql
-- Versão: 1.0.0
-- Objetivo: Criar os schemas da plataforma.
-- Autor: DF Analysis IA
-- ==========================================================

BEGIN;

-- ==========================================================
-- Core
-- ==========================================================
CREATE SCHEMA IF NOT EXISTS core;
COMMENT ON SCHEMA core IS 'Cadastros principais da plataforma.';

-- ==========================================================
-- Financeiro
-- ==========================================================
CREATE SCHEMA IF NOT EXISTS financeiro;
COMMENT ON SCHEMA financeiro IS 'Controle financeiro.';

-- ==========================================================
-- Fiscal
-- ==========================================================
CREATE SCHEMA IF NOT EXISTS fiscal;
COMMENT ON SCHEMA fiscal IS 'Emissão de NFS-e e documentos fiscais.';

-- ==========================================================
-- Comercial
-- ==========================================================
CREATE SCHEMA IF NOT EXISTS comercial;
COMMENT ON SCHEMA comercial IS 'CRM, clientes e oportunidades.';

-- ==========================================================
-- Workflow
-- ==========================================================
CREATE SCHEMA IF NOT EXISTS workflow;
COMMENT ON SCHEMA workflow IS 'Fluxos e automações do n8n.';

-- ==========================================================
-- Integração
-- ==========================================================
CREATE SCHEMA IF NOT EXISTS integracao;
COMMENT ON SCHEMA integracao IS 'Integrações com APIs externas.';

-- ==========================================================
-- Auditoria
-- ==========================================================
CREATE SCHEMA IF NOT EXISTS auditoria;
COMMENT ON SCHEMA auditoria IS 'Logs e trilhas de auditoria.';

COMMIT;
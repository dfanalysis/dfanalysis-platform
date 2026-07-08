-- =====================================================
-- Plataforma DF Analysis IA
-- Migration: 007_create_perfil.sql
-- Objetivo:
-- Cadastro de perfis de acesso.
-- =====================================================

BEGIN;

CREATE TABLE IF NOT EXISTS core.perfil (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    nome VARCHAR(100) NOT NULL UNIQUE,

    descricao TEXT,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP

);

COMMENT ON TABLE core.perfil IS
'Tabela de perfis de acesso da plataforma.';

CREATE TRIGGER trg_perfil_updated_at

BEFORE UPDATE ON core.perfil

FOR EACH ROW

EXECUTE FUNCTION core.fn_update_updated_at();

INSERT INTO core.perfil (nome, descricao)
VALUES
('Administrador','Acesso total'),
('Financeiro','Rotinas financeiras'),
('Fiscal','Rotinas fiscais'),
('Comercial','Área comercial'),
('Operador','Operação diária'),
('IA','Agentes de Inteligência Artificial'),
('API','Integrações externas')
ON CONFLICT (nome) DO NOTHING;

COMMIT;
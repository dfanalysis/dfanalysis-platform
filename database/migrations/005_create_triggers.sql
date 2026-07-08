-- ============================================================================
-- Plataforma DF Analysis IA
-- Migration : 005_create_triggers.sql
-- Versão    : 1.0.0
-- Objetivo  : Criar triggers reutilizáveis.
-- ============================================================================

BEGIN;

CREATE TRIGGER trg_empresa_updated_at

BEFORE UPDATE
ON core.empresa

FOR EACH ROW

EXECUTE FUNCTION core.fn_update_updated_at();

COMMIT;
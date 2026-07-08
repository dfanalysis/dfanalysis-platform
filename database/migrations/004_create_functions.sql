-- ============================================================================
-- Plataforma DF Analysis IA
-- Migration : 004_create_functions.sql
-- Versão    : 1.0.0
-- Objetivo  : Criar funções reutilizáveis da plataforma.
-- ============================================================================

BEGIN;

-- ============================================================================
-- Atualiza automaticamente o campo updated_at
-- ============================================================================

CREATE OR REPLACE FUNCTION core.fn_update_updated_at()
RETURNS TRIGGER
LANGUAGE plpgsql
AS
$$
BEGIN

    NEW.updated_at = NOW();

    RETURN NEW;

END;
$$;

COMMENT ON FUNCTION core.fn_update_updated_at IS
'Atualiza automaticamente o campo updated_at antes de um UPDATE.';

COMMIT;
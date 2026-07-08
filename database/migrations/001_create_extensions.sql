-- ============================================================================
-- Plataforma DF Analysis IA
-- Migration : 001_create_extensions.sql
-- Versão    : 1.0.0
-- Objetivo  : Instalar as extensões utilizadas pela plataforma.
-- Autor     : DF Analysis IA
-- ============================================================================

BEGIN;

-- Geração de UUIDs
CREATE EXTENSION IF NOT EXISTS pgcrypto;

COMMENT ON EXTENSION pgcrypto IS
'Permite a geração de UUIDs utilizando a função gen_random_uuid().';

COMMIT;
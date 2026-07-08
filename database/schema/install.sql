-- ============================================================
-- DF Analysis IA Platform
-- Script Mestre de Instalação
--
-- Objetivo:
-- Criar toda a estrutura do banco do zero.
--
-- Ordem de execução das migrations.
-- ============================================================

\echo '======================================'
\echo 'DF Analysis IA Platform'
\echo 'Iniciando instalação...'
\echo '======================================'

\i ../migrations/001_create_extensions.sql
\i ../migrations/002_create_schemas.sql
\i ../migrations/003_create_empresa.sql
\i ../migrations/004_create_functions.sql
\i ../migrations/005_create_triggers.sql
\i ../migrations/006_create_usuario.sql

\echo '======================================'
\echo 'Instalação concluída com sucesso.'
\echo '======================================'
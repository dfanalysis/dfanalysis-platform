-- ==========================================================
-- Plataforma DF Analysis IA
-- Migration: 018_create_rps.sql
-- Objetivo:
-- Cadastro dos Recibos Provisórios de Serviços (RPS).
-- ==========================================================

BEGIN;

CREATE TABLE IF NOT EXISTS fiscal.rps (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    empresa_id UUID NOT NULL,

    prestador_id UUID NOT NULL,

    tomador_id UUID NOT NULL,

    servico_id UUID NOT NULL,

    numero_rps VARCHAR(30) NOT NULL,

    serie VARCHAR(20) NOT NULL DEFAULT '1',

    tipo VARCHAR(20) NOT NULL DEFAULT 'RPS',

    data_emissao TIMESTAMP NOT NULL,

    competencia DATE NOT NULL,

    valor_servicos NUMERIC(15,2) NOT NULL,

    valor_deducoes NUMERIC(15,2) DEFAULT 0,

    valor_iss NUMERIC(15,2) DEFAULT 0,

    aliquota NUMERIC(5,2),

    iss_retido BOOLEAN NOT NULL DEFAULT FALSE,

    discriminacao TEXT NOT NULL,

    status VARCHAR(30) NOT NULL DEFAULT 'PENDENTE',

    protocolo VARCHAR(100),

    mensagem_retorno TEXT,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_rps_empresa
        FOREIGN KEY (empresa_id)
        REFERENCES core.empresa(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_rps_prestador
        FOREIGN KEY (prestador_id)
        REFERENCES fiscal.prestador(id),

    CONSTRAINT fk_rps_tomador
        FOREIGN KEY (tomador_id)
        REFERENCES fiscal.tomador(id),

    CONSTRAINT fk_rps_servico
        FOREIGN KEY (servico_id)
        REFERENCES fiscal.servico(id)

);

COMMENT ON TABLE fiscal.rps IS
'Recibos Provisórios de Serviços utilizados na emissão de NFS-e.';

CREATE INDEX IF NOT EXISTS idx_rps_empresa
ON fiscal.rps (empresa_id);

CREATE INDEX IF NOT EXISTS idx_rps_status
ON fiscal.rps (status);

CREATE INDEX IF NOT EXISTS idx_rps_numero
ON fiscal.rps (numero_rps);

CREATE INDEX IF NOT EXISTS idx_rps_competencia
ON fiscal.rps (competencia);

CREATE TRIGGER trg_rps_updated_at

BEFORE UPDATE
ON fiscal.rps

FOR EACH ROW

EXECUTE FUNCTION core.fn_update_updated_at();

COMMIT;
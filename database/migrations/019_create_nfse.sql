-- ==========================================================
-- Plataforma DF Analysis IA
-- Migration: 019_create_nfse.sql
-- Objetivo:
-- Cadastro das Notas Fiscais de Serviços Eletrônicas.
-- ==========================================================

BEGIN;

CREATE TABLE IF NOT EXISTS fiscal.nfse (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    rps_id UUID NOT NULL,

    empresa_id UUID NOT NULL,

    numero_nfse VARCHAR(50) NOT NULL,

    codigo_verificacao VARCHAR(100),

    protocolo VARCHAR(100),

    data_emissao TIMESTAMP NOT NULL,

    competencia DATE NOT NULL,

    valor_servicos NUMERIC(15,2) NOT NULL,

    valor_deducoes NUMERIC(15,2) DEFAULT 0,

    valor_iss NUMERIC(15,2) DEFAULT 0,

    aliquota NUMERIC(5,2),

    iss_retido BOOLEAN NOT NULL DEFAULT FALSE,

    status VARCHAR(30) NOT NULL DEFAULT 'EMITIDA',

    xml TEXT,

    pdf TEXT,

    url_consulta TEXT,

    observacoes TEXT,

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_nfse_rps
        FOREIGN KEY (rps_id)
        REFERENCES fiscal.rps(id),

    CONSTRAINT fk_nfse_empresa
        FOREIGN KEY (empresa_id)
        REFERENCES core.empresa(id)
        ON DELETE CASCADE,

    CONSTRAINT uk_nfse_numero_empresa
        UNIQUE (empresa_id, numero_nfse)

);

COMMENT ON TABLE fiscal.nfse IS
'Notas Fiscais de Serviços Eletrônicas emitidas.';

CREATE INDEX IF NOT EXISTS idx_nfse_empresa
ON fiscal.nfse (empresa_id);

CREATE INDEX IF NOT EXISTS idx_nfse_numero
ON fiscal.nfse (numero_nfse);

CREATE INDEX IF NOT EXISTS idx_nfse_data
ON fiscal.nfse (data_emissao);

CREATE INDEX IF NOT EXISTS idx_nfse_status
ON fiscal.nfse (status);

CREATE TRIGGER trg_nfse_updated_at

BEFORE UPDATE
ON fiscal.nfse

FOR EACH ROW

EXECUTE FUNCTION core.fn_update_updated_at();

COMMIT;
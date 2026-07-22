# ADR-008 — Ciclo de Vida do Domínio Fiscal

- **Status:** Aceito
- **Data:** 2026-07-20
- **Decisores:** DF Analysis
- **Contexto:** Plataforma DF Analysis IA
- **Domínio:** Fiscal / Emissão de NFS-e

---

## 1. Contexto

A Plataforma DF Analysis IA automatizará o processo de emissão de Notas
Fiscais de Serviços Eletrônicas — NFS-e.

O processo operacional começa com uma solicitação recebida por canais como
e-mail, API, ERP, portal, WhatsApp, n8n ou agentes de IA.

Essa solicitação pode conter relatórios de produção, documentos fiscais,
planilhas, PDFs, XMLs e outras evidências necessárias para determinar:

- empresa prestadora;
- tomador do serviço;
- competência;
- descrição do serviço;
- valor;
- executantes;
- tributação;
- demais dados necessários à emissão.

Após interpretação e validação, a plataforma prepara o documento fiscal,
realiza a integração com o provedor municipal e registra o resultado
autorizado ou rejeitado.

A implementação inicial utilizará o ISSNET do Distrito Federal, mas o núcleo
da plataforma não deverá depender diretamente de um provedor ou município.

---

## 2. Problema

Sem uma separação explícita entre solicitação operacional, documento
provisório e documento fiscal autorizado, o sistema poderia:

- misturar dados recebidos com dados fiscais preparados;
- confundir validação interna com validação municipal;
- duplicar responsabilidades entre módulos;
- acoplar o domínio ao ISSNET;
- dificultar reprocessamentos;
- dificultar auditoria;
- dificultar suporte a outros municípios;
- permitir transições inválidas de status;
- reenviar documentos já processados;
- perder rastreabilidade entre entrada, RPS, lote, protocolo e NFS-e.

---

## 3. Decisão

O domínio fiscal será estruturado inicialmente em três aggregates principais:

1. `SolicitacaoEmissao`;
2. `Rps`;
3. `Nfse`.

O envio ao provedor será representado separadamente por uma entidade de
integração, inicialmente denominada `LoteRps`.

Os aggregates possuem responsabilidades distintas e não deverão ser tratados
como diferentes nomes para o mesmo documento.

---

## 4. Aggregate `SolicitacaoEmissao`

### 4.1 Definição

Representa a intenção operacional de emitir uma NFS-e.

É criada após a recepção, interpretação e consolidação das informações
necessárias à emissão.

### 4.2 Responsabilidades

A solicitação é responsável por:

- identificar a empresa proprietária;
- manter a origem da solicitação;
- manter a correlação com o processo operacional;
- garantir idempotência;
- registrar competência;
- registrar descrição e valor do serviço;
- passar por validação interna;
- indicar se está apta à preparação fiscal;
- registrar rejeições anteriores ao envio municipal.

### 4.3 Estados

```text
RECEBIDA
    ↓
EM_VALIDACAO
    ├── VALIDADA
    └── REJEITADA

VALIDADA
    ↓
AGUARDANDO_PROCESSAMENTO
    ↓
PROCESSANDO
    ├── EMITIDA
    ├── FALHA
    └── CANCELADA
cat > ../docs/adr/ADR-008-fiscal-lifecycle.md <<'EOF'
# ADR-008 — Ciclo de Vida do Domínio Fiscal

- **Status:** Aceito
- **Data:** 2026-07-20
- **Decisores:** DF Analysis
- **Contexto:** Plataforma DF Analysis IA
- **Domínio:** Fiscal / Emissão de NFS-e

---

## 1. Contexto

A Plataforma DF Analysis IA automatizará o processo de emissão de Notas
Fiscais de Serviços Eletrônicas — NFS-e.

O processo operacional começa com uma solicitação recebida por canais como
e-mail, API, ERP, portal, WhatsApp, n8n ou agentes de IA.

Essa solicitação pode conter relatórios de produção, documentos fiscais,
planilhas, PDFs, XMLs e outras evidências necessárias para determinar:

- empresa prestadora;
- tomador do serviço;
- competência;
- descrição do serviço;
- valor;
- executantes;
- tributação;
- demais dados necessários à emissão.

Após interpretação e validação, a plataforma prepara o documento fiscal,
realiza a integração com o provedor municipal e registra o resultado
autorizado ou rejeitado.

A implementação inicial utilizará o ISSNET do Distrito Federal, mas o núcleo
da plataforma não deverá depender diretamente de um provedor ou município.

---

## 2. Problema

Sem uma separação explícita entre solicitação operacional, documento
provisório e documento fiscal autorizado, o sistema poderia:

- misturar dados recebidos com dados fiscais preparados;
- confundir validação interna com validação municipal;
- duplicar responsabilidades entre módulos;
- acoplar o domínio ao ISSNET;
- dificultar reprocessamentos;
- dificultar auditoria;
- dificultar suporte a outros municípios;
- permitir transições inválidas de status;
- reenviar documentos já processados;
- perder rastreabilidade entre entrada, RPS, lote, protocolo e NFS-e.

---

## 3. Decisão

O domínio fiscal será estruturado inicialmente em três aggregates principais:

1. `SolicitacaoEmissao`;
2. `Rps`;
3. `Nfse`.

O envio ao provedor será representado separadamente por uma entidade de
integração, inicialmente denominada `LoteRps`.

Os aggregates possuem responsabilidades distintas e não deverão ser tratados
como diferentes nomes para o mesmo documento.

---

## 4. Aggregate `SolicitacaoEmissao`

### 4.1 Definição

Representa a intenção operacional de emitir uma NFS-e.

É criada após a recepção, interpretação e consolidação das informações
necessárias à emissão.

### 4.2 Responsabilidades

A solicitação é responsável por:

- identificar a empresa proprietária;
- manter a origem da solicitação;
- manter a correlação com o processo operacional;
- garantir idempotência;
- registrar competência;
- registrar descrição e valor do serviço;
- passar por validação interna;
- indicar se está apta à preparação fiscal;
- registrar rejeições anteriores ao envio municipal.

### 4.3 Estados

```text
RECEBIDA
    ↓
EM_VALIDACAO
    ├── VALIDADA
    └── REJEITADA

VALIDADA
    ↓
AGUARDANDO_PROCESSAMENTO
    ↓
PROCESSANDO
    ├── EMITIDA
    ├── FALHA
    └── CANCELADA

# Modelo Conceitual da Plataforma DF Analysis IA

## Objetivo

Este documento define os principais conceitos de negócio da plataforma, seus relacionamentos e responsabilidades.

O modelo conceitual representa o domínio do negócio de forma independente da implementação técnica.

Ele servirá como referência para:

- Modelagem das entidades
- Modelagem do banco de dados
- APIs
- Agentes de IA
- Regras de negócio
- Fluxos de automação
- Documentação da plataforma

---

# Estrutura Geral

```
                    ORGANIZAÇÃO
                         │
      ┌──────────────────┼──────────────────┐
      │                  │                  │
      ▼                  ▼                  ▼
Empresa Médica      Hospital          Clínica
      │
      ▼
Cooperativa (quando aplicável)


                    PESSOA
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
       Médico                  Paciente
```

---

# Papéis

As entidades assumem papéis de acordo com o contexto do processo.

Os papéis não representam entidades.

Representam responsabilidades temporárias dentro de um fluxo.

```
Empresa Médica
        │
        ▼
Prestador


Hospital
Clínica
Paciente
Empresa
        │
        ▼
Tomador


Hospital
Clínica
Administrador
Secretária
Médico
        │
        ▼
Solicitante


Médico
        │
        ▼
Médico Executante
```

---

# Relações

Empresa Médica
    emite
        ↓
      NFS-e

NFS-e
    possui
        ↓
Tomador

NFS-e
    possui
        ↓
Prestador

Solicitação de Emissão
    gera
        ↓
NFS-e

InboxMessage
    origina
        ↓
Solicitação de Emissão

Solicitação de Emissão
    utiliza
        ↓
EvidenceBundle

EvidenceBundle
    agrupa
        ↓
Documentos

Documentos
    são interpretados por
        ↓
Agentes de IA

Agentes de IA
    produzem
        ↓
Dados Estruturados

Dados Estruturados
    alimentam
        ↓
Solicitação de Emissão
```

---

# Princípios

## Entidade

Representa algo que existe independentemente do processo.

Exemplos:

- Empresa Médica
- Hospital
- Clínica
- Médico
- Paciente

---

## Papel

Representa a função desempenhada por uma entidade dentro de um processo.

Exemplos:

- Prestador
- Tomador
- Solicitante
- Médico Executante

Uma mesma entidade pode assumir papéis diferentes em processos distintos.

---

## Processo

Representa uma sequência organizada de atividades.

Exemplo:

Recebimento do e-mail

↓

Leitura dos anexos

↓

Extração de informações

↓

Validação

↓

Solicitação de emissão

↓

Emissão da NFS-e

---

## Documento

Representa qualquer evidência utilizada pelo sistema.

Exemplos:

- XML
- PDF
- XLSX
- E-mail
- Imagem

---

## Evidência

Conjunto de documentos relacionados a uma mesma comunicação.

Representado internamente pelo EvidenceBundle.

---

## Agente

Responsável por interpretar documentos, aplicar regras de negócio e produzir informações estruturadas.

Os agentes não substituem o domínio.

Eles operam sobre o domínio.

---

# Regra Fundamental

O domínio é a fonte da verdade.

A implementação deve refletir o domínio.

Nunca o contrário.
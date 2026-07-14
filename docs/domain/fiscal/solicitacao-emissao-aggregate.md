# Aggregate — Solicitação de Emissão

## Visão Geral

A Solicitação de Emissão é o Aggregate Root do domínio fiscal.

Ela representa todo o ciclo de vida de uma emissão de documento fiscal, desde a recepção da solicitação até a autorização, rejeição ou cancelamento.

## Estrutura conceitual

```text
SolicitacaoEmissao
│
├── Identificação
│   ├── id
│   ├── correlation_id
│   ├── idempotency_key
│
├── Origem
│   ├── origem
│   ├── referencia_externa
│
├── Empresa
│   └── empresa_id
│
├── Serviço
│   ├── competência
│   ├── descrição
│   └── município
│
├── Valores
│   ├── valor_servico
│   ├── descontos
│   └── valor_liquido
│
├── Situação
│   └── status
│
├── Documento Provisório
│   ├── RPS
│   └── DPS
│
├── Documento Fiscal
│   └── NFS-e
│
├── Eventos
│
├── Protocolos
│
└── Auditoria
    ├── created_at
    └── updated_at
```

## Responsabilidades

A Solicitação de Emissão é responsável por:

- controlar o ciclo de vida da emissão;
- garantir a consistência das informações fiscais;
- controlar mudanças de estado;
- manter rastreabilidade;
- relacionar documentos provisórios e NFS-e;
- registrar eventos fiscais;
- impedir emissões duplicadas.

## Fora do Aggregate

Não pertencem diretamente ao Aggregate:

- SOAP;
- XML;
- ISSNet;
- certificados digitais;
- URLs externas;
- autenticação;
- filas;
- workflows do n8n.

Esses componentes pertencem às camadas de integração e infraestrutura.
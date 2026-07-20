# Hospital

## Objetivo

Representa uma instituição hospitalar que contrata serviços médicos e recebe documentos fiscais emitidos pelas Empresas Médicas.

## Especialização

Herda os atributos da entidade Organização.

## Responsabilidades

- Contratar serviços médicos.
- Receber NFS-e.
- Disponibilizar relatórios analíticos de produção.
- Efetuar pagamentos aos prestadores.

## Relacionamentos

Um Hospital pode:

- contratar diversas Empresas Médicas;
- receber diversas NFS-e;
- gerar diversos relatórios analíticos;
- participar de diversos processos administrativos.

## Papéis

Pode assumir os papéis de:

- Tomador
- Solicitante

## Regras de Negócio

- Deve possuir CNPJ válido.
- Pode contratar diversas Empresas Médicas simultaneamente.
- Pode possuir regras específicas para faturamento e prestação de contas.

## Observações

O Hospital é um dos principais tomadores de serviços da plataforma e uma importante fonte de documentos para os Agentes de IA.
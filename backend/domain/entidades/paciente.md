# Paciente

## Objetivo

Representa a pessoa física destinatária de serviços médicos quando houver faturamento direto.

## Especialização

Herda os atributos da entidade Pessoa.

## Responsabilidades

- Receber serviços médicos.
- Atuar como tomador em atendimentos particulares.

## Relacionamentos

Um Paciente pode:

- receber diversos atendimentos;
- constar como tomador em NFS-e;
- participar de processos administrativos relacionados ao atendimento.

## Papéis

Pode assumir o papel de:

- Tomador

## Regras de Negócio

- Deve possuir identificação válida (CPF quando aplicável).
- Pode receber serviços de diferentes Empresas Médicas.

## Observações

Na maioria dos processos da plataforma, o tomador será um Hospital ou Clínica. Entretanto, em atendimentos particulares, o Paciente poderá assumir o papel de Tomador.
# Pessoa

## Objetivo

Representa qualquer pessoa física que participa dos processos da Plataforma DF Analysis IA.

## Especializações

- Médico
- Paciente
- Administrador
- Secretária
- Colaborador

## Atributos

- id
- nome
- CPF
- data de nascimento
- e-mail
- telefone
- endereço
- status

## Papéis possíveis

Uma pessoa pode assumir diferentes papéis conforme o processo:

- Médico Executante
- Solicitante
- Responsável Técnico
- Usuário da Plataforma

## Relacionamentos

Uma pessoa pode:

- estar vinculada a uma ou mais organizações;
- solicitar processos administrativos;
- executar procedimentos médicos;
- utilizar a plataforma conforme suas permissões.

## Observações

Assim como Organização, Pessoa representa uma entidade permanente.

Os papéis exercidos dependem exclusivamente do contexto do processo.
# Organização

## Objetivo

Representa qualquer pessoa jurídica cadastrada na Plataforma DF Analysis IA.

É a entidade base para todas as organizações que participam dos processos administrativos.

## Especializações

- Empresa Médica
- Hospital
- Clínica
- Cooperativa
- Empresa Contratante

## Atributos

- id
- razão social
- nome fantasia
- CNPJ
- inscrição municipal
- inscrição estadual
- endereço
- município
- UF
- CEP
- e-mail
- telefone
- status

## Papéis possíveis

Uma organização pode assumir diferentes papéis conforme o processo:

- Prestador
- Tomador
- Solicitante

## Relacionamentos

Uma organização pode:

- emitir NFS-e;
- receber NFS-e;
- solicitar emissões;
- participar de processos administrativos;
- possuir usuários vinculados.

## Observações

Os papéis são definidos pelo contexto do processo e não pela entidade em si.
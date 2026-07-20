# Prestador

## Objetivo

Representa o papel exercido pela entidade responsável pela prestação do serviço descrito na NFS-e.

O Prestador não é uma entidade, mas um papel assumido por uma Organização durante um processo de prestação de serviços.

## Quem pode assumir este papel

- Empresa Médica

## Responsabilidades

- Executar a prestação do serviço.
- Emitir a NFS-e.
- Cumprir obrigações fiscais decorrentes da prestação.

## Relacionamentos

O Prestador:

- emite NFS-e;
- possui um ou mais Médicos vinculados;
- presta serviços para um Tomador.

## Regras de Negócio

- Deve possuir CNPJ ativo.
- Deve possuir Inscrição Municipal quando exigida.
- Deve estar autorizado a emitir NFS-e.
- Pode emitir diversas NFS-e para diferentes Tomadores.

## Observações

Na Plataforma DF Analysis IA, o Prestador será, na prática, uma Empresa Médica, mas o conceito permanece desacoplado da entidade para preservar a flexibilidade do modelo de domínio.
---

id: ENT-FAT-001
titulo: Prestador de Serviços
contexto: Faturamento
versao: 1.0.0
status: Aprovada
ultima_atualizacao: 2026-07-19
responsavel: DF Analysis
------------------------

# Prestador de Serviços

## Definição

O Prestador é a empresa médica responsável pela execução ou formalização dos serviços médicos e pela emissão da NFS-e.

No escopo inicial da Plataforma DF Analysis IA, o Prestador será uma pessoa jurídica identificada por CNPJ.

## Responsabilidades

O Prestador:

* presta ou formaliza a prestação do serviço médico;
* possui cadastro fiscal e municipal;
* possui configuração tributária;
* utiliza credenciais ou certificado para emissão;
* emite a NFS-e;
* recebe o valor correspondente aos serviços faturados.

## Exemplos

* empresa médica de um médico individual;
* empresa médica formada por vários médicos;
* empresa médica responsável por plantões;
* empresa médica contratada por hospital ou clínica.

## Restrições

Uma solicitação de emissão deverá estar vinculada a um único Prestador.

O Prestador deverá estar cadastrado, ativo e autorizado para emissão antes do processamento da NFS-e.

O Prestador não deverá ser confundido com:

* médico executante;
* hospital;
* clínica;
* paciente;
* remetente do e-mail;
* solicitante operacional.

# Solicitante

## Objetivo

Representa o papel exercido pelo ator que inicia formalmente um processo na Plataforma DF Analysis IA.

O Solicitante pode encaminhar uma demanda por e-mail, formulário, API, integração com ERP, WhatsApp ou outro canal autorizado.

## Quem pode assumir este papel

* Hospital
* Clínica
* Cooperativa
* Empresa Médica
* Médico
* Administrador
* Secretária
* Colaborador
* Sistema externo

## Responsabilidades

* Iniciar uma solicitação.
* Fornecer informações e documentos necessários.
* Identificar o tipo de processo solicitado.
* Responder a pedidos de complementação.
* Acompanhar o resultado da solicitação, quando autorizado.

## Relacionamentos

O Solicitante:

* cria ou origina uma Solicitação;
* pode encaminhar documentos e evidências;
* pode representar uma Pessoa ou Organização;
* pode ser notificado sobre validações, pendências, erros e conclusões;
* pode também assumir outro papel no mesmo processo.

## Regras de Negócio

* Deve ser identificável por um canal ou credencial confiável.
* Deve estar autorizado a solicitar o processo em nome da organização relacionada.
* Toda solicitação deve registrar sua origem.
* A identidade do Solicitante deve permanecer vinculada ao histórico do processo.
* Solicitações automatizadas devem identificar o sistema ou integração de origem.
* Um Solicitante não precisa ser o Tomador, o Prestador ou o beneficiário final do processo.

## Origem da solicitação

A solicitação pode ser originada por:

* e-mail;
* formulário da plataforma;
* API;
* webhook;
* integração com ERP;
* WhatsApp;
* processamento interno;
* rotina agendada;
* evento de domínio.

## Observações

O Solicitante é um papel operacional e de auditoria.

A plataforma deve distinguir:

* quem solicitou;
* em nome de quem solicitou;
* quem executou o serviço;
* quem presta o serviço;
* quem recebe o serviço.

Essa separação é necessária para segurança, rastreabilidade e controle de acesso.

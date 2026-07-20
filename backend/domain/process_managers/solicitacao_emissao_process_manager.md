# Process Manager — Solicitação de Emissão

## Objetivo

Coordenar todo o ciclo de vida de uma Solicitação de Emissão de NFS-e, reagindo aos eventos do domínio e das integrações para conduzir o processo até sua conclusão.

---

## Responsabilidades

- Orquestrar o fluxo da emissão.
- Reagir aos Business Events.
- Reagir aos Integration Events.
- Reagir aos Exception Events.
- Iniciar novas ações quando necessário.
- Controlar timeout e reprocessamentos.

---

## Eventos observados

### Business Events

- Solicitação de Emissão Criada
- Documento Validado
- Competência Validada
- Cálculo Tributário Concluído
- Emissão Autorizada
- NFS-e Emitida
- Repasse Apurado

### Integration Events

- E-mail Recebido
- Requisição de Emissão Enviada
- Resposta de Emissão Recebida
- XML Recebido
- PDF Recebido

### Exception Events

- Documento Rejeitado
- Competência Bloqueada
- Emissão Bloqueada
- NFS-e Rejeitada
- Provedor Indisponível

---

## Fluxo

E-mail Recebido
↓
Criar Solicitação
↓
Validar Documentos
↓
Calcular Tributos
↓
Autorizar Emissão
↓
Emitir NFS-e
↓
Receber XML/PDF
↓
Apurar Repasse
↓
Solicitar Notificação

---

## Observações

O Process Manager coordena o fluxo, mas não executa regras de negócio. As decisões permanecem nos Aggregates, Policies e Domain Services.
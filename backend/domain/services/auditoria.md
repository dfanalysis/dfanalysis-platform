# Domain Service — Auditoria

## Objetivo

O Domain Service de Auditoria é responsável por registrar, consolidar e disponibilizar informações que permitam reconstruir todo o histórico de execução dos processos da Plataforma DF Analysis IA.

Seu objetivo é garantir rastreabilidade, transparência e conformidade, preservando evidências das decisões tomadas pelo domínio.

---

# Motivação

Durante o ciclo operacional de uma Solicitação de Emissão diversos eventos ocorrem:

* documentos são recebidos;
* validações são executadas;
* decisões são tomadas;
* cálculos são realizados;
* NFS-e são emitidas;
* repasses são apurados.

Todos esses acontecimentos precisam ser registrados para permitir auditorias futuras.

---

# Responsabilidades

O serviço é responsável por:

* registrar eventos relevantes;
* registrar alterações de estado;
* registrar responsáveis;
* registrar origem das operações;
* registrar versões de regras utilizadas;
* registrar decisões automatizadas;
* registrar decisões humanas;
* consolidar trilhas de auditoria.

---

# Entradas

O serviço recebe:

* eventos de domínio;
* Aggregates;
* decisões;
* alterações;
* metadados de execução.

---

# Saídas

O serviço produz:

* registros de auditoria;
* trilhas de execução;
* histórico consolidado;
* evidências para conformidade.

---

# Regras de Negócio

O serviço deve garantir que:

* registros nunca sejam alterados;
* alterações sejam registradas como novos eventos;
* toda decisão possua responsável identificado;
* decisões automatizadas registrem mecanismo e versão;
* registros possuam data e hora;
* registros sejam cronológicos.

---

# Eventos auditáveis

Exemplos:

* Solicitação criada;
* Documento anexado;
* Documento validado;
* Pendência criada;
* NFS-e emitida;
* NFS-e cancelada;
* Repasse aprovado;
* Pagamento registrado.

---

# Limites

Este Domain Service não:

* controla permissões;
* envia notificações;
* realiza persistência diretamente;
* executa integrações externas.

---

# Observações

Toda informação produzida pela Auditoria deve ser suficiente para reconstruir integralmente um processo administrativo, mesmo anos após sua execução.

# Domain Policy — Política Tributária

## Objetivo

A Política Tributária define as regras utilizadas para determinar quais normas fiscais e tributárias devem ser aplicadas a uma operação de prestação de serviços.

Seu objetivo é orientar as decisões tributárias do domínio, sem executar cálculos ou integrações com sistemas externos.

---

# Motivação

As regras tributárias variam conforme diversos fatores, incluindo:

* município;
* legislação vigente;
* regime tributário do Prestador;
* natureza do serviço;
* local da prestação;
* retenções;
* benefícios fiscais.

Essas decisões representam políticas do domínio e não pertencem aos Aggregates nem aos Domain Services.

---

# Responsabilidades

A Política Tributária é responsável por responder perguntas como:

* qual legislação deve ser aplicada?
* existe incidência de ISS?
* existe retenção tributária?
* quais tributos devem ser considerados?
* qual regime tributário está vigente?
* existe alguma regra municipal específica?
* existe benefício fiscal aplicável?
* esta operação possui tratamento tributário diferenciado?

---

# Escopo

A política pode ser aplicada sobre:

* Solicitação de Emissão;
* NFS-e;
* Prestador;
* Tomador;
* Município;
* Competência;
* Natureza do Serviço;
* Configuração Tributária.

---

# Critérios de decisão

A avaliação pode considerar:

* município da incidência;
* legislação vigente;
* CNAE;
* item da lista de serviços;
* natureza da operação;
* regime tributário;
* retenções;
* imunidades;
* isenções;
* incentivos fiscais;
* acordos específicos.

---

# Resultado da avaliação

A política pode produzir:

* Tributação Padrão;
* Tributação Diferenciada;
* Tributação com Retenção;
* Tributação Isenta;
* Tributação Imune;
* Tributação Não Permitida;
* Tributação Requer Análise Manual.

Quando aplicável, todos os fundamentos da decisão devem ser registrados.

---

# Regras de Negócio

A política deve garantir que:

* apenas regras vigentes sejam utilizadas;
* toda decisão possua fundamento identificável;
* alterações legislativas possam coexistir por versão;
* exceções sejam registradas;
* decisões tributárias sejam reproduzíveis;
* diferentes municípios possam possuir políticas distintas.

---

# Versionamento

As regras tributárias devem permitir versionamento.

Mudanças legislativas não devem alterar decisões já registradas em competências anteriores.

Cada decisão deve estar vinculada à versão da política utilizada.

---

# Exceções

A política pode permitir exceções quando:

* houver determinação legal;
* existir decisão administrativa formal;
* houver regime especial concedido ao Prestador;
* existir benefício fiscal vigente;
* legislação municipal determinar tratamento específico.

Toda exceção deve possuir justificativa e registro de auditoria.

---

# Relação com Domain Services

Esta Policy não realiza cálculos tributários.

Ela apenas determina quais regras devem ser utilizadas.

O cálculo efetivo é responsabilidade do Domain Service de Cálculo Tributário.

---

# Evolução

A política deve ser preparada para suportar:

* ISS;
* IBS;
* CBS;
* futuros tributos;
* alterações da Reforma Tributária;
* múltiplos municípios;
* múltiplos provedores de NFS-e;
* novas versões da legislação.

---

# Observações

A Política Tributária representa o ponto central de decisão fiscal da Plataforma DF Analysis IA.

Ao concentrar as decisões tributárias em uma Policy, o domínio permanece desacoplado das constantes mudanças legislativas, permitindo que novas regras sejam incorporadas sem alterar Aggregates ou Domain Services.

Essa abordagem favorece a evolução contínua da plataforma, especialmente diante da implementação gradual da Reforma Tributária e da expansão para novos municípios.

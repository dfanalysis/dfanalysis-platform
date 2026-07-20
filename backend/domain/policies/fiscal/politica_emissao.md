# Domain Policy — Política de Emissão

## Objetivo

A Política de Emissão define os critérios que determinam se uma Solicitação de Emissão está apta a prosseguir para a geração de uma Nota Fiscal de Serviços Eletrônica (NFS-e).

Seu objetivo é centralizar as decisões relacionadas à autorização da emissão, garantindo que todas as condições obrigatórias do domínio tenham sido atendidas antes do início do processo fiscal.

---

# Motivação

A emissão de uma NFS-e depende da verificação simultânea de diversos requisitos.

Entre eles:

* documentação completa;
* validações aprovadas;
* competência permitida;
* Prestador habilitado;
* Tomador identificado;
* regras tributárias definidas;
* inexistência de bloqueios fiscais;
* requisitos específicos do município.

Essas decisões representam políticas do domínio e devem permanecer desacopladas dos Aggregates e dos Domain Services.

---

# Responsabilidades

A Política de Emissão é responsável por responder perguntas como:

* esta Solicitação pode ser emitida?
* todos os requisitos obrigatórios foram atendidos?
* existe alguma pendência impeditiva?
* existe alguma restrição tributária?
* o Prestador está autorizado?
* o Tomador está apto?
* a competência permite emissão?
* existe bloqueio operacional?

---

# Escopo

A política pode ser aplicada sobre:

* Solicitação de Emissão;
* Prestador;
* Tomador;
* Competência;
* documentos;
* resultados das validações;
* configuração tributária;
* município;
* processo administrativo.

---

# Critérios de decisão

A avaliação pode considerar:

* documentos obrigatórios;
* resultado das validações;
* situação do Prestador;
* situação do Tomador;
* competência;
* política tributária;
* regras municipais;
* existência de bloqueios;
* pendências críticas;
* aprovações obrigatórias;
* inconsistências cadastrais.

---

# Resultado da avaliação

A política pode produzir:

* Emissão Permitida;
* Emissão Permitida com Ressalvas;
* Emissão Bloqueada;
* Emissão Condicionada à Aprovação;
* Emissão Requer Revisão Manual.

Sempre que a emissão não for permitida, todos os motivos devem ser registrados.

---

# Motivos comuns de bloqueio

Exemplos:

* documentos obrigatórios ausentes;
* divergência crítica;
* competência encerrada;
* Prestador inativo;
* Tomador inválido;
* município não suportado;
* erro tributário;
* cálculo tributário inconsistente;
* ausência de autorização obrigatória;
* bloqueio administrativo.

---

# Regras de Negócio

A política deve garantir que:

* nenhuma emissão ocorra sem validação prévia;
* apenas competências permitidas sejam utilizadas;
* decisões tributárias estejam definidas;
* documentos obrigatórios estejam presentes;
* bloqueios críticos interrompam automaticamente o processo;
* exceções sejam registradas;
* aprovações especiais sejam auditadas;
* toda decisão seja reproduzível.

---

# Exceções

A política pode permitir emissão excepcional quando:

* houver autorização administrativa formal;
* existir determinação legal;
* houver procedimento extraordinário previsto;
* existir justificativa registrada;
* a exceção estiver prevista em política organizacional.

Toda exceção deve ser auditada.

---

# Dependências

A Política de Emissão pode depender de:

* Política de Competência;
* Política Tributária;
* Política de Documentos;
* Política de Validação;
* regras específicas do município;
* regras organizacionais.

---

# Relação com Domain Services

Esta Policy não:

* emite NFS-e;
* gera XML;
* transmite documentos;
* consulta provedores;
* grava informações em banco.

Ela apenas informa ao Domain Service de Emissão da NFS-e se a operação pode prosseguir.

---

# Evolução

Novos critérios poderão ser adicionados para suportar:

* padrão nacional da NFS-e;
* novos municípios;
* novos provedores;
* múltiplos regimes tributários;
* Reforma Tributária;
* novos processos internos.

---

# Observações

A Política de Emissão representa o principal mecanismo decisório do contexto fiscal da Plataforma DF Analysis IA.

Ao concentrar todas as regras que autorizam ou impedem uma emissão, o domínio permanece consistente, auditável e preparado para evoluir sem modificar os Aggregates ou os Domain Services.

Essa abordagem reforça a separação entre **decisão** (Policy) e **execução** (Domain Service), um dos princípios fundamentais da arquitetura adotada pela plataforma.

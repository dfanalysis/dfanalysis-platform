# Domain Event — Documento Não Identificado

## Objetivo

O evento **Documento Não Identificado** representa o momento em que um documento recebido pela Plataforma DF Analysis IA não pôde ser classificado de forma confiável durante o processo de identificação documental.

Esse evento indica que o domínio não conseguiu determinar a natureza do documento e, por consequência, não pode prosseguir automaticamente com as etapas subsequentes do processo.

---

# Motivação

A plataforma recebe documentos provenientes de diversas fontes, como:

* e-mails;
* uploads manuais;
* integrações com ERPs;
* sistemas hospitalares;
* provedores fiscais.

Embora a maioria dos documentos possa ser identificada automaticamente, alguns podem apresentar características que inviabilizam sua classificação.

Exemplos:

* formato desconhecido;
* conteúdo incompatível;
* arquivo corrompido;
* baixa qualidade de digitalização;
* documento incompleto;
* novo tipo documental ainda não suportado.

Quando isso ocorre, o domínio publica este evento para registrar o fato e permitir tratamento apropriado.

---

# Quando ocorre

O evento deve ser publicado quando:

* o processo de identificação documental for concluído sem sucesso;
* não houver confiança suficiente para classificar o documento;
* a continuidade automática representar risco para o processo.

---

# Dados do evento

O evento pode conter:

* identificador do documento;
* identificador do Evidence Bundle;
* origem do documento;
* tipo do arquivo;
* nome original;
* hash do arquivo;
* tamanho;
* data e hora do recebimento;
* motivo da não identificação;
* nível de confiança da classificação, quando aplicável;
* identificador do Processo Administrativo.

O evento deve conter apenas as informações necessárias para seus consumidores.

---

# Possíveis consumidores

O evento pode ser consumido por:

* Domain Service de Auditoria;
* Domain Service de Notificação;
* módulo Administrativo;
* fila de análise manual;
* monitoramento operacional;
* agentes especializados em classificação documental.

Cada consumidor reage ao evento conforme sua responsabilidade.

---

# Regras de Negócio

O evento deve ser publicado quando:

* nenhuma classificação atingir o nível mínimo de confiança definido pela Política de Documentos;
* não existir regra determinística capaz de identificar o documento;
* a continuidade automática puder comprometer a integridade do processo.

A publicação do evento interrompe apenas o fluxo relacionado ao documento afetado, preservando os demais documentos do mesmo processo sempre que possível.

---

# Imutabilidade

Após publicado, o evento é imutável.

Caso o documento seja posteriormente identificado por intervenção humana ou por reprocessamento automático, um novo evento deverá representar esse fato.

---

# Auditoria

Devem ser registrados:

* documento analisado;
* algoritmos utilizados;
* nível de confiança obtido;
* motivo da rejeição da classificação;
* data e hora;
* origem da análise;
* identificador do Processo Administrativo;
* identificador do Evidence Bundle.

---

# Relação com o domínio

Este evento representa um fato operacional do domínio.

Ele não significa falha técnica da plataforma, mas sim a impossibilidade de classificar um documento com segurança suficiente para permitir a continuidade automática do processo.

---

# Relação com políticas

A decisão de considerar um documento "não identificado" deve respeitar os critérios definidos pela Política de Documentos e pelos mecanismos de classificação adotados pela plataforma.

---

# Observações

O evento **Documento Não Identificado** inaugura o conjunto de Exception Events da Plataforma DF Analysis IA.

Sua existência permite que situações excepcionais sejam tratadas de forma explícita, auditável e desacoplada, evitando interrupções silenciosas e favorecendo a atuação coordenada de usuários, agentes inteligentes e processos de reclassificação.

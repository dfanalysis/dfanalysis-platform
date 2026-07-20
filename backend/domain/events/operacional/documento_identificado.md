# Domain Event — Documento Identificado

## Objetivo

O evento **Documento Identificado** representa o momento em que um documento recebido pela Plataforma DF Analysis IA foi reconhecido, classificado e associado ao seu tipo documental.

Esse evento marca a conclusão da etapa de identificação documental e permite que os próximos componentes do domínio iniciem suas atividades.

---

# Motivação

Após o recebimento de arquivos, o domínio precisa reconhecer o que cada documento representa antes de qualquer validação.

Exemplos:

* PDF de NFS-e;
* XML da NFS-e;
* Relatório de Produção;
* RPS;
* Contrato;
* Planilha;
* Documento desconhecido.

Quando essa classificação é concluída, o evento deve ser publicado.

---

# Quando ocorre

O evento deve ser publicado quando:

* o documento for identificado com sucesso;
* sua classificação estiver concluída;
* o documento estiver associado ao contexto correto;
* o processo de identificação terminar, independentemente da confiança da classificação.

---

# Dados do evento

O evento pode conter:

* identificador do documento;
* identificador do Evidence Bundle;
* identificador da Solicitação de Emissão;
* tipo documental identificado;
* nível de confiança da classificação;
* origem do documento;
* mecanismo de identificação utilizado;
* data e hora da identificação;
* versão do algoritmo de classificação, quando aplicável.

O evento deve transportar apenas as informações necessárias para os consumidores.

---

# Possíveis consumidores

O evento pode ser consumido por:

* Domain Service de Validação de Documentos;
* Domain Service de Auditoria;
* Domain Service de Notificação;
* módulo de monitoramento;
* futuros agentes de IA especializados.

Cada consumidor decide independentemente como reagir ao evento.

---

# Regras de Negócio

O evento somente deve ser publicado quando:

* existir um documento associado;
* o processo de identificação tiver sido concluído;
* o tipo documental estiver definido, mesmo que provisoriamente.

Documentos classificados como desconhecidos também podem gerar este evento, desde que essa classificação seja explícita.

---

# Imutabilidade

Após publicado, o evento é imutável.

Caso uma nova identificação seja realizada posteriormente, um novo evento deve ser publicado, preservando o histórico das classificações anteriores.

---

# Auditoria

Devem ser registrados:

* identificador do documento;
* tipo documental identificado;
* data e hora;
* origem do documento;
* algoritmo ou mecanismo utilizado;
* nível de confiança;
* usuário responsável, quando aplicável;
* correlação com a Solicitação de Emissão e o Evidence Bundle.

---

# Relação com o domínio

Este evento encerra a etapa de identificação documental e habilita o início das validações previstas pelas Policies e pelos Domain Services.

Ele representa a transição entre o reconhecimento dos documentos e a verificação de sua consistência.

---

# Observações

O evento **Documento Identificado** estabelece um ponto de integração entre os componentes responsáveis pela entrada de documentos e aqueles encarregados da validação e do processamento do domínio.

Sua existência favorece arquiteturas orientadas a eventos, processamento assíncrono e integração entre múltiplos agentes especializados, preservando o desacoplamento entre os módulos da plataforma.

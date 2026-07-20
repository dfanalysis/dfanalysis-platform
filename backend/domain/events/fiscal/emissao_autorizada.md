# Domain Event — Emissão Autorizada

## Objetivo

O evento **Emissão Autorizada** representa o momento em que o domínio conclui que uma Solicitação de Emissão atende a todos os requisitos necessários para prosseguir com a geração da Nota Fiscal de Serviços Eletrônica (NFS-e).

Esse evento marca a transição entre a fase de validação e decisão para a fase de execução da emissão.

---

# Motivação

A autorização da emissão depende da combinação de diversas decisões de negócio.

Entre elas:

* documentos válidos;
* competência permitida;
* cálculo tributário concluído;
* Prestador habilitado;
* Tomador válido;
* inexistência de bloqueios fiscais;
* inexistência de bloqueios administrativos;
* aprovação obrigatória, quando aplicável.

Quando todas essas condições forem satisfeitas, o domínio publica este evento.

---

# Quando ocorre

O evento deve ser publicado quando:

* todas as Policies obrigatórias forem satisfeitas;
* o Domain Service de Emissão estiver autorizado a prosseguir;
* não existir nenhuma restrição impeditiva.

Caso a emissão seja bloqueada, um evento específico deverá representar esse fato.

---

# Dados do evento

O evento pode conter:

* identificador da Solicitação de Emissão;
* identificador do Processo Administrativo;
* competência;
* Prestador;
* Tomador;
* município;
* data e hora da autorização;
* versão das Policies utilizadas;
* identificador da memória de cálculo tributário;
* usuário ou mecanismo responsável pela autorização.

O evento deve conter apenas os dados necessários aos consumidores.

---

# Possíveis consumidores

O evento pode ser consumido por:

* Domain Service de Emissão de NFS-e;
* Domain Service de Auditoria;
* Domain Service de Notificação;
* módulo gerencial;
* monitoramento operacional;
* futuros agentes especializados.

Cada consumidor decide independentemente como reagir ao evento.

---

# Regras de Negócio

O evento somente deve ser publicado quando:

* a Solicitação estiver íntegra;
* todos os documentos obrigatórios forem válidos;
* a competência estiver permitida;
* o cálculo tributário estiver concluído;
* não existirem bloqueios impeditivos;
* todas as aprovações obrigatórias tiverem sido realizadas.

---

# Imutabilidade

Após publicado, o evento é imutável.

Caso uma autorização seja posteriormente revogada, um novo evento deverá representar essa alteração, preservando o histórico do domínio.

---

# Auditoria

Devem ser registrados:

* data e hora;
* Policies utilizadas;
* versão das regras;
* responsável pela autorização;
* mecanismo da decisão;
* correlação com a Solicitação de Emissão;
* correlação com a memória de cálculo tributário.

---

# Relação com o domínio

Este evento representa uma decisão de negócio.

Ele não executa a emissão da NFS-e.

Sua função é informar ao domínio que todas as condições necessárias foram satisfeitas, permitindo que o Domain Service de Emissão realize a execução da operação.

---

# Observações

O evento **Emissão Autorizada** representa um dos principais marcos do contexto fiscal da Plataforma DF Analysis IA.

Sua existência reforça a separação entre decisão e execução, permitindo que diferentes componentes do domínio reajam de forma independente à autorização da emissão, preservando o baixo acoplamento e a rastreabilidade do processo.

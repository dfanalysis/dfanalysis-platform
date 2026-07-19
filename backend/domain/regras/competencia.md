---

id: BR-FAT-001
titulo: Definição da Competência da NFS-e
contexto: Faturamento
versao: 1.0.0
status: Aprovada
ultima_atualizacao: 2026-07-19
responsavel: DF Analysis
------------------------

# BR-FAT-001 — Definição da Competência da NFS-e

## 1. Objetivo

Definir a competência que deverá ser utilizada na emissão da NFS-e a partir das informações recebidas na solicitação de faturamento.

---

## 2. Definição

A competência representa o período de referência considerado pelo hospital, clínica ou instituição solicitante para a emissão da NFS-e.

A competência não deverá ser definida automaticamente com base:

* na data de recebimento do e-mail;
* na data atual;
* na data de emissão da NFS-e;
* na data de pagamento;
* na data isolada de um procedimento.

---

## 3. Fontes de identificação

A competência poderá ser identificada nas seguintes fontes:

1. corpo do e-mail da solicitação;
2. relatório analítico anexado ao e-mail;
3. outros documentos enviados pelo solicitante.

---

## 4. Ordem de prioridade

### 4.1 Competência informada no corpo do e-mail

Quando a competência estiver explicitamente informada no corpo do e-mail, essa informação deverá prevalecer.

A plataforma deverá utilizar a competência indicada pelo solicitante, mesmo que o relatório analítico contenha procedimentos realizados em meses diferentes.

### 4.2 Competência não informada no corpo do e-mail

Quando a competência não estiver informada no corpo do e-mail, a plataforma deverá analisar as datas dos procedimentos constantes no relatório analítico.

Deverá ser considerada como competência o mês e ano com a maior quantidade de ocorrências no relatório.

---

## 5. Justificativa operacional

O relatório analítico pode conter repasses referentes a procedimentos realizados em competências anteriores.

Isso pode ocorrer, por exemplo, quando:

* a operadora de saúde demora a efetuar o pagamento ao hospital;
* o hospital repassa posteriormente os honorários à empresa médica;
* procedimentos de períodos anteriores são incluídos no fechamento atual;
* existem ajustes ou complementações de pagamentos.

Por esse motivo, quando a competência estiver informada no corpo do e-mail, ela representa a orientação oficial do hospital para emissão da NFS-e e deverá prevalecer sobre as datas individuais dos procedimentos.

---

## 6. Regra de predominância

Quando não houver competência explícita no corpo do e-mail, a plataforma deverá:

1. extrair todas as datas de procedimentos válidas do relatório analítico;
2. agrupar as datas por mês e ano;
3. contar a quantidade de ocorrências de cada competência;
4. selecionar a competência com maior quantidade de ocorrências;
5. registrar a origem e o cálculo utilizado na decisão.

---

## 7. Exemplo

### Procedimentos identificados

```text
Consulta realizada em 12/04/2026
Consulta realizada em 26/04/2026
Consulta realizada em 28/04/2026
Consulta realizada em 12/02/2026
```

### Agrupamento

| Competência    | Quantidade |
| -------------- | ---------: |
| Abril/2026     |          3 |
| Fevereiro/2026 |          1 |

### Resultado

```text
Competência definida: Abril/2026
```

Abril de 2026 deverá ser utilizado porque representa a competência com maior número de procedimentos no relatório.

---

## 8. Empate entre competências

Quando duas ou mais competências apresentarem a mesma quantidade de ocorrências, a plataforma não deverá escolher automaticamente uma delas.

A solicitação deverá ser encaminhada para revisão humana.

Exemplo:

| Competência | Quantidade |
| ----------- | ---------: |
| Março/2026  |          2 |
| Abril/2026  |          2 |

Resultado:

```text
Status: revisão humana necessária
Motivo: empate entre competências predominantes
```

---

## 9. Ausência de competência identificável

A solicitação deverá ser encaminhada para revisão humana quando:

* não houver competência no corpo do e-mail;
* não houver relatório analítico;
* o relatório não possuir datas válidas;
* as datas estiverem ilegíveis;
* não for possível associar as datas aos procedimentos;
* houver conflito ou ambiguidade relevante;
* houver empate entre as competências predominantes.

A plataforma não deverá utilizar a data atual como competência substituta.

---

## 10. Rastreabilidade

A decisão deverá registrar:

* competência selecionada;
* fonte utilizada;
* texto ou documento de origem;
* quantidade de ocorrências por competência;
* regra aplicada;
* nível de confiança;
* necessidade ou não de revisão humana.

Exemplo com competência extraída do corpo do e-mail:

```json
{
  "competencia": {
    "valor": "2026-04",
    "fonte": "email_body",
    "regra": "BR-FAT-001",
    "metodo": "explicitamente_informada",
    "confianca": 1.0,
    "revisao_humana": false
  }
}
```

Exemplo com competência predominante no relatório:

```json
{
  "competencia": {
    "valor": "2026-04",
    "fonte": "relatorio_analitico",
    "regra": "BR-FAT-001",
    "metodo": "maior_frequencia",
    "ocorrencias": {
      "2026-04": 3,
      "2026-02": 1
    },
    "confianca": 0.9,
    "revisao_humana": false
  }
}
```

---

## 11. Algoritmo de decisão

```text
Existe competência explícita no corpo do e-mail?
        │
        ├── Sim
        │     ↓
        │  Utilizar a competência do e-mail
        │
        └── Não
              ↓
        Existe relatório analítico com datas válidas?
              │
              ├── Não
              │     ↓
              │  Encaminhar para revisão humana
              │
              └── Sim
                    ↓
              Agrupar procedimentos por mês e ano
                    ↓
              Existe uma única competência predominante?
                    │
                    ├── Sim
                    │     ↓
                    │  Utilizar a competência predominante
                    │
                    └── Não
                          ↓
                       Encaminhar para revisão humana
```

---

## 12. Critérios de aceitação

### Cenário 1 — Competência informada no e-mail

**Dado que** o e-mail informa competência abril de 2026
**E** o relatório contém procedimentos de fevereiro, março e abril
**Quando** a solicitação for analisada
**Então** a competência deverá ser abril de 2026.

### Cenário 2 — Competência predominante no relatório

**Dado que** o e-mail não informa competência
**E** o relatório contém três procedimentos de abril de 2026 e um de fevereiro de 2026
**Quando** a solicitação for analisada
**Então** a competência deverá ser abril de 2026.

### Cenário 3 — Empate

**Dado que** o e-mail não informa competência
**E** o relatório contém dois procedimentos de março e dois de abril
**Quando** a solicitação for analisada
**Então** nenhuma competência deverá ser selecionada automaticamente
**E** a solicitação deverá exigir revisão humana.

### Cenário 4 — Datas ausentes

**Dado que** o e-mail não informa competência
**E** o relatório não possui datas válidas
**Quando** a solicitação for analisada
**Então** a solicitação deverá exigir revisão humana.

---

## 13. Responsabilidade da Inteligência Artificial

A Inteligência Artificial poderá:

* localizar a competência no corpo do e-mail;
* identificar datas de procedimentos;
* interpretar diferentes formatos de data;
* associar datas aos respectivos procedimentos;
* estruturar as evidências extraídas.

A escolha da competência predominante deverá ser realizada por regra determinística após a extração das datas.

A IA não deverá escolher livremente a competência quando existir empate, ausência de dados ou ambiguidade relevante.

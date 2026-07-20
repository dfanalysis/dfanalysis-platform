# Domain Event — Repasse Apurado

## Objetivo

O evento **Repasse Apurado** representa o momento em que os valores devidos aos participantes de uma prestação de serviços foram calculados e consolidados pelo domínio.

Esse evento confirma que a apuração financeira foi concluída e que os resultados estão disponíveis para revisão, aprovação ou processamento financeiro.

---

# Motivação

Após a consolidação da produção, do faturamento e das regras contratuais, a Plataforma DF Analysis IA deve determinar os valores correspondentes a cada Médico Executante ou participante elegível.

A conclusão dessa apuração representa um fato relevante para diversos módulos da plataforma, incluindo:

* Financeiro;
* Administrativo;
* Gerencial;
* Auditoria;
* Notificações;
* Integrações com ERP.

O evento permite que esses componentes reajam ao resultado sem depender diretamente do Domain Service de Apuração de Repasses.

---

# Quando ocorre

O evento deve ser publicado quando:

* os dados de produção estiverem disponíveis e validados;
* as regras contratuais aplicáveis forem identificadas;
* os participantes elegíveis forem determinados;
* os cálculos individuais forem concluídos;
* a memória de cálculo estiver disponível;
* não existirem inconsistências impeditivas.

O evento não significa necessariamente que os valores foram aprovados ou pagos.

---

# Dados do evento

O evento pode conter:

* identificador do Repasse Médico;
* identificador da Empresa Médica;
* competência;
* identificador do Relatório de Produção;
* identificadores das NFS-e relacionadas;
* quantidade de participantes;
* valor bruto de referência;
* valor total apurado;
* valor total de retenções;
* valor total de descontos;
* valor líquido total;
* identificador da memória de cálculo;
* versão das regras aplicadas;
* data e hora da apuração;
* identificador do Processo Administrativo.

O evento deve transportar somente as informações necessárias para seus consumidores.

Dados detalhados de cada participante devem permanecer no Aggregate ou em uma representação apropriada, evitando eventos excessivamente grandes.

---

# Possíveis consumidores

O evento pode ser consumido por:

* módulo Financeiro;
* fluxo de aprovação de repasses;
* Domain Service de Auditoria;
* Domain Service de Notificação;
* módulo Gerencial;
* integração com ERP;
* módulo de pagamentos;
* agentes financeiros;
* agentes contábeis;
* dashboards e relatórios.

Cada consumidor deve reagir ao evento de forma independente.

---

# Regras de Negócio

O evento somente deve ser publicado quando:

* a apuração estiver integralmente concluída;
* os participantes estiverem identificados;
* os cálculos forem reproduzíveis;
* a memória de cálculo estiver preservada;
* os valores totais estiverem conciliados;
* nenhuma regra impeditiva permanecer pendente.

O valor total distribuído não pode ultrapassar a base financeira disponível, salvo quando houver ajuste formal e devidamente registrado.

---

# Situação posterior à apuração

A publicação deste evento não significa automaticamente que o repasse:

* foi aprovado;
* foi autorizado para pagamento;
* foi enviado ao banco;
* foi pago;
* foi conciliado.

Esses fatos devem ser representados por eventos próprios.

Exemplos futuros:

* Repasse Aprovado;
* Pagamento de Repasse Autorizado;
* Repasse Pago;
* Repasse Conciliado.

---

# Imutabilidade

Após publicado, o evento é imutável.

Caso os valores sejam recalculados, corrigidos ou reprocessados, um novo evento deverá ser publicado.

O novo evento deve manter correlação com:

* a apuração anterior;
* o motivo do recálculo;
* a versão das regras;
* o responsável pela alteração.

---

# Auditoria

Devem ser registrados:

* identificador do Aggregate;
* competência;
* participantes considerados;
* documentos utilizados;
* regras contratuais aplicadas;
* versão das Policies;
* identificador da memória de cálculo;
* valores consolidados;
* data e hora;
* executor;
* origem da execução;
* correlação com o Processo Administrativo;
* correlação com as NFS-e e o Relatório de Produção.

---

# Relação com o domínio

O evento é produzido após a execução do Domain Service de Apuração de Repasses e a atualização consistente do Aggregate Repasse Médico.

A Política de Repasses determina quais regras devem ser aplicadas.

O Domain Service executa os cálculos.

O Aggregate preserva o estado e as invariantes.

O evento comunica que a apuração foi concluída.

---

# Relação com integrações externas

Este evento não representa:

* criação de contas a pagar no ERP;
* envio de arquivo bancário;
* realização de transferência;
* confirmação bancária;
* baixa financeira.

Essas operações pertencem às camadas de Aplicação e Infraestrutura e podem produzir Integration Events próprios.

---

# Observações

O evento **Repasse Apurado** representa um dos principais marcos do contexto financeiro da Plataforma DF Analysis IA.

Ele transforma a conclusão de uma regra financeira complexa em um fato de domínio consumível por diversos módulos e agentes.

Essa abordagem permite que o Agente Financeiro, o Agente Gerencial, o módulo de Auditoria e futuras integrações reajam à apuração sem criar dependências diretas com o serviço responsável pelo cálculo.

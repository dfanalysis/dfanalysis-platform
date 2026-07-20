# Domain Event — Cálculo Tributário Concluído

## Objetivo

O evento **Cálculo Tributário Concluído** representa o momento em que todos os tributos, retenções, deduções e bases de cálculo aplicáveis à operação foram determinados com sucesso pelo domínio.

Esse evento confirma que o processo de cálculo tributário foi finalizado e que seus resultados estão disponíveis para as próximas etapas do fluxo fiscal.

---

# Motivação

O cálculo tributário é uma etapa crítica do processo de emissão da NFS-e.

Antes da autorização da emissão, o domínio deve determinar corretamente:

* base de cálculo;
* ISS;
* retenções;
* deduções;
* valor líquido;
* memória de cálculo.

Somente após essa etapa concluída outros componentes poderão avaliar a possibilidade de emissão.

---

# Quando ocorre

O evento deve ser publicado quando:

* o cálculo tributário for concluído com sucesso;
* todas as regras tributárias aplicáveis tiverem sido processadas;
* a memória de cálculo tiver sido gerada.

Falhas no cálculo devem produzir eventos específicos.

---

# Dados do evento

O evento pode conter:

* identificador da Solicitação de Emissão;
* identificador da memória de cálculo;
* competência;
* município;
* natureza do serviço;
* valor bruto;
* valor líquido;
* tributos incidentes;
* retenções aplicadas;
* versão da Política Tributária;
* data e hora da conclusão.

O evento deve transportar apenas os dados necessários aos seus consumidores.

---

# Possíveis consumidores

O evento pode ser consumido por:

* Política de Emissão;
* Domain Service de Emissão de NFS-e;
* Domain Service de Auditoria;
* Domain Service de Notificação;
* módulos gerenciais;
* futuros agentes especializados.

Cada consumidor reage ao evento de forma independente.

---

# Regras de Negócio

O evento somente deve ser publicado quando:

* todas as regras tributárias forem processadas;
* a memória de cálculo estiver disponível;
* não existirem inconsistências impeditivas;
* os resultados estiverem consistentes para utilização nas próximas etapas.

---

# Imutabilidade

Após publicado, o evento é imutável.

Caso seja necessário recalcular os tributos, um novo evento deverá ser publicado, preservando o histórico das versões anteriores.

---

# Auditoria

Devem ser registrados:

* identificador da memória de cálculo;
* legislação aplicada;
* versão da Política Tributária;
* tributos calculados;
* retenções;
* deduções;
* data e hora;
* executor;
* correlação com a Solicitação de Emissão.

---

# Relação com o domínio

Este evento representa a conclusão da etapa de cálculo tributário.

Ele não autoriza automaticamente a emissão da NFS-e.

A decisão de prosseguir pertence à Política de Emissão, que poderá utilizar este evento como uma das evidências para autorizar ou bloquear a continuidade do processo.

---

# Observações

O evento **Cálculo Tributário Concluído** registra um dos principais marcos do contexto fiscal da Plataforma DF Analysis IA.

Sua separação em relação à autorização da emissão reforça a distinção entre **execução** e **decisão** dentro do domínio, preservando a clareza do modelo e permitindo maior flexibilidade para lidar com exceções, aprovações e futuras mudanças legislativas.

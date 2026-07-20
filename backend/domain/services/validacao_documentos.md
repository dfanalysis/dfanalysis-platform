# Domain Service — Validação de Documentos

## Objetivo

O Domain Service de Validação de Documentos é responsável por verificar se os documentos recebidos pela Plataforma DF Analysis IA estão completos, consistentes e aptos a sustentar a continuidade de um processo administrativo, fiscal ou financeiro.

Enquanto o serviço de Identificação de Documentos determina o que cada arquivo representa, o serviço de Validação de Documentos determina se o conteúdo identificado atende às regras de negócio aplicáveis.

---

# Motivação

Na operação da DF Analysis, um documento pode estar corretamente identificado e ainda assim não estar apto para uso.

Exemplos:

* relatório de produção de competência incorreta;
* NFS-e com Prestador divergente;
* XML incompatível com o PDF;
* CNPJ do Tomador incorreto;
* valor total diferente do demonstrativo;
* ausência do Médico Executante;
* documento ilegível;
* arquivo duplicado;
* período incompatível com a solicitação.

A validação documental impede que dados inconsistentes avancem para emissão, faturamento, repasse ou pagamento.

---

# Responsabilidades

O serviço é responsável por:

* validar integridade do arquivo;
* validar tipo documental;
* validar obrigatoriedade;
* validar legibilidade;
* validar origem;
* validar competência;
* validar período;
* validar Prestador;
* validar Tomador;
* validar Médico Executante;
* validar valores;
* validar consistência entre documentos;
* identificar divergências;
* registrar pendências;
* determinar se o conjunto documental está apto para processamento.

---

# Entradas

O serviço pode receber:

* Solicitação de Emissão;
* documentos classificados;
* Evidence Bundle;
* Relatório de Produção;
* NFS-e;
* metadados extraídos;
* regras do Tomador;
* regras do Prestador;
* configuração do processo.

---

# Saídas

O serviço pode produzir:

* validação aprovada;
* validação reprovada;
* validação com ressalvas;
* lista de divergências;
* lista de pendências;
* nível de severidade;
* eventos de domínio.

---

# Tipos de validação

## Validação estrutural

Verifica:

* formato do arquivo;
* integridade;
* tamanho;
* extensão;
* possibilidade de leitura;
* presença de conteúdo.

## Validação cadastral

Verifica:

* CNPJ;
* CPF;
* Inscrição Municipal;
* CRM;
* razão social;
* nome;
* endereço;
* município;
* UF.

## Validação temporal

Verifica:

* competência;
* período;
* data de emissão;
* data de prestação;
* vigência de vínculos;
* vigência contratual.

## Validação financeira

Verifica:

* valor bruto;
* descontos;
* retenções;
* impostos;
* valor líquido;
* soma de itens;
* divergências de arredondamento.

## Validação relacional

Verifica:

* vínculo entre Médico e Empresa Médica;
* vínculo entre Prestador e Tomador;
* vínculo entre documento e Solicitação;
* vínculo entre produção e NFS-e;
* vínculo entre relatório e competência.

## Validação cruzada

Compara informações entre documentos distintos.

Exemplos:

* XML versus PDF da NFS-e;
* relatório de produção versus solicitação;
* demonstrativo versus valor faturado;
* NFS-e versus relatório de produção;
* planilha versus documento oficial.

---

# Resultado da validação

A validação pode resultar em:

* Aprovada;
* Aprovada com Ressalvas;
* Pendente;
* Reprovada.

## Aprovada

Todos os critérios obrigatórios foram atendidos.

## Aprovada com Ressalvas

Existem inconsistências não impeditivas, devidamente registradas.

## Pendente

São necessárias informações ou documentos adicionais.

## Reprovada

Existe erro impeditivo que inviabiliza a continuidade do processo.

---

# Severidade das divergências

As divergências podem ser classificadas como:

* Informativa;
* Baixa;
* Média;
* Alta;
* Crítica.

Divergências críticas devem bloquear automaticamente a continuidade do processo.

---

# Regras de Negócio

O serviço deve garantir que:

* todo documento validado possua origem registrada;
* toda divergência possua descrição;
* toda divergência possua severidade;
* toda pendência possua responsável;
* toda validação possua data e executor;
* documentos oficiais prevaleçam sobre documentos auxiliares;
* documentos originais nunca sejam alterados;
* revalidações preservem o histórico anterior;
* validações automatizadas registrem o mecanismo utilizado;
* validações por IA registrem nível de confiança.

---

# Fluxo conceitual

1. Receber documentos classificados.
2. Carregar regras aplicáveis.
3. Executar validações estruturais.
4. Executar validações cadastrais.
5. Executar validações temporais.
6. Executar validações financeiras.
7. Executar validações relacionais.
8. Executar validações cruzadas.
9. Classificar divergências.
10. Determinar resultado.
11. Atualizar o Aggregate correspondente.
12. Publicar eventos de domínio.

---

# Eventos produzidos

* Validação Iniciada;
* Documento Validado;
* Divergência Identificada;
* Pendência Criada;
* Validação Aprovada;
* Validação Aprovada com Ressalvas;
* Validação Pendente;
* Validação Reprovada.

---

# Dependências

Este Domain Service pode utilizar:

* Aggregate Solicitação de Emissão;
* Aggregate Relatório de Produção;
* Aggregate NFS-e;
* Evidence Bundle;
* Policies de validação;
* Policies de competência;
* regras específicas do Tomador;
* regras específicas do Prestador;
* serviços de extração;
* serviços de OCR;
* serviços de IA.

---

# Limites

Este Domain Service não:

* altera documentos;
* emite NFS-e;
* calcula tributos definitivos;
* realiza pagamentos;
* acessa diretamente banco de dados;
* executa chamadas HTTP;
* envia notificações diretamente.

Essas responsabilidades pertencem a outros componentes do domínio, da aplicação ou da infraestrutura.

---

# Auditoria

Cada validação deve registrar:

* documentos analisados;
* versão das regras utilizadas;
* data e hora;
* resultado;
* divergências;
* pendências;
* executor;
* origem da execução;
* nível de confiança;
* necessidade de revisão humana.

---

# Observações

A Validação de Documentos representa a transformação do conhecimento operacional da DF Analysis em regras explícitas, reutilizáveis e auditáveis.

Esse serviço será progressivamente enriquecido com regras determinísticas, heurísticas e modelos de Inteligência Artificial.

A IA poderá auxiliar na detecção de padrões e divergências, mas decisões críticas devem permanecer submetidas a regras de negócio explícitas e, quando necessário, à revisão humana.

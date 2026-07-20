# Domain Service — Notificação

## Objetivo

O Domain Service de Notificação é responsável por determinar quando uma comunicação deve ser gerada, quem deve recebê-la, qual conteúdo deve ser comunicado e qual prioridade deve ser atribuída.

Seu objetivo é representar as regras de negócio relacionadas às comunicações da Plataforma DF Analysis IA, mantendo o domínio independente dos canais utilizados para entrega.

---

# Motivação

Durante a execução dos processos administrativos, fiscais e financeiros, diversos acontecimentos exigem comunicação aos usuários ou responsáveis.

Exemplos:

* uma Solicitação de Emissão foi recebida;
* um documento obrigatório está ausente;
* uma divergência crítica foi identificada;
* uma NFS-e foi emitida;
* uma emissão foi rejeitada;
* um repasse foi apurado;
* um processo aguarda aprovação;
* um prazo está próximo do vencimento.

A decisão de notificar pertence ao domínio.

Entretanto, o envio por e-mail, WhatsApp, Microsoft Teams, portal, SMS ou outro canal pertence à camada de infraestrutura.

---

# Responsabilidades

O serviço é responsável por:

* avaliar eventos do domínio;
* determinar se uma notificação deve ser gerada;
* identificar os destinatários;
* definir o tipo da notificação;
* definir prioridade;
* definir criticidade;
* definir o conteúdo semântico da comunicação;
* definir prazo esperado de resposta;
* evitar notificações duplicadas;
* consolidar notificações relacionadas;
* registrar o motivo da comunicação;
* produzir uma intenção de notificação.

---

# Entradas

O serviço pode receber:

* eventos de domínio;
* Solicitação de Emissão;
* Processo Administrativo;
* NFS-e;
* Relatório de Produção;
* Repasse Médico;
* divergências;
* pendências;
* prazos;
* responsáveis;
* preferências de comunicação;
* regras organizacionais;
* configurações do processo.

---

# Saídas

O serviço pode produzir:

* intenção de notificação;
* destinatários;
* assunto;
* conteúdo semântico;
* prioridade;
* criticidade;
* prazo de resposta;
* contexto relacionado;
* evento de domínio.

---

# Tipos de notificação

As notificações podem ser classificadas como:

* Informativa;
* Confirmação;
* Alerta;
* Pendência;
* Aprovação;
* Rejeição;
* Falha;
* Vencimento;
* Urgência;
* Conclusão.

---

# Prioridade

A prioridade pode ser:

* Baixa;
* Normal;
* Alta;
* Urgente.

A prioridade deve considerar:

* impacto operacional;
* impacto fiscal;
* impacto financeiro;
* prazo;
* risco de perda;
* necessidade de intervenção humana.

---

# Criticidade

A criticidade pode ser:

* Informativa;
* Baixa;
* Média;
* Alta;
* Crítica.

Notificações críticas podem exigir:

* confirmação de leitura;
* escalonamento;
* múltiplos destinatários;
* prazo reduzido;
* repetição controlada;
* registro obrigatório de tratamento.

---

# Destinatários

Os destinatários devem ser definidos por papel, responsabilidade ou vínculo com o processo.

Exemplos:

* Solicitante;
* Responsável Fiscal;
* Responsável Financeiro;
* Gestor da Empresa Médica;
* Médico Executante;
* Administrador da Plataforma;
* Responsável pelo Processo;
* Usuário designado;
* Grupo operacional.

O domínio deve evitar dependência direta de endereços de e-mail, números de telefone ou identificadores específicos de canais.

---

# Regras de Negócio

O serviço deve garantir que:

* toda notificação possua um motivo;
* toda notificação esteja vinculada a um contexto de domínio;
* toda notificação possua ao menos um destinatário válido;
* notificações duplicadas sejam evitadas;
* notificações críticas não sejam silenciosamente descartadas;
* o conteúdo não exponha dados além do necessário;
* informações sensíveis sejam protegidas;
* falhas de entrega não alterem o estado do Aggregate;
* reenvios preservem o histórico;
* notificações automatizadas sejam identificadas;
* comunicações que exijam ação possuam prazo e responsável.

---

# Deduplicação

O serviço deve evitar a geração repetida de notificações equivalentes.

Uma notificação pode ser considerada duplicada quando possuir:

* mesmo tipo;
* mesmo contexto;
* mesmo destinatário;
* mesmo motivo;
* mesmo período de referência;
* ausência de alteração relevante desde a última comunicação.

A deduplicação não deve impedir novas notificações quando:

* a criticidade aumentar;
* o prazo estiver próximo;
* houver nova tentativa prevista;
* o responsável mudar;
* surgir nova evidência;
* a pendência permanecer sem tratamento além do prazo.

---

# Consolidação

Notificações relacionadas podem ser consolidadas quando isso melhorar a clareza da comunicação.

Exemplos:

* múltiplos documentos ausentes em uma única Solicitação;
* várias divergências do mesmo Evidence Bundle;
* diversas emissões concluídas em um mesmo lote;
* múltiplos repasses disponíveis para aprovação.

Notificações críticas não devem ser ocultadas em consolidações excessivamente genéricas.

---

# Escalonamento

O serviço pode determinar escalonamento quando:

* uma pendência não for resolvida dentro do prazo;
* uma falha crítica persistir;
* uma emissão estiver próxima do prazo limite;
* uma aprovação permanecer pendente;
* um destinatário não responder;
* houver reincidência de erro.

O escalonamento pode alterar:

* destinatários;
* prioridade;
* criticidade;
* prazo;
* necessidade de confirmação.

---

# Fluxo conceitual

1. Receber evento ou situação de domínio.
2. Avaliar se existe necessidade de comunicação.
3. Identificar o tipo de notificação.
4. Definir prioridade e criticidade.
5. Identificar destinatários.
6. Verificar duplicidade.
7. Verificar possibilidade de consolidação.
8. Definir conteúdo semântico.
9. Definir prazo de resposta, quando aplicável.
10. Produzir intenção de notificação.
11. Publicar evento de domínio.
12. Encaminhar a intenção para a camada de Aplicação.

---

# Exemplos de decisões

## Documento obrigatório ausente

Resultado:

* Tipo: Pendência;
* Prioridade: Alta;
* Destinatário: Solicitante;
* Ação esperada: Enviar documento;
* Prazo: Conforme regra do processo.

## NFS-e emitida com sucesso

Resultado:

* Tipo: Conclusão;
* Prioridade: Normal;
* Destinatário: Solicitante e responsável fiscal;
* Ação esperada: Nenhuma;
* Anexos potenciais: PDF e XML.

## Emissão rejeitada pelo provedor

Resultado:

* Tipo: Falha;
* Prioridade: Alta;
* Destinatário: Responsável fiscal;
* Ação esperada: Corrigir dados e reprocessar;
* Escalonamento: Aplicável em caso de recorrência.

## Divergência tributária crítica

Resultado:

* Tipo: Alerta;
* Prioridade: Urgente;
* Criticidade: Crítica;
* Destinatário: Responsável fiscal e gestor;
* Ação esperada: Revisão humana obrigatória.

---

# Eventos produzidos

* Notificação Solicitada;
* Notificação Priorizada;
* Notificação Consolidada;
* Notificação Escalonada;
* Confirmação de Leitura Exigida;
* Ação do Destinatário Solicitada.

---

# Dependências

Este Domain Service pode utilizar:

* eventos de domínio;
* Aggregate Solicitação de Emissão;
* Aggregate Processo Administrativo;
* Aggregate NFS-e;
* Aggregate Repasse Médico;
* Policies de Notificação;
* Policies de Escalonamento;
* configuração organizacional;
* responsabilidades atribuídas;
* preferências de comunicação.

---

# Relação com a camada de Aplicação

A camada de Aplicação é responsável por:

* receber a intenção de notificação;
* selecionar o canal disponível;
* preparar o comando de envio;
* coordenar tentativas;
* registrar o resultado operacional;
* tratar falhas técnicas;
* acionar integrações.

O Domain Service não executa diretamente essas operações.

---

# Relação com a Infraestrutura

A Infraestrutura é responsável por:

* enviar e-mails;
* enviar mensagens por WhatsApp;
* publicar notificações no portal;
* integrar com Microsoft Teams;
* integrar com Google Workspace;
* integrar com serviços de SMS;
* armazenar comprovantes de entrega;
* receber webhooks de status;
* implementar filas e retentativas.

---

# Segurança da informação

O serviço deve considerar:

* princípio do menor privilégio;
* minimização de dados;
* ocultação de informações sensíveis;
* restrição de documentos por perfil;
* proibição de exposição desnecessária de CPF, CNPJ ou dados financeiros;
* rastreabilidade de comunicações;
* conformidade com a LGPD.

Uma notificação não deve conter mais informações do que o destinatário necessita para compreender e tratar a situação.

---

# Auditoria

Cada intenção de notificação deve registrar:

* motivo;
* evento de origem;
* contexto;
* destinatários;
* tipo;
* prioridade;
* criticidade;
* conteúdo semântico;
* prazo;
* regra aplicada;
* data e hora;
* origem automatizada ou humana;
* necessidade de confirmação;
* critérios de escalonamento.

O resultado técnico do envio deve ser registrado posteriormente pela camada responsável pela entrega.

---

# Limites

Este Domain Service não:

* envia e-mails;
* envia mensagens de WhatsApp;
* escolhe provedores;
* chama APIs externas;
* executa webhooks;
* cria templates visuais;
* persiste diretamente em banco de dados;
* controla filas;
* realiza retentativas técnicas;
* altera o estado de um Aggregate por falha de entrega.

Essas responsabilidades pertencem às camadas de Aplicação e Infraestrutura.

---

# Evolução do domínio

O serviço deve permitir a inclusão de novos canais de comunicação sem alteração das regras centrais do domínio.

A entrada de um novo canal, como aplicativo móvel, chatbot, Microsoft Teams ou outro mensageiro, deve exigir apenas um novo adaptador de infraestrutura.

As regras sobre quando notificar, quem notificar e qual prioridade aplicar devem permanecer estáveis no domínio.

---

# Observações

A Notificação é um mecanismo transversal da Plataforma DF Analysis IA.

Sua separação como Domain Service evita que Aggregates e processos de negócio fiquem acoplados a e-mail, WhatsApp ou qualquer tecnologia específica.

O domínio determina a necessidade da comunicação e produz uma intenção estruturada.

A camada de Aplicação coordena o envio.

A Infraestrutura realiza a entrega.

Essa separação aumenta a testabilidade, a segurança, a reutilização e a capacidade de evolução da plataforma.

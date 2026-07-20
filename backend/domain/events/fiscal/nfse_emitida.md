# Domain Event — NFS-e Emitida

## Objetivo

O evento **NFS-e Emitida** representa o momento em que a emissão da Nota Fiscal de Serviços Eletrônica foi concluída com sucesso e confirmada pelo provedor responsável.

Esse evento registra um fato definitivo do domínio: a NFS-e passou a existir oficialmente.

---

# Motivação

Após a autorização da emissão, o Domain Service de Emissão solicita a geração da NFS-e ao provedor competente.

Quando o provedor confirma a emissão, o domínio incorpora esse fato por meio deste evento.

A partir desse momento, diversos processos podem ser iniciados automaticamente.

---

# Quando ocorre

O evento deve ser publicado quando:

* o provedor confirmar a emissão da NFS-e;
* existir número definitivo da NFS-e;
* existir protocolo ou identificador oficial da emissão;
* o XML oficial estiver disponível, quando aplicável.

Falhas de emissão devem produzir eventos específicos.

---

# Dados do evento

O evento pode conter:

* identificador da Solicitação de Emissão;
* identificador da NFS-e;
* número da NFS-e;
* código de verificação;
* protocolo de emissão;
* município emissor;
* data e hora da emissão;
* data da prestação do serviço;
* Prestador;
* Tomador;
* valor total da nota;
* identificador do XML;
* identificador do PDF;
* provedor responsável;
* versão do layout utilizado.

O evento deve transportar apenas os dados necessários aos consumidores.

---

# Possíveis consumidores

O evento pode ser consumido por:

* Aggregate NFS-e;
* Domain Service de Apuração de Repasses;
* Domain Service de Auditoria;
* Domain Service de Notificação;
* módulo Financeiro;
* módulo Gerencial;
* integrações com ERP;
* futuros agentes especializados.

Cada consumidor decide independentemente como reagir ao evento.

---

# Regras de Negócio

O evento somente deve ser publicado quando:

* a emissão for oficialmente confirmada pelo provedor;
* existir identificação definitiva da NFS-e;
* os dados mínimos da nota estiverem disponíveis;
* o processo de emissão tiver sido concluído com sucesso.

---

# Imutabilidade

Após publicado, o evento é imutável.

Caso a NFS-e seja posteriormente cancelada, substituída ou retificada, novos eventos deverão representar esses fatos, preservando o histórico completo.

---

# Auditoria

Devem ser registrados:

* identificador da NFS-e;
* número da nota;
* protocolo;
* provedor responsável;
* município;
* layout utilizado;
* data e hora da emissão;
* identificador da Solicitação de Emissão;
* correlação com o Processo Administrativo.

---

# Relação com o domínio

Este evento representa um fato externo incorporado ao domínio.

Ele confirma que a emissão foi aceita pelo provedor e que a NFS-e passou a integrar oficialmente o patrimônio informacional da Plataforma DF Analysis IA.

---

# Observações

O evento **NFS-e Emitida** representa um dos principais marcos do contexto fiscal da plataforma.

Sua publicação permite que módulos financeiros, administrativos, gerenciais e integrações externas iniciem seus próprios processos sem depender diretamente do fluxo de emissão.

Essa abordagem reforça o desacoplamento entre o núcleo do domínio e os sistemas externos, facilitando a evolução para múltiplos provedores de NFS-e, novos municípios e futuras integrações com o padrão nacional.

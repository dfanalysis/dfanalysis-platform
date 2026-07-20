# Integration Event — PDF Recebido

## Objetivo

O evento **PDF Recebido** representa o momento em que o DANFSe ou outro documento em formato PDF é disponibilizado pelo provedor e recebido pela Plataforma DF Analysis IA.

Este evento registra a chegada da representação visual oficial da Nota Fiscal de Serviços Eletrônica.

---

# Motivação

Embora o XML seja o documento fiscal estruturado, o PDF é amplamente utilizado para:

- consulta humana;
- envio ao cliente;
- anexação em processos administrativos;
- arquivamento;
- impressão;
- conferência operacional.

Ao registrar sua chegada como Integration Event, o processamento do PDF permanece desacoplado da integração com o provedor.

---

# Quando ocorre

O evento deve ser publicado quando:

- o PDF oficial estiver disponível;
- sua transferência for concluída;
- o arquivo puder ser armazenado.

---

# Dados do evento

O evento pode conter:

- identificador da NFS-e;
- identificador do PDF;
- identificador da Solicitação de Emissão;
- provedor;
- município;
- data e hora do recebimento;
- hash do arquivo;
- tamanho do arquivo;
- identificador de correlação.

O conteúdo do PDF não deve ser publicado no evento.

---

# Possíveis consumidores

O evento pode ser consumido por:

- Storage Service;
- módulo Administrativo;
- Auditoria;
- Portal do Cliente;
- ERP;
- OCR;
- Notificações;
- Arquivamento.

---

# Relação com o domínio

Este evento representa apenas a disponibilização do PDF pelo sistema externo.

Ele não altera o estado do domínio nem substitui o XML como documento fiscal oficial.

---

# Auditoria

Devem ser registrados:

- identificador do PDF;
- hash;
- provedor;
- data e hora;
- origem da integração.

---

# Segurança

O PDF deve ser preservado em sua forma original, garantindo rastreabilidade e integridade ao longo do ciclo de vida do processo administrativo.

---

# Observações

O evento **PDF Recebido** permite que processos administrativos, operacionais e de atendimento utilizem o documento visual da NFS-e de forma independente dos componentes responsáveis pela integração com o provedor.
# Integration Event — Autenticação Realizada

## Objetivo

O evento **Autenticação Realizada** representa a confirmação de que a Plataforma DF Analysis IA estabeleceu com sucesso uma sessão autenticada junto ao provedor ISSNET ou outro sistema responsável pela emissão de NFS-e.

Este evento indica que a infraestrutura obteve autorização para executar operações disponíveis naquele ambiente.

---

# Motivação

Antes de qualquer consulta, emissão, cancelamento ou substituição de NFS-e, a plataforma deve autenticar-se no sistema externo utilizando o mecanismo suportado pelo provedor.

A autenticação pode ocorrer por diferentes meios, como:

- certificado digital;
- login e senha;
- token de acesso;
- OAuth;
- mecanismos futuros suportados pelos provedores.

Ao registrar esse fato como Integration Event, o domínio permanece desacoplado dos detalhes técnicos da autenticação.

---

# Quando ocorre

O evento deve ser publicado quando:

- a autenticação for concluída com sucesso;
- a sessão estiver válida;
- a infraestrutura estiver autorizada a iniciar operações no provedor.

---

# Dados do evento

O evento pode conter:

- provedor autenticado;
- ambiente (produção ou homologação);
- identificador da sessão;
- método de autenticação utilizado;
- data e hora da autenticação;
- instante previsto para expiração da sessão;
- identificador de correlação.

Credenciais, certificados, senhas e tokens não devem ser publicados no evento.

---

# Possíveis consumidores

O evento pode ser consumido por:

- módulo de emissão;
- módulo de consultas;
- módulo de cancelamentos;
- monitoramento;
- auditoria;
- serviços de infraestrutura.

Cada consumidor decide autonomamente como utilizar a sessão autenticada.

---

# Relação com o domínio

Este evento não representa qualquer decisão de negócio.

Ele apenas informa que um sistema externo autorizou a comunicação da plataforma.

A partir desse momento, operações fiscais poderão ser executadas.

---

# Auditoria

Devem ser registrados:

- provedor;
- ambiente;
- método de autenticação;
- data e hora;
- mecanismo responsável;
- identificador de correlação.

Informações sensíveis jamais devem ser armazenadas no evento.

---

# Segurança

Este evento não deve conter:

- senha;
- certificado digital;
- chave privada;
- token JWT;
- access token;
- refresh token;
- cookies de sessão.

Esses elementos pertencem exclusivamente à camada de infraestrutura e devem ser protegidos conforme as políticas de segurança da plataforma.

---

# Observações

O evento **Autenticação Realizada** representa o estabelecimento de uma sessão válida junto ao provedor externo.

Sua existência permite monitorar a disponibilidade das integrações, auditar o ciclo de vida das sessões e desacoplar o domínio dos mecanismos específicos de autenticação utilizados por diferentes provedores de NFS-e.
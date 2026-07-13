# Convenções Git da Plataforma DF Analysis IA

**Versão:** 1.0

---

# Objetivo

Este documento define os padrões de utilização do Git para toda a Plataforma DF Analysis IA.

O objetivo é manter um histórico limpo, rastreável e consistente.

---

# Branch Principal

A branch principal será:

main

Somente código estável deverá ser enviado para esta branch.

---

# Branches de Desenvolvimento

Novas funcionalidades deverão ser criadas em branches específicas.

Padrões:

feature/nome-da-feature

fix/nome-do-ajuste

hotfix/nome-do-hotfix

docs/nome-da-documentacao

refactor/nome-do-refactor

---

# Commits

Todos os commits deverão seguir o padrão Conventional Commits.

Exemplos:

feat(core): add empresa module

feat(fiscal): add nfse module

fix(workflow): correct timeout

docs(api): update endpoints

refactor(core): simplify authentication

chore(repository): reorganize folders

---

# Idioma

Os commits deverão ser escritos em inglês.

A documentação poderá ser escrita em português.

---

# Frequência

Realizar commits pequenos e frequentes.

Evitar grandes volumes de alterações em um único commit.

---

# Pull Requests

Todo Pull Request deverá conter:

- objetivo;
- descrição;
- impacto;
- módulos afetados;
- checklist de testes.

---

# Versionamento

A plataforma seguirá Semantic Versioning.

Formato:

MAJOR.MINOR.PATCH

Exemplo:

1.0.0

1.1.0

1.1.1

---

# Releases

Cada release deverá possuir:

- changelog;
- versão;
- data;
- funcionalidades;
- correções;
- migrações necessárias.

---

# Tags

Toda versão publicada deverá possuir uma tag Git correspondente.

Exemplo:

v1.0.0

v1.1.0

v2.0.0

---

# Boas Práticas

Evitar commits genéricos.

Exemplos que não devem ser utilizados:

update

ajustes

teste

alterações

Sempre utilizar mensagens descritivas.

---

# Histórico

O histórico Git representa parte da documentação técnica da plataforma.

Todo commit deverá permitir compreender claramente:

- o que mudou;
- por que mudou;
- qual módulo foi impactado.
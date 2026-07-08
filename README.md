## Banco de Dados

### Instalar toda a estrutura

```bash
psql -U dfanalysis -d dfanalysis -f database/schema/install.sql
```

### Resetar o ambiente

```bash
psql -U dfanalysis -d dfanalysis -f database/schema/reset.sql
```
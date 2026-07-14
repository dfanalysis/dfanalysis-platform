# Módulo Fiscal

O módulo fiscal concentra os componentes responsáveis pelo ciclo de vida de documentos fiscais de serviços da Plataforma DF Analysis IA.

## Estrutura

### nfse

Representa o domínio da Nota Fiscal de Serviços Eletrônica já emitida.

Responsabilidades previstas:

- armazenamento da NFS-e;
- identificação do prestador e tomador;
- valores fiscais;
- situação da nota;
- protocolo e número da NFS-e;
- XML de retorno;
- cancelamento e substituição;
- consultas internas.

### rps

Representa o documento provisório utilizado para solicitar a emissão de NFS-e.

Responsabilidades previstas:

- numeração do RPS;
- série;
- competência;
- dados do serviço;
- valores;
- retenções;
- validações;
- controle do envio;
- vínculo com a NFS-e emitida.

O nome `rps` será mantido inicialmente por compatibilidade com o ISSNet/ABRASF 2.04.

Quando a integração com o padrão nacional for implementada, o módulo poderá receber um componente específico para DPS, sem alterar o domínio da NFS-e.

### integracoes

Contém adaptadores para sistemas fiscais externos.

Cada provedor deverá possuir sua própria implementação.

Exemplo:

- `integracoes/issnet`

## Regras de dependência

A direção permitida das dependências é:

```text
integrações externas
        ↓
serviços de aplicação
        ↓
domínio fiscal
        ↓
infraestrutura compartilhada


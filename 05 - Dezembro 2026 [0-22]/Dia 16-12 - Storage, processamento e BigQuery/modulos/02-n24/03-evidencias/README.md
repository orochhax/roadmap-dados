# Evidências — N24: BigQuery e custo de consultas

Redija projeto, conta e job IDs antes de publicar.

## Ambiente e contrato

- projeto/datasets parcialmente ocultados:
- região do bucket e datasets:
- schema e timezone adotados:
- partição, clustering e justificativas:
- versão do `bq`/SDK e comandos:

## Reconciliação da carga

| etapa | linhas | duplicatas | nulos obrigatórios | inválidos |
|---|---:|---:|---:|---:|
| origem |  |  |  |  |
| staging |  |  |  |  |
| curated |  |  |  |  |
| rejeitados |  |  |  |  |

- contagem antes/depois de repetir o `MERGE`:
- diferença de reconciliação e explicação:

## Benchmark equivalente

| consulta | resultado/hash | bytes processados | bytes faturados | duração | slot ms | custo estimado |
|---|---|---:|---:|---:|---:|---:|
| baseline |  |  |  |  |  |  |
| particionada |  |  |  |  |  |  |
| particionada + clustering |  |  |  |  |  |  |

## Qualidade e casos de borda

Registre o resultado de lote vazio, duplicatas, atraso, timezone, valores negativos, tipo desconhecido, ausência de filtro e reprocessamento.

## Decisão

- desenho aprovado/rejeitado:
- economia medida versus estimada:
- limitação do volume de laboratório:
- contrato SQL que o Airflow chamará no N25:
- recursos mantidos/removidos:

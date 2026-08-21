# BigQuery: warehouse particionado, qualidade e custo de consultas

## Objetivo

Levar os eventos da landing zone do N23 a tabelas analíticas no BigQuery. Você implementará camadas de staging e curated, carga idempotente, consultas de qualidade e um benchmark que mostre quando particionamento e clustering realmente reduzem bytes processados.

## Pesquise estes nomes exatos

1. `BigQuery Sandbox limitations getting started`
2. `BigQuery load data Cloud Storage CSV schema`
3. `BigQuery partitioned tables require_partition_filter`
4. `BigQuery clustered tables block pruning best practices`
5. `BigQuery INFORMATION_SCHEMA JOBS bytes processed slot ms`
6. `BigQuery dry run query bytes processed bq query`
7. `BigQuery MERGE idempotent incremental load`
8. `BigQuery QUALIFY ROW_NUMBER deduplication`
9. `BigQuery query pricing on demand cost estimate`

## Conceitos essenciais

- **Staging:** preserva dados carregados e facilita validação.
- **Curated:** tabela limpa com contrato para consumidores.
- **Partição:** limita a leitura por data quando o filtro é utilizável.
- **Clustering:** organiza blocos por colunas frequentes de filtro/agregação.
- **Idempotência:** repetir a carga não duplica nem altera indevidamente o resultado.

## Entrega obrigatória

Implemente as instruções do [enunciado](<01-exercicios/ENUNCIADO.md>) em `01-exercicios/consultas_bigquery.sql`. Execute dry runs e consultas reais pequenas; registre IDs redigidos, bytes, tempo e custo em [evidências](<03-evidencias/README.md>).

O SQL aprovado será chamado pela DAG do N25.

## LinkedIn

Depois de demonstrar o pipeline, adicione: **Google BigQuery**, **Data Warehousing** e **Otimização de SQL**.

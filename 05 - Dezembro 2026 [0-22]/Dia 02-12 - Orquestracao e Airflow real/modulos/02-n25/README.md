# Airflow real: DAG idempotente de GCS para BigQuery

## Objetivo

Orquestrar os recursos N23–N24 como um pipeline diário de verdade. A DAG deverá esperar o lote da data lógica, validar o manifesto, carregar staging, executar testes de qualidade, fazer `MERGE` em curated e publicar métricas. Você provará retries, reexecução e backfill sem duplicar dados.

## Pesquise estes nomes exatos

1. `Apache Airflow TaskFlow API @dag @task`
2. `Airflow logical date data interval templates`
3. `Airflow schedule catchup backfill explained`
4. `Airflow retries retry_delay exponential_backoff`
5. `Airflow idempotent DAG best practices`
6. `Airflow Google Cloud Storage BigQuery operators connection`
7. `Airflow data quality checks fail pipeline`
8. `Airflow DAG import test unit test DagBag`
9. `Airflow observability task duration SLA data freshness`

## Conceitos essenciais

- **DAG:** grafo de dependências; não é um script linear com `sleep`.
- **Data interval:** janela de dados processada por uma execução.
- **Retry:** nova tentativa para falha transitória, não correção de dado inválido.
- **Backfill:** processamento explícito de intervalos históricos.
- **Idempotência:** repetir a mesma data mantém o mesmo resultado final.

## Entrega obrigatória

Implemente o [enunciado](<01-exercicios/ENUNCIADO.md>) em `01-exercicios/dag_telecom.py`. O código não deve acessar a nuvem durante o import. Registre grafo, logs redigidos e provas de falha/reexecução em [evidências](<03-evidencias/README.md>).

## LinkedIn

Após executar o backfill e explicar a idempotência, adicione: **Apache Airflow**, **Orquestração de dados** e **Pipelines ETL/ELT**.

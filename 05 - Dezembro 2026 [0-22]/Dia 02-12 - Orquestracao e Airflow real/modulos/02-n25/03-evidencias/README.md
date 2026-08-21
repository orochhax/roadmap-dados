# Evidências — N25: DAG GCS → BigQuery

Não publique conexões, tokens, e-mails completos, nomes de projeto completos ou trechos sensíveis de logs.

## Ambiente e contrato

- versão de Python, Airflow e providers Google:
- executor e forma de execução local:
- schedule, timezone, `start_date` e `catchup`:
- conexões utilizadas (nomes, não segredos):
- comando de import test/DagBag:
- comando de execução/backfill:

## Estrutura da DAG

- lista de tarefas e responsabilidade de cada uma:
- dependências e trigger rules justificadas:
- uso do `data_interval` nos caminhos/partições:
- contrato de XCom:
- imagem ou saída textual do grafo:

## Testes operacionais

| cenário | resultado esperado | tentativas | estado final | linhas/hash curated | evidência |
|---|---|---:|---|---|---|
| lote válido | publicar |  |  |  |  |
| falha transitória | retry e publicar |  |  |  |  |
| schema/checksum inválido | bloquear |  |  |  |  |
| rerun da mesma data | não duplicar |  |  |  |  |
| backfill dia 1 | partição correta |  |  |  |  |
| backfill dia 2 | partição correta |  |  |  |  |

## Observabilidade e custo

| tarefa | duração P50/P95 | retries | bytes processados | falhas |
|---|---:|---:|---:|---:|
|  |  |  |  |  |

- freshness final e atraso contra 07:00:
- custo estimado por execução/mês:
- alerta ou gatilho operacional proposto:

## Decisão

- DAG aprovada/rejeitada:
- evidência de idempotência:
- maior modo de falha ainda não coberto:
- condição de rollback/pausa:
- recursos GCP limpos ou mantidos:

# Orquestracao conceitual + Airflow real: DAG, retries, backfill e observabilidade

**Data de estudo:** 02/12/2026  
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Orquestracao conceitual

#### O que pesquisar
- `Orquestracao conceitual Python explicado passo a passo`
- `Orquestracao conceitual Python exercícios práticos`

#### Aula guiada — projeto de engenharia de dados (parte 2)

- [ ] Continue [**Engenharia de Dados para INICIANTES | Projeto Completo Explicado do ZERO**](https://www.youtube.com/watch?v=I8qPqbXQBDU), de `00:47:31` a `01:10:55` (23min24s).
- Nesta segunda parte, acompanhe os conceitos de Docker e Airflow, o setup, a criação e a execução da DAG e a publicação do projeto.
- Compare a demonstração com sua DAG: identifique explicitamente dependências, política de retry, data interval, backfill, observabilidade e idempotência que a atividade exige.

**Arquivos da atividade:** [abrir a pasta `01-orquestracao-conceitual`](<atividades/01-orquestracao-conceitual/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-orquestracao-conceitual/dia-088-orquestracao-conceitual.py`.
- **Entradas:** manifesto local com extrair, validar, transformar, publicar e auditar. **Fallback local:** estados simulados em Python.

#### O que você precisa entender

- **Definição:** DAG representa dependências; retry repete falha transitória, timeout limita duração, backfill processa janela ausente e runbook orienta resposta.
- **Exemplo mínimo:** `extrair → validar → transformar → publicar → auditar`; cada tarefa define entrada, saída, tentativas e estado.
- **Erro comum:** repetir erro determinístico indefinidamente ou iniciar tarefa sem validar a saída anterior.

#### O que fazer

- [ ] Modele o pipeline como tarefas com dependências: extrair → validar → transformar → carregar → testar.
- [ ] Crie um DAG conceitual em Mermaid ou use Prefect/Airflow local se desejar.
- [ ] Defina política de retry, timeout, alerta e backfill.

- [ ] **Em `atividades/01-orquestracao-conceitual/dia-088-orquestracao-conceitual.py`:** Simule falha na transformação e confirme que carregar e testar ficam bloqueadas.
- [ ] **No mesmo arquivo:** defina retry máximo 3, timeout de 10 minutos e alerta após a última falha; escreva um runbook com diagnóstico e recuperação.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

### Atividade 2 — Airflow real: DAG, retries, backfill e observabilidade

#### O que pesquisar
- `Airflow TaskFlow API`
- `retries e idempotência`
- `backfill e data interval`
- `Airflow monitoring`

**Arquivos da atividade:** [abrir a pasta `02-airflow-real-dag-retries-backfill`](<atividades/02-airflow-real-dag-retries-backfill/>)

#### Objetivo

Orquestrar a landing zone de Cloud/GCP e as consultas do BigQuery como um pipeline diário de verdade. A DAG deverá esperar o lote da data lógica, validar o manifesto, carregar staging, executar testes de qualidade, fazer `MERGE` em curated e publicar métricas. Você provará retries, reexecução e backfill sem duplicar dados.

#### Termos complementares para pesquisar

1. `Apache Airflow TaskFlow API @dag @task`
2. `Airflow logical date data interval templates`
3. `Airflow schedule catchup backfill explained`
4. `Airflow retries retry_delay exponential_backoff`
5. `Airflow idempotent DAG best practices`
6. `Airflow Google Cloud Storage BigQuery operators connection`
7. `Airflow data quality checks fail pipeline`
8. `Airflow DAG import test unit test DagBag`
9. `Airflow observability task duration SLA data freshness`

#### O que você precisa entender

- **DAG:** grafo de dependências; não é um script linear com `sleep`.
- **Data interval:** janela de dados processada por uma execução.
- **Retry:** nova tentativa para falha transitória, não correção de dado inválido.
- **Backfill:** processamento explícito de intervalos históricos.
- **Idempotência:** repetir a mesma data mantém o mesmo resultado final.

#### O que fazer

Implemente o [enunciado](<atividades/02-airflow-real-dag-retries-backfill/ENUNCIADO.md>) em `atividades/02-airflow-real-dag-retries-backfill/dag_telecom.py`. O código não deve acessar a nuvem durante o import. Registre grafo, logs redigidos e provas de falha/reexecução no próprio artefato.

#### LinkedIn

Após executar o backfill e explicar a idempotência, adicione: **Apache Airflow**, **Orquestração de dados** e **Pipelines ETL/ELT**.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

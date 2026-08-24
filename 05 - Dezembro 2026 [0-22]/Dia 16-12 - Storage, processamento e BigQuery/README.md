# Armazenamento, BigQuery, dbt e Analytics Engineering

**Data de estudo:** 16/12/2026  
**Carga planejada:** 6 a 8 horas

## Atividades do dia

### Atividade 1 — Armazenamento e processamento

#### O que pesquisar
- `Armazenamento e processamento Python explicado passo a passo`
- `Armazenamento e processamento Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-armazenamento-e-processamento`](<atividades/01-armazenamento-e-processamento/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-armazenamento-e-processamento/dia-102-armazenamento-e-processamento.py`.
- **Entradas:** `dados/pedidos.csv` e schema. **Fallback local:** Parquet particionado consultado com DuckDB.

#### O que você precisa entender

- **Definição:** objeto guarda arquivos, relacional serve transações, warehouse serve análise, lakehouse combina arquivos e tabelas; partição reduz leitura.
- **Exemplo mínimo:** grave Parquet particionado por `ano/mes` e leia somente uma partição; compare bytes e tempo.
- **Erro comum:** criar partição por coluna de alta cardinalidade ou usar CSV como contrato tipado.

#### O que fazer

- [ ] Compare objeto, arquivo, banco relacional, warehouse e lakehouse para quatro tipos de dados.
- [ ] Crie uma matriz decisão com volume, latência, custo, governança e acesso.
- [ ] Converta CSV para Parquet e compare tamanho/tempo de leitura.

- [ ] **Em `atividades/01-armazenamento-e-processamento/dia-102-armazenamento-e-processamento.py`:** compare CSV e Parquet ao projetar somente `data_pedido` e `valor_pedido`; explique quando Spark ou warehouse seria excesso.
- [ ] Particione por ano/mês, leia somente janeiro de 2026 e registre arquivos lidos e linhas retornadas.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

### Atividade 2 — BigQuery: warehouse, partições, custo e consultas reais

#### O que pesquisar
- `BigQuery Sandbox`
- `partitioned clustered tables`
- `dry run bytes processed`
- `query optimization`

**Arquivos da atividade:** [abrir a pasta `02-bigquery-warehouse-particoes-custo`](<atividades/02-bigquery-warehouse-particoes-custo/>)

#### Objetivo

Levar os eventos da landing zone criada na atividade de Cloud e GCP prático a tabelas analíticas no BigQuery. Você implementará camadas de staging e curated, carga idempotente, consultas de qualidade e um benchmark que mostre quando particionamento e clustering realmente reduzem bytes processados.

#### Termos complementares para pesquisar

1. `BigQuery Sandbox limitations getting started`
2. `BigQuery load data Cloud Storage CSV schema`
3. `BigQuery partitioned tables require_partition_filter`
4. `BigQuery clustered tables block pruning best practices`
5. `BigQuery INFORMATION_SCHEMA JOBS bytes processed slot ms`
6. `BigQuery dry run query bytes processed bq query`
7. `BigQuery MERGE idempotent incremental load`
8. `BigQuery QUALIFY ROW_NUMBER deduplication`
9. `BigQuery query pricing on demand cost estimate`

#### O que você precisa entender

- **Staging:** preserva dados carregados e facilita validação.
- **Curated:** tabela limpa com contrato para consumidores.
- **Partição:** limita a leitura por data quando o filtro é utilizável.
- **Clustering:** organiza blocos por colunas frequentes de filtro/agregação.
- **Idempotência:** repetir a carga não duplica nem altera indevidamente o resultado.

#### O que fazer

Implemente as instruções do [enunciado](<atividades/02-bigquery-warehouse-particoes-custo/ENUNCIADO.md>) em `atividades/02-bigquery-warehouse-particoes-custo/consultas_bigquery.sql`. Execute dry runs e consultas reais pequenas; registre IDs redigidos, bytes, tempo e custo no próprio artefato.

O SQL aprovado será chamado pela DAG criada na atividade de orquestração e Airflow real.

#### LinkedIn

Depois de demonstrar o pipeline, adicione: **Google BigQuery**, **Data Warehousing** e **Otimização de SQL**.

### Atividade 3 — dbt e Analytics Engineering

#### O que pesquisar
- `dbt Core com DuckDB tutorial projeto local`
- `dbt sources staging marts ref source`
- `dbt generic tests singular tests documentation lineage`
- `dbt snapshots check strategy timestamp strategy`
- `dbt incremental model unique_key is_incremental`
- `dbt BigQuery profile service account OAuth`

Depois siga o enunciado desta atividade sem procurar uma solução completa. O primeiro ambiente será local com DuckDB; a adaptação ao BigQuery será documentada sem expor credenciais.

**Arquivos da atividade:** [abrir a pasta `03-dbt-e-analytics-engineering`](<atividades/03-dbt-e-analytics-engineering/>)

#### Objetivo

Transformar tabelas brutas de clientes e pedidos em uma pequena camada analítica confiável. Você organizará o projeto em `sources`, `staging` e `marts`, construirá dependências com `source()` e `ref()`, validará contratos com testes e publicará documentação e lineage.

#### O que você precisa entender

- **Analytics Engineering:** disciplina que transforma dados brutos em tabelas de negócio versionadas, testadas e documentadas.
- **DAG/lineage:** mapa das dependências entre fontes e modelos; permite entender o impacto de uma alteração.
- **Teste genérico:** regra reutilizável declarada em YAML, como unicidade ou ausência de nulos.
- **Teste singular:** consulta SQL específica que deve retornar zero linhas quando a regra está correta.
- **Snapshot:** registra mudanças históricas de uma entidade ao longo do tempo.
- **Modelo incremental:** processa somente dados novos ou alterados; precisa de chave e estratégia para continuar idempotente.

#### O que fazer

- [ ] Instale `dbt-core` e `dbt-duckdb` em ambiente virtual e execute `dbt debug`.
- [ ] Carregue os dados fake com `dbt seed` e declare as fontes brutas.
- [ ] Implemente modelos de `staging` que padronizem tipos, textos e duplicidades sem esconder decisões de qualidade.
- [ ] Implemente uma dimensão de clientes e uma tabela fato de vendas usando `source()` e `ref()`.
- [ ] Crie testes genéricos de `unique`, `not_null`, `relationships` e `accepted_values` onde fizer sentido.
- [ ] Crie pelo menos dois testes singulares para regras de negócio.
- [ ] Gere `dbt docs`, abra o lineage e registre uma captura que mostre o caminho da fonte até o mart.
- [ ] Implemente e demonstre um snapshot de clientes com uma mudança controlada.
- [ ] Escolha um modelo adequado, converta-o para incremental e prove que uma segunda execução não duplica registros.
- [ ] Desenhe a adaptação para BigQuery: autenticação, dataset, materializações, particionamento, clustering e controle de bytes. Não registre segredo no repositório.

#### Entrega esperada

Siga o [enunciado](<atividades/03-dbt-e-analytics-engineering/ENUNCIADO.md>), complete os arquivos com `TODO` e registre comandos, resultados e limitações no próprio artefato.

#### Marcos obrigatórios de credenciais

- [ ] Conclua o curso gratuito [dbt Fundamentals (VS Code)](https://learn.getdbt.com/learn/course/dbt-fundamentals-vs-code), salve o comprovante de conclusão disponibilizado na plataforma e relacione o conteúdo ao projeto local.
- [ ] Antes da atividade final de dbt, resolva o [simulado de dbt Fundamentals](<../../00 - Recursos Compartilhados/simulados-credenciais/simulado-dbt-fundamentals.md>) sem consultar respostas prontas e registre as lacunas que revisou.
- [ ] Use os créditos de estudante para concluir o skill badge oficial [Derive Insights from BigQuery Data](https://www.skills.google/paths/18/course_templates/623?locale=en).
- [ ] Antes do challenge lab do badge, resolva o [simulado Google Skills de BigQuery](<../../00 - Recursos Compartilhados/simulados-credenciais/simulado-google-skills-bigquery.md>) e refaça somente os tópicos em que não conseguiu justificar a resposta.
- [ ] Registre o nome e a URL pública do badge somente depois de concluir o laboratório e confirmar a emissão no seu perfil.

O curso dbt Fundamentals é uma conquista de aprendizagem; ele não equivale à certificação profissional paga **dbt Analytics Engineering Certification Exam**.

#### Como validar

- `dbt seed`, `dbt run` e `dbt test` terminam sem erro após a implementação.
- O DAG contém fontes, staging e marts com nomes e descrições compreensíveis.
- Uma alteração controlada comprova o snapshot e outra comprova a idempotência do incremental.
- A documentação explica o que mudaria no BigQuery e como custo e credenciais seriam controlados.
- Consigo explicar com minhas palavras `source`, `ref`, materialização, teste, snapshot e incremental.
- Concluí o dbt Fundamentals, os dois simulados e o skill badge de BigQuery, guardando evidência verificável sem expor credenciais.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

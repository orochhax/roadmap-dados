# Modelagem dimensional: fatos, dimensões, grão e SCD + Performance SQL: EXPLAIN, índices, partições e custo

**Data de estudo:** 21/09/2026  
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Modelagem dimensional: fatos, dimensões, grão e SCD

#### O que pesquisar
- `tabela fato e dimensão`
- `granularidade de fatos`
- `star schema`
- `SCD tipo 1 e tipo 2`

**Arquivos da atividade:** [abrir a pasta `01-modelagem-dimensional-fatos-dimensoes`](<atividades/01-modelagem-dimensional-fatos-dimensoes/>)

#### Objetivo

Projetar um modelo estrela auditável para responder perguntas de incidentes, clientes e planos sem multiplicar métricas em joins. Você praticará grão, chaves substitutas, dimensões conformadas e histórico SCD tipo 2.

#### Termos complementares para pesquisar

- `Kimball dimensional modeling grain fact dimension`
- `star schema fact table dimension table`
- `surrogate key vs natural key data warehouse`
- `slowly changing dimension type 1 type 2`
- `role playing date dimension`
- `accumulating snapshot fact table`
- `DuckDB CREATE TABLE constraints`

#### O que fazer

Leia o [enunciado](<atividades/01-modelagem-dimensional-fatos-dimensoes/ENUNCIADO.md>), complete [modelo_estrela.sql](<atividades/01-modelagem-dimensional-fatos-dimensoes/modelo_estrela.sql>) e registre as reconciliações no próprio artefato.

#### Como validar

- o grão de cada fato está escrito antes do DDL;
- o histórico de plano não reescreve o passado;
- joins preservam a quantidade e o valor das linhas-fato;
- uma mudança tardia e uma chave desconhecida foram tratadas;
- o modelo responde às perguntas do gerente sem consulta ambígua.

### Atividade 2 — Performance SQL: EXPLAIN, índices, partições e custo

#### O que pesquisar
- `SQL EXPLAIN`
- `índices compostos`
- `partition pruning`
- `query cost`

**Arquivos da atividade:** [abrir a pasta `02-performance-sql-explain-indices-particoes`](<atividades/02-performance-sql-explain-indices-particoes/>)

#### Objetivo

Aprender a diagnosticar uma consulta antes de “otimizá-la”, preservar o resultado e medir custo, tempo e volume lido. O exercício usa consultas operacionais de telecom, mas a técnica vale para bancos e warehouses.

#### Termos complementares para pesquisar

- `DuckDB EXPLAIN ANALYZE query profiling`
- `PostgreSQL EXPLAIN ANALYZE sequential scan index scan`
- `composite index leftmost prefix`
- `predicate pushdown Parquet`
- `partition pruning data warehouse`
- `sargable predicates SQL`
- `SQL join cardinality estimation`

#### O que fazer

Complete o [enunciado](<atividades/02-performance-sql-explain-indices-particoes/ENUNCIADO.md>) em [consultas_para_otimizar.sql](<atividades/02-performance-sql-explain-indices-particoes/consultas_para_otimizar.sql>) e documente planos e medições no próprio artefato.

#### Como validar

- cada alteração parte de uma hipótese sobre o plano;
- consulta original e otimizada retornam o mesmo conjunto;
- pelo menos cinco execuções são medidas sem esconder variabilidade;
- uma “otimização” que não compensou também é registrada.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

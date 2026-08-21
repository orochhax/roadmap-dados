# Performance SQL baseada em evidência

## Objetivo

Aprender a diagnosticar uma consulta antes de “otimizá-la”, preservar o resultado e medir custo, tempo e volume lido. O exercício usa consultas operacionais de telecom, mas a técnica vale para bancos e warehouses.

## Pesquise exatamente estes nomes

- `DuckDB EXPLAIN ANALYZE query profiling`
- `PostgreSQL EXPLAIN ANALYZE sequential scan index scan`
- `composite index leftmost prefix`
- `predicate pushdown Parquet`
- `partition pruning data warehouse`
- `sargable predicates SQL`
- `SQL join cardinality estimation`

## Trabalho obrigatório

Complete o [enunciado](01-exercicios/ENUNCIADO.md) em [consultas_para_otimizar.sql](01-exercicios/consultas_para_otimizar.sql) e documente planos e medições em [Evidências](03-evidencias/README.md).

## Concluído quando

- cada alteração parte de uma hipótese sobre o plano;
- consulta original e otimizada retornam o mesmo conjunto;
- pelo menos cinco execuções são medidas sem esconder variabilidade;
- uma “otimização” que não compensou também é registrada.


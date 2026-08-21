# Databricks e Spark introdutório

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-089-databricks-e-spark-introdutorio.py`.
- **Entradas:** `dados/pedidos.csv` e schema explícito. **Fallback local:** mesmas operações em pandas.

## Aprenda agora

- **Definição:** Spark avalia DataFrames de forma lazy e distribui transformações; schema e particionamento controlam leitura e custo.
- **Exemplo mínimo:** `spark.read.schema(schema).parquet(path).groupBy("mes").sum("valor")`; se Spark não estiver disponível, reproduza localmente em pandas e registre a equivalência.
- **Erro comum:** chamar `.collect()` em toda a base ou inferir schema crítico automaticamente.

## Núcleo essencial

1. [ ] Crie conta/ambiente Databricks Free ou use PySpark local.
2. [ ] Carregue `clientes_telecom.csv` como DataFrame Spark e inspecione esquema.
3. [ ] Faça seleção, filtro, agregação, join e criação de coluna.

## Prática obrigatória

- [ ] **Em `01-exercicios/dia-089-databricks-e-spark-introdutorio.py`:** Filtre clientes com `chamados_90d>=3`, agrupe por cidade e confirme que Spark e pandas produzem o mesmo resultado; explique quando Spark é desnecessário.
- [ ] **No mesmo arquivo:** remova `cliente_id` de uma cópia da entrada e faça a checagem de esquema impedir o processamento.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-089-databricks-e-spark-introdutorio.py` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

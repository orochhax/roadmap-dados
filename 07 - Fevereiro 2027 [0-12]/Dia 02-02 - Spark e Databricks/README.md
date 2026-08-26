# Databricks e Spark introdutorio

**Data de estudo:** 02/02/2027
**Carga planejada:** 4 a 5 horas, com pausa antes da avaliação

## Atividades do dia

### Atividade 1 — Databricks e Spark introdutorio

#### O que pesquisar
- `Databricks e Spark introdutorio engenharia de dados e MLOps explicado passo a passo`
- `Databricks e Spark introdutorio engenharia de dados e MLOps exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-databricks-e-spark-introdutorio`](<atividades/01-databricks-e-spark-introdutorio/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-databricks-e-spark-introdutorio/dia-089-databricks-e-spark-introdutorio.py`.
- **Entradas:** `dados/pedidos.csv` e schema explícito. **Fallback local:** mesmas operações em pandas.

#### O que você precisa entender

- **Definição:** Spark avalia DataFrames de forma lazy e distribui transformações; schema e particionamento controlam leitura e custo.
- **Exemplo mínimo:** `spark.read.schema(schema).parquet(path).groupBy("mes").sum("valor")`; se Spark não estiver disponível, reproduza localmente em pandas e registre a equivalência.
- **Erro comum:** chamar `.collect()` em toda a base ou inferir schema crítico automaticamente.

#### O que fazer

- [ ] Crie conta/ambiente Databricks Free ou use PySpark local.
- [ ] Carregue `clientes_telecom.csv` como DataFrame Spark e inspecione esquema.
- [ ] Faça seleção, filtro, agregação, join e criação de coluna.

- [ ] **Em `atividades/01-databricks-e-spark-introdutorio/dia-089-databricks-e-spark-introdutorio.py`:** Filtre clientes com `chamados_90d>=3`, agrupe por cidade e confirme que Spark e pandas produzem o mesmo resultado; explique quando Spark é desnecessário.
- [ ] **No mesmo arquivo:** remova `cliente_id` de uma cópia da entrada e faça a checagem de esquema impedir o processamento.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Acreditação gratuita — Databricks Fundamentals

Esta etapa prepara a **Databricks Fundamentals Accreditation**, uma acreditação introdutória gratuita. Ela não é a certificação profissional supervisionada da Databricks.

1. Conclua o curso `Databricks Fundamentals` na Databricks Academy.
2. Refaça com suas palavras os conceitos de lakehouse, Data Intelligence Platform, workloads, governança e segurança.
3. Resolva o [simulado de Databricks Fundamentals](<../../00 - Recursos Compartilhados/simulados-credenciais/simulado-databricks-fundamentals.md>) sem consulta e registre os erros.
4. Só então faça a avaliação oficial de 20 questões.
5. Registre a conclusão no [controle de tentativas](<../../00 - Recursos Compartilhados/simulados-credenciais/registro-de-tentativas.md>) e guarde o link ou comprovante do badge.

### Checklist da acreditação

- [ ] Concluí o curso e consigo diferenciar Spark, Delta Lake, lakehouse e os workloads suportados.
- [ ] Fiz o simulado sem gabarito, revisei apenas os pontos fracos e executei o caso prático deste dia.
- [ ] Conquistei o badge oficial e o registrei no LinkedIn com o nome exato, sem chamar de certificação profissional.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

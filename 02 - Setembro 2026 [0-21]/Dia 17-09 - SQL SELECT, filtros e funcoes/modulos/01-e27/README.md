# Banco relacional e SELECT

## Aprenda agora

Use um único banco na prática. Em DuckDB, importe o CSV e consulte a tabela assim:

```sql
CREATE OR REPLACE TABLE incidentes AS
SELECT * FROM read_csv_auto('dados/incidentes.csv', header = true);

SELECT cidade, duracao_min
FROM incidentes
ORDER BY duracao_min DESC
LIMIT 5;
```

**Erro comum:** misturar comandos de importação ou funções de MySQL, PostgreSQL e DuckDB na mesma solução.

## Aulas guiadas — Curso MySQL

- [ ] #01 — **O que é um Banco de Dados?** (22:28).
- [ ] #03 — **Criando o primeiro Banco de Dados** (27:55).
- [ ] #04 — **Melhorando a Estrutura do Banco de Dados** (27:09).
- [ ] #11 — **SELECT, parte 1** (34:31).
- **Carga:** 1h52. O curso usa MySQL como exemplo, mas a prática do roadmap continua em DuckDB ou PostgreSQL. Não instale WAMP/XAMPP nem troque de banco para acompanhar os vídeos.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/select_basico.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

## Núcleo essencial

1. [ ] Use DuckDB ou PostgreSQL, crie a tabela `incidentes` e importe `dados/incidentes.csv`.
2. [ ] Depois das aulas, resolva as consultas 2, 3, 5 e 6 de `select_basico.sql`, cobrindo seleção de colunas, aliases, limite e ordenação.
3. [ ] Antes de duas consultas, registre o formato esperado e confira o resultado retornado.

## Prática obrigatória

- [ ] **Em `01-exercicios/select_basico.sql`:** Escreva uma consulta que liste incidentes P1 não resolvidos, calcule impacto e ordene do maior para o menor, limitando a cinco linhas.
- [ ] **Em `01-exercicios/select_basico.sql`:** Escreva uma consulta de validação que compare COUNT(*) com COUNT(DISTINCT id) e conte ids nulos antes de aceitar a importação.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

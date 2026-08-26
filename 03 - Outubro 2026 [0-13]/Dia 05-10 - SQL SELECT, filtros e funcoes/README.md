# Banco relacional e SELECT + Filtros e funcoes

**Data de estudo:** 05/10/2026
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Banco relacional e SELECT

#### O que pesquisar
- `Banco relacional e SELECT Python explicado passo a passo`
- `Banco relacional e SELECT Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-banco-relacional-e-select`](<atividades/01-banco-relacional-e-select/>)

#### O que você precisa entender

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

#### Aulas guiadas — SELECT e DuckDB

- [ ] Assista [**Curso MySQL #11 - SELECT (Parte 1)**](https://www.youtube.com/watch?v=GaOlyL3Uv9M) (34:31).
- [ ] Assista **DuckDB - Analise Qualquer Volume de Dados com Python** (26:47). [Abrir no YouTube](https://www.youtube.com/watch?v=hIvUE-P6Ep4)
- **Carga em vídeo:** 1h01. O curso de MySQL demonstra a linguagem; o vídeo de DuckDB mostra consultas diretamente sobre CSV, JSON, Parquet e DataFrames. A prática do roadmap continua em DuckDB ou PostgreSQL. Não instale WAMP/XAMPP nem troque de banco para acompanhar os vídeos.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-banco-relacional-e-select/select_basico.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

#### O que fazer

- [ ] Use DuckDB ou PostgreSQL, crie a tabela `incidentes` e importe `dados/incidentes.csv`.
- [ ] Depois das aulas, resolva as consultas 2, 3, 5 e 6 de `select_basico.sql`, cobrindo seleção de colunas, aliases, limite e ordenação.
- [ ] Antes de duas consultas, registre o formato esperado e confira o resultado retornado.

- [ ] **Em `atividades/01-banco-relacional-e-select/select_basico.sql`:** Escreva uma consulta que liste incidentes P1 não resolvidos, calcule impacto e ordene do maior para o menor, limitando a cinco linhas.
- [ ] **Em `atividades/01-banco-relacional-e-select/select_basico.sql`:** Escreva uma consulta de validação que compare COUNT(*) com COUNT(DISTINCT id) e conte ids nulos antes de aceitar a importação.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

### Atividade 2 — Filtros e funcoes

#### O que pesquisar
- `Filtros e funcoes Python explicado passo a passo`
- `Filtros e funcoes Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-filtros-e-funcoes`](<atividades/02-filtros-e-funcoes/>)

#### Aula guiada — Curso MySQL

- [ ] Assista [**Curso MySQL #12 - SELECT (Parte 2)**](https://www.youtube.com/watch?v=q4hPo83-Buo) (38:14).
- **Carga total de vídeo do dia:** 1h39min32s, incluindo a introdução ao DuckDB.
- Use a aula como demonstração e execute as consultas selecionadas abaixo com os dados de incidentes do roadmap.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-filtros-e-funcoes/dia-022-filtros-e-funcoes.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

#### O que fazer

- [ ] Resolva as consultas 5, 7, 8 e 12 de `dia-022-filtros-e-funcoes.sql`, cobrindo `BETWEEN`, `LIKE`, nulos e precedência com parênteses. As consultas básicas demonstradas na aula ficam como reforço.
- [ ] Crie um filtro de negócio e confira manualmente ao menos uma linha incluída e uma excluída.
- [ ] Teste os limites 50/51 e 120/121 para diferenciar operadores inclusivos e exclusivos.

- [ ] **Em `atividades/02-filtros-e-funcoes/dia-022-filtros-e-funcoes.sql`:** Escreva uma consulta para incidentes de Salvador ou Ilhéus, com duração entre 51 e 120 minutos e causa contendo 'fibra'.
- [ ] **Em `atividades/02-filtros-e-funcoes/dia-022-filtros-e-funcoes.sql`:** Crie uma consulta que conte duração nula, cidade nula e ids duplicados; mantenha cada contagem em uma coluna identificada.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

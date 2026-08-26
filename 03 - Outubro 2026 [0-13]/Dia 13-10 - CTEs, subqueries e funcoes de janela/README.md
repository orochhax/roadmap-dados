# Subqueries e CTEs + Funcoes de janela

**Data de estudo:** 13/10/2026
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Subqueries e CTEs

#### O que pesquisar
- `Subqueries e CTEs SQL para análise de dados explicado passo a passo`
- `Subqueries e CTEs SQL para análise de dados exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-subqueries-e-ctes`](<atividades/01-subqueries-e-ctes/>)

#### Aula guiada — CTE

- [ ] Assista **Usando CTE no MySQL para criar Consultas Mais Organizadas e Poderosas** (16:58).
- Reproduza a ideia em DuckDB ou PostgreSQL e compare a mesma consulta escrita como subquery e como CTE. Use o nome completo acima para localizar a aula no YouTube.

#### O que você precisa entender

Uma subquery produz um valor ou tabela dentro de outra consulta; uma CTE nomeia uma etapa para tornar o fluxo legível.

```sql
WITH media_cidade AS (
  SELECT cidade, AVG(duracao_min) AS media FROM incidentes GROUP BY cidade
)
SELECT i.*
FROM incidentes AS i
JOIN media_cidade AS m USING (cidade)
WHERE i.duracao_min > m.media;
```

**Erro comum:** aplicar um filtro cedo demais e alterar o conjunto usado no denominador ou na média.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-subqueries-e-ctes/dia-026-subqueries-e-ctes.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

#### O que fazer

- [ ] Escreva uma subquery escalar para comparar cada incidente à duração média geral.
- [ ] Escreva uma subquery correlacionada para identificar incidentes acima da média de sua própria cidade.
- [ ] Reescreva ambas usando CTEs e compare legibilidade.

- [ ] Crie uma sequência de três CTEs: dados válidos → métricas por cidade → ranking final.
- [ ] Introduza um filtro em posição errada e demonstre como ele altera o denominador de uma taxa.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

### Atividade 2 — Funcoes de janela

#### O que pesquisar
- `Funcoes de janela Python explicado passo a passo`
- `Funcoes de janela Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-funcoes-de-janela`](<atividades/02-funcoes-de-janela/>)

#### Aulas guiadas — funções de janela

- [ ] Assista **Série Funções de Janela no SQL para Análise de Dados - Aula 1 - Rankings com RANK() e DENSE_RANK()** (13:10).
- [ ] Assista **Série Funções de Janela no SQL para Análise de Dados - Aula 2 - Enésimo maior valor com ROW_NUMBER()** (10:53).
- [ ] Assista **Série Funções de Janela no SQL para Análise de Dados - Aula 3 - Médias móveis com AVG()** (14:16).
- [ ] Assista **Série Funções de Janela no SQL para Análise de Dados - Aula 4 - Comparar Valores com LAG() e LEAD()** (15:21).
- [ ] Assista **Série Funções de Janela no SQL para Análise de Dados - Aula 5 - Somas acumuladas com SUM** (9:09).
- [ ] Assista **Série Funções de Janela no SQL para Análise de Dados - Aula 10 - Análises segmentadas: PARTITION BY** (7:31).
- **Carga em vídeo da sequência:** 1h10. Use os nomes completos acima para localizar as aulas no YouTube e, depois de cada conceito, aplique-o em `dia-027-funcoes-de-janela.sql` com os dados do roadmap.

#### O que você precisa entender

Funções de janela calculam sobre linhas relacionadas sem reduzir o resultado como `GROUP BY`.

```sql
SELECT cidade, id, impacto,
       DENSE_RANK() OVER (PARTITION BY cidade ORDER BY impacto DESC) AS posicao,
       LAG(impacto) OVER (PARTITION BY cidade ORDER BY data_abertura) AS impacto_anterior
FROM incidentes;
```

**Erro comum:** omitir `ORDER BY` dentro da janela e obter acumulados ou posições sem ordem definida.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-funcoes-de-janela/dia-027-funcoes-de-janela.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

#### O que fazer

- [ ] Use `ROW_NUMBER`, `RANK` e `DENSE_RANK` para ranquear incidentes por impacto dentro de cada cidade; explique diferenças em empates.
- [ ] Calcule média móvel de sete dias, soma acumulada e diferença para o evento anterior com `LAG`.
- [ ] Use `LEAD` para calcular tempo até o próximo incidente da mesma cidade.

- [ ] **Em `atividades/02-funcoes-de-janela/dia-027-funcoes-de-janela.sql`:** Retorne os dois maiores impactos por cidade com DENSE_RANK e mantenha todos os empates na segunda posição.
- [ ] **Em `atividades/02-funcoes-de-janela/dia-027-funcoes-de-janela.sql`:** Crie três linhas empatadas para uma cidade em uma CTE de valores e compare ROW_NUMBER, RANK e DENSE_RANK nessa entrada.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

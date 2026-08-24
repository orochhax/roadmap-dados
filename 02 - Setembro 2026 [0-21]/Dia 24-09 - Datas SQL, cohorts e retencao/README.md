# Datas e analise temporal + Cohorts e retencao

**Data de estudo:** 24/09/2026  
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Datas e analise temporal

#### O que pesquisar
- `Datas e analise temporal Python explicado passo a passo`
- `Datas e analise temporal Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-datas-e-analise-temporal`](<atividades/01-datas-e-analise-temporal/>)

#### O que você precisa entender

Converta texto para data antes de extrair períodos. Em DuckDB, `date_trunc` mantém ano e mês juntos.

```sql
SELECT date_trunc('month', CAST(data_abertura AS TIMESTAMP)) AS mes,
       COUNT(*) AS incidentes
FROM incidentes
GROUP BY mes
ORDER BY mes;
```

**Erro comum:** agrupar apenas pelo número do mês e misturar janeiro de anos diferentes.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-datas-e-analise-temporal/dia-028-datas-e-analise-temporal.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

#### O que fazer

- [ ] Converta colunas de texto em data/hora e extraia ano, mês, semana, dia da semana e hora.
- [ ] Calcule incidentes e duração média por dia, semana e mês.
- [ ] Meça tempo entre abertura e fechamento e classifique SLA em `no prazo` ou `atrasado`.

- [ ] Crie calendário completo e faça `LEFT JOIN` para exibir dias sem eventos com zero.
- [ ] Teste virada de mês, ano bissexto, horário nulo e eventos abertos; documente decisões.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

### Atividade 2 — Cohorts e retencao

#### O que pesquisar
- `Cohorts e retencao SQL para análise de dados explicado passo a passo`
- `Cohorts e retencao SQL para análise de dados exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-cohorts-e-retencao`](<atividades/02-cohorts-e-retencao/>)

#### O que você precisa entender

Coorte é o grupo definido pelo período da primeira atividade. A retenção do período `n` é `clientes_ativos_n / clientes_da_coorte_no_periodo_0`.

```sql
WITH primeira AS (
  SELECT cliente_id, MIN(date_trunc('month', data_compra)) AS cohort_month
  FROM pedidos GROUP BY cliente_id
)
SELECT * FROM primeira;
```

**Erro comum:** dividir pelo total de clientes ativos no mês, em vez do tamanho inicial da própria coorte.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-cohorts-e-retencao/dia-029-cohorts-e-retencao.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

#### O que fazer

- [ ] Defina coorte como mês da primeira compra ou ativação; calcule o mês inicial de cada cliente.
- [ ] Crie tabela com `cohort_month`, `period_number`, clientes ativos e taxa de retenção.
- [ ] Monte matriz de retenção do mês 0 ao mês 5 e valide manualmente uma coorte pequena com cinco clientes.

- [ ] Compare retenção por canal de aquisição ou plano.
- [ ] Escreva três conclusões e uma cautela sobre coortes pequenas.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

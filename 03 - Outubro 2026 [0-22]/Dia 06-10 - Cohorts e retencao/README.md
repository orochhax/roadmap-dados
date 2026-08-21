# Cohorts e retenção

## Aprenda agora

Coorte é o grupo definido pelo período da primeira atividade. A retenção do período `n` é `clientes_ativos_n / clientes_da_coorte_no_periodo_0`.

```sql
WITH primeira AS (
  SELECT cliente_id, MIN(date_trunc('month', data_compra)) AS cohort_month
  FROM pedidos GROUP BY cliente_id
)
SELECT * FROM primeira;
```

**Erro comum:** dividir pelo total de clientes ativos no mês, em vez do tamanho inicial da própria coorte.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-029-cohorts-e-retencao.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

## Núcleo essencial

1. [ ] Defina coorte como mês da primeira compra ou ativação; calcule o mês inicial de cada cliente.
2. [ ] Crie tabela com `cohort_month`, `period_number`, clientes ativos e taxa de retenção.
3. [ ] Monte matriz de retenção do mês 0 ao mês 5 e valide manualmente uma coorte pequena com cinco clientes.

## Prática obrigatória

- [ ] Compare retenção por canal de aquisição ou plano.
- [ ] Escreva três conclusões e uma cautela sobre coortes pequenas.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

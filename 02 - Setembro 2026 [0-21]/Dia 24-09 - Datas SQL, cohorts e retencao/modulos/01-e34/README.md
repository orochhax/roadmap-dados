# Datas e análise temporal

## Aprenda agora

Converta texto para data antes de extrair períodos. Em DuckDB, `date_trunc` mantém ano e mês juntos.

```sql
SELECT date_trunc('month', CAST(data_abertura AS TIMESTAMP)) AS mes,
       COUNT(*) AS incidentes
FROM incidentes
GROUP BY mes
ORDER BY mes;
```

**Erro comum:** agrupar apenas pelo número do mês e misturar janeiro de anos diferentes.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-028-datas-e-analise-temporal.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

## Núcleo essencial

1. [ ] Converta colunas de texto em data/hora e extraia ano, mês, semana, dia da semana e hora.
2. [ ] Calcule incidentes e duração média por dia, semana e mês.
3. [ ] Meça tempo entre abertura e fechamento e classifique SLA em `no prazo` ou `atrasado`.

## Prática obrigatória

- [ ] Crie calendário completo e faça `LEFT JOIN` para exibir dias sem eventos com zero.
- [ ] Teste virada de mês, ano bissexto, horário nulo e eventos abertos; documente decisões.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

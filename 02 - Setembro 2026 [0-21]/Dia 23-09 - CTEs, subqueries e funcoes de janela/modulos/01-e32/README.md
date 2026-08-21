# Subqueries e CTEs

## Aprenda agora

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

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-026-subqueries-e-ctes.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

## Núcleo essencial

1. [ ] Escreva uma subquery escalar para comparar cada incidente à duração média geral.
2. [ ] Escreva uma subquery correlacionada para identificar incidentes acima da média de sua própria cidade.
3. [ ] Reescreva ambas usando CTEs e compare legibilidade.

## Prática obrigatória

- [ ] Crie uma sequência de três CTEs: dados válidos → métricas por cidade → ranking final.
- [ ] Introduza um filtro em posição errada e demonstre como ele altera o denominador de uma taxa.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

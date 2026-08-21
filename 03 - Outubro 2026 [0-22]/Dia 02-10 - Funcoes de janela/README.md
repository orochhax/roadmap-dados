# Funções de janela

## Aprenda agora

Funções de janela calculam sobre linhas relacionadas sem reduzir o resultado como `GROUP BY`.

```sql
SELECT cidade, id, impacto,
       DENSE_RANK() OVER (PARTITION BY cidade ORDER BY impacto DESC) AS posicao,
       LAG(impacto) OVER (PARTITION BY cidade ORDER BY data_abertura) AS impacto_anterior
FROM incidentes;
```

**Erro comum:** omitir `ORDER BY` dentro da janela e obter acumulados ou posições sem ordem definida.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-027-funcoes-de-janela.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

## Núcleo essencial

1. [ ] Use `ROW_NUMBER`, `RANK` e `DENSE_RANK` para ranquear incidentes por impacto dentro de cada cidade; explique diferenças em empates.
2. [ ] Calcule média móvel de sete dias, soma acumulada e diferença para o evento anterior com `LAG`.
3. [ ] Use `LEAD` para calcular tempo até o próximo incidente da mesma cidade.

## Prática obrigatória

- [ ] **Em `01-exercicios/dia-027-funcoes-de-janela.sql`:** Retorne os dois maiores impactos por cidade com DENSE_RANK e mantenha todos os empates na segunda posição.
- [ ] **Em `01-exercicios/dia-027-funcoes-de-janela.sql`:** Crie três linhas empatadas para uma cidade em uma CTE de valores e compare ROW_NUMBER, RANK e DENSE_RANK nessa entrada.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

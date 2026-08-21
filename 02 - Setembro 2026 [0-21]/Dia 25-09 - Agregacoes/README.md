# Agregações

## Aula guiada — Curso MySQL

- [ ] #13 — **SELECT, parte 3** (29:11).
- Depois da aula, use o conjunto de dados do roadmap; exemplos copiados da base do curso não contam como prática.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-023-agregacoes.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

## Núcleo essencial

1. [ ] Escreva uma consulta de resumo que contenha `COUNT`, `SUM`, `AVG`, `MIN` e `MAX` para a tabela de incidentes, em vez de repetir uma consulta isolada para cada função.
2. [ ] Agrupe por cidade, causa e severidade; calcule quantidade, duração média, clientes totais e percentual resolvido.
3. [ ] Use `HAVING` para manter apenas cidades com pelo menos cinco incidentes e duração média acima de 60.

## Prática obrigatória

- [ ] Calcule taxa de resolução com proteção contra divisão por zero e compare resultado com pandas.
- [ ] **Em `01-exercicios/dia-023-agregacoes.sql`:** Agrupe por cidade e mantenha apenas grupos com pelo menos 10 incidentes e duração média acima de 90 minutos.
- [ ] **Em `01-exercicios/dia-023-agregacoes.sql`:** Escolha uma cidade do resultado e confira em outra consulta COUNT, SUM(duracao_min) e AVG(duracao_min) sem usar o agrupamento final.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

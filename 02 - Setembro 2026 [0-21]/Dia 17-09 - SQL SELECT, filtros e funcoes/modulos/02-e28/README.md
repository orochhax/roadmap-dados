# Filtros e funções

## Aula guiada — Curso MySQL

- [ ] #12 — **SELECT, parte 2** (38:14).
- Use a aula como demonstração e execute as consultas selecionadas abaixo com os dados de incidentes do roadmap.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-022-filtros-e-funcoes.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

## Núcleo essencial

1. [ ] Resolva as consultas 5, 7, 8 e 12 de `dia-022-filtros-e-funcoes.sql`, cobrindo `BETWEEN`, `LIKE`, nulos e precedência com parênteses. As consultas básicas demonstradas na aula ficam como reforço.
2. [ ] Crie um filtro de negócio e confira manualmente ao menos uma linha incluída e uma excluída.
3. [ ] Teste os limites 50/51 e 120/121 para diferenciar operadores inclusivos e exclusivos.

## Prática obrigatória

- [ ] **Em `01-exercicios/dia-022-filtros-e-funcoes.sql`:** Escreva uma consulta para incidentes de Salvador ou Ilhéus, com duração entre 51 e 120 minutos e causa contendo 'fibra'.
- [ ] **Em `01-exercicios/dia-022-filtros-e-funcoes.sql`:** Crie uma consulta que conte duração nula, cidade nula e ids duplicados; mantenha cada contagem em uma coluna identificada.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

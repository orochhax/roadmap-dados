# JOINs

## Aprenda agora

Um anti-join retorna linhas sem correspondência. Antes de combinar tabelas, declare se cada chave é única e confira a quantidade de linhas.

```sql
SELECT c.id
FROM clientes AS c
LEFT JOIN pagamentos AS p ON p.cliente_id = c.id
WHERE p.cliente_id IS NULL;
```

**Erro comum:** juntar duas tabelas com várias linhas por cliente e somar valores duplicados; agregue antes ou valide a cardinalidade.

## Aulas guiadas — Curso MySQL

- [ ] #14 — **Modelo Relacional** (40:25).
- [ ] #15 — **Chaves Estrangeiras e JOIN** (40:44).
- **Carga:** 1h21. As duas aulas cobrem o necessário para a prática abaixo.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-024-joins.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

## Núcleo essencial

1. [ ] Crie tabelas `clientes`, `planos`, `chamados` e `pagamentos` com chaves primárias e estrangeiras; importe dados do kit.
2. [ ] Como o `INNER JOIN` simples já foi praticado no curso, escreva um `LEFT JOIN` para encontrar clientes sem pagamentos e um anti-join para planos sem clientes.
3. [ ] Crie um caso muitos-para-muitos acidental duplicando chaves; meça como isso infla soma de mensalidade.

## Prática obrigatória

- [ ] Corrija o problema agregando antes do join ou validando cardinalidade.
- [ ] Desenhe em Mermaid ou texto o relacionamento entre as quatro tabelas e anote a granularidade de cada uma.
- [ ] **Em `01-exercicios/dia-024-joins.sql`:** Conte linhas e clientes distintos antes e depois do join com pagamentos para revelar qualquer multiplicação de registros.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

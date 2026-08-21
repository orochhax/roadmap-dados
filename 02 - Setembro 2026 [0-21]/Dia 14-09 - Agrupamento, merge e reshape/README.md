# Agrupamento, merge e reshape

## Aprenda agora

`groupby` resume grupos; `merge` combina tabelas por chave; `melt` e `pivot` alternam entre formatos longo e largo.

```python
resumo = incidentes.groupby("cidade", as_index=False).agg(qtd=("id", "count"))
com_meta = resumo.merge(metas, on="cidade", how="left", validate="one_to_one")
longo = tabela_larga.melt(id_vars="cidade", var_name="metrica", value_name="valor")
```

**Erro comum:** fazer `merge` sem validar a cardinalidade e multiplicar linhas silenciosamente.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-014-agrupamento-merge-e-reshape.ipynb`.
- **Dados:** `dados/incidentes.csv`, `dados/clientes_telecom.csv`, `dados/pedidos.csv` e `dados/metas_cidades.csv`.

## Núcleo essencial

1. [ ] Com `incidentes.csv` e `metas_cidades.csv`, calcule por `groupby` quantidade, média, mediana, soma de clientes e percentual resolvido por cidade.
2. [ ] Faça `merge` `inner`, `left` e `outer`; anote quantas linhas resultam e identifique cidades sem correspondência.
3. [ ] Crie uma tabela dinâmica com cidade nas linhas, severidade nas colunas e duração média nos valores.

## Prática obrigatória

- [ ] Transforme dados largos em longos com `melt` e retorne ao formato largo com `pivot`.
- [ ] Provoque uma chave duplicada, observe o aumento de linhas e crie uma validação para impedir merge muitos-para-muitos acidental.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

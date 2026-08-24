# Limpeza de dados + Agrupamento, merge e reshape

**Data de estudo:** 09/09/2026  
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Limpeza de dados

#### O que pesquisar
- `Limpeza de dados Python explicado passo a passo`
- `Limpeza de dados Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-limpeza-de-dados`](<atividades/01-limpeza-de-dados/>)

#### O que você precisa entender

Limpeza torna regras explícitas: detectar ausentes e duplicados, padronizar categorias e converter tipos sem apagar casos suspeitos automaticamente.

```python
df["cidade"] = df["cidade"].str.strip().str.title()
df["duracao_min"] = pd.to_numeric(df["duracao_min"], errors="coerce")
relatorio = {"ausentes": df.isna().sum(), "duplicados": int(df.duplicated().sum())}
```

**Erro comum:** preencher ou remover valores antes de medir quantos registros serão afetados e justificar a regra.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-limpeza-de-dados/dia-013-limpeza-de-dados.ipynb`.
- **Dados:** `dados/incidentes.csv`, `dados/clientes_telecom.csv`, `dados/pedidos.csv` e `dados/metas_cidades.csv`.

#### O que fazer

- [ ] Produza um relatório inicial de ausentes, duplicados, tipos incorretos e categorias inconsistentes.
- [ ] Padronize textos, converta tipos e trate duplicados com uma regra explícita.
- [ ] Escolha uma estratégia para cada campo ausente, salve `dados_limpos.csv` e registre o antes/depois em poucas linhas.

- [ ] Identifique valores extremos como casos suspeitos e preserve-os; não aplique remoção automática.
- [ ] Teste uma categoria com espaços e capitalização diferente usando a mesma função de padronização.
- [ ] Salve `relatorio_limpeza.md` com o antes/depois, as decisões tomadas e um risco de distorção.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

### Atividade 2 — Agrupamento, merge e reshape

#### O que pesquisar
- `Agrupamento, merge e reshape Python explicado passo a passo`
- `Agrupamento, merge e reshape Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-agrupamento-merge-e-reshape`](<atividades/02-agrupamento-merge-e-reshape/>)

#### O que você precisa entender

`groupby` resume grupos; `merge` combina tabelas por chave; `melt` e `pivot` alternam entre formatos longo e largo.

```python
resumo = incidentes.groupby("cidade", as_index=False).agg(qtd=("id", "count"))
com_meta = resumo.merge(metas, on="cidade", how="left", validate="one_to_one")
longo = tabela_larga.melt(id_vars="cidade", var_name="metrica", value_name="valor")
```

**Erro comum:** fazer `merge` sem validar a cardinalidade e multiplicar linhas silenciosamente.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-agrupamento-merge-e-reshape/dia-014-agrupamento-merge-e-reshape.ipynb`.
- **Dados:** `dados/incidentes.csv`, `dados/clientes_telecom.csv`, `dados/pedidos.csv` e `dados/metas_cidades.csv`.

#### O que fazer

- [ ] Com `incidentes.csv` e `metas_cidades.csv`, calcule por `groupby` quantidade, média, mediana, soma de clientes e percentual resolvido por cidade.
- [ ] Faça `merge` `inner`, `left` e `outer`; anote quantas linhas resultam e identifique cidades sem correspondência.
- [ ] Crie uma tabela dinâmica com cidade nas linhas, severidade nas colunas e duração média nos valores.

- [ ] Transforme dados largos em longos com `melt` e retorne ao formato largo com `pivot`.
- [ ] Provoque uma chave duplicada, observe o aumento de linhas e crie uma validação para impedir merge muitos-para-muitos acidental.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

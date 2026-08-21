# Limpeza de dados

## Aprenda agora

Limpeza torna regras explícitas: detectar ausentes e duplicados, padronizar categorias e converter tipos sem apagar casos suspeitos automaticamente.

```python
df["cidade"] = df["cidade"].str.strip().str.title()
df["duracao_min"] = pd.to_numeric(df["duracao_min"], errors="coerce")
relatorio = {"ausentes": df.isna().sum(), "duplicados": int(df.duplicated().sum())}
```

**Erro comum:** preencher ou remover valores antes de medir quantos registros serão afetados e justificar a regra.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-013-limpeza-de-dados.ipynb`.
- **Dados:** `dados/incidentes.csv`, `dados/clientes_telecom.csv`, `dados/pedidos.csv` e `dados/metas_cidades.csv`.

## Núcleo essencial

1. [ ] Produza um relatório inicial de ausentes, duplicados, tipos incorretos e categorias inconsistentes.
2. [ ] Padronize textos, converta tipos e trate duplicados com uma regra explícita.
3. [ ] Escolha uma estratégia para cada campo ausente, salve `dados_limpos.csv` e registre o antes/depois em poucas linhas.

## Prática obrigatória

- [ ] Identifique valores extremos como casos suspeitos e preserve-os; não aplique remoção automática.
- [ ] Teste uma categoria com espaços e capitalização diferente usando a mesma função de padronização.
- [ ] Salve `relatorio_limpeza.md` com o antes/depois, as decisões tomadas e um risco de distorção.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

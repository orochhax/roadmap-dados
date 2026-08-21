# Medidas e distribuições

## Aprenda agora

Média usa todos os valores; mediana usa a posição central; `IQR = Q3 - Q1`; `z = (x - média) / desvio`. Outliers afetam mais a média e o z-score que a mediana e o IQR.

```python
serie = df["mensalidade"].dropna()
q1, q3 = serie.quantile([0.25, 0.75])
iqr = q3 - q1
limites_iqr = (q1 - 1.5 * iqr, q3 + 1.5 * iqr)
z = (serie - serie.mean()) / serie.std(ddof=1)
```

**Erro comum:** remover automaticamente todo ponto fora do limite sem investigar se ele é erro ou caso real relevante.

## Aplicações integradas

- [ ] No notebook atual, use `[30, 45, 60, 75, 90, 999.9]` e explique como média, mediana e percentis reagem ao valor extremo.
- [ ] Em uma cópia de `clientes_telecom.csv`, sinalize outliers de mensalidade por IQR e por `|z| > 3`; compare quais linhas cada método encontra sem removê-las.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-031-medidas-e-distribuicoes.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/incidentes.csv` e dados sintéticos gerados no notebook com seed 42.

## Núcleo essencial

1. [ ] Com `clientes_telecom.csv`, calcule média, mediana, moda, variância, desvio, quartis, IQR e amplitude para mensalidade, NPS e chamados.
2. [ ] Crie duas distribuições com mesma média e desvios diferentes; mostre por que a média isolada engana.
3. [ ] Compare métricas com e sem um outlier extremo inserido manualmente.

## Prática obrigatória

- [ ] Faça histogramas e boxplots e escreva a forma da distribuição: simétrica, assimétrica ou multimodal.
- [ ] Explique em linguagem de negócio quando mediana é mais adequada que média.
- [ ] **Em `01-exercicios/dia-031-medidas-e-distribuicoes.ipynb`:** Calcule as mesmas medidas somente para Salvador e compare o tamanho desse grupo com o total antes de interpretar a diferença.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

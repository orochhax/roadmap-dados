# Visualização com pandas e Matplotlib

## Aprenda agora

`DataFrame.plot()` prepara o gráfico rapidamente; Matplotlib permite controlar eixos, linhas de referência e anotações.

```python
import matplotlib.pyplot as plt

ax = receita_mensal.plot(marker="o")
ax.axhline(meta, color="red", linestyle="--", label="Meta")
ax.annotate("abaixo da meta", xy=(mes, valor))
plt.legend()
```

**Erro comum:** anotar um ponto calculado com filtro diferente do usado no gráfico.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-017-visualizacao-com-pandas-e-matplotlib.ipynb`.
- **Dados:** `dados/incidentes.csv`, `dados/clientes_telecom.csv`, `dados/pedidos.csv` e `dados/metas_cidades.csv`.

## Núcleo essencial

1. [ ] Com `pedidos.csv`, crie séries temporais de receita diária e mensal, barras de receita por canal e boxplot de valor por categoria.
2. [ ] Faça primeiro com `DataFrame.plot()` e depois recrie dois gráficos diretamente com Matplotlib.
3. [ ] Adicione linha de meta mensal e destaque meses abaixo da meta por anotação textual.

## Prática obrigatória

- [ ] Crie uma função reutilizável que receba DataFrame, coluna temporal, métrica e título.
- [ ] Teste a função com dados vazios, uma única data e categorias desconhecidas.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

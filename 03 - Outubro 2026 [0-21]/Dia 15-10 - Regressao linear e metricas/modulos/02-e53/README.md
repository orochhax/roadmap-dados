# Métricas de regressão

## Aprenda agora

MAE é o erro absoluto médio; RMSE dá peso maior a erros grandes; `R²` compara com a previsão pela média; MAPE divide pelo valor real e falha quando ele é zero.

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

mae = mean_absolute_error(y_real, y_previsto)
rmse = mean_squared_error(y_real, y_previsto) ** 0.5
r2 = r2_score(y_real, y_previsto)
```

**Erro comum:** comparar métricas calculadas em conjuntos ou escalas diferentes.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-047-metricas-de-regressao.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

## Núcleo essencial

1. [ ] No notebook, use `y_real = [100, 120, 80, 0, 200]` e `y_previsto = [90, 135, 70, 10, 180]` para calcular MAE, MSE, RMSE, R² e MAPE manualmente e com biblioteca.
2. [ ] Crie um caso com valor real zero e mostre por que MAPE pode quebrar.
3. [ ] Compare dois modelos: um com poucos erros grandes e outro com muitos erros pequenos.

## Prática obrigatória

- [ ] Escolha a métrica mais coerente para previsão de receita e justifique custo dos erros.
- [ ] Crie intervalo de erro por faixa de valor e verifique se o modelo piora nos pedidos maiores.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

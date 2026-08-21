# Regressão linear

## Aprenda agora

Regressão linear estima `y = intercepto + soma(coeficiente × variável)`. Resíduo é `y_real - y_previsto`; padrões nos resíduos indicam limitações do modelo.

```python
from sklearn.linear_model import LinearRegression

modelo = LinearRegression().fit(X_treino, y_treino)
predicao = modelo.predict(X_validacao)
residuos = y_validacao - predicao
```

**Erro comum:** interpretar coeficiente como efeito causal sem controlar desenho, confundidores e suposições.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-046-regressao-linear.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

## Núcleo essencial

1. [ ] Crie dados sintéticos lineares `y = 3x + 5 + ruído` e ajuste regressão linear.
2. [ ] Recupere coeficiente e intercepto; compare com valores reais usados na geração.
3. [ ] Use `pedidos.csv` para prever valor do pedido com variáveis permitidas.

## Prática obrigatória

- [ ] Plote resíduos versus predição e distribuição dos resíduos.
- [ ] Crie uma relação não linear e demonstre por que regressão linear simples falha.
- [ ] **Em `01-exercicios/dia-046-regressao-linear.ipynb`:** Separe os pedidos acima do percentil 90 e compare o erro desse grupo com o restante.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

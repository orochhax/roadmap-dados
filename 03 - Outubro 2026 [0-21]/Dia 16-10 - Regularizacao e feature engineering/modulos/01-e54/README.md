# Regularização

## Aprenda agora

Ridge adiciona penalidade L2 e reduz coeficientes; Lasso usa L1 e pode zerá-los. `alpha` controla a força da penalidade, por isso as variáveis devem estar na mesma escala.

```python
from sklearn.linear_model import Ridge, Lasso

ridge = Ridge(alpha=1.0).fit(X_treino_padronizado, y_treino)
lasso = Lasso(alpha=0.1).fit(X_treino_padronizado, y_treino)
```

**Erro comum:** comparar coeficientes regularizados de variáveis em escalas muito diferentes.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-048-regularizacao.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

## Núcleo essencial

1. [ ] Treine regressão linear, Ridge e Lasso no mesmo conjunto padronizado.
2. [ ] Varie `alpha` em pelo menos seis valores e registre coeficientes e métricas.
3. [ ] Crie features altamente correlacionadas para observar instabilidade da regressão comum.

## Prática obrigatória

- [ ] Mostre quais coeficientes o Lasso zera e quando isso não significa causalidade.
- [ ] Escolha um modelo equilibrando erro, estabilidade e interpretação.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-048-regularizacao.ipynb`:** Compare Ridge e Lasso com alpha 0,01 e 10, mantendo split e escala iguais, e registre coeficientes e RMSE.
- [ ] **Em `01-exercicios/dia-048-regularizacao.ipynb`:** Duplique uma feature numérica com ruído mínimo e verifique como os coeficientes mudam nos três modelos.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

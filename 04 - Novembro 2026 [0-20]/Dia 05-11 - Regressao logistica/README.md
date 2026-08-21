# Regressão logística

## Aprenda agora

Regressão logística modela a probabilidade da classe positiva: `p = 1 / (1 + exp(-z))`. Após padronização, o sinal do coeficiente indica a direção da associação com o log-odds.

```python
from sklearn.linear_model import LogisticRegression

modelo = LogisticRegression(max_iter=1000).fit(X_treino, y_treino)
probabilidades = modelo.predict_proba(X_validacao)[:, 1]
```

**Erro comum:** interpretar a magnitude bruta de coeficientes de variáveis em escalas diferentes.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-051-regressao-logistica.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

## Núcleo essencial

1. [ ] Implemente regressão logística em dados sintéticos e interprete probabilidade e log-odds em nível conceitual.
2. [ ] Treine no churn com pipeline completa e obtenha probabilidades, não apenas classes.
3. [ ] Interprete sinal e magnitude de cinco coeficientes após padronização.

## Prática obrigatória

- [ ] Compare regressão logística com `DummyClassifier` e regra simples.
- [ ] Teste multicolinearidade e regularização; documente estabilidade dos coeficientes.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-051-regressao-logistica.ipynb`:** Treine a logística com C=0,1 e C=10 no mesmo split e compare cinco coeficientes padronizados.
- [ ] **Em `01-exercicios/dia-051-regressao-logistica.ipynb`:** Avalie probabilidades no grupo chamados_90d>=3 e compare a média com o grupo chamados_90d<3.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

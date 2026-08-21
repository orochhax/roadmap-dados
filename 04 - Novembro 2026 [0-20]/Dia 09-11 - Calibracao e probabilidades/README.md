# Calibração e probabilidades

## Aprenda agora

Um modelo calibrado atribui cerca de 70% de positivos aos casos previstos com probabilidade 0,70. Brier Score é a média de `(probabilidade - resultado)²`; menor é melhor.

```python
from sklearn.calibration import CalibratedClassifierCV
from sklearn.metrics import brier_score_loss

calibrado = CalibratedClassifierCV(modelo_base, method="sigmoid", cv=5).fit(X_treino, y_treino)
prob = calibrado.predict_proba(X_validacao)[:, 1]
print(brier_score_loss(y_validacao, prob))
```

**Erro comum:** calibrar e avaliar nas mesmas observações, produzindo uma estimativa otimista.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-053-calibracao-e-probabilidades.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

## Núcleo essencial

1. [ ] Crie gráfico de calibração e calcule Brier Score para a regressão logística e para uma cópia de suas probabilidades elevada ao quadrado.
2. [ ] Agrupe probabilidades em decis e compare previsão média com frequência real.
3. [ ] Aplique `CalibratedClassifierCV` com métodos sigmoid e isotonic.

## Prática obrigatória

- [ ] Compare discriminação e calibração antes/depois.
- [ ] Explique por que uma probabilidade mal calibrada prejudica política de crédito ou retenção.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-053-calibracao-e-probabilidades.ipynb`:** Crie probabilidades artificialmente confiantes elevando-as ao quadrado e compare Brier Score e curva de calibração.
- [ ] **Em `01-exercicios/dia-053-calibracao-e-probabilidades.ipynb`:** Calcule calibração separadamente para planos Básico 100 e Família 500 e registre o tamanho de cada grupo.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

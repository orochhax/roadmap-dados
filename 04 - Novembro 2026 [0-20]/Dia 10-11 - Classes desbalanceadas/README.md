# Classes desbalanceadas

## Aprenda agora

Desbalanceamento ocorre quando uma classe é rara. Peso de classe altera a perda; under/oversampling altera apenas o conjunto de treino.

```python
modelo = LogisticRegression(class_weight="balanced", max_iter=1000)
modelo.fit(X_treino, y_treino)
```

**Erro comum:** reamostrar antes do split e deixar cópias ou informação sintética vazarem para validação.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-054-classes-desbalanceadas.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

## Núcleo essencial

1. [ ] Meça a proporção de classes e crie baseline que sempre prevê a maioria.
2. [ ] Compare `class_weight='balanced'`, undersampling e oversampling apenas no treino.
3. [ ] Evite aplicar reamostragem antes do split; demonstre como isso vaza informação.

## Prática obrigatória

- [ ] Avalie PR-AUC, recall da minoria, precision e custo.
- [ ] Escolha abordagem final e registre impactos colaterais.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-054-classes-desbalanceadas.ipynb`:** Crie uma amostra com apenas 5% de churn e compare accuracy e PR-AUC com a base original.
- [ ] **Em `01-exercicios/dia-054-classes-desbalanceadas.ipynb`:** Aplique oversampling somente no treino e confirme que a proporção do conjunto de validação permanece inalterada.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

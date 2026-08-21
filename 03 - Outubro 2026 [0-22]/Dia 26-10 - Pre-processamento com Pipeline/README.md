# Pré-processamento com Pipeline

## Aprenda agora

`ColumnTransformer` aplica transformações por tipo de coluna; `Pipeline` ajusta transformação e estimador somente com treino. A regressão logística será usada aqui apenas como estimador binário, sem interpretar coeficientes.

```python
preparo = ColumnTransformer([
    ("num", SimpleImputer(strategy="median"), colunas_numericas),
    ("cat", OneHotEncoder(handle_unknown="ignore"), colunas_categoricas),
])
modelo = Pipeline([("preparo", preparo), ("classificador", LogisticRegression(max_iter=1000))])
modelo.fit(X_treino, y_treino)
```

**Erro comum:** executar `fit_transform` na base completa antes de separar treino e validação.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-043-pre-processamento-com-pipeline.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

## Núcleo essencial

1. [ ] Identifique colunas numéricas e categóricas e faça um primeiro `fit/predict` guiado com `DummyClassifier`.
2. [ ] Construa um `ColumnTransformer` mínimo com imputação e one-hot encoding e conecte-o a uma regressão logística usada apenas como baseline.
3. [ ] Confirme no código que `fit` recebe somente o conjunto de treino e compare a saída do baseline com o Dummy.

## Prática obrigatória

- [ ] Adicione padronização somente para as colunas numéricas que precisam dela.
- [ ] Teste uma categoria inédita com `handle_unknown='ignore'` e outra linha com mensalidade ausente, sem reajustar a pipeline.
- [ ] Salve com `joblib.dump(modelo, "pipeline.joblib")`, recarregue com `joblib.load()` e confirme que as previsões antes e depois são iguais.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

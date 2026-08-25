# Pre-processamento com Pipeline + Metricas de classificacao

**Data de estudo:** 13/10/2026  
**Carga planejada:** 4 a 5 horas

## Aulas selecionadas no YouTube

Trilha **Machine Learning — Téo Me Why**:

- [ ] **Machine Learning 14: Métricas de ajuste - Introdução** (28:04) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=Machine+Learning+14+Metricas+de+ajuste+Introducao+Teo+Me+Why).
- [ ] **Machine Learning 15: Métricas de ajuste (Matriz de Confusão)** (1:04:49) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=Machine+Learning+15+Metricas+de+ajuste+Matriz+de+Confusao+Teo+Me+Why).

**Carga de vídeo selecionada:** aproximadamente 1h33.

**Prática obrigatória:** calcule e interprete as métricas nos mesmos dados e splits dos notebooks. Não escolha modelo apenas pela métrica mostrada em aula.

## Atividades do dia

### Atividade 1 — Pre-processamento com Pipeline

#### O que pesquisar
- `Pre-processamento com Pipeline engenharia de dados e MLOps explicado passo a passo`
- `Pre-processamento com Pipeline engenharia de dados e MLOps exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-pre-processamento-com-pipeline`](<atividades/01-pre-processamento-com-pipeline/>)

#### O que você precisa entender

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

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-pre-processamento-com-pipeline/dia-043-pre-processamento-com-pipeline.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que fazer

- [ ] Identifique colunas numéricas e categóricas e faça um primeiro `fit/predict` guiado com `DummyClassifier`.
- [ ] Construa um `ColumnTransformer` mínimo com imputação e one-hot encoding e conecte-o a uma regressão logística usada apenas como baseline.
- [ ] Confirme no código que `fit` recebe somente o conjunto de treino e compare a saída do baseline com o Dummy.

- [ ] Adicione padronização somente para as colunas numéricas que precisam dela.
- [ ] Teste uma categoria inédita com `handle_unknown='ignore'` e outra linha com mensalidade ausente, sem reajustar a pipeline.
- [ ] Salve com `joblib.dump(modelo, "pipeline.joblib")`, recarregue com `joblib.load()` e confirme que as previsões antes e depois são iguais.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

### Atividade 2 — Metricas de classificacao

#### O que pesquisar
- `Metricas de classificacao Python explicado passo a passo`
- `Metricas de classificacao Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-metricas-de-classificacao`](<atividades/02-metricas-de-classificacao/>)

#### O que você precisa entender

`precision = TP / (TP + FP)`, `recall = TP / (TP + FN)` e `F1` é a média harmônica das duas. ROC-AUC e PR-AUC usam escores contínuos; PR-AUC é especialmente informativa quando a classe positiva é rara.

```python
from sklearn.metrics import classification_report, roc_auc_score, average_precision_score

print(classification_report(y_validacao, classes_previstas))
print(roc_auc_score(y_validacao, escores), average_precision_score(y_validacao, escores))
```

**Erro comum:** usar apenas accuracy quando prever sempre a classe majoritária já produz valor alto.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-metricas-de-classificacao/dia-044-metricas-de-classificacao.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que fazer

- [ ] Calcule matriz de confusão, accuracy, precision, recall, F1, ROC-AUC e PR-AUC para dois modelos ou regras.
- [ ] Crie manualmente uma matriz com TN=700, FP=200, FN=30, TP=70 e calcule todas as métricas.
- [ ] Explique qual métrica priorizaria quando perder um churn custa R$500 e abordar indevidamente custa R$20.

- [ ] Plote curvas ROC e Precision-Recall; compare interpretação em classe desbalanceada.
- [ ] Escolha uma métrica primária e duas guardrails e registre justificativa.
- [ ] **Em `atividades/02-metricas-de-classificacao/dia-044-metricas-de-classificacao.ipynb`:** Calcule o custo da matriz TN=700, FP=200, FN=30, TP=70 usando FN=R$500 e FP=R$20.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

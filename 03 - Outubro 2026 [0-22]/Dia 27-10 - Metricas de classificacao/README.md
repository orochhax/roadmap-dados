# Métricas de classificação

## Aprenda agora

`precision = TP / (TP + FP)`, `recall = TP / (TP + FN)` e `F1` é a média harmônica das duas. ROC-AUC e PR-AUC usam escores contínuos; PR-AUC é especialmente informativa quando a classe positiva é rara.

```python
from sklearn.metrics import classification_report, roc_auc_score, average_precision_score

print(classification_report(y_validacao, classes_previstas))
print(roc_auc_score(y_validacao, escores), average_precision_score(y_validacao, escores))
```

**Erro comum:** usar apenas accuracy quando prever sempre a classe majoritária já produz valor alto.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-044-metricas-de-classificacao.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

## Núcleo essencial

1. [ ] Calcule matriz de confusão, accuracy, precision, recall, F1, ROC-AUC e PR-AUC para dois modelos ou regras.
2. [ ] Crie manualmente uma matriz com TN=700, FP=200, FN=30, TP=70 e calcule todas as métricas.
3. [ ] Explique qual métrica priorizaria quando perder um churn custa R$500 e abordar indevidamente custa R$20.

## Prática obrigatória

- [ ] Plote curvas ROC e Precision-Recall; compare interpretação em classe desbalanceada.
- [ ] Escolha uma métrica primária e duas guardrails e registre justificativa.
- [ ] **Em `01-exercicios/dia-044-metricas-de-classificacao.ipynb`:** Calcule o custo da matriz TN=700, FP=200, FN=30, TP=70 usando FN=R$500 e FP=R$20.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

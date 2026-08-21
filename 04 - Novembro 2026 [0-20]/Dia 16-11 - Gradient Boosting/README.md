# Gradient Boosting

## Aprenda agora

Boosting adiciona árvores sequencialmente para corrigir erros anteriores. `learning_rate` reduz a contribuição de cada árvore e interage com `n_estimators`.

```python
from sklearn.ensemble import GradientBoostingClassifier

modelo = GradientBoostingClassifier(
    learning_rate=0.05, n_estimators=200, max_depth=2, random_state=42
).fit(X_treino, y_treino)
```

**Erro comum:** testar muitas combinações e escolher pela mesma validação sem controlar overfitting de tuning.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-058-gradient-boosting.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.
- **Dependência obrigatória:** `xgboost`. Se a instalação local falhar, execute a atividade em um ambiente compatível, como Google Colab ou Databricks, e registre o ambiente e a versão utilizados.

## Núcleo essencial

1. [ ] Treine `GradientBoostingClassifier` como referência e `XGBClassifier` usando exatamente o mesmo split e pré-processamento.
2. [ ] No XGBoost, compare uma grade pequena de `learning_rate`, `n_estimators` e `max_depth`; registre métrica, tempo de treino e tempo de inferência.
3. [ ] Compare treino e validação para identificar overfitting e salve todas as execuções em `resultados_boosting.csv`.
4. [ ] Registre em `versoes.json` as versões das bibliotecas, a seed, os parâmetros finais e o comando usado para executar o notebook.

## Prática obrigatória

- [ ] Analise importância e erros por segmento.
- [ ] Documente por que boosting pode ganhar em dados tabulares e quais riscos de tuning existem.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-058-gradient-boosting.ipynb`:** Compare learning_rate 0,05 com 0,20 usando 100 e 300 estimadores no mesmo split.
- [ ] **Em `01-exercicios/dia-058-gradient-boosting.ipynb`:** Calcule a métrica separadamente para clientes com até 6 meses e acima de 24 meses de relacionamento.

## Concluído quando

- [ ] O notebook executa um treino real de XGBoost e contém todos os itens do Núcleo essencial.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

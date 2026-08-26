# Gradient Boosting

**Data de estudo:** 03/12/2026
**Carga planejada:** 2 a 4 horas

## Aulas selecionadas no YouTube

Assista nesta ordem:

- [ ] **XGBoost na Prática | Aula 1** (13:33) — [abrir no YouTube](https://www.youtube.com/watch?v=fG8H-0rb0mY).
- [ ] **XGBoost na Prática | Aula 2** (30:23) — [abrir no YouTube](https://www.youtube.com/watch?v=vp7sAKlf7FU).

**Carga de vídeo selecionada:** aproximadamente 44 minutos.

**Prática obrigatória:** execute o benchmark real com XGBoost, registre versões, parâmetros, métricas, tempo e erros por segmento. Assistir às aulas não substitui o notebook.

## Atividades do dia

### Atividade 1 — Gradient Boosting

#### O que pesquisar
- `Gradient Boosting machine learning com Python explicado passo a passo`
- `Gradient Boosting machine learning com Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-gradient-boosting`](<atividades/01-gradient-boosting/>)

#### O que você precisa entender

Boosting adiciona árvores sequencialmente para corrigir erros anteriores. `learning_rate` reduz a contribuição de cada árvore e interage com `n_estimators`.

```python
from sklearn.ensemble import GradientBoostingClassifier

modelo = GradientBoostingClassifier(
    learning_rate=0.05, n_estimators=200, max_depth=2, random_state=42
).fit(X_treino, y_treino)
```

**Erro comum:** testar muitas combinações e escolher pela mesma validação sem controlar overfitting de tuning.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-gradient-boosting/dia-058-gradient-boosting.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.
- **Dependência obrigatória:** `xgboost`. Se a instalação local falhar, execute a atividade em um ambiente compatível, como Google Colab ou Databricks, e registre o ambiente e a versão utilizados.

#### O que fazer

- [ ] Treine `GradientBoostingClassifier` como referência e `XGBClassifier` usando exatamente o mesmo split e pré-processamento.
- [ ] No XGBoost, compare uma grade pequena de `learning_rate`, `n_estimators` e `max_depth`; registre métrica, tempo de treino e tempo de inferência.
- [ ] Compare treino e validação para identificar overfitting e salve todas as execuções em `resultados_boosting.csv`.
- [ ] Registre em `versoes.json` as versões das bibliotecas, a seed, os parâmetros finais e o comando usado para executar o notebook.

- [ ] Analise importância e erros por segmento.
- [ ] Documente por que boosting pode ganhar em dados tabulares e quais riscos de tuning existem.


- [ ] **Em `atividades/01-gradient-boosting/dia-058-gradient-boosting.ipynb`:** Compare learning_rate 0,05 com 0,20 usando 100 e 300 estimadores no mesmo split.
- [ ] **Em `atividades/01-gradient-boosting/dia-058-gradient-boosting.ipynb`:** Calcule a métrica separadamente para clientes com até 6 meses e acima de 24 meses de relacionamento.

#### Como validar

- O notebook executa um treino real de XGBoost e contém todos os requisitos principais da atividade.
- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

# Calibracao e probabilidades + Classes desbalanceadas

**Data de estudo:** 21/10/2026  
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Calibracao e probabilidades

#### O que pesquisar
- `Calibracao e probabilidades estatística para data science explicado passo a passo`
- `Calibracao e probabilidades estatística para data science exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-calibracao-e-probabilidades`](<atividades/01-calibracao-e-probabilidades/>)

#### O que você precisa entender

Um modelo calibrado atribui cerca de 70% de positivos aos casos previstos com probabilidade 0,70. Brier Score é a média de `(probabilidade - resultado)²`; menor é melhor.

```python
from sklearn.calibration import CalibratedClassifierCV
from sklearn.metrics import brier_score_loss

calibrado = CalibratedClassifierCV(modelo_base, method="sigmoid", cv=5).fit(X_treino, y_treino)
prob = calibrado.predict_proba(X_validacao)[:, 1]
print(brier_score_loss(y_validacao, prob))
```

**Erro comum:** calibrar e avaliar nas mesmas observações, produzindo uma estimativa otimista.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-calibracao-e-probabilidades/dia-053-calibracao-e-probabilidades.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que fazer

- [ ] Crie gráfico de calibração e calcule Brier Score para a regressão logística e para uma cópia de suas probabilidades elevada ao quadrado.
- [ ] Agrupe probabilidades em decis e compare previsão média com frequência real.
- [ ] Aplique `CalibratedClassifierCV` com métodos sigmoid e isotonic.

- [ ] Compare discriminação e calibração antes/depois.
- [ ] Explique por que uma probabilidade mal calibrada prejudica política de crédito ou retenção.


- [ ] **Em `atividades/01-calibracao-e-probabilidades/dia-053-calibracao-e-probabilidades.ipynb`:** Crie probabilidades artificialmente confiantes elevando-as ao quadrado e compare Brier Score e curva de calibração.
- [ ] **Em `atividades/01-calibracao-e-probabilidades/dia-053-calibracao-e-probabilidades.ipynb`:** Calcule calibração separadamente para planos Básico 100 e Família 500 e registre o tamanho de cada grupo.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

### Atividade 2 — Classes desbalanceadas

#### O que pesquisar
- `Classes desbalanceadas Python explicado passo a passo`
- `Classes desbalanceadas Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-classes-desbalanceadas`](<atividades/02-classes-desbalanceadas/>)

#### O que você precisa entender

Desbalanceamento ocorre quando uma classe é rara. Peso de classe altera a perda; under/oversampling altera apenas o conjunto de treino.

```python
modelo = LogisticRegression(class_weight="balanced", max_iter=1000)
modelo.fit(X_treino, y_treino)
```

**Erro comum:** reamostrar antes do split e deixar cópias ou informação sintética vazarem para validação.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-classes-desbalanceadas/dia-054-classes-desbalanceadas.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que fazer

- [ ] Meça a proporção de classes e crie baseline que sempre prevê a maioria.
- [ ] Compare `class_weight='balanced'`, undersampling e oversampling apenas no treino.
- [ ] Evite aplicar reamostragem antes do split; demonstre como isso vaza informação.

- [ ] Avalie PR-AUC, recall da minoria, precision e custo.
- [ ] Escolha abordagem final e registre impactos colaterais.


- [ ] **Em `atividades/02-classes-desbalanceadas/dia-054-classes-desbalanceadas.ipynb`:** Crie uma amostra com apenas 5% de churn e compare accuracy e PR-AUC com a base original.
- [ ] **Em `atividades/02-classes-desbalanceadas/dia-054-classes-desbalanceadas.ipynb`:** Aplique oversampling somente no treino e confirme que a proporção do conjunto de validação permanece inalterada.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

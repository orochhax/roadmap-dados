# Regressao logistica + Limiar e custo

**Data de estudo:** 20/10/2026  
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Regressao logistica

#### O que pesquisar
- `Regressao logistica machine learning com Python explicado passo a passo`
- `Regressao logistica machine learning com Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-regressao-logistica`](<atividades/01-regressao-logistica/>)

#### O que você precisa entender

Regressão logística modela a probabilidade da classe positiva: `p = 1 / (1 + exp(-z))`. Após padronização, o sinal do coeficiente indica a direção da associação com o log-odds.

```python
from sklearn.linear_model import LogisticRegression

modelo = LogisticRegression(max_iter=1000).fit(X_treino, y_treino)
probabilidades = modelo.predict_proba(X_validacao)[:, 1]
```

**Erro comum:** interpretar a magnitude bruta de coeficientes de variáveis em escalas diferentes.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-regressao-logistica/dia-051-regressao-logistica.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que fazer

- [ ] Implemente regressão logística em dados sintéticos e interprete probabilidade e log-odds em nível conceitual.
- [ ] Treine no churn com pipeline completa e obtenha probabilidades, não apenas classes.
- [ ] Interprete sinal e magnitude de cinco coeficientes após padronização.

- [ ] Compare regressão logística com `DummyClassifier` e regra simples.
- [ ] Teste multicolinearidade e regularização; documente estabilidade dos coeficientes.


- [ ] **Em `atividades/01-regressao-logistica/dia-051-regressao-logistica.ipynb`:** Treine a logística com C=0,1 e C=10 no mesmo split e compare cinco coeficientes padronizados.
- [ ] **Em `atividades/01-regressao-logistica/dia-051-regressao-logistica.ipynb`:** Avalie probabilidades no grupo chamados_90d>=3 e compare a média com o grupo chamados_90d<3.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

### Atividade 2 — Limiar e custo

#### O que pesquisar
- `Limiar e custo Python explicado passo a passo`
- `Limiar e custo Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-limiar-e-custo`](<atividades/02-limiar-e-custo/>)

#### O que você precisa entender

O limiar converte probabilidade em decisão. Para cada limiar, calcule `custo = FN×custo_FN + FP×custo_FP + TP×custo_TP` e aplique restrições de negócio.

```python
limiar = 0.30
predito = (probabilidades >= limiar).astype(int)
custo = fn * 500 + fp * 20 + tp * 80
```

**Erro comum:** escolher o limiar no conjunto de teste ou ignorar o volume de ações gerado.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-limiar-e-custo/dia-052-limiar-e-custo.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que fazer

- [ ] Calcule previsões para limiares 0.2, 0.3, 0.5, 0.7 e 0.8.
- [ ] Para cada limiar, registre TP, FP, FN, TN, precision, recall e custo total.
- [ ] Use custos definidos: FN=R$500, FP=R$20, TP=R$80 de campanha e benefício esperado de R$300.

- [ ] Escolha o limiar de menor custo respeitando recall mínimo de 70%.
- [ ] Crie gráfico custo versus limiar e escreva recomendação executiva.


- [ ] **Em `atividades/02-limiar-e-custo/dia-052-limiar-e-custo.ipynb`:** Refaça a tabela de limiares aumentando o custo de FP de R$20 para R$50 e mantenha os demais valores.
- [ ] **Em `atividades/02-limiar-e-custo/dia-052-limiar-e-custo.ipynb`:** Escolha novamente o limiar exigindo recall mínimo de 80% em vez de 70% e registre a troca de custo e volume.
- [ ] Compare especificamente os limiares 0,35 e 0,50 no mesmo conjunto e registre precision, recall e custo para cada um.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

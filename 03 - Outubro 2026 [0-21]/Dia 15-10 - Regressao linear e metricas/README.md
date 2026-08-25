# Regressao linear + Metricas de regressao

**Data de estudo:** 15/10/2026  
**Carga planejada:** 4 a 5 horas

## Aulas selecionadas no YouTube

Trilha **Machine Learning — Téo Me Why**:

- [ ] **Machine Learning 07: Regressão Linear** (31:45) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=Machine+Learning+07+Regressao+Linear+Teo+Me+Why).
- [ ] **Machine Learning 09: Prática no Python (Reg. Linear e Árvore)** (28:20) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=Machine+Learning+09+Pratica+no+Python+Reg+Linear+e+Arvore+Teo+Me+Why).

**Carga de vídeo selecionada:** aproximadamente 1h.

**Prática obrigatória:** ajuste, diagnostique e compare os modelos nos notebooks do dia; reproduzir apenas o código do vídeo não conclui a sessão.

## Atividades do dia

### Atividade 1 — Regressao linear

#### O que pesquisar
- `Regressao linear machine learning com Python explicado passo a passo`
- `Regressao linear machine learning com Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-regressao-linear`](<atividades/01-regressao-linear/>)

#### O que você precisa entender

Regressão linear estima `y = intercepto + soma(coeficiente × variável)`. Resíduo é `y_real - y_previsto`; padrões nos resíduos indicam limitações do modelo.

```python
from sklearn.linear_model import LinearRegression

modelo = LinearRegression().fit(X_treino, y_treino)
predicao = modelo.predict(X_validacao)
residuos = y_validacao - predicao
```

**Erro comum:** interpretar coeficiente como efeito causal sem controlar desenho, confundidores e suposições.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-regressao-linear/dia-046-regressao-linear.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que fazer

- [ ] Crie dados sintéticos lineares `y = 3x + 5 + ruído` e ajuste regressão linear.
- [ ] Recupere coeficiente e intercepto; compare com valores reais usados na geração.
- [ ] Use `pedidos.csv` para prever valor do pedido com variáveis permitidas.

- [ ] Plote resíduos versus predição e distribuição dos resíduos.
- [ ] Crie uma relação não linear e demonstre por que regressão linear simples falha.
- [ ] **Em `atividades/01-regressao-linear/dia-046-regressao-linear.ipynb`:** Separe os pedidos acima do percentil 90 e compare o erro desse grupo com o restante.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

### Atividade 2 — Metricas de regressao

#### O que pesquisar
- `Metricas de regressao machine learning com Python explicado passo a passo`
- `Metricas de regressao machine learning com Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-metricas-de-regressao`](<atividades/02-metricas-de-regressao/>)

#### O que você precisa entender

MAE é o erro absoluto médio; RMSE dá peso maior a erros grandes; `R²` compara com a previsão pela média; MAPE divide pelo valor real e falha quando ele é zero.

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

mae = mean_absolute_error(y_real, y_previsto)
rmse = mean_squared_error(y_real, y_previsto) ** 0.5
r2 = r2_score(y_real, y_previsto)
```

**Erro comum:** comparar métricas calculadas em conjuntos ou escalas diferentes.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-metricas-de-regressao/dia-047-metricas-de-regressao.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que fazer

- [ ] No notebook, use `y_real = [100, 120, 80, 0, 200]` e `y_previsto = [90, 135, 70, 10, 180]` para calcular MAE, MSE, RMSE, R² e MAPE manualmente e com biblioteca.
- [ ] Crie um caso com valor real zero e mostre por que MAPE pode quebrar.
- [ ] Compare dois modelos: um com poucos erros grandes e outro com muitos erros pequenos.

- [ ] Escolha a métrica mais coerente para previsão de receita e justifique custo dos erros.
- [ ] Crie intervalo de erro por faixa de valor e verifique se o modelo piora nos pedidos maiores.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

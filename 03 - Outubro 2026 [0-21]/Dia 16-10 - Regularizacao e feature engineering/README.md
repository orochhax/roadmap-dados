# Regularizacao + Feature engineering para regressao

**Data de estudo:** 16/10/2026  
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Regularizacao

#### O que pesquisar
- `Regularizacao Python explicado passo a passo`
- `Regularizacao Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-regularizacao`](<atividades/01-regularizacao/>)

#### O que você precisa entender

Ridge adiciona penalidade L2 e reduz coeficientes; Lasso usa L1 e pode zerá-los. `alpha` controla a força da penalidade, por isso as variáveis devem estar na mesma escala.

```python
from sklearn.linear_model import Ridge, Lasso

ridge = Ridge(alpha=1.0).fit(X_treino_padronizado, y_treino)
lasso = Lasso(alpha=0.1).fit(X_treino_padronizado, y_treino)
```

**Erro comum:** comparar coeficientes regularizados de variáveis em escalas muito diferentes.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-regularizacao/dia-048-regularizacao.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que fazer

- [ ] Treine regressão linear, Ridge e Lasso no mesmo conjunto padronizado.
- [ ] Varie `alpha` em pelo menos seis valores e registre coeficientes e métricas.
- [ ] Crie features altamente correlacionadas para observar instabilidade da regressão comum.

- [ ] Mostre quais coeficientes o Lasso zera e quando isso não significa causalidade.
- [ ] Escolha um modelo equilibrando erro, estabilidade e interpretação.


- [ ] **Em `atividades/01-regularizacao/dia-048-regularizacao.ipynb`:** Compare Ridge e Lasso com alpha 0,01 e 10, mantendo split e escala iguais, e registre coeficientes e RMSE.
- [ ] **Em `atividades/01-regularizacao/dia-048-regularizacao.ipynb`:** Duplique uma feature numérica com ruído mínimo e verifique como os coeficientes mudam nos três modelos.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

### Atividade 2 — Feature engineering para regressao

#### O que pesquisar
- `Feature engineering para regressao machine learning com Python explicado passo a passo`
- `Feature engineering para regressao machine learning com Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-feature-engineering-para-regressao`](<atividades/02-feature-engineering-para-regressao/>)

#### O que você precisa entender

Feature engineering transforma dados disponíveis em sinais reproduzíveis. `log1p` reduz assimetria, interação combina efeitos e ablação mede a contribuição de um grupo de features.

```python
df["log_valor"] = np.log1p(df["valor"])
df["desconto_app"] = df["desconto"] * (df["canal"] == "app").astype(int)
```

**Erro comum:** criar uma feature com informação posterior ao momento da previsão ou fora da pipeline aplicada em produção.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-feature-engineering-para-regressao/dia-049-feature-engineering-para-regressao.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que fazer

- [ ] Crie features de data: mês, dia da semana, fim de semana e dias desde primeira compra.
- [ ] Crie transformações `log1p` para variável assimétrica e interações entre desconto e canal.
- [ ] Agrupe categorias raras com limiar explícito e documente impacto.

- [ ] Construa cada feature dentro da pipeline para evitar diferenças entre treino e inferência.
- [ ] Faça ablação: remova grupos de features e registre quanto cada grupo muda a métrica.


- [ ] **Em `atividades/02-feature-engineering-para-regressao/dia-049-feature-engineering-para-regressao.ipynb`:** Agrupe categorias com frequência abaixo de 1% e depois abaixo de 5%; compare número de colunas e MAE.
- [ ] **Em `atividades/02-feature-engineering-para-regressao/dia-049-feature-engineering-para-regressao.ipynb`:** Remova somente as features de interação e registre a variação da métrica no mesmo conjunto de validação.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

## Publicação da semana no LinkedIn

- **Tema específico:** por que um baseline e um pipeline sem vazamento vêm antes de regularização e feature engineering.
- **Tipo:** progresso.
- **Formato:** carrossel com diagrama do pipeline, tabela de baseline versus regressão e um exemplo controlado de leakage.
- **Artefato/evidência exigida:** split congelado, Dummy/regra/modelo linear no mesmo conjunto, pipeline de pré-processamento, experimento de vazamento, métricas apropriadas e análise de erros produzidos nos exercícios de 13–16/10.

### Roteiro para preencher

- **Problema e alvo:** [o que foi previsto e em qual momento?]
- **Split:** [como treino, validação e teste foram separados?]
- **Baseline:** [qual referência simples o modelo precisa superar?]
- **Pipeline/features:** [quais transformações foram ajustadas somente no treino?]
- **Regularização:** [qual hipótese foi testada e qual resultado ocorreu?]
- **Leakage controlado:** [qual sinal indevido alterou a métrica e como foi removido?]
- **Próximo passo:** [o que ainda falta para o benchmark de 28/10?]

### Limitação obrigatória

Declare que os resultados são intermediários, dependem do split e ainda não incluem a comparação completa entre modelos, custo e slices.

### Cuidado contra afirmações falsas

Não chame a maior métrica de melhor solução sem baseline, teste congelado e análise de erro. Não declare Machine Learning dominado nem altere headline/Competências por um post de progresso.

### Checklist de publicação

- [ ] Usei o mesmo split e a mesma métrica em todas as comparações mostradas.
- [ ] Ajustei transformações somente no treino.
- [ ] Mantive o baseline visível e identifiquei o experimento de leakage.
- [ ] Registrei um erro e uma limitação.
- [ ] Removi dados sensíveis e conferi a evidência compartilhada.
- [ ] **URL publicada:**
- [ ] **Data da publicação:**

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

# Arvore de decisao + Random Forest

**Data de estudo:** 23/10/2026  
**Carga planejada:** 4 a 5 horas

## Aulas selecionadas no YouTube

- [ ] **O que é ENTROPIA? | Data Science Descomplicado** (6:24) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=O+que+e+ENTROPIA+Data+Science+Descomplicado).
- [ ] **Machine Learning 11: Árvore de Decisão (Classificação)** (25:36), da trilha **Machine Learning — Téo Me Why** — [pesquisar no YouTube](https://www.youtube.com/results?search_query=Machine+Learning+11+Arvore+de+Decisao+Classificacao+Teo+Me+Why).

**Carga de vídeo selecionada:** 32 minutos.

**Prática obrigatória:** use as aulas para entender impureza e divisões. O treino com várias profundidades, a análise de overfitting e a comparação com Random Forest continuam obrigatórios.

## Atividades do dia

### Atividade 1 — Arvore de decisao

#### O que pesquisar
- `Arvore de decisao Python explicado passo a passo`
- `Arvore de decisao Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-arvore-de-decisao`](<atividades/01-arvore-de-decisao/>)

#### O que você precisa entender

Uma árvore divide os dados por regras até chegar a folhas. Profundidade e `min_samples_leaf` controlam complexidade e risco de overfitting.

```python
from sklearn.tree import DecisionTreeClassifier

arvore = DecisionTreeClassifier(max_depth=3, min_samples_leaf=20, random_state=42)
arvore.fit(X_treino, y_treino)
```

**Erro comum:** escolher a árvore pela métrica de treino e ignorar a queda na validação.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-arvore-de-decisao/dia-056-arvore-de-decisao.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que fazer

- [ ] Treine árvore de decisão com profundidades 1, 3, 5, 10 e sem limite.
- [ ] Visualize uma árvore pequena e traduza cinco divisões em regras de negócio.
- [ ] Compare desempenho de treino e validação para identificar overfitting.

- [ ] Varie `min_samples_leaf` e registre estabilidade.
- [ ] Crie uma árvore deliberadamente complexa e explique por que não deve ser usada apesar da métrica de treino.


- [ ] **Em `atividades/01-arvore-de-decisao/dia-056-arvore-de-decisao.ipynb`:** Compare profundidade 3 e 10 com min_samples_leaf=20 no mesmo split e registre treino e validação.
- [ ] **Em `atividades/01-arvore-de-decisao/dia-056-arvore-de-decisao.ipynb`:** Escolha uma previsão errada da árvore profunda e escreva as regras percorridas até a folha.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

### Atividade 2 — Random Forest

#### O que pesquisar
- `Random Forest machine learning com Python explicado passo a passo`
- `Random Forest machine learning com Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-random-forest`](<atividades/02-random-forest/>)

#### O que você precisa entender

Random Forest combina muitas árvores treinadas com amostras e subconjuntos de features. Permutation importance mede a queda da métrica ao embaralhar uma feature.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance

floresta = RandomForestClassifier(n_estimators=200, max_depth=8, random_state=42).fit(X_treino, y_treino)
importancia = permutation_importance(floresta, X_validacao, y_validacao, random_state=42)
```

**Erro comum:** interpretar importância como causalidade ou compará-la entre conjuntos de validação diferentes.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-random-forest/dia-057-random-forest.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que fazer

- [ ] Treine Random Forest variando número de árvores, profundidade e número de features.
- [ ] Compare variância de uma árvore única com a floresta em cinco seeds.
- [ ] Calcule importância por impureza e permutation importance; compare rankings.

- [ ] Meça tempo e tamanho do modelo.
- [ ] Escolha configuração considerando desempenho, estabilidade e custo de inferência.


- [ ] **Em `atividades/02-random-forest/dia-057-random-forest.ipynb`:** Compare 50 e 300 árvores em cinco seeds, mantendo as demais configurações, e registre média e desvio da métrica.
- [ ] **Em `atividades/02-random-forest/dia-057-random-forest.ipynb`:** Calcule permutation importance para a melhor configuração e compare as cinco primeiras com a importância por impureza.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

## Publicação da semana no LinkedIn

- **Tema específico:** por que o limiar de decisão e o custo podem importar mais que escolher entre regressão logística, árvore e Random Forest.
- **Tipo:** progresso.
- **Formato:** carrossel com curva/tabela de limiares, três políticas de decisão e comparação curta dos modelos.
- **Artefato/evidência exigida:** probabilidades calibradas, restrição de capacidade, custo de falsos positivos/negativos, políticas conservadora/equilibrada/agressiva, caso de decisão e modelos avaliados no mesmo split durante 19–23/10.

### Roteiro para preencher

- **Decisão:** [quem recebe a ação e qual é a capacidade disponível?]
- **Probabilidade e calibração:** [como o score foi conferido?]
- **Custos:** [qual erro custa mais e por quê?]
- **Políticas:** [quais limiares/regras foram comparados?]
- **Resultado verificável:** [métrica/custo por política e caminho da evidência]
- **Modelo versus política:** [o que mudou ao trocar algoritmo e ao trocar limiar?]
- **Próximo passo:** [qual comparação ainda entra no benchmark final?]

### Limitação obrigatória

Explique que custos e capacidade foram definidos para o exercício e não representam valores observados em uma operação real.

### Cuidado contra afirmações falsas

Não use acurácia isolada para justificar ação nem trate probabilidade como certeza. Não declare economia ou retenção real. O post não antecipa Competências, Projeto em Destaques ou headline.

### Checklist de publicação

- [ ] Mantive split, população e métricas iguais nas comparações.
- [ ] Registrei capacidade, custos e limiares antes da leitura final.
- [ ] Conferi calibração e resultados por política.
- [ ] Mostrei um trade-off e uma limitação.
- [ ] Removi dados sensíveis e testei a evidência compartilhada.
- [ ] **URL publicada:**
- [ ] **Data da publicação:**

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

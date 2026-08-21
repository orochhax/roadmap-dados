# Random Forest

## Aprenda agora

Random Forest combina muitas árvores treinadas com amostras e subconjuntos de features. Permutation importance mede a queda da métrica ao embaralhar uma feature.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance

floresta = RandomForestClassifier(n_estimators=200, max_depth=8, random_state=42).fit(X_treino, y_treino)
importancia = permutation_importance(floresta, X_validacao, y_validacao, random_state=42)
```

**Erro comum:** interpretar importância como causalidade ou compará-la entre conjuntos de validação diferentes.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-057-random-forest.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

## Núcleo essencial

1. [ ] Treine Random Forest variando número de árvores, profundidade e número de features.
2. [ ] Compare variância de uma árvore única com a floresta em cinco seeds.
3. [ ] Calcule importância por impureza e permutation importance; compare rankings.

## Prática obrigatória

- [ ] Meça tempo e tamanho do modelo.
- [ ] Escolha configuração considerando desempenho, estabilidade e custo de inferência.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-057-random-forest.ipynb`:** Compare 50 e 300 árvores em cinco seeds, mantendo as demais configurações, e registre média e desvio da métrica.
- [ ] **Em `01-exercicios/dia-057-random-forest.ipynb`:** Calcule permutation importance para a melhor configuração e compare as cinco primeiras com a importância por impureza.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

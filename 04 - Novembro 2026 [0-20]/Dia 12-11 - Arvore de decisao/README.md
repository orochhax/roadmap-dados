# Árvore de decisão

## Aprenda agora

Uma árvore divide os dados por regras até chegar a folhas. Profundidade e `min_samples_leaf` controlam complexidade e risco de overfitting.

```python
from sklearn.tree import DecisionTreeClassifier

arvore = DecisionTreeClassifier(max_depth=3, min_samples_leaf=20, random_state=42)
arvore.fit(X_treino, y_treino)
```

**Erro comum:** escolher a árvore pela métrica de treino e ignorar a queda na validação.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-056-arvore-de-decisao.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

## Núcleo essencial

1. [ ] Treine árvore de decisão com profundidades 1, 3, 5, 10 e sem limite.
2. [ ] Visualize uma árvore pequena e traduza cinco divisões em regras de negócio.
3. [ ] Compare desempenho de treino e validação para identificar overfitting.

## Prática obrigatória

- [ ] Varie `min_samples_leaf` e registre estabilidade.
- [ ] Crie uma árvore deliberadamente complexa e explique por que não deve ser usada apesar da métrica de treino.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-056-arvore-de-decisao.ipynb`:** Compare profundidade 3 e 10 com min_samples_leaf=20 no mesmo split e registre treino e validação.
- [ ] **Em `01-exercicios/dia-056-arvore-de-decisao.ipynb`:** Escolha uma previsão errada da árvore profunda e escreva as regras percorridas até a folha.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

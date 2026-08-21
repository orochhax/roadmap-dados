# Seleção de modelo

## Aprenda agora

Bootstrap reamostra, com reposição, os mesmos pares `y`/predição para estimar a estabilidade da diferença entre modelos.

```python
import numpy as np

rng = np.random.default_rng(42)
diferencas = []
for _ in range(200):
    idx = rng.integers(0, len(y_validacao), len(y_validacao))
    diferencas.append(metrica(y_validacao[idx], pred_a[idx]) - metrica(y_validacao[idx], pred_b[idx]))
ic95 = np.percentile(diferencas, [2.5, 97.5])
```

**Erro comum:** reamostrar cada modelo com índices diferentes e destruir a comparação pareada.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-059-selecao-de-modelo.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.
- **Entradas concretas:** `y_validacao` e, no mesmo conjunto, probabilidades ou previsões de cada candidato.
- **Fallback local:** se não houver previsões salvas, treine no próprio notebook `DummyClassifier`, regressão logística e `GradientBoostingClassifier` com a pipeline e o split fixos; guarde os três vetores de previsão.

## Núcleo essencial

1. [ ] Crie tabela única com todos os candidatos das entradas ou do fallback, usando a mesma validação e as mesmas métricas.
2. [ ] Defina critérios de escolha antes de olhar o vencedor: custo, recall, calibração, tempo, explicabilidade.
3. [ ] Use teste ou bootstrap para verificar estabilidade da diferença entre os dois melhores.

## Prática obrigatória

- [ ] Escolha modelo campeão e um challenger.
- [ ] Escreva decisão com trade-offs, não apenas ranking.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-059-selecao-de-modelo.ipynb`:** Refaça o ranking dando peso dobrado ao custo e depois peso dobrado à explicabilidade; registre se campeão e challenger mudam.
- [ ] **Em `01-exercicios/dia-059-selecao-de-modelo.ipynb`:** Use bootstrap com seed 42 para comparar os dois melhores em 200 reamostragens do conjunto de validação.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

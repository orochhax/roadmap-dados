# NumPy essencial

## Aprenda agora

Um `ndarray` armazena valores do mesmo tipo e aplica operações a todos eles sem laço explícito.

```python
import numpy as np

duracoes = np.array([30, 60, 120, 180])
acima_da_meta = duracoes > 90
ajustadas = np.where(acima_da_meta, duracoes * 0.9, duracoes)
print(np.median(ajustadas), np.percentile(ajustadas, [25, 75]))
```

**Erro comum:** usar `and`/`or` com arrays; combine máscaras com `&`/`|` e parênteses.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/numpy_essencial.ipynb`.
- **Dados:** `dados/incidentes.csv`, `dados/clientes_telecom.csv`, `dados/pedidos.csv` e `dados/metas_cidades.csv`.

## Núcleo essencial

1. [ ] Crie o array fornecido e calcule média, mediana, mínimo, máximo e percentis 25/75.
2. [ ] Crie uma matriz 4x3 e pratique seleção de linhas, colunas e fatias.
3. [ ] Use uma operação vetorizada para modificar valores acima de um limite e compare o resultado com um laço, sem medir desempenho ainda.

## Prática obrigatória

- [ ] Normalize uma coluna pelo método min-max e confira manualmente os valores mínimo e máximo produzidos.
- [ ] Teste `NaN`, array vazio e desvio zero e registre o comportamento de cada caso.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

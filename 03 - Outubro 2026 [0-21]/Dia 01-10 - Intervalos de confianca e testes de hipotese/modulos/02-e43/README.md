# Testes de hipótese

## Aprenda agora

`H0` representa ausência da diferença de interesse; `H1`, a diferença. O p-valor mede quão incompatíveis os dados são com `H0`, não o tamanho nem a importância do efeito.

```python
from scipy import stats

estatistica, p_valor = stats.ttest_ind(grupo_a, grupo_b, equal_var=False)
```

**Erro comum:** concluir que `p < 0,05` prova causalidade ou que `p >= 0,05` prova igualdade.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-037-testes-de-hipotese.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/incidentes.csv` e dados sintéticos gerados no notebook com seed 42.

## Núcleo essencial

1. [ ] Formule H0 e H1 para diferença de média de duração entre duas cidades.
2. [ ] Escolha e execute teste apropriado; verifique suposições e calcule tamanho de efeito.
3. [ ] Resolva um teste de proporções para taxa de churn entre dois planos.

## Prática obrigatória

- [ ] Crie cenários de erro tipo I e II com consequências de negócio.
- [ ] Escreva decisão usando significância, efeito, intervalo e custo, sem depender só de p-valor.
- [ ] **Em `01-exercicios/dia-037-testes-de-hipotese.ipynb`:** Acrescente um outlier de 1500 minutos a uma cidade, refaça suposições e tamanho de efeito e compare com a análise original.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

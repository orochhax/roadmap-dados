# Selecao de modelo

**Data de estudo:** 07/12/2026
**Carga planejada:** 2 a 4 horas

## Atividades do dia

### Atividade 1 — Selecao de modelo

#### O que pesquisar
- `Selecao de modelo machine learning com Python explicado passo a passo`
- `Selecao de modelo machine learning com Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-selecao-de-modelo`](<atividades/01-selecao-de-modelo/>)

#### O que você precisa entender

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

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-selecao-de-modelo/dia-059-selecao-de-modelo.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.
- **Entradas concretas:** `y_validacao` e, no mesmo conjunto, probabilidades ou previsões de cada candidato.
- **Fallback local:** se não houver previsões salvas, treine no próprio notebook `DummyClassifier`, regressão logística e `GradientBoostingClassifier` com a pipeline e o split fixos; guarde os três vetores de previsão.

#### O que fazer

- [ ] Crie tabela única com todos os candidatos das entradas ou do fallback, usando a mesma validação e as mesmas métricas.
- [ ] Defina critérios de escolha antes de olhar o vencedor: custo, recall, calibração, tempo, explicabilidade.
- [ ] Use teste ou bootstrap para verificar estabilidade da diferença entre os dois melhores.

- [ ] Escolha modelo campeão e um challenger.
- [ ] Escreva decisão com trade-offs, não apenas ranking.


- [ ] **Em `atividades/01-selecao-de-modelo/dia-059-selecao-de-modelo.ipynb`:** Refaça o ranking dando peso dobrado ao custo e depois peso dobrado à explicabilidade; registre se campeão e challenger mudam.
- [ ] **Em `atividades/01-selecao-de-modelo/dia-059-selecao-de-modelo.ipynb`:** Use bootstrap com seed 42 para comparar os dois melhores em 200 reamostragens do conjunto de validação.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

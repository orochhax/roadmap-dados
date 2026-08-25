# NumPy essencial + pandas - Series e DataFrame

**Data de estudo:** 08/09/2026  
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — NumPy essencial

#### O que pesquisar
- `NumPy essencial análise de dados com Python explicado passo a passo`
- `NumPy essencial análise de dados com Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-numpy-essencial`](<atividades/01-numpy-essencial/>)

#### O que você precisa entender

Um `ndarray` armazena valores do mesmo tipo e aplica operações a todos eles sem laço explícito.

```python
import numpy as np

duracoes = np.array([30, 60, 120, 180])
acima_da_meta = duracoes > 90
ajustadas = np.where(acima_da_meta, duracoes * 0.9, duracoes)
print(np.median(ajustadas), np.percentile(ajustadas, [25, 75]))
```

**Erro comum:** usar `and`/`or` com arrays; combine máscaras com `&`/`|` e parênteses.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-numpy-essencial/numpy_essencial.ipynb`.
- **Dados:** `dados/incidentes.csv`, `dados/clientes_telecom.csv`, `dados/pedidos.csv` e `dados/metas_cidades.csv`.

#### O que fazer

- [ ] Crie o array fornecido e calcule média, mediana, mínimo, máximo e percentis 25/75.
- [ ] Crie uma matriz 4x3 e pratique seleção de linhas, colunas e fatias.
- [ ] Use uma operação vetorizada para modificar valores acima de um limite e compare o resultado com um laço, sem medir desempenho ainda.

- [ ] Normalize uma coluna pelo método min-max e confira manualmente os valores mínimo e máximo produzidos.
- [ ] Teste `NaN`, array vazio e desvio zero e registre o comportamento de cada caso.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

### Atividade 2 — pandas - Series e DataFrame

#### O que pesquisar
- `pandas - Series e DataFrame análise de dados com Python explicado passo a passo`
- `pandas - Series e DataFrame análise de dados com Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-pandas-series-e-dataframe`](<atividades/02-pandas-series-e-dataframe/>)

#### Aula guiada — pandas, parte 1

- [ ] Assista de **00:00 a 01:14:10** de **Tudo de Pandas para Python (DIDÁTICA SUPREMA)**. [Abrir no YouTube](https://www.youtube.com/watch?v=TMfMkgLkeBQ)
- Nesta primeira parte, concentre-se em criação e inspeção de DataFrames, limpeza inicial, criação de colunas e métricas. A continuação será feita em 09/09; não assista às duas partes no mesmo dia.

#### O que você precisa entender

`Series` é uma coluna rotulada; `DataFrame` é uma tabela. Selecione linhas por rótulo com `.loc` e por posição com `.iloc`.

```python
import pandas as pd

df = pd.DataFrame({"cidade": ["Salvador", "Feira"], "duracao": [80, 30]})
filtro = df.loc[df["duracao"] > 60, ["cidade", "duracao"]]
primeira_linha = df.iloc[0]
```

**Erro comum:** encadear filtros e atribuições; crie uma cópia explícita antes de alterar um recorte.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-pandas-series-e-dataframe/pandas_basico.ipynb`.
- **Dados:** `dados/incidentes.csv`, `dados/clientes_telecom.csv`, `dados/pedidos.csv` e `dados/metas_cidades.csv`.

#### O que fazer

- [ ] Monte um DataFrame de 12 incidentes a partir de um dicionário.
- [ ] Inspecione `shape`, `columns`, `dtypes`, `head`, `tail`, `info` e `describe`; escreva uma interpretação de cada saída.
- [ ] Selecione colunas com `[]`, linhas com `loc` e posições com `iloc`; crie cinco filtros combinando cidade, severidade e duração.

- [ ] Crie colunas `duracao_horas` e `impacto = duracao_min * clientes_afetados` sem usar laço.
- [ ] Ordene pelos maiores impactos, selecione os três principais e confirme manualmente os cálculos.
- [ ] Em uma cópia, substitua uma duração por valor ausente e registre o efeito em `dtypes`, `describe()` e no cálculo de impacto.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

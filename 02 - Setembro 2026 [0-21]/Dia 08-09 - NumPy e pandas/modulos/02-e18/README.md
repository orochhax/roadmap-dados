# pandas: Series e DataFrame

## Aprenda agora

`Series` é uma coluna rotulada; `DataFrame` é uma tabela. Selecione linhas por rótulo com `.loc` e por posição com `.iloc`.

```python
import pandas as pd

df = pd.DataFrame({"cidade": ["Salvador", "Feira"], "duracao": [80, 30]})
filtro = df.loc[df["duracao"] > 60, ["cidade", "duracao"]]
primeira_linha = df.iloc[0]
```

**Erro comum:** encadear filtros e atribuições; crie uma cópia explícita antes de alterar um recorte.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/pandas_basico.ipynb`.
- **Dados:** `dados/incidentes.csv`, `dados/clientes_telecom.csv`, `dados/pedidos.csv` e `dados/metas_cidades.csv`.

## Núcleo essencial

1. [ ] Monte um DataFrame de 12 incidentes a partir de um dicionário.
2. [ ] Inspecione `shape`, `columns`, `dtypes`, `head`, `tail`, `info` e `describe`; escreva uma interpretação de cada saída.
3. [ ] Selecione colunas com `[]`, linhas com `loc` e posições com `iloc`; crie cinco filtros combinando cidade, severidade e duração.

## Prática obrigatória

- [ ] Crie colunas `duracao_horas` e `impacto = duracao_min * clientes_afetados` sem usar laço.
- [ ] Ordene pelos maiores impactos, selecione os três principais e confirme manualmente os cálculos.
- [ ] Em uma cópia, substitua uma duração por valor ausente e registre o efeito em `dtypes`, `describe()` e no cálculo de impacto.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

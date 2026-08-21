# Correlação, causalidade e vieses

## Aprenda agora

Pearson mede relação linear; Spearman mede relação monotônica por postos. Um confundidor influencia exposição e resultado; um DAG registra essas relações antes da análise.

```python
pearson = df[["mensalidade", "nps"]].corr(method="pearson").iloc[0, 1]
spearman = df[["mensalidade", "nps"]].corr(method="spearman").iloc[0, 1]
```

**Erro comum:** escrever “X causa Y” a partir de correlação em dados observacionais.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-039-correlacao-causalidade-e-vieses.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/incidentes.csv` e dados sintéticos gerados no notebook com seed 42.

## Núcleo essencial

1. [ ] Calcule Pearson e Spearman em duas relações e compare o que cada medida captura.
2. [ ] Crie um exemplo de correlação sem causalidade e liste um possível confundidor.
3. [ ] Reescreva três conclusões causais como associações compatíveis com os dados observacionais.

## Prática obrigatória

- [ ] Construa um DAG simples depois de identificar exposição, resultado e confundidor.
- [ ] **Em `01-exercicios/dia-039-correlacao-causalidade-e-vieses.ipynb`:** Construa um exemplo de Simpson com duas cidades em que a associação geral tenha sinal diferente das associações por cidade.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

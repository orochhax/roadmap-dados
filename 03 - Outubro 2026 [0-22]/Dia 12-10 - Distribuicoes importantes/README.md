# Distribuições importantes

## Aprenda agora

Bernoulli modela um evento binário; Binomial conta sucessos; Poisson conta eventos em intervalo; Exponencial modela tempo entre eventos; Normal modela valores contínuos aproximadamente simétricos.

```python
rng = np.random.default_rng(42)
churn = rng.binomial(n=1, p=0.12, size=1_000)
incidentes_dia = rng.poisson(lam=4, size=1_000)
tempo_entre = rng.exponential(scale=1 / 4, size=1_000)
```

**Erro comum:** usar Normal para contagens pequenas e aceitar valores negativos impossíveis.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-033-distribuicoes-importantes.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/incidentes.csv` e dados sintéticos gerados no notebook com seed 42.

## Núcleo essencial

1. [ ] Simule distribuições Bernoulli, Binomial, Normal, Poisson e Exponencial com parâmetros definidos.
2. [ ] Para cada uma, escreva um exemplo real: churn individual, número de churns, duração, incidentes por dia e tempo entre incidentes.
3. [ ] Compare média/variância teórica e amostral com 100, 1.000 e 100.000 observações.

## Prática obrigatória

- [ ] Padronize uma normal em z-score e calcule percentuais abaixo/acima de dois limites.
- [ ] Crie um caso em que usar Normal para contagem gera valores impossíveis e explique a distribuição mais adequada.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

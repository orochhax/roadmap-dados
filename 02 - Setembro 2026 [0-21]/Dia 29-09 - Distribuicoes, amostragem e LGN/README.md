# Distribuicoes importantes + Amostragem e Lei dos Grandes Numeros

**Data de estudo:** 29/09/2026  
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Distribuicoes importantes

#### O que pesquisar
- `Distribuicoes importantes Python explicado passo a passo`
- `Distribuicoes importantes Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-distribuicoes-importantes`](<atividades/01-distribuicoes-importantes/>)

#### O que você precisa entender

Bernoulli modela um evento binário; Binomial conta sucessos; Poisson conta eventos em intervalo; Exponencial modela tempo entre eventos; Normal modela valores contínuos aproximadamente simétricos.

```python
rng = np.random.default_rng(42)
churn = rng.binomial(n=1, p=0.12, size=1_000)
incidentes_dia = rng.poisson(lam=4, size=1_000)
tempo_entre = rng.exponential(scale=1 / 4, size=1_000)
```

**Erro comum:** usar Normal para contagens pequenas e aceitar valores negativos impossíveis.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-distribuicoes-importantes/dia-033-distribuicoes-importantes.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/incidentes.csv` e dados sintéticos gerados no notebook com seed 42.

#### O que fazer

- [ ] Simule distribuições Bernoulli, Binomial, Normal, Poisson e Exponencial com parâmetros definidos.
- [ ] Para cada uma, escreva um exemplo real: churn individual, número de churns, duração, incidentes por dia e tempo entre incidentes.
- [ ] Compare média/variância teórica e amostral com 100, 1.000 e 100.000 observações.

- [ ] Padronize uma normal em z-score e calcule percentuais abaixo/acima de dois limites.
- [ ] Crie um caso em que usar Normal para contagem gera valores impossíveis e explique a distribuição mais adequada.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

### Atividade 2 — Amostragem e Lei dos Grandes Numeros

#### O que pesquisar
- `Amostragem e Lei dos Grandes Numeros IA generativa aplicada explicado passo a passo`
- `Amostragem e Lei dos Grandes Numeros IA generativa aplicada exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-amostragem-e-lei-dos-grandes-numeros`](<atividades/02-amostragem-e-lei-dos-grandes-numeros/>)

#### O que você precisa entender

A Lei dos Grandes Números aproxima a média amostral da média populacional. O Teorema Central do Limite descreve a distribuição de muitas médias; o erro padrão é `s / sqrt(n)`.

```python
rng = np.random.default_rng(42)
amostra = rng.choice(populacao, size=100, replace=True)
erro_padrao = amostra.std(ddof=1) / np.sqrt(len(amostra))
```

**Erro comum:** aumentar `n` em uma amostra enviesada e esperar que o viés desapareça.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-amostragem-e-lei-dos-grandes-numeros/dia-034-amostragem-e-lei-dos-grandes-numeros.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/incidentes.csv` e dados sintéticos gerados no notebook com seed 42.

#### O que fazer

- [ ] Simule uma sequência crescente de observações e mostre a média acumulada se aproximando da média da população; identifique isso como Lei dos Grandes Números.
- [ ] Compare amostras aleatórias e uma amostra enviesada da mesma população.
- [ ] Explique como tamanho, aleatoriedade e representatividade afetam uma estimativa empresarial.

- [ ] Retire várias amostras de tamanhos 30, 100 e 500 e observe a distribuição das médias; identifique essa normalização como Teorema Central do Limite, não como Lei dos Grandes Números.
- [ ] Compare erro padrão teórico e observado e explique a diferença entre uma amostra e a distribuição de muitas médias.
- [ ] **Em `atividades/02-amostragem-e-lei-dos-grandes-numeros/dia-034-amostragem-e-lei-dos-grandes-numeros.ipynb`:** Crie uma amostra apenas de Salvador e outra aleatória com o mesmo tamanho; compare o erro das duas em relação à população.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

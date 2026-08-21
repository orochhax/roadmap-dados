# Amostragem e Lei dos Grandes Números

## Aprenda agora

A Lei dos Grandes Números aproxima a média amostral da média populacional. O Teorema Central do Limite descreve a distribuição de muitas médias; o erro padrão é `s / sqrt(n)`.

```python
rng = np.random.default_rng(42)
amostra = rng.choice(populacao, size=100, replace=True)
erro_padrao = amostra.std(ddof=1) / np.sqrt(len(amostra))
```

**Erro comum:** aumentar `n` em uma amostra enviesada e esperar que o viés desapareça.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-034-amostragem-e-lei-dos-grandes-numeros.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/incidentes.csv` e dados sintéticos gerados no notebook com seed 42.

## Núcleo essencial

1. [ ] Simule uma sequência crescente de observações e mostre a média acumulada se aproximando da média da população; identifique isso como Lei dos Grandes Números.
2. [ ] Compare amostras aleatórias e uma amostra enviesada da mesma população.
3. [ ] Explique como tamanho, aleatoriedade e representatividade afetam uma estimativa empresarial.

## Prática obrigatória

- [ ] Retire várias amostras de tamanhos 30, 100 e 500 e observe a distribuição das médias; identifique essa normalização como Teorema Central do Limite, não como Lei dos Grandes Números.
- [ ] Compare erro padrão teórico e observado e explique a diferença entre uma amostra e a distribuição de muitas médias.
- [ ] **Em `01-exercicios/dia-034-amostragem-e-lei-dos-grandes-numeros.ipynb`:** Crie uma amostra apenas de Salvador e outra aleatória com o mesmo tamanho; compare o erro das duas em relação à população.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

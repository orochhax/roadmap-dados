# TCC: carteiras e backtest walk-forward — roteiro

> Folha de trabalho. Preencha os registros sem apagar os enunciados.

## Entradas

- `ranking.parquet`, retornos, calendário de rebalanceamento e custo declarado.
- Saídas em `projetos/portfolio-intelligence-lab/src/portfolio/carteiras.py`, `projetos/portfolio-intelligence-lab/src/backtest/walk_forward.py` e `projetos/portfolio-intelligence-lab/outputs/metrics/`.

## Núcleo essencial

1. [ ] Implemente a carteira de pesos iguais como baseline.

### Registro 1

<!-- Escreva aqui a saída, o teste e a decisão. -->

2. [ ] Implemente uma carteira Top-K baseada no ranking.

### Registro 2

<!-- Escreva aqui a saída, o teste e a decisão. -->

3. [ ] Execute o backtest walk-forward com rebalanceamento e custos, sem recalcular fatores com informação futura.

### Registro 3

<!-- Escreva aqui a saída, o teste e a decisão. -->

4. [ ] Compare retorno, volatilidade, Sharpe, máximo drawdown e turnover.

### Registro 4

<!-- Escreva aqui a saída, o teste e a decisão. -->

5. [ ] Faça uma única sensibilidade variando K ou custo e analise pelo menos um período ruim.

### Registro 5

<!-- Escreva aqui a saída, o teste e a decisão. -->

## Prática obrigatória

1. [ ] Dobre o custo de transação sem alterar datas ou previsões e compare o resultado.

### Registro 6

<!-- Escreva aqui. -->

2. [ ] Divida o histórico em dois subperíodos e verifique a dependência de um mercado de alta.

### Registro 7

<!-- Escreva aqui. -->

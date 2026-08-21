# TCC: carteiras e backtest walk-forward

## Preparação
- **Enunciado local:** `01-exercicios/roteiro_tcc.md`.
- **Saídas canônicas:** `projetos/portfolio-intelligence-lab/src/portfolio/carteiras.py`, `projetos/portfolio-intelligence-lab/src/backtest/walk_forward.py` e métricas em `projetos/portfolio-intelligence-lab/outputs/metrics/`.

## Manifesto de entradas

- **Obrigatórias:** `ranking.parquet`, retornos, calendário de rebalanceamento e custo declarado.
- **Fallback local:** use os arquivos locais e grave `backtest_resultados.csv` na pasta canônica.

## Aprenda agora

- **Definição:** retorno da carteira agrega pesos; Sharpe é `(retorno-rf)/vol`; drawdown mede queda desde pico; turnover é a soma das mudanças de peso.
- **Exemplo mínimo:** compare pesos iguais e Top-K nas mesmas datas, com `retorno_líquido = retorno_bruto - custo×turnover`.
- **Erro comum:** comparar janelas diferentes, ignorar custos ou recalcular fator com informação indisponível.

## Núcleo essencial

1. [ ] Implemente carteira de pesos iguais como baseline.
2. [ ] Implemente uma carteira Top-K baseada no ranking.
3. [ ] Execute backtest walk-forward com rebalanceamento e custos, sem recalcular fatores com dados futuros.
4. [ ] Compare retorno, volatilidade, Sharpe, máximo drawdown e turnover.
5. [ ] Faça uma única sensibilidade variando K ou custo e analise pelo menos um período ruim.

## Prática obrigatória

- [ ] Dobre o custo de transação sem alterar previsões ou datas e compare o resultado.
- [ ] Divida o histórico em dois subperíodos para verificar dependência de um único mercado de alta.

## Concluído quando

- [ ] Os módulos e as métricas canônicas contêm todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

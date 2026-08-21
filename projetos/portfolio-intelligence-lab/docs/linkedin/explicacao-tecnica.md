# Explicação técnica do projeto

## Versão curta

Construa um parágrafo com problema, dados, dois fatores, comparação de carteiras, validação temporal, custos, resultado e limitação.

## Versão detalhada

Explique:

1. uma classe e o protocolo de elegibilidade;
2. momentum, volatilidade e score transparente;
3. ranking e seleção Top-K;
4. pesos iguais como baseline;
5. walk-forward, turnover e custos;
6. dashboard, testes e reprodução;
7. período ruim e principal limitação.

## Decisões verificáveis

| Decisão | Evidência |
|---|---|
| universo | `docs/protocolo-financeiro.md` |
| fatores | `src/features/fatores.py` |
| ranking | `src/ranking/motor_ranking.py` |
| carteiras | `src/portfolio/carteiras.py` |
| backtest | `src/backtest/walk_forward.py` |
| métricas | `outputs/metrics/` |

## Limite de linguagem

Use “na amostra analisada” e “resultado líquido de custos”. Não use “previsão garantida”, “melhor investimento” ou “recomendação”.

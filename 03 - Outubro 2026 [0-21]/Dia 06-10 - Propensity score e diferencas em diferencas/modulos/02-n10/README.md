# Causalidade III — diferenças em diferenças e estudo de evento

## Objetivo

Avaliar um rollout regional quando não houve randomização, separando mudança comum no tempo do efeito específico da região tratada. Você testará tendências prévias e mostrará quando diferenças em diferenças não é confiável.

## Pesquise exatamente estes nomes

- `difference in differences 2x2 estimator`
- `parallel trends assumption difference in differences`
- `event study leads and lags`
- `cluster robust standard errors panel data`
- `staggered adoption difference in differences bias`
- `placebo treatment date difference in differences`
- `anticipation effect causal inference`

## Trabalho obrigatório

Leia o [enunciado](01-exercicios/ENUNCIADO.md), complete [diferencas_em_diferencas.py](01-exercicios/diferencas_em_diferencas.py) e registre o diagnóstico em [Evidências](03-evidencias/README.md).

## Concluído quando

- o estimador 2x2 confere com a regressão;
- a hipótese de tendências paralelas é investigada antes do rollout;
- event study, placebo e sensibilidade são registrados;
- uma base que viola a hipótese não recebe conclusão causal forte.


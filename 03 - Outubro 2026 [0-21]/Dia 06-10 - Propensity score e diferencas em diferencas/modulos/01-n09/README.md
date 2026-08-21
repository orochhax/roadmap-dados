# Causalidade II — propensity score e balanceamento

## Objetivo

Estimar o efeito de uma oferta de retenção em dados observacionais, comparando matching e ponderação. O objetivo central é diagnosticar sobreposição e balanceamento, não obter um número causal a qualquer custo.

## Pesquise exatamente estes nomes

- `propensity score logistic regression causal inference`
- `propensity score common support overlap`
- `standardized mean difference love plot`
- `nearest neighbor matching caliper propensity score`
- `inverse probability weighting stabilized weights`
- `effective sample size IPW`
- `positivity violation extreme weights`
- `propensity score trimming sensitivity`

## Trabalho obrigatório

Leia o [enunciado](01-exercicios/ENUNCIADO.md), complete [propensity_score.py](01-exercicios/propensity_score.py) e registre diagnósticos em [Evidências](03-evidencias/README.md).

## Concluído quando

- somente variáveis pré-tratamento entram no propensity;
- overlap e SMD são vistos antes do efeito;
- matching e IPW usam o estimando declarado;
- pesos extremos e perda de amostra são reportados;
- é permitido concluir que os dados não sustentam a estimativa.


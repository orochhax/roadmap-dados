# Causalidade IV — controle sintético e placebos

## Objetivo

Construir um contrafactual ponderado para uma única região tratada, avaliar o ajuste antes da intervenção e comparar o gap observado com placebos. O método só será aceito se os doadores reproduzirem bem o pré-período.

## Pesquise exatamente estes nomes

- `synthetic control method Abadie donor pool`
- `synthetic control nonnegative weights sum to one`
- `pre treatment RMSPE synthetic control`
- `synthetic control in space placebo test`
- `post pre RMSPE ratio synthetic control`
- `leave one out synthetic control sensitivity`
- `convex hull synthetic control extrapolation`
- `scipy optimize minimize constraints`

## Trabalho obrigatório

Leia o [enunciado](01-exercicios/ENUNCIADO.md), implemente [controle_sintetico.py](01-exercicios/controle_sintetico.py) e registre pesos, placebos e decisão em [Evidências](03-evidencias/README.md).

## Concluído quando

- o donor pool é definido antes de observar o pós;
- pesos obedecem às restrições e ajustam o pré-período;
- o gap é comparado a placebos e sensibilidades;
- mau ajuste prévio impede uma conclusão forte.


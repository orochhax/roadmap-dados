# Experimentação avançada para produto digital

## Objetivo

Analisar um experimento de autoatendimento sem cair em três armadilhas comuns: grupos desbalanceados, escolha entre muitas métricas e interrupção antecipada. Você também usará CUPED para reduzir variância sem alterar a unidade randomizada.

## Pesquise exatamente estes nomes

- `sample ratio mismatch chi square test`
- `Holm Bonferroni multiple testing`
- `false discovery rate Benjamini Hochberg`
- `CUPED controlled experiments using pre experiment data`
- `variance reduction CUPED theta covariance`
- `sequential testing alpha spending`
- `peeking inflated false positive rate A/B test`

## Trabalho obrigatório

Leia o [enunciado](01-exercicios/ENUNCIADO.md), implemente [analisar_experimento.py](01-exercicios/analisar_experimento.py) e registre protocolo e decisão em [Evidências](03-evidencias/README.md).

## Concluído quando

- hipóteses, MDE e regra de parada estão congeladas antes da análise;
- SRM, multiplicidade, CUPED e peeking foram medidos;
- a análise diferencia significância de relevância prática;
- lançar, repetir ou abandonar é decidido por critérios anteriores ao resultado.


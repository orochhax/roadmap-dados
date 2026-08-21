# Data card — Energy ForecastOps

## Fonte

- arquivo: ../../dados/energia.csv;
- origem: kit sintético do roadmap, gerado com seed 42;
- unidade: um dia;
- linhas esperadas: 730;
- período e hash: TODO calcular e registrar na primeira execução.

## Campos

| Campo | Uso permitido | Risco |
|---|---|---|
| data | índice e features de calendário | parsing e lacunas |
| consumo_mwh | alvo e lags passados | vazamento por rolling incorreto |
| temperatura_c | covariável | disponibilidade futura deve ser declarada |
| feriado | calendário conhecido | confirmar codificação |

## Protocolo a congelar

- frequência: TODO;
- horizontes: TODO;
- tamanho mínimo de treino: TODO;
- passo entre origens: TODO;
- janela expansiva ou móvel: TODO;
- custo de sub e sobreprevisão: TODO;
- tratamento de temperatura futura: TODO.

## Qualidade

Valide unicidade e monotonicidade de data, frequência, lacunas, duplicatas,
unidade, valores impossíveis e mudanças de distribuição.

## Limitações

Os dados são pequenos e sintéticos. Não alegue desempenho em rede elétrica real
nem use temperatura observada no futuro sem explicar como estaria disponível no
momento da previsão.

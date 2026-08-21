# Enunciado — programa de prevenção de rompimento de fibra

## Cenário real

Salvador recebeu um programa de inspeção preventiva de fibra; nenhuma outra capital recebeu a mesma política naquele momento. A direção quer estimar quantos incidentes semanais foram evitados. Uma média simples das outras cidades não reproduz Salvador no período anterior.

## Entradas

Gere `painel_fibra.csv` com seed 42:

- Salvador como unidade tratada;
- pelo menos oito cidades doadoras;
- 24 semanas prévias e 12 posteriores;
- `incidentes_fibra`, `chuva_mm`, `obras_via` e `base_clientes`;
- intervenção após a semana 24 e efeito conhecido apenas em Salvador;
- uma cidade doadora com choque posterior não relacionado;
- uma segunda versão na qual nenhum conjunto convexo reproduz bem Salvador.

## Saídas

- [controle_sintetico.py](controle_sintetico.py) completo;
- `pesos_doadores.csv`;
- `serie_contrafactual.csv` com observado, sintético e gap;
- `placebos.csv` com RMSPE pré/pós e razão;
- gráficos da trajetória e dos gaps;
- [evidências](../03-evidencias/README.md).

## Regras obrigatórias

1. Congele o donor pool e preditores usando somente informação pré-intervenção.
2. Exclua cidades com política concorrente conhecida e explique cada exclusão.
3. Otimize pesos não negativos cuja soma seja 1; registre tolerância numérica.
4. Minimize o erro prévio sem usar semanas posteriores para selecionar pesos.
5. Compare com baseline de média simples dos doadores.
6. Calcule RMSPE pré, RMSPE pós e razão pós/pré.
7. Rode placebo no espaço, tratando cada doadora como se tivesse recebido a política.
8. Faça leave-one-donor-out nas cidades com peso positivo.
9. Repita na base sem bom ajuste e limite a conclusão.

## Casos de borda obrigatórios

- doador com todos os valores ausentes;
- semana ausente;
- peso negativo retornado por erro de implementação;
- soma dos pesos diferente de 1;
- uma cidade concentra quase todo o peso;
- choque pós-tratamento em doador importante;
- RMSPE pré alto;
- efeito aparente também frequente nos placebos.

## Métricas

- RMSPE pré do sintético e da média simples;
- gap médio e acumulado pós-intervenção;
- razão RMSPE pós/pré da tratada e rank entre placebos;
- número efetivo de doadores e maior peso;
- faixa do efeito no leave-one-out;
- erro em relação ao efeito injetado na base controlada.

## Critério de aceite

- [ ] Pesos são não negativos, somam 1 dentro da tolerância e usam só o pré.
- [ ] O sintético supera ou é comparado honestamente à média simples no pré.
- [ ] Placebos e leave-one-out são executados antes da recomendação.
- [ ] A base de mau ajuste não recebe conclusão causal forte.
- [ ] O relatório distingue efeito estimado, incerteza por placebos e limitações do donor pool.


# Energy ForecastOps

Projeto obrigatório de previsão de consumo para planejamento operacional. O
objetivo é aprender validação temporal e decisão sob erro, não procurar o modelo
mais sofisticado.

Documentos: [dados](data_card.md), [backlog](backlog.md),
[apresentação em inglês](docs/presentation-en.md) e
[versão em inglês](README.en.md). A entrada vem dos
[dados compartilhados](../../dados/README.md).

## Problema e usuário

- **Problema:** prever consumo diário para os próximos horizontes definidos no
  protocolo.
- **Usuário:** gestor de operação e capacidade.
- **Decisão:** reservar capacidade considerando o custo diferente de prever
  abaixo ou acima do consumo real.

## Dados

Use ../../dados/energia.csv, com duas séries anuais sintéticas de consumo,
temperatura e feriado. Preserve a fonte e grave derivados somente em
data/processed/. Consulte data_card.md antes de modelar.

## Baselines

Implemente obrigatoriamente:

1. último valor observado;
2. sazonal ingênuo de sete dias;
3. média móvel definida apenas com passado.

## Modelos candidatos

- ETS ou SARIMA;
- regressão com tendência, calendário e lags;
- Gradient Boosting com features temporais.

Não use split aleatório. Toda comparação deve usar backtest rolling-origin com
horizontes e janelas congelados antes de observar os resultados.

## Métricas e testes

Avalie MAE, RMSE, sMAPE, cobertura de intervalos e custo operacional de
subprevisão. Teste continuidade das datas, criação de lags, folds temporais,
métricas e reprodução das previsões.

## Artefatos

- protocolo de backtest;
- tabela de métricas por fold e horizonte;
- previsões e intervalos;
- gráficos de erros e períodos ruins;
- relatório de decisão e limitações;
- README em português/inglês e apresentação em inglês.

## Concluído quando

- [ ] Um comando reproduz todos os folds e artefatos.
- [ ] Nenhuma feature acessa o futuro.
- [ ] Todos os candidatos são comparados com o sazonal ingênuo.
- [ ] A estabilidade por horizonte é discutida.
- [ ] Se o modelo avançado perder, o baseline é recomendado honestamente.
- [ ] Os testes passam e resultados do relatório reconciliam com os CSVs.
- [ ] README.en.md e docs/presentation-en.md contêm resultados executados.

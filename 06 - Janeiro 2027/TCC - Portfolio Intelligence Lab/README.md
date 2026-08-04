# TCC — Portfolio Intelligence Lab

> [!important] Escopo mínimo viável
> O objetivo é terminar um produto correto, reproduzível e explicável. Funcionalidades adicionais não devem atrasar a publicação.

## Núcleo obrigatório

- [ ] Uma classe com 10–20 ativos e uma fonte de preços ajustados validada.
- [ ] Dois fatores transparentes: momentum e volatilidade.
- [ ] Ranking por data sem uso de informação futura.
- [ ] Comparação walk-forward entre carteira de pesos iguais e carteira Top-K.
- [ ] Custos, retorno, volatilidade, Sharpe, drawdown e turnover.
- [ ] Um dashboard simples ou notebook-relatório, testes essenciais, README e relatório de 4–6 páginas.
- [ ] Limitações, períodos ruins e aviso de que o conteúdo não é recomendação de investimento.

## Desafios pós-entrega

- [ ] Outras classes de ativos e fatores adicionais.
- [ ] Machine Learning como comparação ao score transparente.
- [ ] Mínima volatilidade ou risk parity.
- [ ] Simulador, API, Docker e deploy.
- [ ] Relatório técnico extenso e novas estratégias.

## Estrutura sugerida

```text
portfolio-intelligence-lab/
├── data/raw/
├── data/processed/
├── notebooks/
├── src/
├── tests/
├── reports/
└── README.md
```

## Pergunta de conclusão

Outra pessoa consegue reproduzir o ranking e o backtest, identificar os custos e períodos ruins e contestar suas decisões usando somente os arquivos publicados?

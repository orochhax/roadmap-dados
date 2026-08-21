# Protocolo financeiro

## Universo

- **Classe escolhida:** _preencher_.
- **Quantidade:** 10–20 ativos.
- **Período:** _preencher_.
- **Fonte e licença:** _preencher_.
- **Hash do snapshot:** _preencher_.

## Regras congeladas

- [ ] preços ajustados e camada bruta preservada;
- [ ] elegibilidade definida antes da análise;
- [ ] rebalanceamento mensal;
- [ ] janelas de momentum e volatilidade declaradas;
- [ ] score `z_momentum - z_volatilidade`;
- [ ] pesos iguais como baseline e Top-K como candidata;
- [ ] walk-forward com cortes crescentes;
- [ ] custo em pontos-base aplicado ao turnover;
- [ ] retorno, volatilidade, Sharpe, drawdown e turnover como métricas.

## Disponibilidade temporal

Cada observação usada precisa satisfazer `disponivel_em <= data_rebalanceamento`. Alterar valores posteriores ao corte não pode mudar fatores, ranking ou pesos já calculados.

## Critérios de qualidade

- chave ticker/data única;
- preços positivos;
- datas ordenadas;
- ausentes e histórico insuficiente reportados;
- ativos removidos registrados com motivo.

## Critério de sucesso

Compare as duas estratégias sem exigir superioridade. O projeto é válido se o protocolo for reproduzível, os custos estiverem corretos e as conclusões incluírem períodos ruins e incerteza.

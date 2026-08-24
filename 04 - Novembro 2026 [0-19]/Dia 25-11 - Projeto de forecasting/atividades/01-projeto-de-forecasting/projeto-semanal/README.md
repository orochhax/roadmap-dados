# Projeto — Forecasting de volume de chamados

## Manifesto de entradas

- **Obrigatórias:** série local com frequência, alvo, horizonte e datas de corte.
- **Saídas:** baselines, modelo, backtest, intervalos e recomendação operacional.
- **Fallback local:** use a série versionada ou uma fixture determinística com sazonalidade documentada.

## Entregas obrigatórias
1. Valide frequência e crie baselines de último valor e sazonal.
2. Compare um modelo no mesmo walk-forward e nas mesmas métricas.
3. Traduza previsão e intervalo em recomendação de capacidade.

- Teste custo assimétrico para falta e excesso de capacidade.

## Concluído quando

- Todos os métodos usam horizonte e cortes idênticos.
- A tabela contém erro por janela e resultado agregado.
- A recomendação declara incerteza e uma limitação.

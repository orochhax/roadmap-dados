# Portfolio Intelligence Lab

Pesquisa educacional reproduzível sobre ranking quantitativo e carteiras. Não constitui recomendação de investimento.

## Escopo congelado

- uma classe de ativos com 10–20 tickers;
- preços ajustados com fonte, licença, período, data de coleta e hash;
- dois fatores transparentes: momentum e volatilidade;
- score e ranking calculados em cada data de rebalanceamento;
- comparação walk-forward entre pesos iguais e Top-K;
- custos, retorno, volatilidade, Sharpe, drawdown e turnover;
- dashboard simples como entrega visual;
- testes essenciais e relatório de 4–6 páginas.

## Entradas e saídas

- **Entrada principal:** `data/raw/precos_ajustados.csv` ou `.parquet`, no formato descrito em `docs/dicionario-de-dados.md`.
- **Protocolo:** `docs/protocolo-financeiro.md`.
- **Metodologia:** `docs/metodologia-score.md`.
- **Dados processados:** `data/processed/`.
- **Métricas e gráficos:** `outputs/metrics/` e `outputs/charts/`.
- **Relatório:** `docs/relatorio-final.md`.
- **Fallback local:** uma amostra determinística com os mesmos campos pode validar o fluxo sem coleta online.

## Execução

```powershell
python -m pip install -r requirements.txt
python -m pytest -q
streamlit run dashboard/app.py
```

O dashboard deve ler somente artefatos processados e não recalcular o protocolo.

## Estrutura

```text
portfolio-intelligence-lab/
├── data/raw/
├── data/processed/
├── dashboard/
├── docs/
├── outputs/
├── sql/
├── src/
├── tests/
└── README.md
```

## Fora do escopo

Várias classes, fatores adicionais, modelos preditivos, simulador, serviço web, conteinerização, hospedagem e relatório longo não pertencem à entrega.

## Concluído quando

- Outra pessoa reproduz fatores, ranking e backtest pelo README.
- Testes provam disponibilidade temporal, fatores e uma métrica de carteira.
- Dashboard e relatório reconciliam custos, períodos ruins, resultado e limitações.

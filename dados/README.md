# Dados compartilhados

Esta pasta contém o kit sintético usado como entrada nos exercícios. Os
arquivos não possuem respostas ou métricas calculadas.

## Arquivos

- `incidentes.csv` e `metas_cidades.csv`: Python, pandas, visualização e SQL.
- `clientes_telecom.csv`: churn, classificação e decisão.
- `pedidos.csv`: vendas, regressão e análise temporal.
- `clientes.csv`, `planos.csv`, `chamados.csv` e `pagamentos.csv`: modelagem relacional e SQL.
- `credito.csv`: risco de crédito.
- `energia.csv`: forecasting.

Todos foram gerados com seed `42` por
`../00 - Recursos Compartilhados/gerar_dados.py`. Os CSVs desta pasta são as
entradas imutáveis. Use `raw/` apenas para snapshots adicionais e grave versões
tratadas em `processed/` ou na pasta do projeto quando o enunciado solicitar.

Os resultados obtidos com este kit demonstram o funcionamento do método no
cenário simulado. Eles não medem impacto em clientes, empresas ou redes reais.
Toda publicação deve manter essa limitação visível e nunca transformar uma
métrica sintética em alegação de resultado profissional.

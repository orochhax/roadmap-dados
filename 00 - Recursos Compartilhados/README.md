# Recursos compartilhados

> Este índice reproduz as referências do roadmap. As bases reais não foram inventadas nem preenchidas nesta organização.

## Kit prático incluído

> [!important] Como usar no Obsidian
> Copie a pasta inteira do roadmap para dentro do seu Vault. O arquivo Markdown usa caminhos relativos para que os exercícios encontrem os dados sem depender de downloads externos.

### Arquivos de dados

| Arquivo | Uso principal |
|---|---|
| `dados/incidentes.csv` | Python, pandas, visualização, SQL e operações de telecom |
| `dados/metas_cidades.csv` | joins, metas e dashboard |
| `dados/clientes_telecom.csv` | churn, classificação, explicabilidade e decisão |
| `dados/pedidos.csv` | análise de vendas, regressão e séries temporais |
| `dados/clientes.csv` | modelagem relacional em SQL |
| `dados/planos.csv` | joins e dimensões |
| `dados/chamados.csv` | agregações e features de comportamento |
| `dados/pagamentos.csv` | inadimplência, joins e cohorts |
| `dados/credito.csv` | risco de crédito, calibração e políticas |
| `dados/energia.csv` | forecasting e validação temporal |
| `documentos_suporte/` | embeddings, busca semântica e RAG |

### Regra de uso

1. Preserve uma cópia dos arquivos originais em `dados/raw/`.
2. Nunca edite o arquivo bruto manualmente para “corrigir” um resultado.
3. Grave versões tratadas em `dados/processed/` ou dentro da pasta do projeto.
4. Use seed `42` sempre que gerar dados aleatórios, salvo quando o exercício pedir teste de estabilidade.
5. O script `gerar_dados.py` recria o kit caso algum arquivo seja perdido.

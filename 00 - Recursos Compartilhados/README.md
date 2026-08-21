# Recursos compartilhados

- [LinkedIn e evidências do roadmap](linkedin-e-evidencias.md)
- [LinkedIn — perfil atual e próximas mudanças](linkedin-perfil-atual.md)
- [Vagas para análise do roadmap](VAGAS.md)
- [Análise das vagas e decisões do currículo](analise-vagas-e-decisoes.md)
- [Decisões de Carlos](PERGUNTAS-PARA-CARLOS.md)

Materiais usados por mais de uma sessão:

- [Cobertura do Curso em Vídeo — Python](<trilha-curso-em-video-python.md>)
- [Cursos gratuitos e lacunas](<cursos-complementares-selecionados.md>)
- [Mapa de arquivos](<mapa-de-arquivos.md>)
- [Plano e método de estudo](<../PLANO-DE-ESTUDOS.md>)

## Kit prático incluído

Mantenha a pasta inteira do projeto unida. Os caminhos são relativos para que exercícios e dados funcionem no VS Code, no terminal e no Obsidian.

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
| `projetos/assistente-suporte-ia/data/corpus/` | embeddings, busca semântica e RAG |

### Regra de uso

1. Trate os CSVs na raiz de `dados/` como entradas imutáveis; não os edite para “corrigir” um resultado.
2. Use `dados/raw/` somente para snapshots adicionais pedidos por um enunciado.
3. Grave versões tratadas em `dados/processed/` ou dentro da pasta do projeto.
4. Use seed `42` sempre que gerar dados aleatórios, salvo quando o exercício pedir teste de estabilidade.
5. O script `gerar_dados.py` recria o kit caso algum arquivo seja perdido.

### Como apresentar dados sintéticos

- Informe no data card e no README que os registros são simulados e não representam pessoas ou empresas reais.
- Registre gerador, seed, esquema e regras usadas para produzir os dados.
- Use os resultados para demonstrar método, código, testes e tomada de decisão; não os apresente como impacto real de negócio.
- Uma simulação causal comprova que a análise foi implementada corretamente dentro das hipóteses simuladas, não que a mesma intervenção funcionaria numa operadora real.
- Em imagens, prefira dados públicos licenciados quando precisar estimar desempenho de campo; imagens artificiais isoladas servem apenas para validar o fluxo técnico.

# Recursos compartilhados

Esta pasta guarda somente orientações, dados de referência e controles usados em mais de um dia. O estudo diário começa na [agenda principal](../README.md), não aqui.

## Navegação

| Preciso de... | Abra |
|---|---|
| método, critérios e organização das pastas | [Plano de estudos](<../PLANO-DE-ESTUDOS.md>) |
| próximo dia e progresso mensal | [README principal](../README.md) |
| aulas do Curso em Vídeo | [Cobertura do Curso em Vídeo — Python](<trilha-curso-em-video-python.md>) |
| cursos gratuitos selecionados | [Cursos gratuitos e lacunas](<cursos-complementares-selecionados.md>) |
| preparação para badges, cursos e certificado | [Credenciais gratuitas e simulados](<credenciais-gratuitas-e-simulados.md>) |
| atualização honesta do perfil | [LinkedIn e evidências](linkedin-e-evidencias.md) |
| estado atual do perfil | [LinkedIn — perfil atual](linkedin-perfil-atual.md) |
| requisitos observados no mercado | [Vagas](VAGAS.md) e [análise das vagas](analise-vagas-e-decisoes.md) |
| decisões pessoais já respondidas | [Decisões de Carlos](PERGUNTAS-PARA-CARLOS.md) |
| localizar um artefato | [Mapa de arquivos](<mapa-de-arquivos.md>) |

## Estrutura em uma frase

- O README principal controla **quando** estudar.
- O README de cada dia explica **o que** estudar e entregar.
- `atividades/NN-nome-descritivo/` contém **onde** trabalhar.
- `dados/` fornece entradas compartilhadas.
- `projetos/` concentra produtos que atravessam vários dias.
- Esta pasta centraliza somente regras que seriam repetidas.

Os códigos internos e caminhos anteriores existem apenas no [manifesto técnico](<manifesto-reorganizacao-2026.json>). Eles servem à manutenção e não fazem parte da navegação do estudante.

## Regra para artefatos e evidências

O próprio código, consulta, notebook, planilha, dashboard ou relatório é a comprovação de um exercício comum. Não crie documentação paralela apenas para repetir que ele foi executado.

Um registro separado de evidências é usado somente para:

- publicação no LinkedIn;
- credencial ou resultado externo verificável;
- projeto selecionado para portfólio;
- TCC, banca ou release.

Nesses casos, registre URL, data, resultado emitido e conferência de publicação sem duplicar o conteúdo técnico do artefato.

## Kit prático incluído

Mantenha a pasta inteira do projeto unida. Os caminhos relativos permitem usar os dados no VS Code, terminal e notebooks.

| Arquivo | Uso principal |
|---|---|
| `dados/incidentes.csv` | Python, pandas, visualização, SQL e operações de telecom |
| `dados/metas_cidades.csv` | joins, metas e dashboards |
| `dados/clientes_telecom.csv` | churn, classificação, explicabilidade e decisão |
| `dados/pedidos.csv` | vendas, regressão e séries temporais |
| `dados/clientes.csv` | modelagem relacional em SQL |
| `dados/planos.csv` | joins e dimensões |
| `dados/chamados.csv` | agregações e features de comportamento |
| `dados/pagamentos.csv` | inadimplência, joins e cohorts |
| `dados/credito.csv` | risco, calibração e políticas |
| `dados/energia.csv` | forecasting e validação temporal |
| `projetos/assistente-suporte-ia/data/corpus/` | embeddings, busca semântica e RAG |

### Regra de uso dos dados

1. Trate os CSVs da raiz de `dados/` como entradas imutáveis.
2. Use `dados/raw/` para snapshots adicionais pedidos por uma atividade.
3. Grave versões tratadas em `dados/processed/` ou dentro do projeto correspondente.
4. Use seed `42` ao gerar dados aleatórios, salvo quando o enunciado pedir teste de estabilidade.
5. Use `gerar_dados.py` para recriar o kit se algum arquivo for perdido.

### Como apresentar dados sintéticos

- Informe no data card e no README que os registros são simulados.
- Registre gerador, seed, esquema e regras de geração.
- Demonstre método, código, testes e decisão; não alegue impacto real de negócio.
- Uma simulação causal valida a implementação sob hipóteses simuladas, não prova efeito numa empresa real.
- Em visão computacional, prefira dados públicos licenciados para estimativas; imagens artificiais isoladas comprovam apenas o fluxo técnico.

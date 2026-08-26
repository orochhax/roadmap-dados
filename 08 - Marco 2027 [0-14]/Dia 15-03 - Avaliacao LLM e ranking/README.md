# Avaliação de aplicações LLM + ranking e sistemas de recomendação

**Data de estudo:** 15/03/2027
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Avaliacao de aplicacoes LLM

#### O que pesquisar
- `Avaliacao de aplicacoes LLM IA generativa aplicada explicado passo a passo`
- `Avaliacao de aplicacoes LLM IA generativa aplicada exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `projeto-assistente-suporte-ia`](<../../projetos/assistente-suporte-ia/>)

#### Aulas guiadas — Curso em Vídeo IA

- [ ] #38 — **Desvendando falhas dos LLMs: Verifique suas fontes!** (12:39).
- [ ] #41 — **Entenda as Armadilhas Matemáticas em Modelos de IA** (15:09).
- **Carga:** 28 min. As aulas motivam a verificação; o conjunto de avaliação, as métricas e a análise de erros continuam obrigatórios.

#### Arquivos e dados

- **Pasta/arquivo principal:** `projetos/assistente-suporte-ia/src/assistente_suporte_ia/metricas_avaliacao.py`.
- **Dados:** `projetos/assistente-suporte-ia/data/perguntas_avaliacao.csv`.

#### Diagnóstico de base

- [ ] Confirme agora, em `projetos/assistente-suporte-ia/governanca/gate-fundamentos.md`, autonomia 3/5 ou maior em Python, SQL, estatística e ML: script testado, consulta com JOIN/agregação, cálculo interpretado e pipeline com baseline.
- Use as lacunas encontradas para planejar uma revisão posterior; elas não substituem as atividades obrigatórias de LLM/RAG.

#### O que você precisa entender

- **Definição:** Precision@k é relevantes recuperados/k; Recall@k é relevantes recuperados/total relevante; MRR é a média de `1/rank` do primeiro relevante.
- **Exemplo mínimo:** relevantes {A,C}, ranking [B,A,C] em k=2: precision=1/2, recall=1/2 e reciprocal rank=1/2.
- **Erro comum:** mudar gabarito ou k entre sistemas e comparar números incompatíveis.

#### O que fazer

- [ ] Preencha dez perguntas com resposta esperada e fonte correta em `projetos/assistente-suporte-ia/data/perguntas_avaliacao.csv`.
- [ ] Calcule recall@k e precision@k em exemplos pequenos e interprete pelo menos dois erros.
- [ ] Use uma rubrica curta de correção, fundamentação e segurança para avaliar as respostas.

- [ ] **Em `projetos/assistente-suporte-ia/src/assistente_suporte_ia/metricas_avaliacao.py`:** inclua a pergunta 'Posso desconectar o cabo óptico quando a LOS está vermelha?' com a fonte correta no conjunto de avaliação.
- [ ] **No mesmo arquivo:** compare a mesma avaliação com k=1 e k=5 e registre precision@k, recall@k e erros recuperados.

#### Como validar

- O diagnóstico está registrado e o artefato obrigatório de LLM/RAG foi executado com a saída exigida.
- Um caso de borda ou erro foi testado, com resultado esperado e observado registrados.
- A entrega explica o resultado, a decisão tomada e uma limitação concreta.

### Atividade 2 — Ranking de candidatos e introdução a sistemas de recomendação

#### O que pesquisar
- `candidate generation e reranking`
- `Precision at k e Recall at k`
- `MRR e NDCG`
- `ranking latency`
- `recommender systems implicit feedback popularity baseline`
- `content based filtering versus collaborative filtering`
- `recommender cold start users items`
- `recommender system temporal split Precision at K Recall at K NDCG`

**Arquivos da atividade:** [abrir a pasta `02-ranking-de-candidatos-e-introducao`](<atividades/02-ranking-de-candidatos-e-introducao/>)

#### Objetivo

Transformar os candidatos recuperados nas atividades anteriores em uma lista ordenada e uma decisão operacional. Você comparará uma regra ponderada com um ranker supervisionado, medirá a posição da entidade correta e separará decisões automáticas de casos que exigem revisão humana.

Em um segundo exercício obrigatório e mais curto, você transferirá os conceitos de ranking para recomendação: baseline de popularidade, feedback implícito, cold start e avaliação temporal. Os problemas são diferentes, mas compartilham a pergunta central: “o item relevante ficou nas primeiras posições?”.

#### Termos complementares para pesquisar

1. `learning to rank pointwise pairwise listwise`
2. `XGBoost XGBRanker rank:pairwise qid`
3. `ranking feature engineering entity matching`
4. `Mean Reciprocal Rank MRR interpretation`
5. `NDCG at k ranking metric relevance`
6. `ranking train validation split by query group leakage`
7. `score calibration selective classification coverage risk`
8. `reranking latency cost quality tradeoff`
9. `recommender systems implicit feedback popularity baseline`
10. `recommender system temporal train test split leakage`
11. `content based filtering versus collaborative filtering`
12. `recommender cold start users items`
13. `Precision at K Recall at K NDCG recommender systems`

#### O que você precisa entender

- **Gerador:** recupera uma lista ampla e barata.
- **Reranker:** usa sinais mais caros para reordenar poucos candidatos.
- **Grupo/query:** todos os candidatos pertencentes ao mesmo registro consultado.
- **MRR:** valoriza a primeira posição do item relevante.
- **Abstenção:** evita automatizar casos em que primeiro e segundo lugares são próximos.

#### Entregas obrigatórias

O [enunciado](<atividades/02-ranking-de-candidatos-e-introducao/ENUNCIADO.md>) possui dois exercícios e ambos devem ser concluídos:

1. reranking de entity matching em `atividades/02-ranking-de-candidatos-e-introducao/avaliar_ranking.py`, usando os artefatos de normalização, baseline, geração de candidatos e embeddings sem reavaliar limiares no teste;
2. recomendador com feedback implícito em `atividades/02-ranking-de-candidatos-e-introducao/recomendador_baseline.py`.

Preencha as duas seções de registro no próprio artefato e não misture resultados dos dois produtos.

#### LinkedIn

Depois de concluir os dois exercícios, adicione: **Learning to Rank**, **XGBoost** e **Sistemas de recomendação**.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

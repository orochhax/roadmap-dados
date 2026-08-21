# Ranking de candidatos e introdução a sistemas de recomendação

## Objetivo

Transformar os candidatos recuperados nos módulos anteriores em uma lista ordenada e uma decisão operacional. Você comparará uma regra ponderada com um ranker supervisionado, medirá a posição da entidade correta e separará decisões automáticas de casos que exigem revisão humana.

Em um segundo exercício obrigatório e mais curto, você transferirá os conceitos de ranking para recomendação: baseline de popularidade, feedback implícito, cold start e avaliação temporal. Os problemas são diferentes, mas compartilham a pergunta central: “o item relevante ficou nas primeiras posições?”.

## Pesquise estes nomes exatos

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

## Conceitos essenciais

- **Gerador:** recupera uma lista ampla e barata.
- **Reranker:** usa sinais mais caros para reordenar poucos candidatos.
- **Grupo/query:** todos os candidatos pertencentes ao mesmo registro consultado.
- **MRR:** valoriza a primeira posição do item relevante.
- **Abstenção:** evita automatizar casos em que primeiro e segundo lugares são próximos.

## Entregas obrigatórias

O [enunciado](<01-exercicios/ENUNCIADO.md>) possui dois exercícios e ambos devem ser concluídos:

1. reranking de entity matching em `01-exercicios/avaliar_ranking.py`, usando os artefatos N14–N16 sem reavaliar limiares no teste;
2. recomendador com feedback implícito em `01-exercicios/recomendador_baseline.py`.

Preencha as duas seções de [evidências](<03-evidencias/README.md>) e não misture resultados dos dois produtos.

## LinkedIn

Depois de concluir os dois exercícios, adicione: **Learning to Rank**, **XGBoost** e **Sistemas de recomendação**.

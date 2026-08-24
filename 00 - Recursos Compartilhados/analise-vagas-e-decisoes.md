# Análise das vagas e decisões do roadmap

## Base analisada

O arquivo VAGAS.md contém anúncios brasileiros e internacionais, inclusive repetições. A auditoria encontrou cerca de 44 vagas únicas:

- 23 mais próximas de entrada ou júnior;
- 8 intermediárias;
- 13 aspiracionais ou seniores, usadas para enxergar a evolução futura.

Nas vagas de entrada, os sinais mais frequentes foram Python, Machine Learning, SQL, comunicação com stakeholders, pipelines, estatística, BI, cloud e experimentação. No conjunto completo cresceram também MLOps, LLM/RAG, causalidade, governança, ranking, Spark, APIs, deep learning e visão computacional.

## Conteúdos adicionados

- Python profissional com OOP, dataclasses, tipos, módulos e profiling;
- modelagem dimensional, grão, fatos, dimensões e SCD;
- performance SQL com EXPLAIN, índices, partições e custo;
- Power BI com modelo estrela, DAX, contexto de filtro e performance;
- Product Analytics com tracking plan, eventos, North Star, funil, ativação, retenção, cohorts e LTV;
- experimentação avançada com SRM, testes múltiplos, CUPED e desenho sequencial;
- inferência causal com DAG, propensity score, matching, IPW, diferenças em diferenças, estudo de evento e controle sintético;
- NLP clássico, NER e avaliação multilíngue;
- entity matching, deduplicação, blocking, embeddings, candidate generation e ranking;
- sistemas de recomendação com popularidade, conteúdo, feedback implícito, cold start, split temporal e métricas Top-K;
- PyTorch e visão computacional;
- execução prática em GCP, Cloud Storage e BigQuery;
- DAG real em Apache Airflow.
- Excel analítico e Power Query para reconciliação, transformação e atualização reproduzível;
- consumo de APIs REST com paginação, autenticação segura, timeout, retry, rate limit, cache e carga incremental;
- dbt e Analytics Engineering com camadas de transformação, testes, documentação e linhagem;
- case técnico cronometrado integrando Excel, SQL, Python e Power BI.

## Conteúdos aprofundados

- XGBoost permanece obrigatório no benchmark tabular;
- aprendizado não supervisionado mantém K-Means, PCA e DBSCAN com avaliação e interpretação;
- avaliação de ML passa a exigir baseline, slices, calibração, custo e análise de erros;
- séries temporais exigem backtest rolling-origin e comparação com baseline ingênuo;
- engenharia de dados exige contrato, idempotência, qualidade, backfill e observabilidade;
- MLOps exige MLflow, serviço, CI, monitoramento, retreino, champion/challenger e rollback;
- RAG exige baseline lexical, recuperação, fontes, recusa, conjunto de avaliação, latência e custo;
- inglês aparece como aplicação profissional nas entregas, sem duplicar Duolingo ou filmes.

## Escolhas de foco

O roadmap escolhe uma ferramenta principal por categoria para permitir profundidade e evidência:

- deep learning: PyTorch;
- cloud e warehouse: GCP e BigQuery;
- orquestração: Apache Airflow;
- tracking de experimentos: MLflow;
- BI: Power BI;
- boosting tabular: XGBoost.

Não foram adicionadas trilhas paralelas de TensorFlow, AWS, Azure, Snowflake, SAS ou R. Essas ferramentas podem ser aprendidas depois por transferência de conceito, quando uma vaga específica exigir.

## Direção estratégica

O crescimento de Engenharia de IA e Big Data reforça a direção do roadmap, mas não justifica começar por agentes ou modelos sem dominar a base. Python e SQL permanecem profundos o suficiente para uma candidatura júnior porque avançam de lógica e manipulação de dados até APIs, testes, modelagem, consultas analíticas e desempenho. Estatística e Machine Learning cobrem desenho de avaliação, baselines, incerteza, análise de erros e decisão por custo. Só depois entram Spark, cloud, MLOps, NLP, embeddings, LLMs e RAG.

O risco principal não é falta de assuntos, e sim atravessar as sessões rápido demais sem conseguir alterar e explicar os artefatos. A nota mínima 3 e os cases sem gabarito funcionam como controle de profundidade: concluir o calendário não vale como domínio se a evidência ainda depender de cópia.

A estratégia de candidatura usa um funil, não um único título. Analista de Dados/BI, auxiliar de dados, Cientista de Dados Júnior e funções iniciais de ML são portas de entrada coerentes com a base construída. Engenharia de IA permanece como direção de crescimento: os projetos de entity matching, RAG, APIs e MLOps criam evidência para essa transição, sem fingir que um título que costuma exigir experiência anterior virou vaga de entrada.

## Credenciais e evidência

Foram selecionadas cinco conquistas gratuitas alinhadas ao conteúdo: trilhas do Microsoft Learn, dbt Fundamentals, Google Skills, Databricks Fundamentals Accreditation e EF SET de quatro habilidades. O roadmap registra o nome exato de cada conquista, mas não chama curso ou badge de certificação profissional. As provas profissionais PL-300, dbt Analytics Engineering Certification Exam e Databricks Certified continuam pagas e não são exigidas.

Cada conquista gratuita terá preparação prática e simulado sem respostas. Ela só será adicionada ao LinkedIn após a conclusão real e com a categoria correta; o projeto produzido permanece como evidência mais importante do que o badge isolado.

## Produtos de portfólio

O currículo concentra as entregas em cinco produtos que evoluem:

1. Telecom Customer Intelligence;
2. Energy ForecastOps;
3. Entity Matching Lab;
4. Intelligent Support Operations;
5. Portfolio Intelligence Lab.

Cada entrega exige problema e usuário definidos, data card, baseline, métricas escolhidas antes do resultado, análise de erros, testes, reprodução curta, README em português e inglês, apresentação curta em inglês e conclusão honesta.

## Tema escolhido para o TCC

O TCC passa a ser **Do risco de churn ao efeito incremental: priorização de campanhas de retenção em telecom sob restrição de capacidade**. A escolha conecta a experiência profissional em telecom às exigências recorrentes de classificação, experimentação, decisão por custo, monitoramento e MLOps encontradas nas vagas.

O núcleo compara regra de negócio, regressão logística e XGBoost na mesma data de decisão, horizonte e capacidade de contato. Um piloto randomizado sintético demonstra a diferença entre alto risco de churn e resposta causada pela intervenção, sem apresentar a simulação como impacto real. O MLOps fica limitado a MLflow, testes críticos, monitoramento temporal, champion/challenger, retreinamento e rollback.

O Portfolio Intelligence Lab continua obrigatório como projeto financeiro independente; deixa de ser o TCC.

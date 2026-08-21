# Telecom Customer Intelligence

Projeto obrigatório e incremental de Product Analytics, inferência causal,
Machine Learning tabular e MLOps aplicado a uma operadora de telecomunicações.
Os arquivos deste diretório fornecem o problema, os contratos e os critérios;
a implementação faz parte dos exercícios do roadmap.

Documentos: [dados](data_card.md), [backlog](backlog.md),
[apresentação em inglês](docs/presentation-en.md) e
[versão em inglês](README.en.md). A [entrega do TCC](entrega-tcc/README.md)
congela a pesquisa final de priorização de retenção. As entradas vêm dos
[dados compartilhados](../../dados/README.md).

## Problema e usuários

O produto deve ajudar duas pessoas:

- Product Manager: entender ativação, retenção, churn, reclamações e receita;
- gerente de retenção/operações: priorizar ações dentro de uma capacidade
  limitada e medir se uma intervenção produziu impacto.

## Dados

Use somente informações disponíveis antes da data de decisão. As fontes
iniciais ficam em ../../dados/:

- clientes_telecom.csv;
- clientes.csv e planos.csv;
- chamados.csv e pagamentos.csv;
- incidentes.csv e metas_cidades.csv.

Não edite os CSVs compartilhados. Grave derivados em data/processed/ e
documente cada transformação em data_card.md.

## Entregas obrigatórias

### 1. Product Analytics

1. Defina uma árvore de métricas com ativação, retenção, churn, NPS, receita,
   atrasos e chamados.
2. Construa consultas SQL e uma pipeline Python que reconciliem os mesmos
   totais.
3. Analise cohorts, cidade, plano e canal sem esconder o tamanho das amostras.
4. Entregue dashboard, relatório executivo e três recomendações verificáveis.

### 2. Impacto causal

1. Declare intervenção, unidade, período, desfecho e hipótese antes da análise.
2. Compare o baseline ingênuo antes/depois com diferenças em diferenças.
3. Faça diagnóstico de tendências paralelas, estudo de evento, placebos e
   controle sintético.
4. Recuse linguagem causal quando as premissas não forem sustentadas.

### 3. ML tabular para retenção

1. Implemente uma regra de negócio e regressão logística como baselines.
2. Compare Random Forest e XGBoost ou LightGBM.
3. Use split temporal, pipeline de pré-processamento e busca de limiar por
   capacidade/custo.
4. Avalie PR-AUC, recall no Top-K, calibração, custo e segmentos.

### 4. Engenharia de dados e MLOps

1. Construa ETL idempotente, contrato de dados e tabela de features.
2. Registre experimentos e modelos no MLflow.
3. Sirva a política por FastAPI e Docker.
4. Adicione CI, logs, drift, simulação de retreinamento e rollback.
5. Execute uma transformação no BigQuery Sandbox e reconcilie-a com a versão
   local em DuckDB.

### 5. TCC — retenção sob capacidade limitada

1. Congele data de decisão, horizonte de churn, capacidade de contato e custos antes de comparar políticas.
2. Compare regra de negócio, regressão logística e XGBoost no mesmo split e nas mesmas métricas.
3. Use um piloto randomizado sintético, claramente identificado como simulação, para estudar resposta incremental sem alegar impacto real.
4. Avalie PR-AUC, recall no Top-K, calibração, custo, ganho por 100 contatos e desempenho por segmentos.
5. Demonstre somente o MLOps essencial: MLflow, testes críticos, monitoramento temporal, champion/challenger, retreinamento e rollback.
6. Siga o escopo e os critérios em [entrega-tcc/README.md](entrega-tcc/README.md).

## Baselines e regra de decisão

O método avançado nunca é considerado melhor apenas por ser mais complexo.
Defina previamente a métrica principal, capacidade operacional e custo dos
erros. Se nenhum método superar o baseline de maneira útil e estável, entregue
o baseline e documente o resultado negativo.

## Estrutura esperada

- data/raw/: manifesto ou snapshots adicionais permitidos;
- data/processed/: tabelas geradas;
- src/telecom_customer_intelligence/: código reutilizável;
- tests/: testes de dados, tempo, métricas, API e rollback;
- docs/: relatórios, diagramas e apresentações;
- outputs/: métricas e figuras reproduzíveis.

## Concluído quando

- [ ] Um ambiente limpo reproduz dados processados, métricas e artefatos.
- [ ] SQL, Python, dashboard e relatório apresentam totais reconciliados.
- [ ] Nenhuma feature utiliza informação posterior à decisão.
- [ ] Baselines, modelos, limiar e custos estão comparados.
- [ ] Há análise de erros e desempenho por pelo menos dois segmentos.
- [ ] Testes de dados, pipeline, métricas e contrato passam.
- [ ] Retreinamento e rollback foram simulados e registrados.
- [ ] README.en.md e docs/presentation-en.md refletem resultados reais.

## Limites

Os dados são sintéticos e pequenos. O projeto demonstra método e comunicação,
não prova impacto em uma operadora real. Não publique métricas antes de executar
a própria solução.

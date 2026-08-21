# TCC — pré-projeto e banca zero sobre retenção incremental

**Data de estudo:** 18/01/2027  
**Carga planejada:** 4 a 5 horas

## Tema congelado

**Do risco de churn ao efeito incremental: priorização de campanhas de retenção em telecom sob restrição de capacidade**

O TCC deve responder duas perguntas diferentes: quem apresenta maior risco de churn e qual efeito incremental uma campanha produz. Prever risco não prova resposta ao tratamento; essa distinção precisa aparecer desde o pré-projeto.

## Assuntos para pesquisar

Pesquise exatamente:

- `churn prediction retention campaign capacity constraint`
- `randomized experiment incremental treatment effect retention`
- `PR-AUC recall at K probability calibration churn`
- `cost per retained customer campaign evaluation`
- `machine learning project scope pre registration`

Depois siga o [guia e o enunciado](<modulos/01-e133/README.md>) e preencha o roteiro sem copiar texto pronto.

## Escopo obrigatório

- data de decisão, horizonte do churn e capacidade máxima de contatos;
- regra de negócio, regressão logística e XGBoost;
- piloto sintético randomizado, identificado em toda publicação como simulação;
- PR-AUC, recall@K, calibração, custo por retenção, efeito com intervalo de confiança, ganho por 100 contatos e slices;
- MLflow, testes, monitoramento temporal, champion/challenger, retreino e rollback.

## Fora do escopo

Controle sintético, múltiplas nuvens, LLMs, entity matching, forecasting e aplicação grande. Não acrescente esses itens na banca.

## Concluído quando

- [ ] O pré-projeto separa predição de risco e inferência do efeito da campanha.
- [ ] Data de decisão, horizonte, capacidade, métricas e custos foram congelados antes dos resultados.
- [ ] Dados e piloto estão descritos honestamente como sintéticos, e a banca zero gerou cortes ou critérios verificáveis sem ampliar o escopo.

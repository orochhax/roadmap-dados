# TCC — modelos de risco e priorização sob capacidade

**Data de estudo:** 19/04/2027
**Carga planejada:** 4 a 5 horas

## Objetivo do dia

Comparar uma regra de negócio, regressão logística e XGBoost no mesmo protocolo temporal. A saída é um ranking de risco limitado à capacidade `K`, não uma estimativa de quem responderá à campanha.

## Atividades do dia

Pesquise exatamente:

- `churn prediction business rule baseline logistic regression XGBoost`
- `imbalanced classification PR-AUC churn`
- `recall at K capacity constrained targeting`
- `probability calibration reliability diagram Brier score`
- `MLflow log model parameters metrics artifacts`
- `model performance slices fairness sample size`

Siga o guia e o roteiro disponíveis abaixo e use somente os métodos de retenção previstos no escopo.

### Conteúdo e atividades — TCC — benchmark preditivo e ranking de risco

**Arquivos da atividade:** [abrir a pasta `01-tcc-benchmark-preditivo-e-ranking-de-risco`](<atividades/01-tcc-benchmark-preditivo-e-ranking-de-risco/>)

#### Objetivo

Construir uma comparação justa entre três políticas de priorização e escolher champion/challenger com evidência. O ranking opera somente sobre clientes elegíveis e respeita a capacidade congelada no pré-projeto.

#### Arquivos e dados

- **Enunciado local:** `atividades/01-tcc-benchmark-preditivo-e-ranking-de-risco/roteiro_tcc.md`.
- **Projeto canônico:** `projetos/telecom-customer-intelligence/`.
- **Entrada:** snapshot sintético, splits temporais e contrato de features previamente congelado.
- **Saídas esperadas:** pipeline em `src/telecom_customer_intelligence/modeling.py`, benchmark em `outputs/`, runs no MLflow e model card do TCC.

#### Pesquise exatamente

- `scikit-learn Pipeline ColumnTransformer leakage`
- `business rule baseline machine learning comparison`
- `logistic regression calibrated probabilities churn`
- `XGBoost imbalanced classification scale_pos_weight`
- `average precision PR AUC versus ROC AUC imbalance`
- `top k recall lift targeting campaign`
- `MLflow champion challenger model comparison`

#### O que fazer

- [ ] Reproduza uma regra de negócio simples e auditável como baseline.
- [ ] Treine regressão logística e XGBoost no mesmo split, pipeline e features disponíveis.
- [ ] Escolha hiperparâmetros e calibração somente com treino/validação.
- [ ] Registre em MLflow dados/versão, seed, parâmetros, PR-AUC, recall@K, calibração, latência e artefatos.
- [ ] Avalie uma única vez no teste temporal congelado.
- [ ] Analise erros e slices por plano, região, tempo de contrato e outra dimensão justificada, sempre exibindo tamanho da amostra.
- [ ] Escolha champion e challenger considerando qualidade, calibração, estabilidade, explicabilidade e custo.

#### Regras de decisão

- `K` vem da capacidade operacional e não pode ser escolhido para maximizar o teste.
- Um modelo complexo só vence se produzir ganho útil e estável sobre a regra.
- Score de churn não é score de efeito do tratamento.
- Slices pequenos devem ser descritos como inconclusivos.
- Nenhum resultado sintético deve ser apresentado como impacto observado em operadora real.

#### Casos de borda

- mês sem positivo ou com poucos churns;
- categoria desconhecida e nulos no teste;
- `K` maior que a população elegível;
- scores empatados;
- diferença grande entre validação e teste;
- slice pequeno ou calibração ruim.

#### Como validar

- Os três candidatos foram comparados com protocolo comum e reproduzível.
- Runs e artefatos do MLflow permitem reconstruir a escolha.
- Ranking Top-K, erros, slices e calibração foram auditados.
- Champion/challenger e condição de rollback estão documentados.

## Integração do dia

Os três modelos usam o contrato temporal congelado no protocolo. O ranking define quem seria elegível para contato dentro da capacidade. O efeito do contato pertence ao piloto randomizado simulado e não pode ser inferido pelo ranking de risco.

## Finalização

Antes de concluir, confirme:

- Regra, logística e XGBoost foram comparados no mesmo split e métricas.
- PR-AUC, recall@K, calibração, latência e slices foram registrados no MLflow.
- Champion e challenger foram escolhidos com trade-offs e critério de rollback, e o relatório não confunde risco previsto com efeito incremental.

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

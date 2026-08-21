# TCC — benchmark preditivo e ranking de risco

## Objetivo

Construir uma comparação justa entre três políticas de priorização e escolher champion/challenger com evidência. O ranking opera somente sobre clientes elegíveis e respeita a capacidade congelada no pré-projeto.

## Preparação

- **Enunciado local:** `01-exercicios/roteiro_tcc.md`.
- **Projeto canônico:** `projetos/telecom-customer-intelligence/`.
- **Entrada:** snapshot sintético, splits temporais e contrato de features do dia 19/01.
- **Saídas esperadas:** pipeline em `src/telecom_customer_intelligence/modeling.py`, benchmark em `outputs/`, runs no MLflow e model card do TCC.

## Pesquise exatamente

- `scikit-learn Pipeline ColumnTransformer leakage`
- `business rule baseline machine learning comparison`
- `logistic regression calibrated probabilities churn`
- `XGBoost imbalanced classification scale_pos_weight`
- `average precision PR AUC versus ROC AUC imbalance`
- `top k recall lift targeting campaign`
- `MLflow champion challenger model comparison`

## Núcleo essencial

1. [ ] Reproduza uma regra de negócio simples e auditável como baseline.
2. [ ] Treine regressão logística e XGBoost no mesmo split, pipeline e features disponíveis.
3. [ ] Escolha hiperparâmetros e calibração somente com treino/validação.
4. [ ] Registre em MLflow dados/versão, seed, parâmetros, PR-AUC, recall@K, calibração, latência e artefatos.
5. [ ] Avalie uma única vez no teste temporal congelado.
6. [ ] Analise erros e slices por plano, região, tempo de contrato e outra dimensão justificada, sempre exibindo tamanho da amostra.
7. [ ] Escolha champion e challenger considerando qualidade, calibração, estabilidade, explicabilidade e custo.

## Regras de decisão

- `K` vem da capacidade operacional e não pode ser escolhido para maximizar o teste.
- Um modelo complexo só vence se produzir ganho útil e estável sobre a regra.
- Score de churn não é score de efeito do tratamento.
- Slices pequenos devem ser descritos como inconclusivos.
- Nenhum resultado sintético deve ser apresentado como impacto observado em operadora real.

## Casos de borda

- mês sem positivo ou com poucos churns;
- categoria desconhecida e nulos no teste;
- `K` maior que a população elegível;
- scores empatados;
- diferença grande entre validação e teste;
- slice pequeno ou calibração ruim.

## Concluído quando

- [ ] Os três candidatos foram comparados com protocolo comum e reproduzível.
- [ ] Runs e artefatos do MLflow permitem reconstruir a escolha.
- [ ] Ranking Top-K, erros, slices e calibração foram auditados.
- [ ] Champion/challenger e condição de rollback estão documentados.

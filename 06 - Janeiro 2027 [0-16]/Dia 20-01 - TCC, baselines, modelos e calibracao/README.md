# TCC — modelos de risco e priorização sob capacidade

**Data de estudo:** 20/01/2027  
**Carga planejada:** 4 a 5 horas

## Objetivo do dia

Comparar uma regra de negócio, regressão logística e XGBoost no mesmo protocolo temporal. A saída é um ranking de risco limitado à capacidade `K`, não uma estimativa de quem responderá à campanha.

## Assuntos para pesquisar

Pesquise exatamente:

- `churn prediction business rule baseline logistic regression XGBoost`
- `imbalanced classification PR-AUC churn`
- `recall at K capacity constrained targeting`
- `probability calibration reliability diagram Brier score`
- `MLflow log model parameters metrics artifacts`
- `model performance slices fairness sample size`

Siga o [guia e o roteiro](<modulos/01-e135/README.md>) e use somente os métodos de retenção previstos no escopo.

## Integração

Os três modelos usam o contrato temporal congelado no protocolo. O ranking define quem seria elegível para contato dentro da capacidade. O efeito do contato pertence ao piloto randomizado simulado e não pode ser inferido pelo ranking de risco.

## Concluído quando

- [ ] Regra, logística e XGBoost foram comparados no mesmo split e métricas.
- [ ] PR-AUC, recall@K, calibração, latência e slices foram registrados no MLflow.
- [ ] Champion e challenger foram escolhidos com trade-offs e critério de rollback, e o relatório não confunde risco previsto com efeito incremental.

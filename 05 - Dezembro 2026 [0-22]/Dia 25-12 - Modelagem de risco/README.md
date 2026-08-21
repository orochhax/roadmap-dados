# Modelagem de risco

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-083-modelagem-de-risco.ipynb`.
- **Dados:** `dados/credito.csv`.

## Aprenda agora

- **Definição:** ROC-AUC mede ordenação geral; PR-AUC enfatiza a classe rara; KS é a maior separação entre distribuições; calibração avalia probabilidades.
- **Exemplo mínimo:** compare os modelos na mesma janela com `ROC-AUC, PR-AUC, KS` e curva de calibração, sempre com suporte.
- **Erro comum:** escolher só ROC-AUC em evento raro ou interpretar KS como qualidade de probabilidade.

## Núcleo essencial

1. [ ] Treine regressão logística como scorecard básico e modelos de árvore.
2. [ ] Avalie ROC-AUC, PR-AUC, KS, calibração e matriz de confusão.
3. [ ] Faça validação temporal, não apenas aleatória.

## Prática obrigatória

- [ ] Analise estabilidade e desempenho por segmentos.
- [ ] Escolha modelo explicável compatível com política de crédito.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-083-modelagem-de-risco.ipynb`:** Compare calibração e KS no conjunto temporal final para logística e o melhor modelo de árvore.
- [ ] **Em `01-exercicios/dia-083-modelagem-de-risco.ipynb`:** Calcule as métricas separadamente para contratos com prazo até 12 meses e acima de 24 meses.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-083-modelagem-de-risco.ipynb` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

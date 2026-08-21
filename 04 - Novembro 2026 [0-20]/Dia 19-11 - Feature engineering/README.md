# Feature engineering

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-061-feature-engineering.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

## Aprenda agora

- **Definição:** um transformer encapsula uma transformação em `fit/transform`; ablação mede o efeito de retirar uma feature ou grupo.
- **Exemplo mínimo:** compare a mesma pipeline com e sem `tempo_cliente × gasto_mensal` e registre `delta = métrica_com - métrica_sem`.
- **Erro comum:** calcular a feature com dados de avaliação ou retirar várias features de uma vez.

## Núcleo essencial

1. [ ] Crie pelo menos oito features de churn agrupadas em comportamento, financeiro, suporte e relacionamento.
2. [ ] Defina para cada feature: fórmula, fonte, momento de disponibilidade e risco de leakage.
3. [ ] Implemente features em funções ou transformer customizado.

## Prática obrigatória

- [ ] Faça análise de ablação por grupo.
- [ ] Elimine features que dependam do futuro ou duplicam o alvo.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-061-feature-engineering.ipynb`:** Crie a feature chamados_por_mes usando somente chamados anteriores à data de referência e documente a fórmula.
- [ ] **Em `01-exercicios/dia-061-feature-engineering.ipynb`:** Remova todas as features financeiras e refaça a ablação no mesmo split para medir a perda de desempenho.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-061-feature-engineering.ipynb` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

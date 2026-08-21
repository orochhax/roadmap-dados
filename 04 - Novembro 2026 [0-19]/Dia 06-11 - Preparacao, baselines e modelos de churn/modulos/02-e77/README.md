# Baselines e modelos

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-071-baselines-e-modelos.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

## Aprenda agora

- **Definição:** champion é escolhido por regra declarada; challenger é alternativa comparável. A regra pode combinar métrica, custo, estabilidade e explicabilidade.
- **Exemplo mínimo:** `score = 0.5*AUC + 0.3*(1-custo_norm) + 0.2*estabilidade`; fixe pesos antes da comparação.
- **Erro comum:** trocar a regra para favorecer o vencedor.

## Núcleo essencial

1. [ ] Treine regressão logística e um modelo de árvore usando a mesma pipeline e validação.
2. [ ] Compare média, desvio, custo e tempo em uma tabela única.
3. [ ] Analise dez erros críticos e escolha campeão e challenger com critérios definidos antes do resultado.

## Prática obrigatória

- [ ] Amplie a análise para 20 erros críticos e registre se os padrões encontrados nos dez primeiros permanecem.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-071-baselines-e-modelos.ipynb`:** Compare campeão e challenger no segmento plano Básico 100 e registre tamanho, custo, recall e precision.
- [ ] **Em `01-exercicios/dia-071-baselines-e-modelos.ipynb`:** Aumente o custo de falso negativo de R$500 para R$800 e confira se a escolha do campeão muda.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-071-baselines-e-modelos.ipynb` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

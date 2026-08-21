# Seleção de variáveis

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-063-selecao-de-variaveis.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

## Aprenda agora

- **Definição:** seleção univariada avalia uma variável por vez; importância usa o modelo; RFE elimina iterativamente; near-constant encontra colunas quase invariáveis.
- **Exemplo mínimo:** ajuste o seletor em `X_train`, transforme treino e validação e compare métrica, colunas e tempo.
- **Erro comum:** selecionar com a base completa ou tratar importância como causalidade.

## Núcleo essencial

1. [ ] Remova colunas constantes, quase constantes e duplicadas.
2. [ ] Calcule correlação entre numéricas e identifique grupos redundantes.
3. [ ] Compare seleção univariada, importância de modelo e RFE em subconjunto pequeno.

## Prática obrigatória

- [ ] Treine modelo com todas as features e com seleção; compare métrica e estabilidade.
- [ ] Documente por que feature selecionada não implica causalidade.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-063-selecao-de-variaveis.ipynb`:** Compare remoção de correlações acima de 0,90 e 0,75 e registre quantidade de features e métrica.
- [ ] **Em `01-exercicios/dia-063-selecao-de-variaveis.ipynb`:** Adicione uma cópia exata de uma coluna, faça a detecção removê-la e confirme que a original permanece.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-063-selecao-de-variaveis.ipynb` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

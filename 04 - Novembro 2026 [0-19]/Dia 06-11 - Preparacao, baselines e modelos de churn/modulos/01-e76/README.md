# Preparação para modelagem

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/roteiro_atividades.md`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

## Aprenda agora

- **Definição:** preparação fixa alvo, unidade, corte, imputação e codificação dentro da pipeline; baseline mede o ganho mínimo.
- **Exemplo mínimo:** `fit` ocorre no treino anterior ao corte; validação recebe somente `transform`.
- **Erro comum:** imputar, escalar ou codificar com estatísticas da base completa.

## Núcleo essencial

1. [ ] Defina corte temporal e conjuntos de treino, validação e teste.
2. [ ] Construa pipeline de imputação, codificação e escala sem usar dados futuros.
3. [ ] Crie baseline de negócio e DummyClassifier.
4. [ ] Defina métricas técnicas e custo de decisão.

## Prática obrigatória

- [ ] Salve um `data_card.md` com origem, período, população, exclusões e limitações.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Compare o baseline de negócio chamados_90d>=3 com o DummyClassifier usando a métrica e o custo definidos.
- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Altere o corte temporal em 30 dias e confira se nenhuma data posterior entrou no conjunto de treino.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/roteiro_atividades.md` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

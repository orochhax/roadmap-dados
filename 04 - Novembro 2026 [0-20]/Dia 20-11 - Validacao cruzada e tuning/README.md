# Validação cruzada e tuning

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-062-validacao-cruzada-e-tuning.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

## Aprenda agora

- **Definição:** `KFold` divide observações; `StratifiedKFold` preserva o alvo; validação temporal respeita a ordem. Tuning usa apenas treino e validação.
- **Exemplo mínimo:** classificação desbalanceada usa `StratifiedKFold(5, shuffle=True, random_state=42)`; séries usam cortes crescentes sem embaralhar.
- **Erro comum:** escolher hiperparâmetros pelo teste; mantenha-o isolado até a avaliação final.

## Núcleo essencial

1. [ ] Compare KFold, StratifiedKFold e validação temporal em um exemplo apropriado.
2. [ ] Execute cross-validation com cinco folds e registre média e desvio das métricas.
3. [ ] Faça `RandomizedSearchCV` com espaço pequeno e limite de tempo.

## Prática obrigatória

- [ ] Separe conjunto de teste final e não o use durante tuning.
- [ ] Compare melhor configuração com padrão e avalie se ganho compensa complexidade.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-062-validacao-cruzada-e-tuning.ipynb`:** Compare StratifiedKFold com 3 e 5 folds usando a mesma pipeline e registre média, desvio e tempo.
- [ ] **Em `01-exercicios/dia-062-validacao-cruzada-e-tuning.ipynb`:** Confirme no código que o conjunto de teste final não aparece em fit, busca de parâmetros ou escolha da configuração.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-062-validacao-cruzada-e-tuning.ipynb` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

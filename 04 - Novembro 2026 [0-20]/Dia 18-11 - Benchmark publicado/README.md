# Benchmark publicado

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/roteiro_atividades.md`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

## Aprenda agora

- **Definição:** benchmark é um protocolo de comparação: mesmos dados, divisão, pré-processamento e métricas para todos os modelos; o Dummy mostra o mínimo que um modelo útil precisa superar.
- **Exemplo mínimo:** fixe `random_state=42`, treine todos no mesmo `X_train, y_train` e salve `modelo, métrica, tempo_ms` em uma única tabela.
- **Erro comum:** mudar o split ou ajustar o pré-processamento com todos os dados; isso torna as métricas incomparáveis e pode vazar informação da avaliação.

## Núcleo essencial

1. [ ] Compare obrigatoriamente Dummy, regressão logística, Random Forest e XGBoost usando o mesmo split, pré-processamento e protocolo.
2. [ ] Registre biblioteca, versão, seed, métricas primária e secundária, tempo de treino e tempo de inferência de cada modelo.
3. [ ] Salve os resultados em `benchmark.csv` e os hiperparâmetros em `parametros.json`.
4. [ ] Escolha champion e challenger e defenda a decisão com qualidade, custo, latência, explicabilidade e três trade-offs.

## Atualização do LinkedIn — após concluir

- **Evidência exigida:** `benchmark.csv` reproduzível com uma linha executada de XGBoost e comparação justa entre os quatro modelos.
- **Competências:** adicione **XGBoost** e **Avaliação de modelos**.
- **Sobre e headline:** não altere ainda; a revisão de posicionamento ocorrerá após a auditoria completa do pipeline.

## Prática obrigatória

- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Reexecute o benchmark com random_state=17 além de 42 e acrescente as métricas à mesma tabela, sem sobrescrever a primeira rodada.
- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Compare tamanho em disco e tempo de inferência de logística e Random Forest em 100 previsões.

## Concluído quando

- [ ] O núcleo foi executado e `benchmark.csv` contém Dummy, regressão logística, Random Forest e XGBoost.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

---

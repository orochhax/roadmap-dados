# Baselines temporais

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-077-baselines-temporais.ipynb`.
- **Dados:** `dados/energia.csv`.

## Aprenda agora

- **Definição:** walk-forward treina em uma janela e avalia no bloco seguinte; MAE mede erro absoluto, RMSE penaliza erros grandes, MAPE/SMAPE medem erro relativo.
- **Exemplo mínimo:** `MAE = mean(abs(y - y_hat))`; compare média histórica, último valor e sazonal ingênuo nos mesmos cortes.
- **Erro comum:** usar MAPE com zeros ou comparar baselines em horizontes diferentes.

## Núcleo essencial

1. [ ] Implemente baselines: último valor, média móvel de 7 dias, média do mesmo dia da semana e média sazonal.
2. [ ] Use validação walk-forward em pelo menos três janelas.
3. [ ] Calcule MAE, RMSE e MAPE/SMAPE quando adequado.

## Prática obrigatória

- [ ] Compare desempenho por períodos de alta e baixa demanda.
- [ ] Escolha baseline oficial que qualquer modelo deve superar.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-077-baselines-temporais.ipynb`:** Compare horizonte de 7 e 14 dias nas mesmas três janelas walk-forward e registre MAE por horizonte.
- [ ] **Em `01-exercicios/dia-077-baselines-temporais.ipynb`:** Avalie o baseline oficial separadamente em dias úteis e fins de semana.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-077-baselines-temporais.ipynb` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

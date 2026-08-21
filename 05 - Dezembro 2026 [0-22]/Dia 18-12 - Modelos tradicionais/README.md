# Modelos tradicionais

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-078-modelos-tradicionais.ipynb`.
- **Dados:** `dados/energia.csv`.

## Aprenda agora

- **Definição:** Holt-Winters modela nível, tendência e sazonalidade; ARIMA combina autoregressão, diferenciação e erro móvel; resíduo é `y - y_hat`.
- **Exemplo mínimo:** escolha um modelo, ajuste somente no treino e verifique resíduos nos lags 1 e 7 em cortes walk-forward.
- **Erro comum:** escolher ordem ou sazonalidade pelo teste final e ignorar autocorrelação residual.

## Núcleo essencial

1. [ ] Treine regressão linear com lags, árvore/Random Forest e modelo estatístico simples como Holt-Winters ou ARIMA, se disponível.
2. [ ] Garanta que features sejam criadas respeitando tempo.
3. [ ] Faça backtesting com múltiplos cortes.

## Prática obrigatória

- [ ] Compare erro e estabilidade por horizonte.
- [ ] Analise resíduos e autocorrelação remanescente.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-078-modelos-tradicionais.ipynb`:** Adicione um quarto corte ao backtesting e compare a estabilidade de Random Forest e Holt-Winters.
- [ ] **Em `01-exercicios/dia-078-modelos-tradicionais.ipynb`:** Meça autocorrelação dos resíduos nos lags 1 e 7 e registre qual padrão ainda não foi capturado.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-078-modelos-tradicionais.ipynb` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

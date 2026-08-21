# Fundamentos temporais

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-076-fundamentos-temporais.ipynb`.
- **Dados:** `dados/energia.csv`.

## Aprenda agora

- **Definição:** tendência é movimento de longo prazo, sazonalidade é padrão repetido e ruído é variação não explicada; lag desloca uma série e ACF mede autocorrelação.
- **Exemplo mínimo:** `df["lag_7"] = df["y"].shift(7)` e `df["y"].autocorr(lag=7)`; confira também frequência e datas ausentes.
- **Erro comum:** criar lag após embaralhar ou preencher lacunas sem registrar a regra.

## Núcleo essencial

1. [ ] Carregue `energia.csv`, converta índice temporal e verifique frequência, lacunas e duplicidades.
2. [ ] Separe tendência, sazonalidade e ruído por gráficos e médias móveis.
3. [ ] Calcule autocorrelação em atrasos 1, 7 e 30.

## Prática obrigatória

- [ ] Crie features de calendário e lags sem olhar o futuro.
- [ ] Defina horizonte de previsão e decisão operacional associada.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-076-fundamentos-temporais.ipynb`:** Remova sete dias consecutivos de uma cópia da série e mostre como a verificação de frequência identifica a lacuna.
- [ ] **Em `01-exercicios/dia-076-fundamentos-temporais.ipynb`:** Crie lags 1, 7 e 30 e confirme que cada linha usa somente datas anteriores à própria data.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-076-fundamentos-temporais.ipynb` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

# Fundamentos temporais + Baselines temporais

**Data de estudo:** 19/11/2026  
**Carga planejada:** 4 a 5 horas

## Aulas selecionadas no YouTube

Sequência do **Professor Vinicius Lima**:

- [ ] **Séries Temporais: Conceitos Básicos 01** (14:36) — [abrir no YouTube](https://www.youtube.com/watch?v=rexHHx6Nwec).
- [ ] **Séries Temporais: Conceitos Básicos 02** (11:37) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=Series+Temporais+Conceitos+Basicos+02+Professor+Vinicius+Lima).
- [ ] **Séries Temporais: Conceitos Básicos 03** (7:01) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=Series+Temporais+Conceitos+Basicos+03+Professor+Vinicius+Lima).
- [ ] **Séries Temporais: Conceitos Básicos 04** (24:03) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=Series+Temporais+Conceitos+Basicos+04+Professor+Vinicius+Lima).
- [ ] **Séries Temporais: Conceitos Básicos 05** (10:18) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=Series+Temporais+Conceitos+Basicos+05+Professor+Vinicius+Lima).
- [ ] **Séries Temporais: Conceitos Básicos 06** (2:51) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=Series+Temporais+Conceitos+Basicos+06+Professor+Vinicius+Lima).
- [ ] **Componentes de uma série temporal** (19:48) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=Componentes+de+uma+serie+temporal+Professor+Vinicius+Lima).
- [ ] **Estacionariedade 1** (10:00) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=Estacionariedade+1+Professor+Vinicius+Lima).
- [ ] **Função autocorrelação amostral 01** (18:50) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=Funcao+autocorrelacao+amostral+01+Professor+Vinicius+Lima).

**Carga de vídeo selecionada:** aproximadamente 1h59.

**Prática obrigatória:** verifique frequência e lacunas, crie lags sem futuro, implemente baselines e faça walk-forward nos notebooks. A teoria não substitui o backtesting.

## Atividades do dia

### Atividade 1 — Fundamentos temporais

#### O que pesquisar
- `Fundamentos temporais Python explicado passo a passo`
- `Fundamentos temporais Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-fundamentos-temporais`](<atividades/01-fundamentos-temporais/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-fundamentos-temporais/dia-076-fundamentos-temporais.ipynb`.
- **Dados:** `dados/energia.csv`.

#### O que você precisa entender

- **Definição:** tendência é movimento de longo prazo, sazonalidade é padrão repetido e ruído é variação não explicada; lag desloca uma série e ACF mede autocorrelação.
- **Exemplo mínimo:** `df["lag_7"] = df["y"].shift(7)` e `df["y"].autocorr(lag=7)`; confira também frequência e datas ausentes.
- **Erro comum:** criar lag após embaralhar ou preencher lacunas sem registrar a regra.

#### O que fazer

- [ ] Carregue `energia.csv`, converta índice temporal e verifique frequência, lacunas e duplicidades.
- [ ] Separe tendência, sazonalidade e ruído por gráficos e médias móveis.
- [ ] Calcule autocorrelação em atrasos 1, 7 e 30.

- [ ] Crie features de calendário e lags sem olhar o futuro.
- [ ] Defina horizonte de previsão e decisão operacional associada.


- [ ] **Em `atividades/01-fundamentos-temporais/dia-076-fundamentos-temporais.ipynb`:** Remova sete dias consecutivos de uma cópia da série e mostre como a verificação de frequência identifica a lacuna.
- [ ] **Em `atividades/01-fundamentos-temporais/dia-076-fundamentos-temporais.ipynb`:** Crie lags 1, 7 e 30 e confirme que cada linha usa somente datas anteriores à própria data.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

### Atividade 2 — Baselines temporais

#### O que pesquisar
- `Baselines temporais Python explicado passo a passo`
- `Baselines temporais Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-baselines-temporais`](<atividades/02-baselines-temporais/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-baselines-temporais/dia-077-baselines-temporais.ipynb`.
- **Dados:** `dados/energia.csv`.

#### O que você precisa entender

- **Definição:** walk-forward treina em uma janela e avalia no bloco seguinte; MAE mede erro absoluto, RMSE penaliza erros grandes, MAPE/SMAPE medem erro relativo.
- **Exemplo mínimo:** `MAE = mean(abs(y - y_hat))`; compare média histórica, último valor e sazonal ingênuo nos mesmos cortes.
- **Erro comum:** usar MAPE com zeros ou comparar baselines em horizontes diferentes.

#### O que fazer

- [ ] Implemente baselines: último valor, média móvel de 7 dias, média do mesmo dia da semana e média sazonal.
- [ ] Use validação walk-forward em pelo menos três janelas.
- [ ] Calcule MAE, RMSE e MAPE/SMAPE quando adequado.

- [ ] Compare desempenho por períodos de alta e baixa demanda.
- [ ] Escolha baseline oficial que qualquer modelo deve superar.


- [ ] **Em `atividades/02-baselines-temporais/dia-077-baselines-temporais.ipynb`:** Compare horizonte de 7 e 14 dias nas mesmas três janelas walk-forward e registre MAE por horizonte.
- [ ] **Em `atividades/02-baselines-temporais/dia-077-baselines-temporais.ipynb`:** Avalie o baseline oficial separadamente em dias úteis e fins de semana.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

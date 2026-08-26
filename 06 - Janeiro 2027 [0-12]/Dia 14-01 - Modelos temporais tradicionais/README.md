# Modelos tradicionais

**Data de estudo:** 14/01/2027
**Carga planejada:** 2 a 4 horas

## Aulas selecionadas no YouTube

Sequência do **Professor Vinicius Lima**:

- [ ] **Ruído Branco 1** (21:43) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=Ruido+Branco+1+Professor+Vinicius+Lima).
- [ ] **Processos AR e MA** (15:58) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=Processos+AR+e+MA+Professor+Vinicius+Lima).
- [ ] **Testes para verificar estacionariedade 1** (20:59) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=Testes+para+verificar+estacionariedade+1+Professor+Vinicius+Lima).
- [ ] **Testes para verificar estacionariedade 2** (5:09) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=Testes+para+verificar+estacionariedade+2+Professor+Vinicius+Lima).
- [ ] **Aplicação de Diferenças** (25:18) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=Aplicacao+de+Diferencas+Professor+Vinicius+Lima).
- [ ] **Modelagem de Séries Temporais** (24:28) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=Modelagem+de+Series+Temporais+Professor+Vinicius+Lima).

**Carga de vídeo selecionada:** aproximadamente 1h54.

**Prática obrigatória:** ajuste e compare os modelos no notebook usando os mesmos cortes temporais e o baseline oficial. Registre diagnóstico, métricas, intervalo e falhas; não escolha modelo pela aparência do ajuste.

## Atividades do dia

### Atividade 1 — Modelos tradicionais

#### O que pesquisar
- `Modelos tradicionais machine learning com Python explicado passo a passo`
- `Modelos tradicionais machine learning com Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-modelos-tradicionais`](<atividades/01-modelos-tradicionais/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-modelos-tradicionais/dia-078-modelos-tradicionais.ipynb`.
- **Dados:** `dados/energia.csv`.

#### O que você precisa entender

- **Definição:** Holt-Winters modela nível, tendência e sazonalidade; ARIMA combina autoregressão, diferenciação e erro móvel; resíduo é `y - y_hat`.
- **Exemplo mínimo:** escolha um modelo, ajuste somente no treino e verifique resíduos nos lags 1 e 7 em cortes walk-forward.
- **Erro comum:** escolher ordem ou sazonalidade pelo teste final e ignorar autocorrelação residual.

#### O que fazer

- [ ] Treine regressão linear com lags, árvore/Random Forest e modelo estatístico simples como Holt-Winters ou ARIMA, se disponível.
- [ ] Garanta que features sejam criadas respeitando tempo.
- [ ] Faça backtesting com múltiplos cortes.

- [ ] Compare erro e estabilidade por horizonte.
- [ ] Analise resíduos e autocorrelação remanescente.


- [ ] **Em `atividades/01-modelos-tradicionais/dia-078-modelos-tradicionais.ipynb`:** Adicione um quarto corte ao backtesting e compare a estabilidade de Random Forest e Holt-Winters.
- [ ] **Em `atividades/01-modelos-tradicionais/dia-078-modelos-tradicionais.ipynb`:** Meça autocorrelação dos resíduos nos lags 1 e 7 e registre qual padrão ainda não foi capturado.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

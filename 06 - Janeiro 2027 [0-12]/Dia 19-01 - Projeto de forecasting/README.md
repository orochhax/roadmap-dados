# Projeto de forecasting

**Data de estudo:** 19/01/2027
**Carga planejada:** 2 a 4 horas

## Atividades do dia

### Atividade 1 — Projeto de forecasting

#### O que pesquisar
- `Projeto de forecasting Python explicado passo a passo`
- `Projeto de forecasting Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-projeto-de-forecasting`](<atividades/01-projeto-de-forecasting/>)

#### Conquista para o LinkedIn

- **Competências:** depois de executar o backtesting e defender a validação temporal, adicione **Análise de séries temporais** e **Forecasting**.
- **Projetos ou Destaques:** inclua o projeto com horizonte, baseline, métrica, decisão e limitação.
- O material em inglês comprova prática técnica, não um nível avançado do idioma. Siga o [Guia de LinkedIn e evidências](<../../00 - Recursos Compartilhados/linkedin-e-evidencias.md>).

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-projeto-de-forecasting/roteiro_atividades.md`.
- **Dados:** `dados/energia.csv`.

#### O que você precisa entender

- **Definição:** um projeto temporal reproduzível fixa frequência, horizonte, cortes, baselines, métricas e regra de decisão.
- **Exemplo mínimo:** manifesto com `data_corte, horizonte, coluna_alvo, frequência, métricas, seed`; todos os modelos usam o mesmo manifesto.
- **Erro comum:** alterar cortes entre tabelas ou escolher a melhor janela após olhar toda a série.

#### O que fazer

- [ ] Organize o projeto com dados, notebook ou script, resultados e README.
- [ ] Compare o baseline oficial com um único modelo em backtesting walk-forward.
- [ ] Salve métricas em CSV e crie um gráfico de previsão com intervalo ou faixa de incerteza.
- [ ] Produza resumo executivo de uma página com decisão, horizonte, risco e limitação.
- [ ] Escreva `atividades/01-projeto-de-forecasting/projeto-semanal/README.en.md` em inglês, com 150–250 palavras, cobrindo problema, dados, método, resultados, limitações e reprodução.
- [ ] Prepare `atividades/01-projeto-de-forecasting/projeto-semanal/docs/presentation-en.md` como roteiro em inglês para uma apresentação falada de 2–3 minutos.

- [ ] **Em `atividades/01-projeto-de-forecasting/roteiro_atividades.md`:** Execute o backtesting removendo o mês de maior consumo e registre como ranking de modelos e erro mudam.
- [ ] **Em `atividades/01-projeto-de-forecasting/roteiro_atividades.md`:** Aumente em 25% o custo de subestimação no resumo executivo e confira se a decisão operacional permanece.

#### Como validar

- O projeto foi executado, incluindo `README.en.md` e `docs/presentation-en.md`, e o roteiro contém todas as saídas obrigatórias.
- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Entrega real de portfólio

**Energy ForecastOps — previsão operacional**

Siga o [brief do projeto](<../../projetos/energy-forecastops/README.md>). A entrega precisa ter problema e usuário definidos, data card, dados reproduzíveis, baseline, métricas escolhidas antes do resultado, análise de erros, testes, README em português e inglês e apresentação de 2–3 minutos em inglês. Documente também resultados negativos.

## Publicação da semana no LinkedIn

- **Tema específico:** Energy ForecastOps — escolha de uma previsão por horizonte com backtest temporal e custo de subprevisão.
- **Tipo:** entrega.
- **Formato:** gráfico de previsão com faixa de incerteza e carrossel curto com protocolo, benchmark e decisão.
- **Artefato/evidência exigida:** backtesting walk-forward executado, baseline e modelo no mesmo corte, CSV de métricas, gráfico de previsão, teste sem o mês de maior consumo e resumo executivo em `atividades/01-projeto-de-forecasting/projeto-semanal/`.

### Roteiro para preencher

- **Decisão e horizonte:** [qual decisão operacional e qual horizonte foram avaliados?]
- **Dados e cortes temporais:** [frequência, período de treino, validação e teste]
- **Baseline e modelo:** [quais métodos foram comparados sob o mesmo protocolo?]
- **Resultado verificável:** [métrica, valor e arquivo que o comprova]
- **Custo do erro:** [como subprevisão e sobreprevisão foram tratadas?]
- **Teste de robustez:** [o que mudou ao remover o mês de maior consumo ou alterar o custo?]
- **Link:** [repositório, relatório ou demonstração conferidos]

### Limitação obrigatória

Explique por que desempenho histórico não garante o mesmo erro em outro período, regime ou operação.

### Cuidado contra afirmações falsas

Não apresente a previsão como certeza, não escolha somente a melhor janela e não atribua economia real sem medição operacional. Esta publicação não libera automaticamente Competências ou headline.

### Checklist de publicação

- [ ] Mantive frequência, horizonte e cortes iguais para baseline e modelo.
- [ ] Conferi o CSV, o gráfico e os valores escritos no texto.
- [ ] Mostrei incerteza, um período ruim e a regra de decisão.
- [ ] Registrei fonte, licença, período e limitações dos dados.
- [ ] Testei o link e removi segredos ou caminhos locais.
- [ ] **URL publicada:**
- [ ] **Data da publicação:**

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

# Projeto de forecasting

## Conquista para o LinkedIn

- **Competências:** depois de executar o backtesting e defender a validação temporal, adicione **Análise de séries temporais** e **Forecasting**.
- **Projetos ou Destaques:** inclua o projeto com horizonte, baseline, métrica, decisão e limitação.
- O material em inglês comprova prática técnica, não um nível avançado do idioma. Siga o [Guia de LinkedIn e evidências](<../../../../00 - Recursos Compartilhados/linkedin-e-evidencias.md>).

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/roteiro_atividades.md`.
- **Dados:** `dados/energia.csv`.

## Aprenda agora

- **Definição:** um projeto temporal reproduzível fixa frequência, horizonte, cortes, baselines, métricas e regra de decisão.
- **Exemplo mínimo:** manifesto com `data_corte, horizonte, coluna_alvo, frequência, métricas, seed`; todos os modelos usam o mesmo manifesto.
- **Erro comum:** alterar cortes entre tabelas ou escolher a melhor janela após olhar toda a série.

## Núcleo essencial

1. [ ] Organize o projeto com dados, notebook ou script, resultados e README.
2. [ ] Compare o baseline oficial com um único modelo em backtesting walk-forward.
3. [ ] Salve métricas em CSV e crie um gráfico de previsão com intervalo ou faixa de incerteza.
4. [ ] Produza resumo executivo de uma página com decisão, horizonte, risco e limitação.
5. [ ] Escreva `projeto-semanal/README.en.md` em inglês, com 150–250 palavras, cobrindo problema, dados, método, resultados, limitações e reprodução.
6. [ ] Prepare `projeto-semanal/docs/presentation-en.md` como roteiro em inglês para uma apresentação falada de 2–3 minutos.

## Prática obrigatória

- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Execute o backtesting removendo o mês de maior consumo e registre como ranking de modelos e erro mudam.
- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Aumente em 25% o custo de subestimação no resumo executivo e confira se a decisão operacional permanece.

## Concluído quando

- [ ] O núcleo foi executado, incluindo `README.en.md` e `docs/presentation-en.md`, e o roteiro contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

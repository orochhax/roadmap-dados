# relatorio-final.md — Dia 130

> Este arquivo contém somente o enunciado e espaços para preenchimento. Nenhuma atividade foi resolvida.

## Enunciado

## Dia 126 — TCC: universo, dados e protocolo financeiro — 25/01/2027
> [!abstract] Resultado concreto do dia
> Congelar o universo e criar uma base versionada cuja disponibilidade temporal possa ser auditada.

### Preparação
- **Pasta/arquivo principal:** `13-tcc-final/portfolio-intelligence-lab/`.
- **Unidade de análise:** ativo × data de rebalanceamento.
- **Classes obrigatórias:** ações, ETFs e FIIs.

### Passo a passo completo
1. [ ] Defina o universo mínimo por classe, critérios de inclusão, período histórico e frequência de rebalanceamento.
2. [ ] Crie tabela de ativos com `ticker`, classe, segmento, data inicial, data final e regra de elegibilidade.
3. [ ] Importe preços ajustados, volume/liquidez, proventos e indicadores disponíveis; preserve a camada bruta.
4. [ ] Crie dicionário de dados e coluna `disponivel_em` para indicadores que não surgem no mesmo dia do período de referência.
5. [ ] Gere relatório automático de ausentes, duplicados, gaps, ativos sem histórico suficiente e datas inconsistentes.
6. [ ] Defina baselines, protocolo walk-forward, custos, métricas e critérios de sucesso antes de testar modelos.

### Verificação prática sem consulta
- [ ] Escolha cinco features e prove com datas que nenhuma usa informação futura.
- [ ] Mostre como um ativo que entrou ou saiu do universo pode criar survivorship bias.
- [ ] Explique por que split aleatório seria inadequado neste projeto.

### Perguntas de checagem
1. Qual informação estaria disponível na data real de cada decisão?
2. Como você evitará selecionar hoje apenas ativos que sobreviveram?
3. Qual é o benchmark mais simples que o projeto precisa superar?
4. Que resultado faria você concluir que o ranking não funciona?

### Critério objetivo para marcar como concluído
- [ ] Dados brutos preservados e versionados.
- [ ] Universo e regras de elegibilidade documentados.
- [ ] Protocolo definido antes da modelagem.
- [ ] Pelo menos três testes automáticos de qualidade aprovados.
- [ ] Commit: `dia-126: universo-dados-e-protocolo-financeiro`.

**Autoavaliação do dia:** `__/5`  
**Evidência:** relatório de qualidade, dicionário, protocolo e commit.

## Dia 127 — TCC: fatores e motor de ranking — 26/01/2027
> [!abstract] Resultado concreto do dia
> Construir fatores auditáveis e um ranking separado para ações, ETFs e FIIs.

### Passo a passo completo
1. [ ] Calcule retornos, momentum, volatilidade, drawdown, liquidez, consistência e correlações usando somente janelas anteriores à decisão.
2. [ ] Padronize os fatores dentro de cada classe e trate outliers sem usar o período futuro.
3. [ ] Construa um score quantitativo simples e documente pesos, sinal esperado e justificativa de cada fator.
4. [ ] Crie alvos futuros para classificação/regressão e implemente ao menos regressão logística e um modelo de árvore/boosting.
5. [ ] Gere ranking A–E por classe, Precision@K, retorno dos Top-K, turnover e estabilidade entre rebalanceamentos.
6. [ ] Produza explicabilidade global e exemplos de ativos bem/mal classificados.

### Verificação prática sem consulta
- [ ] Recalcule manualmente o score de três ativos.
- [ ] Remova um fator e meça o efeito no ranking.
- [ ] Inverta deliberadamente uma janela temporal, detecte o leakage e documente por que o resultado falso melhora.

### Perguntas de checagem
1. Por que o ranking deve ser separado por classe?
2. Um ranking estável é necessariamente um ranking bom?
3. Como Precision@K se conecta à seleção de uma carteira?
4. Qual fator tem maior risco de estar apenas ajustado ao passado?

### Critério objetivo para marcar como concluído
- [ ] Baseline e modelos usam o mesmo protocolo temporal.
- [ ] Ranking reproduzível para cada data e classe.
- [ ] Features possuem ficha de disponibilidade temporal.
- [ ] Resultados incluem falhas, não apenas o melhor período.
- [ ] Commit: `dia-127: fatores-e-motor-quantitativo-de-ranking`.

**Autoavaliação do dia:** `__/5`  
**Evidência:** tabela de fatores, ranking, métricas e commit.

## Dia 128 — TCC: carteiras e backtest walk-forward — 27/01/2027
> [!abstract] Resultado concreto do dia
> Converter rankings em carteiras e avaliar risco-retorno fora da amostra.

### Passo a passo completo
1. [ ] Implemente carteira de pesos iguais como baseline.
2. [ ] Implemente carteira Top-K baseada no ranking e uma estratégia de mínima volatilidade ou risk parity.
3. [ ] Defina alocação entre ações, ETFs e FIIs sem misturar os scores brutos das classes.
4. [ ] Execute backtest walk-forward com rebalanceamento, custos e regras mínimas de liquidez.
5. [ ] Compare retorno anualizado, volatilidade, Sharpe, Sortino, máximo drawdown, turnover e períodos negativos.
6. [ ] Faça testes de sensibilidade variando K, custos, janelas, frequência e pesos dos fatores.
7. [ ] Analise períodos em que o ranking e as carteiras falharam.

### Verificação prática sem consulta
- [ ] Recalcule o retorno líquido de um rebalanceamento incluindo custos.
- [ ] Compare a estratégia com um baseline ingênuo no mesmo período.
- [ ] Execute cenário de custo dobrado e mostre se a conclusão muda.

### Perguntas de checagem
1. Por que maior retorno acumulado não basta para escolher uma estratégia?
2. Qual diferença entre risco observado e risco estimado?
3. Como turnover pode destruir uma estratégia aparentemente lucrativa?
4. O que caracteriza overfitting de backtest?

### Critério objetivo para marcar como concluído
- [ ] Nenhum resultado principal usa dados do futuro.
- [ ] Custos aparecem em todos os resultados líquidos.
- [ ] Há comparação dentro e fora da amostra.
- [ ] Pelo menos três estratégias e um benchmark foram comparados.
- [ ] Commit: `dia-128: carteiras-e-backtest-walk-forward`.

**Autoavaliação do dia:** `__/5`  
**Evidência:** curvas, tabela de métricas, testes de sensibilidade e commit.

## Dia 129 — TCC: dashboard, API, testes e relatório — 28/01/2027
> [!abstract] Resultado concreto do dia
> Transformar o estudo em produto demonstrável e reproduzível.

### Passo a passo completo
1. [ ] Crie dashboard com filtros por classe, período e perfil de risco; mostre fatores, ranking, carteira e drawdown.
2. [ ] Crie simulador com número de ativos, frequência, estratégia e custos configuráveis.
3. [ ] Implemente API com endpoints de saúde, ranking por data e métricas de carteira.
4. [ ] Adicione validação de entrada, logs, testes unitários e testes de integração.
5. [ ] Containerize o produto com Docker e execute em clone limpo.
6. [ ] Escreva relatório técnico de 10–18 páginas, resumo executivo de uma página e model card/metodologia do ranking.
7. [ ] Inclua seção explícita: vieses, períodos ruins, limitações e por que o resultado não é recomendação de investimento.

### Verificação prática sem consulta
- [ ] Outra pessoa consegue executar o projeto apenas com o README.
- [ ] Uma entrada inválida não derruba nem produz resposta enganosa.
- [ ] Toda métrica exibida no dashboard pode ser rastreada até uma função ou consulta.

### Perguntas de checagem
1. O produto mostra incerteza e risco ou apenas resultados positivos?
2. Quais decisões são do modelo e quais continuam humanas?
3. O que você retiraria primeiro para reduzir o escopo sem destruir o TCC?
4. Qual teste aumenta mais a confiança no produto?

### Critério objetivo para marcar como concluído
- [ ] Dashboard e API funcionam com dados versionados.
- [ ] Testes e Docker passam em ambiente limpo.
- [ ] Relatório contém método, resultados, limitações e reprodução.
- [ ] Commit: `dia-129: produto-testes-e-relatorio-financeiro`.

**Autoavaliação do dia:** `__/5`  
**Evidência:** demo, testes, relatório e commit.

## Desenvolvimento

<!-- Preencha durante a atividade. -->

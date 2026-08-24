# Causalidade II: propensity score, matching, IPW e balanceamento + Causalidade III: diferenças em diferenças e estudo de evento

**Data de estudo:** 06/10/2026  
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Causalidade II: propensity score, matching, IPW e balanceamento

#### O que pesquisar
- `propensity score matching`
- `inverse probability weighting`
- `standardized mean difference`
- `overlap positivity`

**Arquivos da atividade:** [abrir a pasta `01-causalidade-ii-propensity-score-matching`](<atividades/01-causalidade-ii-propensity-score-matching/>)

#### Objetivo

Estimar o efeito de uma oferta de retenção em dados observacionais, comparando matching e ponderação. O objetivo central é diagnosticar sobreposição e balanceamento, não obter um número causal a qualquer custo.

#### Termos complementares para pesquisar

- `propensity score logistic regression causal inference`
- `propensity score common support overlap`
- `standardized mean difference love plot`
- `nearest neighbor matching caliper propensity score`
- `inverse probability weighting stabilized weights`
- `effective sample size IPW`
- `positivity violation extreme weights`
- `propensity score trimming sensitivity`

#### O que fazer

Leia o [enunciado](<atividades/01-causalidade-ii-propensity-score-matching/ENUNCIADO.md>), complete [propensity_score.py](<atividades/01-causalidade-ii-propensity-score-matching/propensity_score.py>) e registre diagnósticos no próprio artefato.

#### Como validar

- somente variáveis pré-tratamento entram no propensity;
- overlap e SMD são vistos antes do efeito;
- matching e IPW usam o estimando declarado;
- pesos extremos e perda de amostra são reportados;
- é permitido concluir que os dados não sustentam a estimativa.

### Atividade 2 — Causalidade III: diferenças em diferenças e estudo de evento

#### O que pesquisar
- `diferenças em diferenças`
- `tendências paralelas`
- `event study`
- `cluster robust standard errors`

**Arquivos da atividade:** [abrir a pasta `02-causalidade-iii-diferencas-em-diferencas`](<atividades/02-causalidade-iii-diferencas-em-diferencas/>)

#### Objetivo

Avaliar um rollout regional quando não houve randomização, separando mudança comum no tempo do efeito específico da região tratada. Você testará tendências prévias e mostrará quando diferenças em diferenças não é confiável.

#### Termos complementares para pesquisar

- `difference in differences 2x2 estimator`
- `parallel trends assumption difference in differences`
- `event study leads and lags`
- `cluster robust standard errors panel data`
- `staggered adoption difference in differences bias`
- `placebo treatment date difference in differences`
- `anticipation effect causal inference`

#### O que fazer

Leia o [enunciado](<atividades/02-causalidade-iii-diferencas-em-diferencas/ENUNCIADO.md>), complete [diferencas_em_diferencas.py](<atividades/02-causalidade-iii-diferencas-em-diferencas/diferencas_em_diferencas.py>) e registre o diagnóstico no próprio artefato.

#### Como validar

- o estimador 2x2 confere com a regressão;
- a hipótese de tendências paralelas é investigada antes do rollout;
- event study, placebo e sensibilidade são registrados;
- uma base que viola a hipótese não recebe conclusão causal forte.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

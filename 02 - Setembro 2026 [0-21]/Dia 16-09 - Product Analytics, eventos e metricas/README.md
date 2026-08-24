# Product Analytics I: tracking plan, eventos e árvore de métricas + Product Analytics II: funil, ativação, retenção, cohorts e LTV

**Data de estudo:** 16/09/2026  
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Product Analytics I: tracking plan, eventos e árvore de métricas

#### O que pesquisar
- `tracking plan de eventos`
- `North Star Metric`
- `árvore de métricas`
- `guardrail metrics`

**Arquivos da atividade:** [abrir a pasta `01-product-analytics-i-tracking-plan-eventos`](<atividades/01-product-analytics-i-tracking-plan-eventos/>)

#### Objetivo

Desenhar e validar a instrumentação do aplicativo de autoatendimento de uma operadora. Antes de calcular funis, você deverá provar que os eventos têm significado, schema, identidade e privacidade controlados.

#### Termos complementares para pesquisar

- `product analytics tracking plan event taxonomy`
- `event naming convention analytics`
- `user id anonymous id identity resolution analytics`
- `North Star metric input metrics guardrail metrics`
- `data contract schema evolution events`
- `event deduplication idempotency`
- `LGPD data minimization analytics events`

#### O que fazer

Leia o [enunciado](<atividades/01-product-analytics-i-tracking-plan-eventos/ENUNCIADO.md>), complete [validar_tracking_plan.py](<atividades/01-product-analytics-i-tracking-plan-eventos/validar_tracking_plan.py>) e registre o contrato e os testes no próprio artefato.

#### Como validar

- o tracking plan descreve evento, gatilho, propriedades, dono e versão;
- o validador separa eventos aceitos e rejeitados com motivo;
- duplicidade, ordem, identidade e PII são testadas;
- a North Star e suas guardrails são ligadas a uma decisão real.

### Atividade 2 — Product Analytics II: funil, ativação, retenção, cohorts e LTV

#### O que pesquisar
- `funil de conversão`
- `ativação de produto`
- `cohort retention`
- `customer lifetime value`

**Arquivos da atividade:** [abrir a pasta `02-product-analytics-ii-funil-ativacao`](<atividades/02-product-analytics-ii-funil-ativacao/>)

#### Objetivo

Transformar eventos validados em decisões sobre onboarding e autoatendimento. Você implementará funil, ativação, cohorts, retenção e LTV sem misturar usuários, sessões e eventos.

#### Termos complementares para pesquisar

- `product analytics conversion funnel SQL`
- `activation metric time to value`
- `cohort retention SQL date difference`
- `D1 D7 D30 retention`
- `customer lifetime value historical method`
- `revenue refunds net revenue analytics`
- `survivorship bias retention analysis`

#### O que fazer

Leia o [enunciado](<atividades/02-product-analytics-ii-funil-ativacao/ENUNCIADO.md>), implemente as consultas em [product_analytics.sql](<atividades/02-product-analytics-ii-funil-ativacao/product_analytics.sql>) e registre reconciliações e decisão no próprio artefato.

#### Como validar

- cada métrica declara unidade, janela, denominador e timezone;
- funil não conta repetição como conversão adicional;
- retenção usa a própria coorte como denominador;
- receita líquida trata estorno;
- a recomendação cita impacto, segmento e limitação.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

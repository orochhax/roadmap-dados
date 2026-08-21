# TCC — testes, monitoramento temporal e relatório

**Data de estudo:** 22/01/2027  
**Carga planejada:** 4 a 5 horas

## Objetivo do dia

Auditar o TCC do dado à decisão: testes de schema, leakage e métricas; rastreabilidade no MLflow; monitoramento temporal; comparação champion/challenger; retreino e rollback simulados. A entrega visual deve ser um relatório ou painel compacto, não uma aplicação grande.

## Assuntos para pesquisar

Pesquise exatamente:

- `pytest data schema leakage metric unit tests machine learning`
- `MLflow model registry champion challenger aliases`
- `model monitoring temporal performance calibration drift`
- `machine learning retraining trigger rollback simulation`
- `model card limitations synthetic data`
- `reproducible machine learning report checklist`

Siga o [guia e o roteiro](<modulos/01-e137/README.md>). O relatório deve manter separados desempenho preditivo e efeito do piloto simulado.

## Integração

Reconcilie data card, runs do MLflow, benchmark, piloto, métricas de custo e testes. Simule uma janela posterior para monitoramento e um challenger retreinado, mas não invente operação real nem impacto observado.

## Publicação da semana no LinkedIn

- **Tema específico:** bastidores do TCC de retenção — como testes, MLflow e monitoramento impedem promover um modelo apenas porque uma métrica subiu.
- **Tipo:** progresso.
- **Formato:** carrossel metodológico com contrato temporal, matriz de testes, comparação champion/challenger e uma tela preliminar do relatório.
- **Artefato/evidência exigida:** pré-projeto congelado, manifesto dos dados sintéticos, teste de leakage, benchmark regra/logística/XGBoost, piloto randomizado simulado, runs do MLflow, métricas temporais e simulação documentada de retreino/rollback.

### Roteiro para preencher

- **Pergunta e usuário:** [qual decisão de retenção está sendo auditada e por quem?]
- **Contrato:** [data de decisão, horizonte e capacidade]
- **Dados:** [versão, seed, período e declaração sintética]
- **Teste mais importante:** [entrada, esperado, observado e por que protege a decisão]
- **Champion/challenger:** [quais modelos, critérios e trade-offs]
- **Monitoramento:** [janela, métrica e gatilho]
- **Estado atual:** [o que já executa e o que falta para a release]
- **Evidência:** [caminho do teste, run ou gráfico mostrado]

### Limitação obrigatória

Declare que o TCC ainda está em progresso, que dados e piloto são sintéticos e que a análise demonstra método, não redução real de churn nem efeito real de campanha.

### Cuidado contra afirmações falsas

Não anuncie retenções, economia ou causalidade em clientes reais. Não chame uma simulação de produção e não esconda resultado negativo, slice fraco ou intervalo inconclusivo. Este post não antecipa Competências ou headline.

### Checklist de publicação

- [ ] Diferenciei risco previsto de efeito incremental.
- [ ] Exibi resultado esperado e observado de um teste reproduzível.
- [ ] Identifiquei dados, piloto, retreino e rollback como simulados.
- [ ] Mantive limitação, resultado negativo e amostra dos slices visíveis.
- [ ] Registrei o que falta para a release de 25/01.
- [ ] **URL publicada:**
- [ ] **Data da publicação:**

## Concluído quando

- [ ] Testes de schema, leakage e métricas passam e falham nos casos inválidos previstos.
- [ ] MLflow, relatório e artefatos apresentam números reconciliados.
- [ ] Monitoramento, retreino, champion/challenger e rollback foram simulados e documentados em uma entrega visual pequena, reproduzível e com limites de inferência declarados.

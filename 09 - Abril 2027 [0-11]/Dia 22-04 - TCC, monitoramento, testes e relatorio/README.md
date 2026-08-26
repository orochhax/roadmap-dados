# TCC — testes, monitoramento temporal e relatório

**Data de estudo:** 22/04/2027
**Carga planejada:** 4 a 5 horas

## Objetivo do dia

Auditar o TCC do dado à decisão: testes de schema, leakage e métricas; rastreabilidade no MLflow; monitoramento temporal; comparação champion/challenger; retreino e rollback simulados. A entrega visual deve ser um relatório ou painel compacto, não uma aplicação grande.

## Atividades do dia

Pesquise exatamente:

- `pytest data schema leakage metric unit tests machine learning`
- `MLflow model registry champion challenger aliases`
- `model monitoring temporal performance calibration drift`
- `machine learning retraining trigger rollback simulation`
- `model card limitations synthetic data`
- `reproducible machine learning report checklist`

Siga o guia e o roteiro disponíveis abaixo. O relatório deve manter separados desempenho preditivo e efeito do piloto simulado.

### Conteúdo e atividades — TCC — testes, observabilidade e ciclo de vida

**Arquivos da atividade:** [abrir a pasta `01-tcc-testes-observabilidade-e-ciclo-de-vida`](<atividades/01-tcc-testes-observabilidade-e-ciclo-de-vida/>)

#### Objetivo

Provar que os resultados do TCC são reproduzíveis e que existe uma resposta segura quando dados ou desempenho mudam. A sessão fecha o ciclo de vida mínimo sem construir uma aplicação grande.

#### Arquivos e dados

- **Enunciado local:** `atividades/01-tcc-testes-observabilidade-e-ciclo-de-vida/roteiro_tcc.md`.
- **Projeto canônico:** `projetos/telecom-customer-intelligence/`.
- **Entradas:** datasets/versionamento, runs MLflow, champion/challenger, análise do piloto e métricas de custo.
- **Saídas esperadas:** testes em `tests/`, monitoramento em `outputs/`, relatório/model card em `docs/` e execução reproduzível.

#### Pesquise exatamente

- `pytest data validation schema tests pandas`
- `temporal leakage unit test machine learning`
- `metric implementation unit test precision recall calibration`
- `MLflow model registry champion challenger rollback`
- `model monitoring data drift performance drift calibration`
- `retraining trigger model rollback runbook`

#### O que fazer

- [ ] Implemente testes de schema, chave, datas, leakage temporal e campos pós-tratamento.
- [ ] Implemente casos pequenos com oráculo conhecido para PR-AUC/recall@K ou métricas auxiliares e efeito/ganho por 100.
- [ ] Faça uma auditoria dos runs no MLflow e reconcilie champion/challenger com o relatório.
- [ ] Crie uma janela temporal posterior sintética para monitorar qualidade, distribuição, PR-AUC, recall@K e calibração quando houver rótulo.
- [ ] Defina gatilhos de alerta sem tratar drift isolado como ordem automática de retreino.
- [ ] Simule retreino, compare challenger no protocolo congelado e promova somente se os critérios forem cumpridos.
- [ ] Simule rollback para o champion anterior e registre versão, motivo e verificação.
- [ ] Produza relatório de 4–6 páginas, resumo executivo e visual estático/compacto.

#### Visual mínimo

- funil dos dados e capacidade;
- comparação dos três modelos;
- curva/tabela de calibração e recall@K;
- efeito do piloto com intervalo;
- ganho por 100 e custo por retenção;
- slices e evolução temporal.

#### Regras

- Teste precisa possuir entrada, resultado esperado e resultado observado.
- Janela de monitoramento, retreino e rollback devem ser rotulados como simulação.
- O challenger não vence apenas por uma métrica; considere calibração, slices, latência e custo.
- Nenhum painel deve sugerir impacto real ou esconder incerteza.
- Não construa API, frontend ou infraestrutura de nuvem para este TCC.

#### Como validar

- Testes falham nos casos inválidos e passam no caminho válido.
- Monitoramento temporal e runs MLflow são reproduzíveis.
- Promoção, retreino e rollback simulados possuem critérios e evidências.
- Relatório e visual reconciliam métricas preditivas, causais e de custo.

## Integração do dia

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

## Finalização

Antes de concluir, confirme:

- Testes de schema, leakage e métricas passam e falham nos casos inválidos previstos.
- MLflow, relatório e artefatos apresentam números reconciliados.
- Monitoramento, retreino, champion/challenger e rollback foram simulados e documentados em uma entrega visual pequena, reproduzível e com limites de inferência declarados.

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

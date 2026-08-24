# Modelagem de risco + Politica e custo

**Data de estudo:** 27/11/2026  
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Modelagem de risco

#### O que pesquisar
- `Modelagem de risco Python explicado passo a passo`
- `Modelagem de risco Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-modelagem-de-risco`](<atividades/01-modelagem-de-risco/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-modelagem-de-risco/dia-083-modelagem-de-risco.ipynb`.
- **Dados:** `dados/credito.csv`.

#### O que você precisa entender

- **Definição:** ROC-AUC mede ordenação geral; PR-AUC enfatiza a classe rara; KS é a maior separação entre distribuições; calibração avalia probabilidades.
- **Exemplo mínimo:** compare os modelos na mesma janela com `ROC-AUC, PR-AUC, KS` e curva de calibração, sempre com suporte.
- **Erro comum:** escolher só ROC-AUC em evento raro ou interpretar KS como qualidade de probabilidade.

#### O que fazer

- [ ] Treine regressão logística como scorecard básico e modelos de árvore.
- [ ] Avalie ROC-AUC, PR-AUC, KS, calibração e matriz de confusão.
- [ ] Faça validação temporal, não apenas aleatória.

- [ ] Analise estabilidade e desempenho por segmentos.
- [ ] Escolha modelo explicável compatível com política de crédito.


- [ ] **Em `atividades/01-modelagem-de-risco/dia-083-modelagem-de-risco.ipynb`:** Compare calibração e KS no conjunto temporal final para logística e o melhor modelo de árvore.
- [ ] **Em `atividades/01-modelagem-de-risco/dia-083-modelagem-de-risco.ipynb`:** Calcule as métricas separadamente para contratos com prazo até 12 meses e acima de 24 meses.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

### Atividade 2 — Politica e custo

#### O que pesquisar
- `Politica e custo Python explicado passo a passo`
- `Politica e custo Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-politica-e-custo`](<atividades/02-politica-e-custo/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-politica-e-custo/dia-084-politica-e-custo.ipynb`.
- **Dados:** `dados/credito.csv`.

#### O que você precisa entender

- **Definição:** nota A–E é uma política baseada em faixas de risco; perda esperada pode ser `PD × LGD × EAD`; lucro esperado inclui receita, perda e custo operacional.
- **Exemplo mínimo:** para `PD=.08, LGD=.5, EAD=1000`, perda esperada = R$40; compare com margem e custo de revisão.
- **Erro comum:** criar faixas sem justificar cortes ou tratar score como decisão automática.

#### O que fazer

- [ ] Converta probabilidade em faixas de risco A–E.
- [ ] Defina política de aprovar, revisar ou rejeitar por faixa.
- [ ] Simule lucro/prejuízo com taxas, perda esperada e custo operacional.

- [ ] Teste cenários de mudança na taxa de default.
- [ ] Crie regra para casos sem informação suficiente e revisão humana.


- [ ] **Em `atividades/02-politica-e-custo/dia-084-politica-e-custo.ipynb`:** Aumente a perda em caso de default em 30% e recalcule lucro/prejuízo por faixa A–E.
- [ ] **Em `atividades/02-politica-e-custo/dia-084-politica-e-custo.ipynb`:** Envie para revisão humana todos os casos com renda ou tempo de emprego ausente e conte o volume afetado.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

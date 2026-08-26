# EDA, baseline e decisao

**Data de estudo:** 30/03/2027
**Carga planejada:** 2 a 4 horas

## Atividades do dia

### Atividade 1 — EDA, baseline e decisao

#### O que pesquisar
- `EDA, baseline e decisao análise de dados com Python explicado passo a passo`
- `EDA, baseline e decisao análise de dados com Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-eda-baseline-e-decisao`](<atividades/01-eda-baseline-e-decisao/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-eda-baseline-e-decisao/dia-118-eda-baseline-e-decisao.ipynb`.
- **Entradas:** `product_brief.md`, dataset validado, corte e métrica. **Fallback local:** amostra determinística.

#### Manifesto de entradas

- **Obrigatórias:** dataset validado, split/corte, baseline e métrica declarada.
- **Fallback local:** gere amostra determinística com seed fixa apenas para testar o fluxo.

#### O que você precisa entender

- **Definição:** baseline é a alternativa simples que o produto deve justificar; a métrica precisa refletir a decisão.
- **Exemplo mínimo:** churn usa Dummy e custo; forecasting usa último valor e MAE; analítico usa regra atual e tempo/erro; RAG usa busca lexical e precision@k.
- **Erro comum:** escolher baseline fraco ou métrica que não muda a ação.

#### O que fazer

- [ ] Faça EDA focada nas hipóteses do produto.
- [ ] Implemente baseline de negócio e técnico.
- [ ] Defina limiar/regra de decisão.

- [ ] **Em `atividades/01-eda-baseline-e-decisao/dia-118-eda-baseline-e-decisao.ipynb`:** refaça a decisão aumentando o custo do pior erro em 50% e registre se limiar ou ação recomendada muda.
- [ ] **No mesmo notebook:** produza um memorando de uma página com impacto esperado, pior cenário, decisão e limitação.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

# EDA, baseline e decisão

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-118-eda-baseline-e-decisao.ipynb`.
- **Entradas:** `product_brief.md`, dataset validado, corte e métrica. **Fallback local:** amostra determinística.

## Manifesto de entradas

- **Obrigatórias:** dataset validado, split/corte, baseline e métrica declarada.
- **Fallback local:** gere amostra determinística com seed fixa apenas para testar o fluxo.

## Aprenda agora

- **Definição:** baseline é a alternativa simples que o produto deve justificar; a métrica precisa refletir a decisão.
- **Exemplo mínimo:** churn usa Dummy e custo; forecasting usa último valor e MAE; analítico usa regra atual e tempo/erro; RAG usa busca lexical e precision@k.
- **Erro comum:** escolher baseline fraco ou métrica que não muda a ação.

## Núcleo essencial

1. [ ] Faça EDA focada nas hipóteses do produto.
2. [ ] Implemente baseline de negócio e técnico.
3. [ ] Defina limiar/regra de decisão.

## Prática obrigatória

- [ ] **Em `01-exercicios/dia-118-eda-baseline-e-decisao.ipynb`:** refaça a decisão aumentando o custo do pior erro em 50% e registre se limiar ou ação recomendada muda.
- [ ] **No mesmo notebook:** produza um memorando de uma página com impacto esperado, pior cenário, decisão e limitação.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-118-eda-baseline-e-decisao.ipynb` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

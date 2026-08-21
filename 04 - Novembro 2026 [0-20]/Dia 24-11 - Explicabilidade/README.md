# Explicabilidade

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-064-explicabilidade.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

## Aprenda agora

- **Definição:** explicação global resume o comportamento médio; local descreve uma previsão. Coeficientes, permutation importance e SHAP respondem perguntas distintas.
- **Exemplo mínimo:** `queda = métrica_original - métrica_com_coluna_embaralhada`; queda maior indica maior dependência.
- **Erro comum:** comparar coeficientes sem padronização ou generalizar uma explicação local.

## Núcleo essencial

1. [ ] Escolha 10 previsões individuais, incluindo acertos e erros, e explique fatores principais.
2. [ ] Use coeficientes, permutation importance e SHAP se disponível; compare explicações globais e locais.
3. [ ] Teste explicações em dois segmentos demográficos ou operacionais.

## Prática obrigatória

- [ ] Identifique uma explicação plausível porém enganosa causada por correlação.
- [ ] Crie relatório para público não técnico com três cuidados ao interpretar importância.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-064-explicabilidade.ipynb`:** Explique uma previsão correta de churn alto e uma incorreta de churn baixo usando o mesmo método local.
- [ ] **Em `01-exercicios/dia-064-explicabilidade.ipynb`:** Remova a feature mais correlacionada com a principal e gere novamente a explicação para observar estabilidade.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-064-explicabilidade.ipynb` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

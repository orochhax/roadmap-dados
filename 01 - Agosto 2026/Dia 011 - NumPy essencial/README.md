<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 11 — NumPy essencial — 17/08/2026
> [!abstract] Resultado concreto do dia
> Concluir **NumPy essencial** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** NumPy essencial.
- **Pasta/arquivo principal:** `semana-03/dia-011-numpy-essencial.ipynb`.
- **Dados:** `dados/incidentes.csv`, `dados/clientes_telecom.csv`, `dados/pedidos.csv` e `dados/metas_cidades.csv`.

### Passo a passo completo
1. [ ] Crie `numpy_essencial.ipynb` e um array com durações `[15,30,45,60,90,120,180,240]`; calcule média, mediana, desvio, mínimo, máximo e percentis 25/75.
2. [ ] Crie uma matriz 4x3 representando quatro cidades e três métricas; selecione linhas, colunas e fatias usando indexação.
3. [ ] Normalize uma coluna pelo método min-max e padronize outra com z-score, calculando manualmente e com NumPy.
4. [ ] Use operações vetorizadas para aplicar multa de 10% a durações acima de 120; compare com um laço usando `timeit`.
5. [ ] Teste `NaN`, array vazio e divisão por desvio zero; escreva como trataria cada caso.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Aplique a técnica central de **NumPy essencial** a uma segunda coluna, grupo ou recorte dos dados e compare o que mudou.
- [ ] Introduza uma cópia dos dados com um problema controlado — valor ausente, duplicado ou outlier — e verifique como ele afeta o resultado.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Crie `numpy_essencial.ipynb` e um array com durações `[15,30,45,60,90,120,180,240]`; calcule média, mediana, desvio, mínimo, máximo e percentis 25/75.

   **Pergunta:** Antes de tirar conclusões em **NumPy essencial**, qual é a prática mais confiável?

- [ ] A) Começar pelo gráfico mais bonito e escolher os dados depois.
- [ ] B) Remover todas as linhas incompletas sem medir o impacto.
- [ ] C) Calcular médias antes de entender o que cada linha representa.
- [ ] D) Considerar os nomes das colunas suficientes para validar os dados.
- [ ] E) Inspecionar estrutura, tipos, granularidade, valores ausentes e possíveis duplicidades.

2. **Referência — atividade 2:** Crie uma matriz 4x3 representando quatro cidades e três métricas; selecione linhas, colunas e fatias usando indexação.

   **Pergunta:** Qual cuidado evita conclusões distorcidas ao trabalhar com **NumPy essencial**?

- [ ] A) Usar apenas as primeiras linhas como representação de toda a base.
- [ ] B) Substituir valores ausentes pelo maior valor disponível.
- [ ] C) Manter a granularidade correta e conferir o efeito de filtros, agrupamentos e junções.
- [ ] D) Somar todas as colunas numéricas independentemente do significado.
- [ ] E) Arredondar os valores antes de analisar diferenças.

3. **Referência — atividade 3:** Normalize uma coluna pelo método min-max e padronize outra com z-score, calculando manualmente e com NumPy.

   **Pergunta:** Qual verificação é mais útil para encontrar problemas que uma média geral pode esconder em **NumPy essencial**?

- [ ] A) Comparar segmentos, distribuições, valores extremos e grupos com poucos registros.
- [ ] B) Ordenar as colunas pelo tamanho do nome.
- [ ] C) Trocar as cores do gráfico até a tendência ficar mais visível.
- [ ] D) Excluir categorias pequenas antes de examiná-las.
- [ ] E) Duplicar a base e repetir o mesmo cálculo.

4. **Referência — atividade 4:** Use operações vetorizadas para aplicar multa de 10% a durações acima de 120; compare com um laço usando `timeit`.

   **Pergunta:** Como uma análise de **NumPy essencial** deve ser apresentada para apoiar uma decisão?

- [ ] A) Omitindo incertezas para transmitir mais confiança.
- [ ] B) Usando apenas termos técnicos, sem explicar o impacto.
- [ ] C) Escolhendo a recomendação mais popular, mesmo sem evidência.
- [ ] D) Ligando evidências à pergunta de negócio, com limitações e uma ação recomendada.
- [ ] E) Mostrando todas as tabelas produzidas, sem priorizar uma conclusão.

5. **Referência — atividade 5:** Teste `NaN`, array vazio e divisão por desvio zero; escreva como trataria cada caso.

   **Pergunta:** Ordene um fluxo de análise para uma atividade de **NumPy essencial**.

- A) Preparar os dados sem perder a granularidade necessária.
- B) Inspecionar a estrutura e a qualidade dos dados.
- C) Definir a pergunta que precisa ser respondida.
- D) Calcular e visualizar as evidências relevantes.
- E) Comunicar a conclusão, as limitações e a ação sugerida.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene a preparação de uma visualização ou entrega sobre **NumPy essencial**.

- A) Apresentar a mensagem principal e o próximo passo.
- B) Escolher o tipo de visual compatível com a comparação.
- C) Selecionar a métrica e o recorte adequados.
- D) Revisar rótulos, escalas e possíveis interpretações enganosas.
- E) Identificar o público e a decisão que será apoiada.

**Ordem:** `__ → __ → __ → __ → __`

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Alterações registradas em commit e enviadas ao GitHub.

**Autoavaliação do dia:** `__/5`  

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** NumPy essencial.
- **Competência sugerida:** NumPy.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **NumPy** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Python`.
- **Próximo marco do perfil:** Dia 20 — Engenharia de Software | Análise de Dados | Python e Power BI.

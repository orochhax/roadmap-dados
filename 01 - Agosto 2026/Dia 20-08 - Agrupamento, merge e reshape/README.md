<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 14 — Agrupamento, merge e reshape — 20/08/2026
> [!abstract] Resultado concreto do dia
> Concluir **Agrupamento, merge e reshape** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Agrupamento, merge e reshape.
- **Pasta/arquivo principal:** `01-exercicios/dia-014-agrupamento-merge-e-reshape.ipynb`.
- **Dados:** `dados/incidentes.csv`, `dados/clientes_telecom.csv`, `dados/pedidos.csv` e `dados/metas_cidades.csv`.

### Passo a passo completo
1. [ ] Com `incidentes.csv` e `metas_cidades.csv`, calcule por `groupby` quantidade, média, mediana, soma de clientes e percentual resolvido por cidade.
2. [ ] Faça `merge` `inner`, `left` e `outer`; anote quantas linhas resultam e identifique cidades sem correspondência.
3. [ ] Crie uma tabela dinâmica com cidade nas linhas, severidade nas colunas e duração média nos valores.
4. [ ] Transforme dados largos em longos com `melt` e volte ao formato largo com `pivot`.
5. [ ] Provoque uma chave duplicada em `metas_cidades.csv`, observe o aumento de linhas e crie uma validação para impedir merge muitos-para-muitos acidental.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/dia-014-agrupamento-merge-e-reshape.ipynb`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/dia-014-agrupamento-merge-e-reshape.ipynb`:** Inclua Ilhéus nos incidentes sem criar meta para a cidade e compare quantas linhas aparecem nos merges inner, left e outer.
- [ ] **Em `01-exercicios/dia-014-agrupamento-merge-e-reshape.ipynb`:** Duplique a meta de Salvador, execute a validação de cardinalidade e impeça o merge enquanto a chave continuar duplicada.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Com `incidentes.csv` e `metas_cidades.csv`, calcule por `groupby` quantidade, média, mediana, soma de clientes e percentual resolvido por cidade.

   **Pergunta:** Antes de tirar conclusões em **Agrupamento, merge e reshape**, qual é a prática mais confiável?

- [ ] A) Considerar os nomes das colunas suficientes para validar os dados.
- [ ] B) Inspecionar estrutura, tipos, granularidade, valores ausentes e possíveis duplicidades.
- [ ] C) Começar pelo gráfico mais bonito e escolher os dados depois.
- [ ] D) Remover todas as linhas incompletas sem medir o impacto.
- [ ] E) Calcular médias antes de entender o que cada linha representa.

2. **Referência — atividade 2:** Faça `merge` `inner`, `left` e `outer`; anote quantas linhas resultam e identifique cidades sem correspondência.

   **Pergunta:** Qual cuidado evita conclusões distorcidas ao trabalhar com **Agrupamento, merge e reshape**?

- [ ] A) Somar todas as colunas numéricas independentemente do significado.
- [ ] B) Arredondar os valores antes de analisar diferenças.
- [ ] C) Usar apenas as primeiras linhas como representação de toda a base.
- [ ] D) Substituir valores ausentes pelo maior valor disponível.
- [ ] E) Manter a granularidade correta e conferir o efeito de filtros, agrupamentos e junções.

3. **Referência — atividade 3:** Crie uma tabela dinâmica com cidade nas linhas, severidade nas colunas e duração média nos valores.

   **Pergunta:** Qual verificação é mais útil para encontrar problemas que uma média geral pode esconder em **Agrupamento, merge e reshape**?

- [ ] A) Excluir categorias pequenas antes de examiná-las.
- [ ] B) Duplicar a base e repetir o mesmo cálculo.
- [ ] C) Comparar segmentos, distribuições, valores extremos e grupos com poucos registros.
- [ ] D) Ordenar as colunas pelo tamanho do nome.
- [ ] E) Trocar as cores do gráfico até a tendência ficar mais visível.

4. **Referência — atividade 4:** Transforme dados largos em longos com `melt` e volte ao formato largo com `pivot`.

   **Pergunta:** Como uma análise de **Agrupamento, merge e reshape** deve ser apresentada para apoiar uma decisão?

- [ ] A) Ligando evidências à pergunta de negócio, com limitações e uma ação recomendada.
- [ ] B) Mostrando todas as tabelas produzidas, sem priorizar uma conclusão.
- [ ] C) Omitindo incertezas para transmitir mais confiança.
- [ ] D) Usando apenas termos técnicos, sem explicar o impacto.
- [ ] E) Escolhendo a recomendação mais popular, mesmo sem evidência.

5. **Referência — atividade 5:** Provoque uma chave duplicada em `metas_cidades.csv`, observe o aumento de linhas e crie uma validação para impedir merge muitos-para-muitos acidental.

   **Pergunta:** Ordene um fluxo de análise para uma atividade de **Agrupamento, merge e reshape**.

- A) Definir a pergunta que precisa ser respondida.
- B) Inspecionar a estrutura e a qualidade dos dados.
- C) Preparar os dados sem perder a granularidade necessária.
- D) Comunicar a conclusão, as limitações e a ação sugerida.
- E) Calcular e visualizar as evidências relevantes.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene a preparação de uma visualização ou entrega sobre **Agrupamento, merge e reshape**.

- A) Escolher o tipo de visual compatível com a comparação.
- B) Selecionar a métrica e o recorte adequados.
- C) Identificar o público e a decisão que será apoiada.
- D) Apresentar a mensagem principal e o próximo passo.
- E) Revisar rótulos, escalas e possíveis interpretações enganosas.

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

- **Conhecimento praticado hoje:** Agrupamento, merge e reshape.
- **Competência sugerida:** Manipulação e integração de dados com pandas.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Manipulação e integração de dados com pandas** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Python`.
- **Próximo marco do perfil:** Dia 20 — Engenharia de Software | Análise de Dados | Python e Power BI.

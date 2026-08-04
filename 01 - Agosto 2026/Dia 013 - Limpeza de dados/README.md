<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 13 — Limpeza de dados — 19/08/2026
> [!abstract] Resultado concreto do dia
> Concluir **Limpeza de dados** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Limpeza de dados.
- **Pasta/arquivo principal:** `semana-03/dia-013-limpeza-de-dados.ipynb`.
- **Dados:** `dados/incidentes.csv`, `dados/clientes_telecom.csv`, `dados/pedidos.csv` e `dados/metas_cidades.csv`.

### Passo a passo completo
1. [ ] Use uma base com ausentes, duplicados, categorias inconsistentes (`Eunapolis`, `Eunápolis`, `EUNÁPOLIS`) e valores extremos.
2. [ ] Produza um relatório inicial com quantidade e percentual de ausentes, duplicados e valores inválidos por coluna.
3. [ ] Padronize textos, converta datas e tipos, trate duplicados com regra explícita e escolha uma estratégia para cada ausente.
4. [ ] Detecte outliers por IQR e z-score; compare quais linhas cada método marca e não remova nada sem justificativa.
5. [ ] Salve `dados_limpos.csv` e `relatorio_limpeza.md` com antes/depois, decisões e riscos de distorção.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Aplique a técnica central de **Limpeza de dados** a uma segunda coluna, grupo ou recorte dos dados e compare o que mudou.
- [ ] Introduza uma cópia dos dados com um problema controlado — valor ausente, duplicado ou outlier — e verifique como ele afeta o resultado.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Use uma base com ausentes, duplicados, categorias inconsistentes (`Eunapolis`, `Eunápolis`, `EUNÁPOLIS`) e valores extremos.

   **Pergunta:** Antes de tirar conclusões em **Limpeza de dados**, qual é a prática mais confiável?

- [ ] A) Calcular médias antes de entender o que cada linha representa.
- [ ] B) Considerar os nomes das colunas suficientes para validar os dados.
- [ ] C) Inspecionar estrutura, tipos, granularidade, valores ausentes e possíveis duplicidades.
- [ ] D) Começar pelo gráfico mais bonito e escolher os dados depois.
- [ ] E) Remover todas as linhas incompletas sem medir o impacto.

2. **Referência — atividade 2:** Produza um relatório inicial com quantidade e percentual de ausentes, duplicados e valores inválidos por coluna.

   **Pergunta:** Qual cuidado evita conclusões distorcidas ao trabalhar com **Limpeza de dados**?

- [ ] A) Manter a granularidade correta e conferir o efeito de filtros, agrupamentos e junções.
- [ ] B) Somar todas as colunas numéricas independentemente do significado.
- [ ] C) Arredondar os valores antes de analisar diferenças.
- [ ] D) Usar apenas as primeiras linhas como representação de toda a base.
- [ ] E) Substituir valores ausentes pelo maior valor disponível.

3. **Referência — atividade 3:** Padronize textos, converta datas e tipos, trate duplicados com regra explícita e escolha uma estratégia para cada ausente.

   **Pergunta:** Qual verificação é mais útil para encontrar problemas que uma média geral pode esconder em **Limpeza de dados**?

- [ ] A) Trocar as cores do gráfico até a tendência ficar mais visível.
- [ ] B) Excluir categorias pequenas antes de examiná-las.
- [ ] C) Duplicar a base e repetir o mesmo cálculo.
- [ ] D) Comparar segmentos, distribuições, valores extremos e grupos com poucos registros.
- [ ] E) Ordenar as colunas pelo tamanho do nome.

4. **Referência — atividade 4:** Detecte outliers por IQR e z-score; compare quais linhas cada método marca e não remova nada sem justificativa.

   **Pergunta:** Como uma análise de **Limpeza de dados** deve ser apresentada para apoiar uma decisão?

- [ ] A) Escolhendo a recomendação mais popular, mesmo sem evidência.
- [ ] B) Ligando evidências à pergunta de negócio, com limitações e uma ação recomendada.
- [ ] C) Mostrando todas as tabelas produzidas, sem priorizar uma conclusão.
- [ ] D) Omitindo incertezas para transmitir mais confiança.
- [ ] E) Usando apenas termos técnicos, sem explicar o impacto.

5. **Referência — atividade 5:** Salve `dados_limpos.csv` e `relatorio_limpeza.md` com antes/depois, decisões e riscos de distorção.

   **Pergunta:** Ordene um fluxo de análise para uma atividade de **Limpeza de dados**.

- A) Preparar os dados sem perder a granularidade necessária.
- B) Inspecionar a estrutura e a qualidade dos dados.
- C) Definir a pergunta que precisa ser respondida.
- D) Comunicar a conclusão, as limitações e a ação sugerida.
- E) Calcular e visualizar as evidências relevantes.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene a preparação de uma visualização ou entrega sobre **Limpeza de dados**.

- A) Apresentar a mensagem principal e o próximo passo.
- B) Selecionar a métrica e o recorte adequados.
- C) Escolher o tipo de visual compatível com a comparação.
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

- **Conhecimento praticado hoje:** Limpeza de dados.
- **Competência sugerida:** Limpeza de dados.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Limpeza de dados** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Python`.
- **Próximo marco do perfil:** Dia 20 — Engenharia de Software | Análise de Dados | Python e Power BI.

<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 83 — Modelagem de risco — 25/11/2026
> [!abstract] Resultado concreto do dia
> Concluir **Modelagem de risco** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Modelagem de risco.
- **Pasta/arquivo principal:** `01-exercicios/dia-083-modelagem-de-risco.ipynb`.
- **Dados:** `dados/credito.csv`.

### Passo a passo completo
1. [ ] Treine regressão logística como scorecard básico e modelos de árvore.
2. [ ] Avalie ROC-AUC, PR-AUC, KS, calibração e matriz de confusão.
3. [ ] Faça validação temporal, não apenas aleatória.
4. [ ] Analise estabilidade e desempenho por segmentos.
5. [ ] Escolha modelo explicável compatível com política de crédito.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/dia-083-modelagem-de-risco.ipynb`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/dia-083-modelagem-de-risco.ipynb`:** Compare calibração e KS no conjunto temporal final para logística e o melhor modelo de árvore.
- [ ] **Em `01-exercicios/dia-083-modelagem-de-risco.ipynb`:** Calcule as métricas separadamente para contratos com prazo até 12 meses e acima de 24 meses.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Treine regressão logística como scorecard básico e modelos de árvore.

   **Pergunta:** Qual definição é essencial antes de modelar **Modelagem de risco**?

- [ ] A) Remover todos os casos sem histórico longo.
- [ ] B) Definir risco apenas como uma pontuação alta do modelo.
- [ ] C) Estabelecer o evento de risco, o horizonte, a população e a data-limite das informações permitidas.
- [ ] D) Escolher o algoritmo antes de definir o evento.
- [ ] E) Usar dados posteriores ao evento para completar o cadastro.

2. **Referência — atividade 2:** Avalie ROC-AUC, PR-AUC, KS, calibração e matriz de confusão.

   **Pergunta:** Por que a calibração importa em uma aplicação de **Modelagem de risco**?

- [ ] A) Porque a probabilidade estimada precisa representar uma frequência útil para políticas baseadas em custo e risco.
- [ ] B) Porque transforma qualquer modelo no mais preciso.
- [ ] C) Porque elimina diferenças entre grupos.
- [ ] D) Porque permite ignorar a taxa-base do evento.
- [ ] E) Porque substitui a validação temporal.

3. **Referência — atividade 3:** Faça validação temporal, não apenas aleatória.

   **Pergunta:** Qual cuidado de governança é necessário em **Modelagem de risco**?

- [ ] A) Avaliar somente o grupo mais numeroso.
- [ ] B) Usar atributos sensíveis sem analisar consequências.
- [ ] C) Manter a política fixa mesmo quando os dados mudarem.
- [ ] D) Documentar dados, critérios, limitações e desempenho por segmento, com revisão de possíveis impactos injustos.
- [ ] E) Ocultar as variáveis para impedir questionamentos.

4. **Referência — atividade 4:** Analise estabilidade e desempenho por segmentos.

   **Pergunta:** Como transformar uma pontuação de **Modelagem de risco** em política?

- [ ] A) Ignorar o custo de erros porque a probabilidade já resume tudo.
- [ ] B) Definir faixas e ações segundo perdas, capacidade, restrições e acompanhamento posterior.
- [ ] C) Aplicar automaticamente a mesma decisão a toda pontuação positiva.
- [ ] D) Usar 50% como corte obrigatório.
- [ ] E) Escolher o corte que aprova o menor número de pessoas.

5. **Referência — atividade 5:** Escolha modelo explicável compatível com política de crédito.

   **Pergunta:** Ordene o desenvolvimento de um modelo para **Modelagem de risco**.

- A) Definir evento, horizonte, população e restrições.
- B) Construir dados disponíveis até a data de decisão.
- C) Separar períodos e treinar um baseline.
- D) Documentar limites e propor uma política de uso.
- E) Avaliar discriminação, calibração e desempenho por segmento.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene a criação de uma política baseada em **Modelagem de risco**.

- A) Definir custos, benefícios, capacidade e restrições.
- B) Simular faixas de pontuação e decisões possíveis.
- C) Escolher regras compatíveis com risco e operação.
- D) Monitorar impacto, estabilidade e diferenças entre grupos.
- E) Aplicar a política com controles e rastreabilidade.

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

- **Conhecimento praticado hoje:** Modelagem de risco.
- **Competência sugerida:** Modelagem de risco.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Modelagem de risco** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

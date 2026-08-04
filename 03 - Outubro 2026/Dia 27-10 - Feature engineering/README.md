<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 61 — Feature engineering — 26/10/2026
> [!abstract] Resultado concreto do dia
> Concluir **Feature engineering** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Feature engineering.
- **Pasta/arquivo principal:** `01-exercicios/dia-061-feature-engineering.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Passo a passo completo
1. [ ] Crie pelo menos oito features de churn agrupadas em comportamento, financeiro, suporte e relacionamento.
2. [ ] Defina para cada feature: fórmula, fonte, momento de disponibilidade e risco de leakage.
3. [ ] Implemente features em funções ou transformer customizado.
4. [ ] Faça análise de ablação por grupo.
5. [ ] Elimine features que dependam do futuro ou duplicam o alvo.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/dia-061-feature-engineering.ipynb`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/dia-061-feature-engineering.ipynb`:** Crie a feature chamados_por_mes usando somente chamados anteriores à data de referência e documente a fórmula.
- [ ] **Em `01-exercicios/dia-061-feature-engineering.ipynb`:** Remova todas as features financeiras e refaça a ablação no mesmo split para medir a perda de desempenho.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Crie pelo menos oito features de churn agrupadas em comportamento, financeiro, suporte e relacionamento.

   **Pergunta:** Qual prática evita vazamento de dados em uma atividade de **Feature engineering**?

- [ ] A) Normalizar toda a base antes da separação para usar mais informação.
- [ ] B) Escolher variáveis depois de observar o desempenho no teste.
- [ ] C) Duplicar exemplos raros antes de separar os conjuntos.
- [ ] D) Usar a variável-alvo para preencher valores ausentes de todas as colunas.
- [ ] E) Separar treino e teste antes de ajustar transformações, selecionar variáveis ou treinar o modelo.

2. **Referência — atividade 2:** Defina para cada feature: fórmula, fonte, momento de disponibilidade e risco de leakage.

   **Pergunta:** Como escolher uma métrica adequada para avaliar **Feature engineering**?

- [ ] A) Trocando de métrica depois de ver qual favorece o modelo.
- [ ] B) Avaliando apenas o tempo de treinamento do algoritmo.
- [ ] C) Considerando o tipo de problema, o desbalanceamento e o custo dos diferentes erros para o negócio.
- [ ] D) Usando sempre acurácia, pois ela serve para qualquer problema.
- [ ] E) Escolhendo a métrica que produz o maior número.

3. **Referência — atividade 3:** Implemente features em funções ou transformer customizado.

   **Pergunta:** Qual procedimento fornece uma comparação mais confiável entre modelos em **Feature engineering**?

- [ ] A) Usar o mesmo protocolo de validação, ajustar decisões no treino e reservar o teste para a avaliação final.
- [ ] B) Testar cada modelo em uma divisão diferente dos dados.
- [ ] C) Escolher pelo desempenho no conjunto usado para treinar.
- [ ] D) Consultar repetidamente o teste durante cada ajuste.
- [ ] E) Comparar somente a quantidade de parâmetros dos algoritmos.

4. **Referência — atividade 4:** Faça análise de ablação por grupo.

   **Pergunta:** Antes de usar um modelo de **Feature engineering** em uma decisão real, o que deve ser analisado?

- [ ] A) A aparência dos gráficos de treinamento, sem examinar dados.
- [ ] B) A complexidade do nome do algoritmo escolhido.
- [ ] C) A quantidade de linhas de código usada para criar o modelo.
- [ ] D) Erros por segmento, estabilidade, explicabilidade e impacto dos falsos positivos e falsos negativos.
- [ ] E) Somente a métrica média do melhor experimento.

5. **Referência — atividade 5:** Elimine features que dependam do futuro ou duplicam o alvo.

   **Pergunta:** Ordene um fluxo de modelagem para **Feature engineering**.

- A) Definir o problema, a população, o alvo e a métrica.
- B) Avaliar, analisar erros e relacionar o modelo à decisão.
- C) Ajustar o pré-processamento apenas com os dados de treino.
- D) Treinar um baseline e modelos candidatos.
- E) Separar os dados conforme o contexto do problema.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene uma seleção responsável de modelo em **Feature engineering**.

- A) Ajustar hiperparâmetros sem consultar o conjunto de teste.
- B) Comparar candidatos com o mesmo protocolo de validação.
- C) Estabelecer um baseline simples e reproduzível.
- D) Avaliar uma vez no teste após fechar as escolhas.
- E) Documentar limitações, segmentos frágeis e regras de uso.

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

- **Conhecimento praticado hoje:** Feature engineering.
- **Competência sugerida:** Feature Engineering.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Feature Engineering** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

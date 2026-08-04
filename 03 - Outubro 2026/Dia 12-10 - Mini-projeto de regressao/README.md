<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 50 — Mini-projeto de regressão — 09/10/2026
> [!abstract] Resultado concreto do dia
> Concluir **Mini-projeto de regressão** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Mini-projeto de regressão.
- **Pasta/arquivo principal:** `01-exercicios/roteiro_atividades.md`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Passo a passo completo
1. [ ] Escolha um problema de regressão: prever receita diária ou duração de incidente.
2. [ ] Faça EDA orientada, split adequado, baseline pela média e pelo último valor quando temporal.
3. [ ] Treine regressão linear e pelo menos um modelo de árvore; compare MAE/RMSE.
4. [ ] Analise os 10 maiores erros e proponha duas features futuras.
5. [ ] Entregue README com pergunta, dados, validação, resultado, decisão e limitações.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/roteiro_atividades.md`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Use duração de incidente como alvo, compare baseline da média com árvore e mantenha random_state=42.
- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Nos 10 maiores erros, conte quantos são P1/P2 e compare com a proporção dessas classes na base.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Escolha um problema de regressão: prever receita diária ou duração de incidente.

   **Pergunta:** Qual prática evita vazamento de dados em uma atividade de **Mini-projeto de regressão**?

- [ ] A) Separar treino e teste antes de ajustar transformações, selecionar variáveis ou treinar o modelo.
- [ ] B) Normalizar toda a base antes da separação para usar mais informação.
- [ ] C) Escolher variáveis depois de observar o desempenho no teste.
- [ ] D) Duplicar exemplos raros antes de separar os conjuntos.
- [ ] E) Usar a variável-alvo para preencher valores ausentes de todas as colunas.

2. **Referência — atividade 2:** Faça EDA orientada, split adequado, baseline pela média e pelo último valor quando temporal.

   **Pergunta:** Como escolher uma métrica adequada para avaliar **Mini-projeto de regressão**?

- [ ] A) Escolhendo a métrica que produz o maior número.
- [ ] B) Trocando de métrica depois de ver qual favorece o modelo.
- [ ] C) Avaliando apenas o tempo de treinamento do algoritmo.
- [ ] D) Considerando o tipo de problema, o desbalanceamento e o custo dos diferentes erros para o negócio.
- [ ] E) Usando sempre acurácia, pois ela serve para qualquer problema.

3. **Referência — atividade 3:** Treine regressão linear e pelo menos um modelo de árvore; compare MAE/RMSE.

   **Pergunta:** Qual procedimento fornece uma comparação mais confiável entre modelos em **Mini-projeto de regressão**?

- [ ] A) Comparar somente a quantidade de parâmetros dos algoritmos.
- [ ] B) Usar o mesmo protocolo de validação, ajustar decisões no treino e reservar o teste para a avaliação final.
- [ ] C) Testar cada modelo em uma divisão diferente dos dados.
- [ ] D) Escolher pelo desempenho no conjunto usado para treinar.
- [ ] E) Consultar repetidamente o teste durante cada ajuste.

4. **Referência — atividade 4:** Analise os 10 maiores erros e proponha duas features futuras.

   **Pergunta:** Antes de usar um modelo de **Mini-projeto de regressão** em uma decisão real, o que deve ser analisado?

- [ ] A) Somente a métrica média do melhor experimento.
- [ ] B) A aparência dos gráficos de treinamento, sem examinar dados.
- [ ] C) A complexidade do nome do algoritmo escolhido.
- [ ] D) A quantidade de linhas de código usada para criar o modelo.
- [ ] E) Erros por segmento, estabilidade, explicabilidade e impacto dos falsos positivos e falsos negativos.

5. **Referência — atividade 5:** Entregue README com pergunta, dados, validação, resultado, decisão e limitações.

   **Pergunta:** Ordene um fluxo de modelagem para **Mini-projeto de regressão**.

- A) Avaliar, analisar erros e relacionar o modelo à decisão.
- B) Separar os dados conforme o contexto do problema.
- C) Definir o problema, a população, o alvo e a métrica.
- D) Treinar um baseline e modelos candidatos.
- E) Ajustar o pré-processamento apenas com os dados de treino.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene uma seleção responsável de modelo em **Mini-projeto de regressão**.

- A) Documentar limitações, segmentos frágeis e regras de uso.
- B) Comparar candidatos com o mesmo protocolo de validação.
- C) Ajustar hiperparâmetros sem consultar o conjunto de teste.
- D) Avaliar uma vez no teste após fechar as escolhas.
- E) Estabelecer um baseline simples e reproduzível.

**Ordem:** `__ → __ → __ → __ → __`

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Alterações registradas em commit e enviadas ao GitHub.

**Autoavaliação do dia:** `__/5`  

> [!project] Projeto semanal — Previsão de tempo de reparo
> **Desafio:** Estimar duração de atendimento ou reparo e converter a previsão em planejamento operacional.
>
> **Deve reutilizar:** Regressão, métricas, regularização e feature engineering.
>
> **Entregáveis obrigatórios:**
> - [ ] baseline ingênuo;
> - [ ] dois modelos;
> - [ ] análise de resíduos;
> - [ ] impacto operacional;
> - [ ] README;
>
> **Defesa:** demonstração de cinco minutos e resposta a três perguntas técnicas.
>
> **Nota mínima recomendada:** `6/10`.

> [!check] Critério para avançar
> Você consegue traduzir MAE/RMSE em impacto real e identificar quando o modelo falha?

---

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Mini-projeto de regressão.
- **Competência sugerida:** Modelagem de regressão.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Modelagem de regressão** na seção Competências. Se a entrega estiver revisada e representar bem seu trabalho, considere incluí-la em Projetos ou Destaques.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

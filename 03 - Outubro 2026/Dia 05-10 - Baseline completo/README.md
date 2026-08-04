<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 45 — Baseline completo — 02/10/2026
> [!abstract] Resultado concreto do dia
> Concluir **Baseline completo** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Baseline completo.
- **Pasta/arquivo principal:** `01-exercicios/roteiro_atividades.md`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Passo a passo completo
1. [ ] Treine baseline `DummyClassifier`, regressão logística simples e regra de negócio.
2. [ ] Use a mesma divisão e pipeline para todos; registre tempo de treino e métricas em tabela.
3. [ ] Crie uma função `avaliar_modelo()` que retorne métricas e matriz de confusão.
4. [ ] Faça análise de erros de 20 casos: 10 falsos positivos e 10 falsos negativos.
5. [ ] Publique notebook executável do início ao fim e um resumo de qual baseline deve ser superado.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/roteiro_atividades.md`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Avalie Dummy, logística e regra de negócio também no limiar 0,35 usando exatamente o mesmo conjunto de validação.
- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Separe os erros de Salvador e das demais cidades e compare quantidade de FP e FN nos dois grupos.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Treine baseline `DummyClassifier`, regressão logística simples e regra de negócio.

   **Pergunta:** Qual prática evita vazamento de dados em uma atividade de **Baseline completo**?

- [ ] A) Separar treino e teste antes de ajustar transformações, selecionar variáveis ou treinar o modelo.
- [ ] B) Normalizar toda a base antes da separação para usar mais informação.
- [ ] C) Escolher variáveis depois de observar o desempenho no teste.
- [ ] D) Duplicar exemplos raros antes de separar os conjuntos.
- [ ] E) Usar a variável-alvo para preencher valores ausentes de todas as colunas.

2. **Referência — atividade 2:** Use a mesma divisão e pipeline para todos; registre tempo de treino e métricas em tabela.

   **Pergunta:** Como escolher uma métrica adequada para avaliar **Baseline completo**?

- [ ] A) Escolhendo a métrica que produz o maior número.
- [ ] B) Trocando de métrica depois de ver qual favorece o modelo.
- [ ] C) Avaliando apenas o tempo de treinamento do algoritmo.
- [ ] D) Considerando o tipo de problema, o desbalanceamento e o custo dos diferentes erros para o negócio.
- [ ] E) Usando sempre acurácia, pois ela serve para qualquer problema.

3. **Referência — atividade 3:** Crie uma função `avaliar_modelo()` que retorne métricas e matriz de confusão.

   **Pergunta:** Qual procedimento fornece uma comparação mais confiável entre modelos em **Baseline completo**?

- [ ] A) Comparar somente a quantidade de parâmetros dos algoritmos.
- [ ] B) Usar o mesmo protocolo de validação, ajustar decisões no treino e reservar o teste para a avaliação final.
- [ ] C) Testar cada modelo em uma divisão diferente dos dados.
- [ ] D) Escolher pelo desempenho no conjunto usado para treinar.
- [ ] E) Consultar repetidamente o teste durante cada ajuste.

4. **Referência — atividade 4:** Faça análise de erros de 20 casos: 10 falsos positivos e 10 falsos negativos.

   **Pergunta:** Antes de usar um modelo de **Baseline completo** em uma decisão real, o que deve ser analisado?

- [ ] A) Somente a métrica média do melhor experimento.
- [ ] B) A aparência dos gráficos de treinamento, sem examinar dados.
- [ ] C) A complexidade do nome do algoritmo escolhido.
- [ ] D) A quantidade de linhas de código usada para criar o modelo.
- [ ] E) Erros por segmento, estabilidade, explicabilidade e impacto dos falsos positivos e falsos negativos.

5. **Referência — atividade 5:** Publique notebook executável do início ao fim e um resumo de qual baseline deve ser superado.

   **Pergunta:** Ordene um fluxo de modelagem para **Baseline completo**.

- A) Definir o problema, a população, o alvo e a métrica.
- B) Avaliar, analisar erros e relacionar o modelo à decisão.
- C) Separar os dados conforme o contexto do problema.
- D) Treinar um baseline e modelos candidatos.
- E) Ajustar o pré-processamento apenas com os dados de treino.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene uma seleção responsável de modelo em **Baseline completo**.

- A) Estabelecer um baseline simples e reproduzível.
- B) Ajustar hiperparâmetros sem consultar o conjunto de teste.
- C) Documentar limitações, segmentos frágeis e regras de uso.
- D) Avaliar uma vez no teste após fechar as escolhas.
- E) Comparar candidatos com o mesmo protocolo de validação.

**Ordem:** `__ → __ → __ → __ → __`

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Alterações registradas em commit e enviadas ao GitHub.

**Autoavaliação do dia:** `__/5`  

> [!todo] PUBLICAR NO LINKEDIN — projeto prioritário do portfólio
> - [ ] Publique somente após README, resultados e limitações estarem revisados.
> - [ ] Inclua problema, abordagem, principal evidência, decisão e link do GitHub.
> - [ ] **Ângulo sugerido:** apresentar definição do problema, prevenção de leakage, baseline e primeira decisão orientada por métricas.

> [!project] Projeto semanal — Baseline completo de churn
> **Desafio:** Transformar um problema de cancelamento em baseline reproduzível, com separação correta e pipeline de pré-processamento.
>
> **Deve reutilizar:** Fundamentos, SQL, estatística e fluxo de ML.
>
> **Entregáveis obrigatórios:**
> - [ ] definição do alvo;
> - [ ] checagem de leakage;
> - [ ] pipeline;
> - [ ] baseline e métricas;
> - [ ] model card inicial;
>
> **Defesa:** demonstração de cinco minutos e resposta a três perguntas técnicas.
>
> **Nota mínima recomendada:** `6/10`.

> [!check] Critério para avançar
> Você consegue explicar por que seu split, pipeline, baseline e métrica são coerentes com a decisão de negócio?

---

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Baseline completo.
- **Competência sugerida:** Baselines de Machine Learning.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Baselines de Machine Learning** na seção Competências. Se a entrega estiver revisada e representar bem seu trabalho, considere incluí-la em Projetos ou Destaques.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

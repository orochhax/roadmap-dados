<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 41 — Definição do problema — 28/09/2026
> [!abstract] Resultado concreto do dia
> Concluir **Definição do problema** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Definição do problema.
- **Pasta/arquivo principal:** `semana-09/dia-041-definicao-do-problema.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Passo a passo completo
1. [ ] Escolha um problema binário usando `clientes_telecom.csv`: prever churn nos próximos 30 dias; escreva alvo, unidade de previsão e horizonte temporal.
2. [ ] Defina quem usará a previsão, qual ação será tomada e qual erro é mais caro.
3. [ ] Liste 15 variáveis possíveis e classifique cada uma como disponível, indisponível, sensível ou potencial leakage.
4. [ ] Crie baseline de negócio: prever todos como não churn e comparar com regra simples `chamados_90d >= 3`.
5. [ ] Escreva `problem_statement.md` com objetivo, restrições, métrica primária, métricas secundárias e critério de sucesso.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Faça uma alteração controlada em uma feature, modelo, hiperparâmetro ou limiar de **Definição do problema** e compare usando a mesma validação.
- [ ] Separe alguns erros do modelo por grupo ou tipo de caso e registre onde o desempenho piora e o que investigar.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Escolha um problema binário usando `clientes_telecom.csv`: prever churn nos próximos 30 dias; escreva alvo, unidade de previsão e horizonte temporal.

   **Pergunta:** Qual prática evita vazamento de dados em uma atividade de **Definição do problema**?

- [ ] A) Normalizar toda a base antes da separação para usar mais informação.
- [ ] B) Escolher variáveis depois de observar o desempenho no teste.
- [ ] C) Duplicar exemplos raros antes de separar os conjuntos.
- [ ] D) Usar a variável-alvo para preencher valores ausentes de todas as colunas.
- [ ] E) Separar treino e teste antes de ajustar transformações, selecionar variáveis ou treinar o modelo.

2. **Referência — atividade 2:** Defina quem usará a previsão, qual ação será tomada e qual erro é mais caro.

   **Pergunta:** Como escolher uma métrica adequada para avaliar **Definição do problema**?

- [ ] A) Trocando de métrica depois de ver qual favorece o modelo.
- [ ] B) Avaliando apenas o tempo de treinamento do algoritmo.
- [ ] C) Considerando o tipo de problema, o desbalanceamento e o custo dos diferentes erros para o negócio.
- [ ] D) Usando sempre acurácia, pois ela serve para qualquer problema.
- [ ] E) Escolhendo a métrica que produz o maior número.

3. **Referência — atividade 3:** Liste 15 variáveis possíveis e classifique cada uma como disponível, indisponível, sensível ou potencial leakage.

   **Pergunta:** Qual procedimento fornece uma comparação mais confiável entre modelos em **Definição do problema**?

- [ ] A) Usar o mesmo protocolo de validação, ajustar decisões no treino e reservar o teste para a avaliação final.
- [ ] B) Testar cada modelo em uma divisão diferente dos dados.
- [ ] C) Escolher pelo desempenho no conjunto usado para treinar.
- [ ] D) Consultar repetidamente o teste durante cada ajuste.
- [ ] E) Comparar somente a quantidade de parâmetros dos algoritmos.

4. **Referência — atividade 4:** Crie baseline de negócio: prever todos como não churn e comparar com regra simples `chamados_90d >= 3`.

   **Pergunta:** Antes de usar um modelo de **Definição do problema** em uma decisão real, o que deve ser analisado?

- [ ] A) A aparência dos gráficos de treinamento, sem examinar dados.
- [ ] B) A complexidade do nome do algoritmo escolhido.
- [ ] C) A quantidade de linhas de código usada para criar o modelo.
- [ ] D) Erros por segmento, estabilidade, explicabilidade e impacto dos falsos positivos e falsos negativos.
- [ ] E) Somente a métrica média do melhor experimento.

5. **Referência — atividade 5:** Escreva `problem_statement.md` com objetivo, restrições, métrica primária, métricas secundárias e critério de sucesso.

   **Pergunta:** Ordene um fluxo de modelagem para **Definição do problema**.

- A) Definir o problema, a população, o alvo e a métrica.
- B) Separar os dados conforme o contexto do problema.
- C) Ajustar o pré-processamento apenas com os dados de treino.
- D) Avaliar, analisar erros e relacionar o modelo à decisão.
- E) Treinar um baseline e modelos candidatos.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene uma seleção responsável de modelo em **Definição do problema**.

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

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Definição do problema.
- **Competência sugerida:** Definição de problemas de Machine Learning.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Definição de problemas de Machine Learning** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

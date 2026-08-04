<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 63 — Seleção de variáveis — 28/10/2026
> [!abstract] Resultado concreto do dia
> Concluir **Seleção de variáveis** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Seleção de variáveis.
- **Pasta/arquivo principal:** `01-exercicios/dia-063-selecao-de-variaveis.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Passo a passo completo
1. [ ] Remova colunas constantes, quase constantes e duplicadas.
2. [ ] Calcule correlação entre numéricas e identifique grupos redundantes.
3. [ ] Compare seleção univariada, importância de modelo e RFE em subconjunto pequeno.
4. [ ] Treine modelo com todas as features e com seleção; compare métrica e estabilidade.
5. [ ] Documente por que feature selecionada não implica causalidade.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/dia-063-selecao-de-variaveis.ipynb`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/dia-063-selecao-de-variaveis.ipynb`:** Compare remoção de correlações acima de 0,90 e 0,75 e registre quantidade de features e métrica.
- [ ] **Em `01-exercicios/dia-063-selecao-de-variaveis.ipynb`:** Adicione uma cópia exata de uma coluna, faça a detecção removê-la e confirme que a original permanece.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Remova colunas constantes, quase constantes e duplicadas.

   **Pergunta:** Qual prática evita vazamento de dados em uma atividade de **Seleção de variáveis**?

- [ ] A) Duplicar exemplos raros antes de separar os conjuntos.
- [ ] B) Usar a variável-alvo para preencher valores ausentes de todas as colunas.
- [ ] C) Separar treino e teste antes de ajustar transformações, selecionar variáveis ou treinar o modelo.
- [ ] D) Normalizar toda a base antes da separação para usar mais informação.
- [ ] E) Escolher variáveis depois de observar o desempenho no teste.

2. **Referência — atividade 2:** Calcule correlação entre numéricas e identifique grupos redundantes.

   **Pergunta:** Como escolher uma métrica adequada para avaliar **Seleção de variáveis**?

- [ ] A) Considerando o tipo de problema, o desbalanceamento e o custo dos diferentes erros para o negócio.
- [ ] B) Usando sempre acurácia, pois ela serve para qualquer problema.
- [ ] C) Escolhendo a métrica que produz o maior número.
- [ ] D) Trocando de métrica depois de ver qual favorece o modelo.
- [ ] E) Avaliando apenas o tempo de treinamento do algoritmo.

3. **Referência — atividade 3:** Compare seleção univariada, importância de modelo e RFE em subconjunto pequeno.

   **Pergunta:** Qual procedimento fornece uma comparação mais confiável entre modelos em **Seleção de variáveis**?

- [ ] A) Escolher pelo desempenho no conjunto usado para treinar.
- [ ] B) Consultar repetidamente o teste durante cada ajuste.
- [ ] C) Comparar somente a quantidade de parâmetros dos algoritmos.
- [ ] D) Usar o mesmo protocolo de validação, ajustar decisões no treino e reservar o teste para a avaliação final.
- [ ] E) Testar cada modelo em uma divisão diferente dos dados.

4. **Referência — atividade 4:** Treine modelo com todas as features e com seleção; compare métrica e estabilidade.

   **Pergunta:** Antes de usar um modelo de **Seleção de variáveis** em uma decisão real, o que deve ser analisado?

- [ ] A) A quantidade de linhas de código usada para criar o modelo.
- [ ] B) Erros por segmento, estabilidade, explicabilidade e impacto dos falsos positivos e falsos negativos.
- [ ] C) Somente a métrica média do melhor experimento.
- [ ] D) A aparência dos gráficos de treinamento, sem examinar dados.
- [ ] E) A complexidade do nome do algoritmo escolhido.

5. **Referência — atividade 5:** Documente por que feature selecionada não implica causalidade.

   **Pergunta:** Ordene um fluxo de modelagem para **Seleção de variáveis**.

- A) Avaliar, analisar erros e relacionar o modelo à decisão.
- B) Separar os dados conforme o contexto do problema.
- C) Ajustar o pré-processamento apenas com os dados de treino.
- D) Treinar um baseline e modelos candidatos.
- E) Definir o problema, a população, o alvo e a métrica.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene uma seleção responsável de modelo em **Seleção de variáveis**.

- A) Ajustar hiperparâmetros sem consultar o conjunto de teste.
- B) Comparar candidatos com o mesmo protocolo de validação.
- C) Documentar limitações, segmentos frágeis e regras de uso.
- D) Avaliar uma vez no teste após fechar as escolhas.
- E) Estabelecer um baseline simples e reproduzível.

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

- **Conhecimento praticado hoje:** Seleção de variáveis.
- **Competência sugerida:** Seleção de variáveis.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Seleção de variáveis** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

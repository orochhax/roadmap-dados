<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 56 — Árvore de decisão — 19/10/2026
> [!abstract] Resultado concreto do dia
> Concluir **Árvore de decisão** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Árvore de decisão.
- **Pasta/arquivo principal:** `01-exercicios/dia-056-arvore-de-decisao.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Passo a passo completo
1. [ ] Treine árvore de decisão com profundidades 1, 3, 5, 10 e sem limite.
2. [ ] Visualize uma árvore pequena e traduza cinco divisões em regras de negócio.
3. [ ] Compare desempenho de treino e validação para identificar overfitting.
4. [ ] Varie `min_samples_leaf` e registre estabilidade.
5. [ ] Crie uma árvore deliberadamente complexa e explique por que não deve ser usada apesar da métrica de treino.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/dia-056-arvore-de-decisao.ipynb`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/dia-056-arvore-de-decisao.ipynb`:** Compare profundidade 3 e 10 com min_samples_leaf=20 no mesmo split e registre treino e validação.
- [ ] **Em `01-exercicios/dia-056-arvore-de-decisao.ipynb`:** Escolha uma previsão errada da árvore profunda e escreva as regras percorridas até a folha.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Treine árvore de decisão com profundidades 1, 3, 5, 10 e sem limite.

   **Pergunta:** Qual prática evita vazamento de dados em uma atividade de **Árvore de decisão**?

- [ ] A) Normalizar toda a base antes da separação para usar mais informação.
- [ ] B) Escolher variáveis depois de observar o desempenho no teste.
- [ ] C) Duplicar exemplos raros antes de separar os conjuntos.
- [ ] D) Usar a variável-alvo para preencher valores ausentes de todas as colunas.
- [ ] E) Separar treino e teste antes de ajustar transformações, selecionar variáveis ou treinar o modelo.

2. **Referência — atividade 2:** Visualize uma árvore pequena e traduza cinco divisões em regras de negócio.

   **Pergunta:** Como escolher uma métrica adequada para avaliar **Árvore de decisão**?

- [ ] A) Trocando de métrica depois de ver qual favorece o modelo.
- [ ] B) Avaliando apenas o tempo de treinamento do algoritmo.
- [ ] C) Considerando o tipo de problema, o desbalanceamento e o custo dos diferentes erros para o negócio.
- [ ] D) Usando sempre acurácia, pois ela serve para qualquer problema.
- [ ] E) Escolhendo a métrica que produz o maior número.

3. **Referência — atividade 3:** Compare desempenho de treino e validação para identificar overfitting.

   **Pergunta:** Qual procedimento fornece uma comparação mais confiável entre modelos em **Árvore de decisão**?

- [ ] A) Usar o mesmo protocolo de validação, ajustar decisões no treino e reservar o teste para a avaliação final.
- [ ] B) Testar cada modelo em uma divisão diferente dos dados.
- [ ] C) Escolher pelo desempenho no conjunto usado para treinar.
- [ ] D) Consultar repetidamente o teste durante cada ajuste.
- [ ] E) Comparar somente a quantidade de parâmetros dos algoritmos.

4. **Referência — atividade 4:** Varie `min_samples_leaf` e registre estabilidade.

   **Pergunta:** Antes de usar um modelo de **Árvore de decisão** em uma decisão real, o que deve ser analisado?

- [ ] A) A aparência dos gráficos de treinamento, sem examinar dados.
- [ ] B) A complexidade do nome do algoritmo escolhido.
- [ ] C) A quantidade de linhas de código usada para criar o modelo.
- [ ] D) Erros por segmento, estabilidade, explicabilidade e impacto dos falsos positivos e falsos negativos.
- [ ] E) Somente a métrica média do melhor experimento.

5. **Referência — atividade 5:** Crie uma árvore deliberadamente complexa e explique por que não deve ser usada apesar da métrica de treino.

   **Pergunta:** Ordene um fluxo de modelagem para **Árvore de decisão**.

- A) Definir o problema, a população, o alvo e a métrica.
- B) Avaliar, analisar erros e relacionar o modelo à decisão.
- C) Ajustar o pré-processamento apenas com os dados de treino.
- D) Treinar um baseline e modelos candidatos.
- E) Separar os dados conforme o contexto do problema.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene uma seleção responsável de modelo em **Árvore de decisão**.

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

- **Conhecimento praticado hoje:** Árvore de decisão.
- **Competência sugerida:** Árvore de decisão.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Árvore de decisão** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

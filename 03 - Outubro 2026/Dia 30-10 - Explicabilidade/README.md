<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 64 — Explicabilidade — 29/10/2026
> [!abstract] Resultado concreto do dia
> Concluir **Explicabilidade** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Explicabilidade.
- **Pasta/arquivo principal:** `01-exercicios/dia-064-explicabilidade.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Passo a passo completo
1. [ ] Escolha 10 previsões individuais, incluindo acertos e erros, e explique fatores principais.
2. [ ] Use coeficientes, permutation importance e SHAP se disponível; compare explicações globais e locais.
3. [ ] Teste explicações em dois segmentos demográficos ou operacionais.
4. [ ] Identifique uma explicação plausível porém enganosa causada por correlação.
5. [ ] Crie relatório para público não técnico com três cuidados ao interpretar importância.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/dia-064-explicabilidade.ipynb`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/dia-064-explicabilidade.ipynb`:** Explique uma previsão correta de churn alto e uma incorreta de churn baixo usando o mesmo método local.
- [ ] **Em `01-exercicios/dia-064-explicabilidade.ipynb`:** Remova a feature mais correlacionada com a principal e gere novamente a explicação para observar estabilidade.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Escolha 10 previsões individuais, incluindo acertos e erros, e explique fatores principais.

   **Pergunta:** Qual prática evita vazamento de dados em uma atividade de **Explicabilidade**?

- [ ] A) Usar a variável-alvo para preencher valores ausentes de todas as colunas.
- [ ] B) Separar treino e teste antes de ajustar transformações, selecionar variáveis ou treinar o modelo.
- [ ] C) Normalizar toda a base antes da separação para usar mais informação.
- [ ] D) Escolher variáveis depois de observar o desempenho no teste.
- [ ] E) Duplicar exemplos raros antes de separar os conjuntos.

2. **Referência — atividade 2:** Use coeficientes, permutation importance e SHAP se disponível; compare explicações globais e locais.

   **Pergunta:** Como escolher uma métrica adequada para avaliar **Explicabilidade**?

- [ ] A) Usando sempre acurácia, pois ela serve para qualquer problema.
- [ ] B) Escolhendo a métrica que produz o maior número.
- [ ] C) Trocando de métrica depois de ver qual favorece o modelo.
- [ ] D) Avaliando apenas o tempo de treinamento do algoritmo.
- [ ] E) Considerando o tipo de problema, o desbalanceamento e o custo dos diferentes erros para o negócio.

3. **Referência — atividade 3:** Teste explicações em dois segmentos demográficos ou operacionais.

   **Pergunta:** Qual procedimento fornece uma comparação mais confiável entre modelos em **Explicabilidade**?

- [ ] A) Consultar repetidamente o teste durante cada ajuste.
- [ ] B) Comparar somente a quantidade de parâmetros dos algoritmos.
- [ ] C) Usar o mesmo protocolo de validação, ajustar decisões no treino e reservar o teste para a avaliação final.
- [ ] D) Testar cada modelo em uma divisão diferente dos dados.
- [ ] E) Escolher pelo desempenho no conjunto usado para treinar.

4. **Referência — atividade 4:** Identifique uma explicação plausível porém enganosa causada por correlação.

   **Pergunta:** Antes de usar um modelo de **Explicabilidade** em uma decisão real, o que deve ser analisado?

- [ ] A) Erros por segmento, estabilidade, explicabilidade e impacto dos falsos positivos e falsos negativos.
- [ ] B) Somente a métrica média do melhor experimento.
- [ ] C) A aparência dos gráficos de treinamento, sem examinar dados.
- [ ] D) A complexidade do nome do algoritmo escolhido.
- [ ] E) A quantidade de linhas de código usada para criar o modelo.

5. **Referência — atividade 5:** Crie relatório para público não técnico com três cuidados ao interpretar importância.

   **Pergunta:** Ordene um fluxo de modelagem para **Explicabilidade**.

- A) Avaliar, analisar erros e relacionar o modelo à decisão.
- B) Ajustar o pré-processamento apenas com os dados de treino.
- C) Separar os dados conforme o contexto do problema.
- D) Treinar um baseline e modelos candidatos.
- E) Definir o problema, a população, o alvo e a métrica.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene uma seleção responsável de modelo em **Explicabilidade**.

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

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Explicabilidade.
- **Competência sugerida:** Explicabilidade de modelos.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Explicabilidade de modelos** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

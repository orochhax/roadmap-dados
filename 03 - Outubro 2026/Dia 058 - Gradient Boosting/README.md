<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 58 — Gradient Boosting — 21/10/2026
> [!abstract] Resultado concreto do dia
> Concluir **Gradient Boosting** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Gradient Boosting.
- **Pasta/arquivo principal:** `semana-12/dia-058-gradient-boosting.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Passo a passo completo
1. [ ] Treine Gradient Boosting e, se possível, XGBoost ou LightGBM no mesmo split.
2. [ ] Compare learning rate e número de estimadores em grade pequena.
3. [ ] Observe overfitting por curvas de treino/validação.
4. [ ] Analise importância e erros por segmento.
5. [ ] Documente por que boosting pode ganhar em dados tabulares e quais riscos de tuning existem.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Faça uma alteração controlada em uma feature, modelo, hiperparâmetro ou limiar de **Gradient Boosting** e compare usando a mesma validação.
- [ ] Separe alguns erros do modelo por grupo ou tipo de caso e registre onde o desempenho piora e o que investigar.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Treine Gradient Boosting e, se possível, XGBoost ou LightGBM no mesmo split.

   **Pergunta:** Qual prática evita vazamento de dados em uma atividade de **Gradient Boosting**?

- [ ] A) Duplicar exemplos raros antes de separar os conjuntos.
- [ ] B) Usar a variável-alvo para preencher valores ausentes de todas as colunas.
- [ ] C) Separar treino e teste antes de ajustar transformações, selecionar variáveis ou treinar o modelo.
- [ ] D) Normalizar toda a base antes da separação para usar mais informação.
- [ ] E) Escolher variáveis depois de observar o desempenho no teste.

2. **Referência — atividade 2:** Compare learning rate e número de estimadores em grade pequena.

   **Pergunta:** Como escolher uma métrica adequada para avaliar **Gradient Boosting**?

- [ ] A) Considerando o tipo de problema, o desbalanceamento e o custo dos diferentes erros para o negócio.
- [ ] B) Usando sempre acurácia, pois ela serve para qualquer problema.
- [ ] C) Escolhendo a métrica que produz o maior número.
- [ ] D) Trocando de métrica depois de ver qual favorece o modelo.
- [ ] E) Avaliando apenas o tempo de treinamento do algoritmo.

3. **Referência — atividade 3:** Observe overfitting por curvas de treino/validação.

   **Pergunta:** Qual procedimento fornece uma comparação mais confiável entre modelos em **Gradient Boosting**?

- [ ] A) Escolher pelo desempenho no conjunto usado para treinar.
- [ ] B) Consultar repetidamente o teste durante cada ajuste.
- [ ] C) Comparar somente a quantidade de parâmetros dos algoritmos.
- [ ] D) Usar o mesmo protocolo de validação, ajustar decisões no treino e reservar o teste para a avaliação final.
- [ ] E) Testar cada modelo em uma divisão diferente dos dados.

4. **Referência — atividade 4:** Analise importância e erros por segmento.

   **Pergunta:** Antes de usar um modelo de **Gradient Boosting** em uma decisão real, o que deve ser analisado?

- [ ] A) A quantidade de linhas de código usada para criar o modelo.
- [ ] B) Erros por segmento, estabilidade, explicabilidade e impacto dos falsos positivos e falsos negativos.
- [ ] C) Somente a métrica média do melhor experimento.
- [ ] D) A aparência dos gráficos de treinamento, sem examinar dados.
- [ ] E) A complexidade do nome do algoritmo escolhido.

5. **Referência — atividade 5:** Documente por que boosting pode ganhar em dados tabulares e quais riscos de tuning existem.

   **Pergunta:** Ordene um fluxo de modelagem para **Gradient Boosting**.

- A) Definir o problema, a população, o alvo e a métrica.
- B) Avaliar, analisar erros e relacionar o modelo à decisão.
- C) Ajustar o pré-processamento apenas com os dados de treino.
- D) Treinar um baseline e modelos candidatos.
- E) Separar os dados conforme o contexto do problema.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene uma seleção responsável de modelo em **Gradient Boosting**.

- A) Documentar limitações, segmentos frágeis e regras de uso.
- B) Ajustar hiperparâmetros sem consultar o conjunto de teste.
- C) Comparar candidatos com o mesmo protocolo de validação.
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

- **Conhecimento praticado hoje:** Gradient Boosting.
- **Competência sugerida:** Gradient Boosting.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Gradient Boosting** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

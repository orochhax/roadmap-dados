<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 47 — Métricas de regressão — 06/10/2026
> [!abstract] Resultado concreto do dia
> Concluir **Métricas de regressão** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Métricas de regressão.
- **Pasta/arquivo principal:** `01-exercicios/dia-047-metricas-de-regressao.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Passo a passo completo
1. [ ] No notebook, use `y_real = [100, 120, 80, 0, 200]` e `y_previsto = [90, 135, 70, 10, 180]` para calcular MAE, MSE, RMSE, R² e MAPE manualmente e com biblioteca.
2. [ ] Crie um caso com valor real zero e mostre por que MAPE pode quebrar.
3. [ ] Compare dois modelos: um com poucos erros grandes e outro com muitos erros pequenos.
4. [ ] Escolha a métrica mais coerente para previsão de receita e justifique custo dos erros.
5. [ ] Crie intervalo de erro por faixa de valor e verifique se o modelo piora nos pedidos maiores.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/dia-047-metricas-de-regressao.ipynb`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/dia-047-metricas-de-regressao.ipynb`:** Use y_real=[100, 120, 80, 0, 200] e y_pred=[90, 135, 70, 10, 180] para calcular as métricas e tratar MAPE com zero.
- [ ] **Em `01-exercicios/dia-047-metricas-de-regressao.ipynb`:** Separe os dois maiores valores reais e compare o MAE desse recorte com o MAE dos três menores.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Calcule as métricas usando os vetores `y_real` e `y_previsto` já preparados na primeira célula de código.

   **Pergunta:** Qual prática evita vazamento de dados em uma atividade de **Métricas de regressão**?

- [ ] A) Escolher variáveis depois de observar o desempenho no teste.
- [ ] B) Duplicar exemplos raros antes de separar os conjuntos.
- [ ] C) Usar a variável-alvo para preencher valores ausentes de todas as colunas.
- [ ] D) Separar treino e teste antes de ajustar transformações, selecionar variáveis ou treinar o modelo.
- [ ] E) Normalizar toda a base antes da separação para usar mais informação.

2. **Referência — atividade 2:** Crie um caso com valor real zero e mostre por que MAPE pode quebrar.

   **Pergunta:** Como escolher uma métrica adequada para avaliar **Métricas de regressão**?

- [ ] A) Avaliando apenas o tempo de treinamento do algoritmo.
- [ ] B) Considerando o tipo de problema, o desbalanceamento e o custo dos diferentes erros para o negócio.
- [ ] C) Usando sempre acurácia, pois ela serve para qualquer problema.
- [ ] D) Escolhendo a métrica que produz o maior número.
- [ ] E) Trocando de métrica depois de ver qual favorece o modelo.

3. **Referência — atividade 3:** Compare dois modelos: um com poucos erros grandes e outro com muitos erros pequenos.

   **Pergunta:** Qual procedimento fornece uma comparação mais confiável entre modelos em **Métricas de regressão**?

- [ ] A) Testar cada modelo em uma divisão diferente dos dados.
- [ ] B) Escolher pelo desempenho no conjunto usado para treinar.
- [ ] C) Consultar repetidamente o teste durante cada ajuste.
- [ ] D) Comparar somente a quantidade de parâmetros dos algoritmos.
- [ ] E) Usar o mesmo protocolo de validação, ajustar decisões no treino e reservar o teste para a avaliação final.

4. **Referência — atividade 4:** Escolha a métrica mais coerente para previsão de receita e justifique custo dos erros.

   **Pergunta:** Antes de usar um modelo de **Métricas de regressão** em uma decisão real, o que deve ser analisado?

- [ ] A) A complexidade do nome do algoritmo escolhido.
- [ ] B) A quantidade de linhas de código usada para criar o modelo.
- [ ] C) Erros por segmento, estabilidade, explicabilidade e impacto dos falsos positivos e falsos negativos.
- [ ] D) Somente a métrica média do melhor experimento.
- [ ] E) A aparência dos gráficos de treinamento, sem examinar dados.

5. **Referência — atividade 5:** Crie intervalo de erro por faixa de valor e verifique se o modelo piora nos pedidos maiores.

   **Pergunta:** Ordene um fluxo de modelagem para **Métricas de regressão**.

- A) Definir o problema, a população, o alvo e a métrica.
- B) Avaliar, analisar erros e relacionar o modelo à decisão.
- C) Ajustar o pré-processamento apenas com os dados de treino.
- D) Treinar um baseline e modelos candidatos.
- E) Separar os dados conforme o contexto do problema.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene uma seleção responsável de modelo em **Métricas de regressão**.

- A) Estabelecer um baseline simples e reproduzível.
- B) Documentar limitações, segmentos frágeis e regras de uso.
- C) Ajustar hiperparâmetros sem consultar o conjunto de teste.
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

- **Conhecimento praticado hoje:** Métricas de regressão.
- **Competência sugerida:** Métricas de regressão.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Métricas de regressão** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

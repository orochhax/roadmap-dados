<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 62 — Validação cruzada e tuning — 27/10/2026
> [!abstract] Resultado concreto do dia
> Concluir **Validação cruzada e tuning** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Validação cruzada e tuning.
- **Pasta/arquivo principal:** `01-exercicios/dia-062-validacao-cruzada-e-tuning.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Passo a passo completo
1. [ ] Compare KFold, StratifiedKFold e validação temporal em um exemplo apropriado.
2. [ ] Execute cross-validation com cinco folds e registre média e desvio das métricas.
3. [ ] Faça `RandomizedSearchCV` com espaço pequeno e limite de tempo.
4. [ ] Separe conjunto de teste final e não o use durante tuning.
5. [ ] Compare melhor configuração com padrão e avalie se ganho compensa complexidade.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/dia-062-validacao-cruzada-e-tuning.ipynb`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/dia-062-validacao-cruzada-e-tuning.ipynb`:** Compare StratifiedKFold com 3 e 5 folds usando a mesma pipeline e registre média, desvio e tempo.
- [ ] **Em `01-exercicios/dia-062-validacao-cruzada-e-tuning.ipynb`:** Confirme no código que o conjunto de teste final não aparece em fit, busca de parâmetros ou escolha da configuração.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Compare KFold, StratifiedKFold e validação temporal em um exemplo apropriado.

   **Pergunta:** Qual prática evita vazamento de dados em uma atividade de **Validação cruzada e tuning**?

- [ ] A) Escolher variáveis depois de observar o desempenho no teste.
- [ ] B) Duplicar exemplos raros antes de separar os conjuntos.
- [ ] C) Usar a variável-alvo para preencher valores ausentes de todas as colunas.
- [ ] D) Separar treino e teste antes de ajustar transformações, selecionar variáveis ou treinar o modelo.
- [ ] E) Normalizar toda a base antes da separação para usar mais informação.

2. **Referência — atividade 2:** Execute cross-validation com cinco folds e registre média e desvio das métricas.

   **Pergunta:** Como escolher uma métrica adequada para avaliar **Validação cruzada e tuning**?

- [ ] A) Avaliando apenas o tempo de treinamento do algoritmo.
- [ ] B) Considerando o tipo de problema, o desbalanceamento e o custo dos diferentes erros para o negócio.
- [ ] C) Usando sempre acurácia, pois ela serve para qualquer problema.
- [ ] D) Escolhendo a métrica que produz o maior número.
- [ ] E) Trocando de métrica depois de ver qual favorece o modelo.

3. **Referência — atividade 3:** Faça `RandomizedSearchCV` com espaço pequeno e limite de tempo.

   **Pergunta:** Qual procedimento fornece uma comparação mais confiável entre modelos em **Validação cruzada e tuning**?

- [ ] A) Testar cada modelo em uma divisão diferente dos dados.
- [ ] B) Escolher pelo desempenho no conjunto usado para treinar.
- [ ] C) Consultar repetidamente o teste durante cada ajuste.
- [ ] D) Comparar somente a quantidade de parâmetros dos algoritmos.
- [ ] E) Usar o mesmo protocolo de validação, ajustar decisões no treino e reservar o teste para a avaliação final.

4. **Referência — atividade 4:** Separe conjunto de teste final e não o use durante tuning.

   **Pergunta:** Antes de usar um modelo de **Validação cruzada e tuning** em uma decisão real, o que deve ser analisado?

- [ ] A) A complexidade do nome do algoritmo escolhido.
- [ ] B) A quantidade de linhas de código usada para criar o modelo.
- [ ] C) Erros por segmento, estabilidade, explicabilidade e impacto dos falsos positivos e falsos negativos.
- [ ] D) Somente a métrica média do melhor experimento.
- [ ] E) A aparência dos gráficos de treinamento, sem examinar dados.

5. **Referência — atividade 5:** Compare melhor configuração com padrão e avalie se ganho compensa complexidade.

   **Pergunta:** Ordene um fluxo de modelagem para **Validação cruzada e tuning**.

- A) Avaliar, analisar erros e relacionar o modelo à decisão.
- B) Ajustar o pré-processamento apenas com os dados de treino.
- C) Separar os dados conforme o contexto do problema.
- D) Treinar um baseline e modelos candidatos.
- E) Definir o problema, a população, o alvo e a métrica.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene uma seleção responsável de modelo em **Validação cruzada e tuning**.

- A) Comparar candidatos com o mesmo protocolo de validação.
- B) Ajustar hiperparâmetros sem consultar o conjunto de teste.
- C) Avaliar uma vez no teste após fechar as escolhas.
- D) Documentar limitações, segmentos frágeis e regras de uso.
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

- **Conhecimento praticado hoje:** Validação cruzada e tuning.
- **Competência sugerida:** Validação cruzada e tuning de hiperparâmetros.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Validação cruzada e tuning de hiperparâmetros** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 71 — Baselines e modelos — 09/11/2026
> [!abstract] Resultado concreto do dia
> Concluir **Baselines e modelos** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Baselines e modelos.
- **Pasta/arquivo principal:** `01-exercicios/dia-071-baselines-e-modelos.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Passo a passo completo
1. [ ] Treine regressão logística, árvore, Random Forest e boosting usando a mesma pipeline.
2. [ ] Execute cross-validation no treino e avalie no conjunto de validação.
3. [ ] Crie tabela com média, desvio, custo e tempo.
4. [ ] Analise 20 erros críticos.
5. [ ] Selecione campeão e challenger com justificativa pré-definida.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/dia-071-baselines-e-modelos.ipynb`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/dia-071-baselines-e-modelos.ipynb`:** Compare campeão e challenger no segmento plano Básico 100 e registre tamanho, custo, recall e precision.
- [ ] **Em `01-exercicios/dia-071-baselines-e-modelos.ipynb`:** Aumente o custo de falso negativo de R$500 para R$800 e confira se a escolha do campeão muda.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Treine regressão logística, árvore, Random Forest e boosting usando a mesma pipeline.

   **Pergunta:** Ao desenvolver **Baselines e modelos**, qual definição evita um alvo ambíguo ou vazamento de dados?

- [ ] A) Chamar de churn qualquer cliente com poucos registros.
- [ ] B) Usar informações posteriores ao cancelamento para prever o próprio cancelamento.
- [ ] C) Alterar a definição do alvo para melhorar a métrica do modelo.
- [ ] D) Remover clientes ativos sem registrar o critério usado.
- [ ] E) Fixar a população, a data de referência, a janela de observação e a regra objetiva de churn.

2. **Referência — atividade 2:** Execute cross-validation no treino e avalie no conjunto de validação.

   **Pergunta:** Como avaliar um modelo ligado a **Baselines e modelos** para uma estratégia de retenção?

- [ ] A) Contatando todos os clientes classificados pelo modelo.
- [ ] B) Ignorando a capacidade operacional da equipe de retenção.
- [ ] C) Relacionando métricas e limiar ao custo do contato, ao valor do cliente e ao benefício provável da retenção.
- [ ] D) Escolhendo sempre o limiar de 50%.
- [ ] E) Priorizando somente a acurácia geral.

3. **Referência — atividade 3:** Crie tabela com média, desvio, custo e tempo.

   **Pergunta:** Qual análise ajuda a encontrar riscos escondidos em **Baselines e modelos**?

- [ ] A) Comparar qualidade dos dados, erros e desempenho entre períodos e segmentos de clientes.
- [ ] B) Avaliar apenas os clientes com maior probabilidade.
- [ ] C) Excluir segmentos pequenos antes de medir os erros.
- [ ] D) Usar a mesma explicação para todos os perfis.
- [ ] E) Conferir somente o desempenho no conjunto de treino.

4. **Referência — atividade 4:** Analise 20 erros críticos.

   **Pergunta:** Qual é a melhor ligação entre um modelo de **Baselines e modelos** e uma ação de negócio?

- [ ] A) Considerar todo cliente de alto risco automaticamente perdido.
- [ ] B) Escolher a ação apenas pela variável mais importante do modelo.
- [ ] C) Medir sucesso somente pelo número de contatos realizados.
- [ ] D) Criar uma política explícita que defina quem será priorizado, qual ação receberá e como o impacto será medido.
- [ ] E) Enviar a probabilidade bruta sem orientar seu uso.

5. **Referência — atividade 5:** Selecione campeão e challenger com justificativa pré-definida.

   **Pergunta:** Ordene a construção de um projeto relacionado a **Baselines e modelos**.

- A) Realizar EDA e preparar uma separação sem vazamento.
- B) Transformar previsões em estratégia e comunicar limitações.
- C) Definir população, churn, datas e objetivo de negócio.
- D) Treinar baselines e modelos com métricas adequadas.
- E) Construir e auditar dados disponíveis até a data de referência.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene a criação de uma política de retenção baseada em **Baselines e modelos**.

- A) Medir retenção incremental e ajustar a política.
- B) Escolher limiares com base em custo e benefício.
- C) Definir segmentos e ações possíveis para cada perfil.
- D) Executar a ação em um grupo controlado.
- E) Estimar valor, risco, custo de contato e capacidade operacional.

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

- **Conhecimento praticado hoje:** Baselines e modelos.
- **Competência sugerida:** Baselines e modelos de Machine Learning.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Baselines e modelos de Machine Learning** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

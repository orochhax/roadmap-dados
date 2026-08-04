<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 70 — Preparação para modelagem — 06/11/2026
> [!abstract] Resultado concreto do dia
> Concluir **Preparação para modelagem** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Preparação para modelagem.
- **Pasta/arquivo principal:** `01-exercicios/roteiro_atividades.md`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Passo a passo completo
1. [ ] Defina corte temporal e conjuntos de treino, validação e teste.
2. [ ] Construa pipeline de imputação, codificação e escala sem usar dados futuros.
3. [ ] Crie baseline de negócio e DummyClassifier.
4. [ ] Defina métricas técnicas e custo de decisão.
5. [ ] Salve um `data_card.md` com origem, período, população, exclusões e limitações.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/roteiro_atividades.md`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Compare o baseline de negócio chamados_90d>=3 com o DummyClassifier usando a métrica e o custo definidos.
- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Altere o corte temporal em 30 dias e confira se nenhuma data posterior entrou no conjunto de treino.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Defina corte temporal e conjuntos de treino, validação e teste.

   **Pergunta:** Ao desenvolver **Preparação para modelagem**, qual definição evita um alvo ambíguo ou vazamento de dados?

- [ ] A) Fixar a população, a data de referência, a janela de observação e a regra objetiva de churn.
- [ ] B) Chamar de churn qualquer cliente com poucos registros.
- [ ] C) Usar informações posteriores ao cancelamento para prever o próprio cancelamento.
- [ ] D) Alterar a definição do alvo para melhorar a métrica do modelo.
- [ ] E) Remover clientes ativos sem registrar o critério usado.

2. **Referência — atividade 2:** Construa pipeline de imputação, codificação e escala sem usar dados futuros.

   **Pergunta:** Como avaliar um modelo ligado a **Preparação para modelagem** para uma estratégia de retenção?

- [ ] A) Priorizando somente a acurácia geral.
- [ ] B) Contatando todos os clientes classificados pelo modelo.
- [ ] C) Ignorando a capacidade operacional da equipe de retenção.
- [ ] D) Relacionando métricas e limiar ao custo do contato, ao valor do cliente e ao benefício provável da retenção.
- [ ] E) Escolhendo sempre o limiar de 50%.

3. **Referência — atividade 3:** Crie baseline de negócio e DummyClassifier.

   **Pergunta:** Qual análise ajuda a encontrar riscos escondidos em **Preparação para modelagem**?

- [ ] A) Conferir somente o desempenho no conjunto de treino.
- [ ] B) Comparar qualidade dos dados, erros e desempenho entre períodos e segmentos de clientes.
- [ ] C) Avaliar apenas os clientes com maior probabilidade.
- [ ] D) Excluir segmentos pequenos antes de medir os erros.
- [ ] E) Usar a mesma explicação para todos os perfis.

4. **Referência — atividade 4:** Defina métricas técnicas e custo de decisão.

   **Pergunta:** Qual é a melhor ligação entre um modelo de **Preparação para modelagem** e uma ação de negócio?

- [ ] A) Enviar a probabilidade bruta sem orientar seu uso.
- [ ] B) Considerar todo cliente de alto risco automaticamente perdido.
- [ ] C) Escolher a ação apenas pela variável mais importante do modelo.
- [ ] D) Medir sucesso somente pelo número de contatos realizados.
- [ ] E) Criar uma política explícita que defina quem será priorizado, qual ação receberá e como o impacto será medido.

5. **Referência — atividade 5:** Salve um `data_card.md` com origem, período, população, exclusões e limitações.

   **Pergunta:** Ordene a construção de um projeto relacionado a **Preparação para modelagem**.

- A) Definir população, churn, datas e objetivo de negócio.
- B) Realizar EDA e preparar uma separação sem vazamento.
- C) Transformar previsões em estratégia e comunicar limitações.
- D) Treinar baselines e modelos com métricas adequadas.
- E) Construir e auditar dados disponíveis até a data de referência.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene a criação de uma política de retenção baseada em **Preparação para modelagem**.

- A) Estimar valor, risco, custo de contato e capacidade operacional.
- B) Medir retenção incremental e ajustar a política.
- C) Escolher limiares com base em custo e benefício.
- D) Executar a ação em um grupo controlado.
- E) Definir segmentos e ações possíveis para cada perfil.

**Ordem:** `__ → __ → __ → __ → __`

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Alterações registradas em commit e enviadas ao GitHub.

**Autoavaliação do dia:** `__/5`  

> [!project] Projeto semanal — Pipeline auditável do projeto de churn
> **Desafio:** Preparar a base do projeto principal com rastreabilidade, validações e documentação de todas as transformações.
>
> **Deve reutilizar:** Dados, SQL, estatística, ML e engenharia de atributos.
>
> **Entregáveis obrigatórios:**
> - [ ] dicionário de dados;
> - [ ] testes de qualidade;
> - [ ] pipeline reproduzível;
> - [ ] relatório de riscos;
> - [ ] backlog de modelagem;
>
> **Defesa:** demonstração de cinco minutos e resposta a três perguntas técnicas.
>
> **Nota mínima recomendada:** `6/10`.

> [!check] Critério para avançar
> O problema está definido de forma que uma empresa saberia como agir após receber a previsão?

---

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Preparação para modelagem.
- **Competência sugerida:** Preparação de dados para Machine Learning.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Preparação de dados para Machine Learning** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

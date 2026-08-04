<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 74 — Relatório e dashboard — 12/11/2026
> [!abstract] Resultado concreto do dia
> Concluir **Relatório e dashboard** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Relatório e dashboard.
- **Pasta/arquivo principal:** `01-exercicios/dia-074-relatorio-e-dashboard.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Passo a passo completo
1. [ ] Crie dashboard com visão geral, segmentos de risco, drivers e simulação de política.
2. [ ] Valide números contra SQL/notebook.
3. [ ] Escreva relatório técnico e resumo executivo.
4. [ ] Adicione seção de limitações e plano de monitoramento.
5. [ ] Teste dashboard com uma pessoa e corrija pelo menos três ambiguidades.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/dia-074-relatorio-e-dashboard.ipynb`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/dia-074-relatorio-e-dashboard.ipynb`:** Adicione ao dashboard um filtro de plano e valide o total exibido para Básico 100 contra o notebook.
- [ ] **Em `01-exercicios/dia-074-relatorio-e-dashboard.ipynb`:** Peça a uma pessoa para localizar o volume de alto risco em até 30 segundos e registre uma ambiguidade concreta encontrada.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Crie dashboard com visão geral, segmentos de risco, drivers e simulação de política.

   **Pergunta:** Ao desenvolver **Relatório e dashboard**, qual definição evita um alvo ambíguo ou vazamento de dados?

- [ ] A) Remover clientes ativos sem registrar o critério usado.
- [ ] B) Fixar a população, a data de referência, a janela de observação e a regra objetiva de churn.
- [ ] C) Chamar de churn qualquer cliente com poucos registros.
- [ ] D) Usar informações posteriores ao cancelamento para prever o próprio cancelamento.
- [ ] E) Alterar a definição do alvo para melhorar a métrica do modelo.

2. **Referência — atividade 2:** Valide números contra SQL/notebook.

   **Pergunta:** Como avaliar um modelo ligado a **Relatório e dashboard** para uma estratégia de retenção?

- [ ] A) Escolhendo sempre o limiar de 50%.
- [ ] B) Priorizando somente a acurácia geral.
- [ ] C) Contatando todos os clientes classificados pelo modelo.
- [ ] D) Ignorando a capacidade operacional da equipe de retenção.
- [ ] E) Relacionando métricas e limiar ao custo do contato, ao valor do cliente e ao benefício provável da retenção.

3. **Referência — atividade 3:** Escreva relatório técnico e resumo executivo.

   **Pergunta:** Qual análise ajuda a encontrar riscos escondidos em **Relatório e dashboard**?

- [ ] A) Usar a mesma explicação para todos os perfis.
- [ ] B) Conferir somente o desempenho no conjunto de treino.
- [ ] C) Comparar qualidade dos dados, erros e desempenho entre períodos e segmentos de clientes.
- [ ] D) Avaliar apenas os clientes com maior probabilidade.
- [ ] E) Excluir segmentos pequenos antes de medir os erros.

4. **Referência — atividade 4:** Adicione seção de limitações e plano de monitoramento.

   **Pergunta:** Qual é a melhor ligação entre um modelo de **Relatório e dashboard** e uma ação de negócio?

- [ ] A) Criar uma política explícita que defina quem será priorizado, qual ação receberá e como o impacto será medido.
- [ ] B) Enviar a probabilidade bruta sem orientar seu uso.
- [ ] C) Considerar todo cliente de alto risco automaticamente perdido.
- [ ] D) Escolher a ação apenas pela variável mais importante do modelo.
- [ ] E) Medir sucesso somente pelo número de contatos realizados.

5. **Referência — atividade 5:** Teste dashboard com uma pessoa e corrija pelo menos três ambiguidades.

   **Pergunta:** Ordene a construção de um projeto relacionado a **Relatório e dashboard**.

- A) Realizar EDA e preparar uma separação sem vazamento.
- B) Construir e auditar dados disponíveis até a data de referência.
- C) Transformar previsões em estratégia e comunicar limitações.
- D) Treinar baselines e modelos com métricas adequadas.
- E) Definir população, churn, datas e objetivo de negócio.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene a criação de uma política de retenção baseada em **Relatório e dashboard**.

- A) Escolher limiares com base em custo e benefício.
- B) Definir segmentos e ações possíveis para cada perfil.
- C) Medir retenção incremental e ajustar a política.
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

- **Conhecimento praticado hoje:** Relatório e dashboard.
- **Competência sugerida:** Dashboards e comunicação de dados.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Dashboards e comunicação de dados** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

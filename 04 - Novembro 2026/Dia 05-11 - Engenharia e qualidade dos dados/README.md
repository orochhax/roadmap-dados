<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 67 — Engenharia e qualidade dos dados — 03/11/2026
> [!abstract] Resultado concreto do dia
> Concluir **Engenharia e qualidade dos dados** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Engenharia e qualidade dos dados.
- **Pasta/arquivo principal:** `semana-14/dia-067-engenharia-e-qualidade-dos-dados.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Passo a passo completo
1. [ ] Carregue `clientes_telecom.csv`, valide esquema e gere relatório de qualidade por coluna.
2. [ ] Defina regras de negócio para ausentes, duplicados, NPS fora de 0–10, mensalidade negativa e datas inconsistentes.
3. [ ] Implemente função de validação que falhe com mensagens claras.
4. [ ] Crie base analítica limpa e dicionário de dados.
5. [ ] Registre quantidade de linhas alteradas ou removidas e impacto na taxa de churn.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Crie um recorte adicional por segmento de cliente e compare métricas, erros ou recomendações de **Engenharia e qualidade dos dados**.
- [ ] Faça uma análise de sensibilidade alterando uma regra, custo ou limiar e registre se a ação recomendada muda.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Carregue `clientes_telecom.csv`, valide esquema e gere relatório de qualidade por coluna.

   **Pergunta:** Ao desenvolver **Engenharia e qualidade dos dados**, qual definição evita um alvo ambíguo ou vazamento de dados?

- [ ] A) Usar informações posteriores ao cancelamento para prever o próprio cancelamento.
- [ ] B) Alterar a definição do alvo para melhorar a métrica do modelo.
- [ ] C) Remover clientes ativos sem registrar o critério usado.
- [ ] D) Fixar a população, a data de referência, a janela de observação e a regra objetiva de churn.
- [ ] E) Chamar de churn qualquer cliente com poucos registros.

2. **Referência — atividade 2:** Defina regras de negócio para ausentes, duplicados, NPS fora de 0–10, mensalidade negativa e datas inconsistentes.

   **Pergunta:** Como avaliar um modelo ligado a **Engenharia e qualidade dos dados** para uma estratégia de retenção?

- [ ] A) Ignorando a capacidade operacional da equipe de retenção.
- [ ] B) Relacionando métricas e limiar ao custo do contato, ao valor do cliente e ao benefício provável da retenção.
- [ ] C) Escolhendo sempre o limiar de 50%.
- [ ] D) Priorizando somente a acurácia geral.
- [ ] E) Contatando todos os clientes classificados pelo modelo.

3. **Referência — atividade 3:** Implemente função de validação que falhe com mensagens claras.

   **Pergunta:** Qual análise ajuda a encontrar riscos escondidos em **Engenharia e qualidade dos dados**?

- [ ] A) Avaliar apenas os clientes com maior probabilidade.
- [ ] B) Excluir segmentos pequenos antes de medir os erros.
- [ ] C) Usar a mesma explicação para todos os perfis.
- [ ] D) Conferir somente o desempenho no conjunto de treino.
- [ ] E) Comparar qualidade dos dados, erros e desempenho entre períodos e segmentos de clientes.

4. **Referência — atividade 4:** Crie base analítica limpa e dicionário de dados.

   **Pergunta:** Qual é a melhor ligação entre um modelo de **Engenharia e qualidade dos dados** e uma ação de negócio?

- [ ] A) Escolher a ação apenas pela variável mais importante do modelo.
- [ ] B) Medir sucesso somente pelo número de contatos realizados.
- [ ] C) Criar uma política explícita que defina quem será priorizado, qual ação receberá e como o impacto será medido.
- [ ] D) Enviar a probabilidade bruta sem orientar seu uso.
- [ ] E) Considerar todo cliente de alto risco automaticamente perdido.

5. **Referência — atividade 5:** Registre quantidade de linhas alteradas ou removidas e impacto na taxa de churn.

   **Pergunta:** Ordene a construção de um projeto relacionado a **Engenharia e qualidade dos dados**.

- A) Definir população, churn, datas e objetivo de negócio.
- B) Construir e auditar dados disponíveis até a data de referência.
- C) Transformar previsões em estratégia e comunicar limitações.
- D) Treinar baselines e modelos com métricas adequadas.
- E) Realizar EDA e preparar uma separação sem vazamento.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene a criação de uma política de retenção baseada em **Engenharia e qualidade dos dados**.

- A) Estimar valor, risco, custo de contato e capacidade operacional.
- B) Escolher limiares com base em custo e benefício.
- C) Definir segmentos e ações possíveis para cada perfil.
- D) Executar a ação em um grupo controlado.
- E) Medir retenção incremental e ajustar a política.

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

- **Conhecimento praticado hoje:** Engenharia e qualidade dos dados.
- **Competência sugerida:** Qualidade e engenharia de dados.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Qualidade e engenharia de dados** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 69 — SQL do projeto — 05/11/2026
> [!abstract] Resultado concreto do dia
> Concluir **SQL do projeto** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** SQL do projeto.
- **Pasta/arquivo principal:** `semana-14/dia-069-sql-do-projeto.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Passo a passo completo
1. [ ] Crie esquema SQL com tabelas de clientes, planos, chamados e pagamentos.
2. [ ] Escreva consultas para formar features agregadas em janelas de 30, 60 e 90 dias.
3. [ ] Valide granularidade: uma linha por cliente na data de referência.
4. [ ] Crie testes de unicidade, ausência de chaves e totais antes/depois dos joins.
5. [ ] Exporte `base_modelagem.csv` e compare cinco linhas com cálculo manual.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Crie um recorte adicional por segmento de cliente e compare métricas, erros ou recomendações de **SQL do projeto**.
- [ ] Faça uma análise de sensibilidade alterando uma regra, custo ou limiar e registre se a ação recomendada muda.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. Ao desenvolver **SQL do projeto**, qual definição evita um alvo ambíguo ou vazamento de dados?

- [ ] A) Remover clientes ativos sem registrar o critério usado.
- [ ] B) Fixar a população, a data de referência, a janela de observação e a regra objetiva de churn.
- [ ] C) Chamar de churn qualquer cliente com poucos registros.
- [ ] D) Usar informações posteriores ao cancelamento para prever o próprio cancelamento.
- [ ] E) Alterar a definição do alvo para melhorar a métrica do modelo.

2. Como avaliar um modelo ligado a **SQL do projeto** para uma estratégia de retenção?

- [ ] A) Escolhendo sempre o limiar de 50%.
- [ ] B) Priorizando somente a acurácia geral.
- [ ] C) Contatando todos os clientes classificados pelo modelo.
- [ ] D) Ignorando a capacidade operacional da equipe de retenção.
- [ ] E) Relacionando métricas e limiar ao custo do contato, ao valor do cliente e ao benefício provável da retenção.

3. Qual análise ajuda a encontrar riscos escondidos em **SQL do projeto**?

- [ ] A) Usar a mesma explicação para todos os perfis.
- [ ] B) Conferir somente o desempenho no conjunto de treino.
- [ ] C) Comparar qualidade dos dados, erros e desempenho entre períodos e segmentos de clientes.
- [ ] D) Avaliar apenas os clientes com maior probabilidade.
- [ ] E) Excluir segmentos pequenos antes de medir os erros.

4. Qual é a melhor ligação entre um modelo de **SQL do projeto** e uma ação de negócio?

- [ ] A) Criar uma política explícita que defina quem será priorizado, qual ação receberá e como o impacto será medido.
- [ ] B) Enviar a probabilidade bruta sem orientar seu uso.
- [ ] C) Considerar todo cliente de alto risco automaticamente perdido.
- [ ] D) Escolher a ação apenas pela variável mais importante do modelo.
- [ ] E) Medir sucesso somente pelo número de contatos realizados.

5. Ordene a construção de um projeto relacionado a **SQL do projeto**.

- A) Definir população, churn, datas e objetivo de negócio.
- B) Transformar previsões em estratégia e comunicar limitações.
- C) Realizar EDA e preparar uma separação sem vazamento.
- D) Treinar baselines e modelos com métricas adequadas.
- E) Construir e auditar dados disponíveis até a data de referência.

**Ordem:** `__ → __ → __ → __ → __`

6. Ordene a criação de uma política de retenção baseada em **SQL do projeto**.

- A) Escolher limiares com base em custo e benefício.
- B) Medir retenção incremental e ajustar a política.
- C) Estimar valor, risco, custo de contato e capacidade operacional.
- D) Executar a ação em um grupo controlado.
- E) Definir segmentos e ações possíveis para cada perfil.

**Ordem:** `__ → __ → __ → __ → __`

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Alterações registradas em commit e enviadas ao GitHub.

**Autoavaliação do dia:** `__/5`  
**Evidência:** link do commit, notebook, consulta, imagem ou gravação.

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** SQL do projeto.
- **Competência sugerida:** SQL aplicado a projetos.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **SQL aplicado a projetos** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

---

## Anotações pessoais



### Conceitos estudados


### Dúvidas


### Erros encontrados e correções


### Aprendizado principal


### Próxima ação

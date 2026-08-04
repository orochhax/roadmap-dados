<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 69 — SQL do projeto — 05/11/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** SQL do projeto.
- **Competência sugerida:** SQL aplicado a projetos.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **SQL aplicado a projetos** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

> [!abstract] Resultado concreto do dia
> Concluir **SQL do projeto** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** SQL do projeto.
- **Pasta/arquivo principal:** `01-exercicios/dia-069-sql-do-projeto.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Crie esquema SQL com tabelas de clientes, planos, chamados e pagamentos.
2. [ ] Escreva consultas para formar features agregadas em janelas de 30, 60 e 90 dias.
3. [ ] Valide granularidade: uma linha por cliente na data de referência.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Crie testes de unicidade, ausência de chaves e totais antes/depois dos joins.
- [ ] Exporte `base_modelagem.csv` e compare cinco linhas com cálculo manual.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-069-sql-do-projeto.ipynb`:** Crie a feature quantidade_chamados_60d e compare cinco clientes com uma contagem manual na tabela de chamados.
- [ ] **Em `01-exercicios/dia-069-sql-do-projeto.ipynb`:** Duplique um pagamento, execute o teste de unicidade e impeça a exportação da base enquanto o problema existir.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Como avaliar um modelo ligado a **SQL do projeto** para uma estratégia de retenção?

- [ ] A) Escolhendo sempre o limiar de 50%.
- [ ] B) Priorizando somente a acurácia geral.
- [ ] C) Contatando todos os clientes classificados pelo modelo.
- [ ] D) Ignorando a capacidade operacional da equipe de retenção.
- [ ] E) Relacionando métricas e limiar ao custo do contato, ao valor do cliente e ao benefício provável da retenção.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Qual análise ajuda a encontrar riscos escondidos em **SQL do projeto**?

- [ ] A) Usar a mesma explicação para todos os perfis.
- [ ] B) Conferir somente o desempenho no conjunto de treino.
- [ ] C) Comparar qualidade dos dados, erros e desempenho entre períodos e segmentos de clientes.
- [ ] D) Avaliar apenas os clientes com maior probabilidade.
- [ ] E) Excluir segmentos pequenos antes de medir os erros.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene a construção de um projeto relacionado a **SQL do projeto**.

- A) Definir população, churn, datas e objetivo de negócio.
- B) Transformar previsões em estratégia e comunicar limitações.
- C) Realizar EDA e preparar uma separação sem vazamento.
- D) Treinar baselines e modelos com métricas adequadas.
- E) Construir e auditar dados disponíveis até a data de referência.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`

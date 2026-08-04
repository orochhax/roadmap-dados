<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 67 — Engenharia e qualidade dos dados — 03/11/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Engenharia e qualidade dos dados.
- **Competência sugerida:** Qualidade e engenharia de dados.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Qualidade e engenharia de dados** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

> [!abstract] Resultado concreto do dia
> Concluir **Engenharia e qualidade dos dados** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Engenharia e qualidade dos dados.
- **Pasta/arquivo principal:** `01-exercicios/dia-067-engenharia-e-qualidade-dos-dados.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Carregue `clientes_telecom.csv`, valide esquema e gere relatório de qualidade por coluna.
2. [ ] Defina regras de negócio para ausentes, duplicados, NPS fora de 0–10, mensalidade negativa e datas inconsistentes.
3. [ ] Implemente função de validação que falhe com mensagens claras.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Crie base analítica limpa e dicionário de dados.
- [ ] Registre quantidade de linhas alteradas ou removidas e impacto na taxa de churn.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-067-engenharia-e-qualidade-dos-dados.ipynb`:** Crie uma linha com NPS=11 e outra com mensalidade=-1 e faça a validação listar os dois erros separadamente.
- [ ] **Em `01-exercicios/dia-067-engenharia-e-qualidade-dos-dados.ipynb`:** Compare a taxa de churn antes e depois de remover somente registros realmente inválidos e registre quantas linhas mudaram.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Como avaliar um modelo ligado a **Engenharia e qualidade dos dados** para uma estratégia de retenção?

- [ ] A) Ignorando a capacidade operacional da equipe de retenção.
- [ ] B) Relacionando métricas e limiar ao custo do contato, ao valor do cliente e ao benefício provável da retenção.
- [ ] C) Escolhendo sempre o limiar de 50%.
- [ ] D) Priorizando somente a acurácia geral.
- [ ] E) Contatando todos os clientes classificados pelo modelo.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Qual análise ajuda a encontrar riscos escondidos em **Engenharia e qualidade dos dados**?

- [ ] A) Avaliar apenas os clientes com maior probabilidade.
- [ ] B) Excluir segmentos pequenos antes de medir os erros.
- [ ] C) Usar a mesma explicação para todos os perfis.
- [ ] D) Conferir somente o desempenho no conjunto de treino.
- [ ] E) Comparar qualidade dos dados, erros e desempenho entre períodos e segmentos de clientes.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene a construção de um projeto relacionado a **Engenharia e qualidade dos dados**.

- A) Definir população, churn, datas e objetivo de negócio.
- B) Construir e auditar dados disponíveis até a data de referência.
- C) Transformar previsões em estratégia e comunicar limitações.
- D) Treinar baselines e modelos com métricas adequadas.
- E) Realizar EDA e preparar uma separação sem vazamento.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`

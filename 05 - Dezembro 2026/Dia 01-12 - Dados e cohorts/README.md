<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 82 — Dados e cohorts — 24/11/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Dados e cohorts.
- **Competência sugerida:** Cohorts e análise de risco.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Cohorts e análise de risco** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

> [!abstract] Resultado concreto do dia
> Concluir **Dados e cohorts** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Dados e cohorts.
- **Pasta/arquivo principal:** `01-exercicios/dia-082-dados-e-cohorts.ipynb`.
- **Dados:** `dados/credito.csv`.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Carregue `credito.csv`, faça qualidade e EDA da taxa de default.
2. [ ] Crie cohorts por mês de concessão e acompanhe default P1/P2/P3 quando possível.
3. [ ] Analise default por faixas de renda, dívida, atrasos e tempo de emprego.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Valide estabilidade temporal das variáveis.
- [ ] Crie dicionário de features e regras de exclusão.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-082-dados-e-cohorts.ipynb`:** Compare default para renda abaixo de R$3.000 e acima de R$8.000, informando também o tamanho dos grupos.
- [ ] **Em `01-exercicios/dia-082-dados-e-cohorts.ipynb`:** Separe os últimos três meses de concessão e compare a distribuição das cinco principais variáveis com o período anterior.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Por que a calibração importa em uma aplicação de **Dados e cohorts**?

- [ ] A) Porque substitui a validação temporal.
- [ ] B) Porque a probabilidade estimada precisa representar uma frequência útil para políticas baseadas em custo e risco.
- [ ] C) Porque transforma qualquer modelo no mais preciso.
- [ ] D) Porque elimina diferenças entre grupos.
- [ ] E) Porque permite ignorar a taxa-base do evento.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Qual cuidado de governança é necessário em **Dados e cohorts**?

- [ ] A) Ocultar as variáveis para impedir questionamentos.
- [ ] B) Avaliar somente o grupo mais numeroso.
- [ ] C) Usar atributos sensíveis sem analisar consequências.
- [ ] D) Manter a política fixa mesmo quando os dados mudarem.
- [ ] E) Documentar dados, critérios, limitações e desempenho por segmento, com revisão de possíveis impactos injustos.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene o desenvolvimento de um modelo para **Dados e cohorts**.

- A) Separar períodos e treinar um baseline.
- B) Construir dados disponíveis até a data de decisão.
- C) Definir evento, horizonte, população e restrições.
- D) Avaliar discriminação, calibração e desempenho por segmento.
- E) Documentar limites e propor uma política de uso.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`

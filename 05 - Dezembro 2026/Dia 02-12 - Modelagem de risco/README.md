<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 83 — Modelagem de risco — 25/11/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Modelagem de risco.
- **Competência sugerida:** Modelagem de risco.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Modelagem de risco** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning`.
- **Próximo marco do perfil:** Dia 115 — Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa.

> [!abstract] Resultado concreto do dia
> Concluir **Modelagem de risco** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Modelagem de risco.
- **Pasta/arquivo principal:** `01-exercicios/dia-083-modelagem-de-risco.ipynb`.
- **Dados:** `dados/credito.csv`.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Treine regressão logística como scorecard básico e modelos de árvore.
2. [ ] Avalie ROC-AUC, PR-AUC, KS, calibração e matriz de confusão.
3. [ ] Faça validação temporal, não apenas aleatória.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Analise estabilidade e desempenho por segmentos.
- [ ] Escolha modelo explicável compatível com política de crédito.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-083-modelagem-de-risco.ipynb`:** Compare calibração e KS no conjunto temporal final para logística e o melhor modelo de árvore.
- [ ] **Em `01-exercicios/dia-083-modelagem-de-risco.ipynb`:** Calcule as métricas separadamente para contratos com prazo até 12 meses e acima de 24 meses.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Por que a calibração importa em uma aplicação de **Modelagem de risco**?

- [ ] A) Porque a probabilidade estimada precisa representar uma frequência útil para políticas baseadas em custo e risco.
- [ ] B) Porque transforma qualquer modelo no mais preciso.
- [ ] C) Porque elimina diferenças entre grupos.
- [ ] D) Porque permite ignorar a taxa-base do evento.
- [ ] E) Porque substitui a validação temporal.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Qual cuidado de governança é necessário em **Modelagem de risco**?

- [ ] A) Avaliar somente o grupo mais numeroso.
- [ ] B) Usar atributos sensíveis sem analisar consequências.
- [ ] C) Manter a política fixa mesmo quando os dados mudarem.
- [ ] D) Documentar dados, critérios, limitações e desempenho por segmento, com revisão de possíveis impactos injustos.
- [ ] E) Ocultar as variáveis para impedir questionamentos.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene o desenvolvimento de um modelo para **Modelagem de risco**.

- A) Definir evento, horizonte, população e restrições.
- B) Construir dados disponíveis até a data de decisão.
- C) Separar períodos e treinar um baseline.
- D) Documentar limites e propor uma política de uso.
- E) Avaliar discriminação, calibração e desempenho por segmento.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`

<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 59 — Seleção de modelo — 22/10/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Seleção de modelo.
- **Competência sugerida:** Seleção de modelos.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Seleção de modelos** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

> [!abstract] Resultado concreto do dia
> Concluir **Seleção de modelo** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Seleção de modelo.
- **Pasta/arquivo principal:** `01-exercicios/dia-059-selecao-de-modelo.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Crie tabela única com todos os modelos já treinados, mesma validação e métricas.
2. [ ] Defina critérios de escolha antes de olhar o vencedor: custo, recall, calibração, tempo, explicabilidade.
3. [ ] Use teste ou bootstrap para verificar estabilidade da diferença entre os dois melhores.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Escolha modelo campeão e um challenger.
- [ ] Escreva decisão com trade-offs, não apenas ranking.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-059-selecao-de-modelo.ipynb`:** Refaça o ranking dando peso dobrado ao custo e depois peso dobrado à explicabilidade; registre se campeão e challenger mudam.
- [ ] **Em `01-exercicios/dia-059-selecao-de-modelo.ipynb`:** Use bootstrap com seed 42 para comparar os dois melhores em 200 reamostragens do conjunto de validação.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Como escolher uma métrica adequada para avaliar **Seleção de modelo**?

- [ ] A) Usando sempre acurácia, pois ela serve para qualquer problema.
- [ ] B) Escolhendo a métrica que produz o maior número.
- [ ] C) Trocando de métrica depois de ver qual favorece o modelo.
- [ ] D) Avaliando apenas o tempo de treinamento do algoritmo.
- [ ] E) Considerando o tipo de problema, o desbalanceamento e o custo dos diferentes erros para o negócio.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Qual procedimento fornece uma comparação mais confiável entre modelos em **Seleção de modelo**?

- [ ] A) Consultar repetidamente o teste durante cada ajuste.
- [ ] B) Comparar somente a quantidade de parâmetros dos algoritmos.
- [ ] C) Usar o mesmo protocolo de validação, ajustar decisões no treino e reservar o teste para a avaliação final.
- [ ] D) Testar cada modelo em uma divisão diferente dos dados.
- [ ] E) Escolher pelo desempenho no conjunto usado para treinar.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene um fluxo de modelagem para **Seleção de modelo**.

- A) Definir o problema, a população, o alvo e a métrica.
- B) Ajustar o pré-processamento apenas com os dados de treino.
- C) Avaliar, analisar erros e relacionar o modelo à decisão.
- D) Treinar um baseline e modelos candidatos.
- E) Separar os dados conforme o contexto do problema.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`

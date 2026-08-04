<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 43 — Pré-processamento com Pipeline — 30/09/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Pré-processamento com Pipeline.
- **Competência sugerida:** Pipelines e pré-processamento com scikit-learn.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Pipelines e pré-processamento com scikit-learn** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

> [!abstract] Resultado concreto do dia
> Concluir **Pré-processamento com Pipeline** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Pré-processamento com Pipeline.
- **Pasta/arquivo principal:** `01-exercicios/dia-043-pre-processamento-com-pipeline.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Identifique colunas numéricas e categóricas e faça um primeiro `fit/predict` guiado com `DummyClassifier`.
2. [ ] Construa um `ColumnTransformer` mínimo com imputação e one-hot encoding e conecte-o a uma regressão logística usada apenas como baseline.
3. [ ] Confirme no código que `fit` recebe somente o conjunto de treino e compare a saída do baseline com o Dummy.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Adicione padronização somente para as colunas numéricas que precisam dela.
- [ ] Teste categoria inédita com `handle_unknown='ignore'` depois que a pipeline básica executar.
- [ ] Salvar e recarregar a pipeline é desafio de engenharia e será aprofundado no Dia 97.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-043-pre-processamento-com-pipeline.ipynb`:** Passe à pipeline uma linha com plano='Plano Experimental' e confirme que handle_unknown='ignore' evita falha.
- [ ] **Em `01-exercicios/dia-043-pre-processamento-com-pipeline.ipynb`:** Passe outra linha com mensalidade ausente e registre a transformação aplicada sem ajustar novamente a pipeline.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Como escolher uma métrica adequada para avaliar **Pré-processamento com Pipeline**?

- [ ] A) Considerando o tipo de problema, o desbalanceamento e o custo dos diferentes erros para o negócio.
- [ ] B) Usando sempre acurácia, pois ela serve para qualquer problema.
- [ ] C) Escolhendo a métrica que produz o maior número.
- [ ] D) Trocando de métrica depois de ver qual favorece o modelo.
- [ ] E) Avaliando apenas o tempo de treinamento do algoritmo.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Qual procedimento fornece uma comparação mais confiável entre modelos em **Pré-processamento com Pipeline**?

- [ ] A) Escolher pelo desempenho no conjunto usado para treinar.
- [ ] B) Consultar repetidamente o teste durante cada ajuste.
- [ ] C) Comparar somente a quantidade de parâmetros dos algoritmos.
- [ ] D) Usar o mesmo protocolo de validação, ajustar decisões no treino e reservar o teste para a avaliação final.
- [ ] E) Testar cada modelo em uma divisão diferente dos dados.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene um fluxo de modelagem para **Pré-processamento com Pipeline**.

- A) Avaliar, analisar erros e relacionar o modelo à decisão.
- B) Separar os dados conforme o contexto do problema.
- C) Definir o problema, a população, o alvo e a métrica.
- D) Treinar um baseline e modelos candidatos.
- E) Ajustar o pré-processamento apenas com os dados de treino.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`

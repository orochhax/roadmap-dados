<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 56 — Árvore de decisão — 19/10/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Árvore de decisão.
- **Competência sugerida:** Árvore de decisão.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Árvore de decisão** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

> [!abstract] Resultado concreto do dia
> Concluir **Árvore de decisão** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Árvore de decisão.
- **Pasta/arquivo principal:** `01-exercicios/dia-056-arvore-de-decisao.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Treine árvore de decisão com profundidades 1, 3, 5, 10 e sem limite.
2. [ ] Visualize uma árvore pequena e traduza cinco divisões em regras de negócio.
3. [ ] Compare desempenho de treino e validação para identificar overfitting.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Varie `min_samples_leaf` e registre estabilidade.
- [ ] Crie uma árvore deliberadamente complexa e explique por que não deve ser usada apesar da métrica de treino.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-056-arvore-de-decisao.ipynb`:** Compare profundidade 3 e 10 com min_samples_leaf=20 no mesmo split e registre treino e validação.
- [ ] **Em `01-exercicios/dia-056-arvore-de-decisao.ipynb`:** Escolha uma previsão errada da árvore profunda e escreva as regras percorridas até a folha.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Como escolher uma métrica adequada para avaliar **Árvore de decisão**?

- [ ] A) Trocando de métrica depois de ver qual favorece o modelo.
- [ ] B) Avaliando apenas o tempo de treinamento do algoritmo.
- [ ] C) Considerando o tipo de problema, o desbalanceamento e o custo dos diferentes erros para o negócio.
- [ ] D) Usando sempre acurácia, pois ela serve para qualquer problema.
- [ ] E) Escolhendo a métrica que produz o maior número.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Qual procedimento fornece uma comparação mais confiável entre modelos em **Árvore de decisão**?

- [ ] A) Usar o mesmo protocolo de validação, ajustar decisões no treino e reservar o teste para a avaliação final.
- [ ] B) Testar cada modelo em uma divisão diferente dos dados.
- [ ] C) Escolher pelo desempenho no conjunto usado para treinar.
- [ ] D) Consultar repetidamente o teste durante cada ajuste.
- [ ] E) Comparar somente a quantidade de parâmetros dos algoritmos.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene um fluxo de modelagem para **Árvore de decisão**.

- A) Definir o problema, a população, o alvo e a métrica.
- B) Avaliar, analisar erros e relacionar o modelo à decisão.
- C) Ajustar o pré-processamento apenas com os dados de treino.
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

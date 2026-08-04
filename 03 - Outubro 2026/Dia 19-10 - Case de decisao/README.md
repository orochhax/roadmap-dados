<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 55 — Case de decisão — 16/10/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Case de decisão.
- **Competência sugerida:** Machine Learning para tomada de decisão.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Machine Learning para tomada de decisão** na seção Competências. Se a entrega estiver revisada e representar bem seu trabalho, considere incluí-la em Projetos ou Destaques.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

> [!abstract] Resultado concreto do dia
> Concluir **Case de decisão** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 4–5 horas; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Case de decisão.
- **Pasta/arquivo principal:** `01-exercicios/roteiro_atividades.md`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Monte tabela com cliente, probabilidade, limiar, decisão e custo esperado.
2. [ ] Crie três políticas: conservadora, equilibrada e agressiva; calcule volume de ações e custo.
3. [ ] Analise desempenho por cidade, plano e faixa de mensalidade.
4. [ ] Defina regra de revisão humana para casos próximos ao limiar.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Apresente decisão em uma página, incluindo quem não deve receber ação automatizada.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Defina política conservadora com limiar 0,70, equilibrada com 0,50 e agressiva com 0,30; calcule volume e custo no mesmo conjunto.
- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Crie revisão humana para probabilidades entre 0,45 e 0,55 e conte quantos clientes entram nessa faixa.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Como escolher uma métrica adequada para avaliar **Case de decisão**?

- [ ] A) Escolhendo a métrica que produz o maior número.
- [ ] B) Trocando de métrica depois de ver qual favorece o modelo.
- [ ] C) Avaliando apenas o tempo de treinamento do algoritmo.
- [ ] D) Considerando o tipo de problema, o desbalanceamento e o custo dos diferentes erros para o negócio.
- [ ] E) Usando sempre acurácia, pois ela serve para qualquer problema.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Qual procedimento fornece uma comparação mais confiável entre modelos em **Case de decisão**?

- [ ] A) Comparar somente a quantidade de parâmetros dos algoritmos.
- [ ] B) Usar o mesmo protocolo de validação, ajustar decisões no treino e reservar o teste para a avaliação final.
- [ ] C) Testar cada modelo em uma divisão diferente dos dados.
- [ ] D) Escolher pelo desempenho no conjunto usado para treinar.
- [ ] E) Consultar repetidamente o teste durante cada ajuste.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene um fluxo de modelagem para **Case de decisão**.

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


> [!todo] PUBLICAR NO LINKEDIN — projeto prioritário do portfólio
> - [ ] Publique somente após README, resultados e limitações estarem revisados.
> - [ ] Inclua problema, abordagem, principal evidência, decisão e link do GitHub.
> - [ ] **Ângulo sugerido:** mostrar por que o limiar 0,5 não é automático e como custos dos erros mudam a política.


---

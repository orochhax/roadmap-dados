<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 57 — Random Forest — 20/10/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Random Forest.
- **Competência sugerida:** Random Forest.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Random Forest** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

> [!abstract] Resultado concreto do dia
> Concluir **Random Forest** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Random Forest.
- **Pasta/arquivo principal:** `01-exercicios/dia-057-random-forest.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Treine Random Forest variando número de árvores, profundidade e número de features.
2. [ ] Compare variância de uma árvore única com a floresta em cinco seeds.
3. [ ] Calcule importância por impureza e permutation importance; compare rankings.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Meça tempo e tamanho do modelo.
- [ ] Escolha configuração considerando desempenho, estabilidade e custo de inferência.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-057-random-forest.ipynb`:** Compare 50 e 300 árvores em cinco seeds, mantendo as demais configurações, e registre média e desvio da métrica.
- [ ] **Em `01-exercicios/dia-057-random-forest.ipynb`:** Calcule permutation importance para a melhor configuração e compare as cinco primeiras com a importância por impureza.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Como escolher uma métrica adequada para avaliar **Random Forest**?

- [ ] A) Avaliando apenas o tempo de treinamento do algoritmo.
- [ ] B) Considerando o tipo de problema, o desbalanceamento e o custo dos diferentes erros para o negócio.
- [ ] C) Usando sempre acurácia, pois ela serve para qualquer problema.
- [ ] D) Escolhendo a métrica que produz o maior número.
- [ ] E) Trocando de métrica depois de ver qual favorece o modelo.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Qual procedimento fornece uma comparação mais confiável entre modelos em **Random Forest**?

- [ ] A) Testar cada modelo em uma divisão diferente dos dados.
- [ ] B) Escolher pelo desempenho no conjunto usado para treinar.
- [ ] C) Consultar repetidamente o teste durante cada ajuste.
- [ ] D) Comparar somente a quantidade de parâmetros dos algoritmos.
- [ ] E) Usar o mesmo protocolo de validação, ajustar decisões no treino e reservar o teste para a avaliação final.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene um fluxo de modelagem para **Random Forest**.

- A) Avaliar, analisar erros e relacionar o modelo à decisão.
- B) Ajustar o pré-processamento apenas com os dados de treino.
- C) Separar os dados conforme o contexto do problema.
- D) Treinar um baseline e modelos candidatos.
- E) Definir o problema, a população, o alvo e a métrica.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`

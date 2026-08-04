<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 14 — Agrupamento, merge e reshape — 20/08/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Agrupamento, merge e reshape.
- **Competência sugerida:** Manipulação e integração de dados com pandas.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Manipulação e integração de dados com pandas** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Python`.
- **Próximo marco do perfil:** Dia 20 — Engenharia de Software | Análise de Dados | Python e Power BI.

> [!abstract] Resultado concreto do dia
> Concluir **Agrupamento, merge e reshape** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Agrupamento, merge e reshape.
- **Pasta/arquivo principal:** `01-exercicios/dia-014-agrupamento-merge-e-reshape.ipynb`.
- **Dados:** `dados/incidentes.csv`, `dados/clientes_telecom.csv`, `dados/pedidos.csv` e `dados/metas_cidades.csv`.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Com `incidentes.csv` e `metas_cidades.csv`, calcule por `groupby` quantidade, média, mediana, soma de clientes e percentual resolvido por cidade.
2. [ ] Faça `merge` `inner`, `left` e `outer`; anote quantas linhas resultam e identifique cidades sem correspondência.
3. [ ] Crie uma tabela dinâmica com cidade nas linhas, severidade nas colunas e duração média nos valores.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Transforme dados largos em longos com `melt` e volte ao formato largo com `pivot`.
- [ ] Provoque uma chave duplicada em `metas_cidades.csv`, observe o aumento de linhas e crie uma validação para impedir merge muitos-para-muitos acidental.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-014-agrupamento-merge-e-reshape.ipynb`:** Inclua Ilhéus nos incidentes sem criar meta para a cidade e compare quantas linhas aparecem nos merges inner, left e outer.
- [ ] **Em `01-exercicios/dia-014-agrupamento-merge-e-reshape.ipynb`:** Duplique a meta de Salvador, execute a validação de cardinalidade e impeça o merge enquanto a chave continuar duplicada.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Qual cuidado evita conclusões distorcidas ao trabalhar com **Agrupamento, merge e reshape**?

- [ ] A) Somar todas as colunas numéricas independentemente do significado.
- [ ] B) Arredondar os valores antes de analisar diferenças.
- [ ] C) Usar apenas as primeiras linhas como representação de toda a base.
- [ ] D) Substituir valores ausentes pelo maior valor disponível.
- [ ] E) Manter a granularidade correta e conferir o efeito de filtros, agrupamentos e junções.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Qual verificação é mais útil para encontrar problemas que uma média geral pode esconder em **Agrupamento, merge e reshape**?

- [ ] A) Excluir categorias pequenas antes de examiná-las.
- [ ] B) Duplicar a base e repetir o mesmo cálculo.
- [ ] C) Comparar segmentos, distribuições, valores extremos e grupos com poucos registros.
- [ ] D) Ordenar as colunas pelo tamanho do nome.
- [ ] E) Trocar as cores do gráfico até a tendência ficar mais visível.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene um fluxo de análise para uma atividade de **Agrupamento, merge e reshape**.

- A) Definir a pergunta que precisa ser respondida.
- B) Inspecionar a estrutura e a qualidade dos dados.
- C) Preparar os dados sem perder a granularidade necessária.
- D) Comunicar a conclusão, as limitações e a ação sugerida.
- E) Calcular e visualizar as evidências relevantes.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`

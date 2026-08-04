<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 17 — Visualização com pandas e Matplotlib — 25/08/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Visualização com pandas e Matplotlib.
- **Competência sugerida:** Matplotlib.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Matplotlib** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Python`.
- **Próximo marco do perfil:** Dia 20 — Engenharia de Software | Análise de Dados | Python e Power BI.

> [!abstract] Resultado concreto do dia
> Concluir **Visualização com pandas e Matplotlib** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Visualização com pandas e Matplotlib.
- **Pasta/arquivo principal:** `01-exercicios/dia-017-visualizacao-com-pandas-e-matplotlib.ipynb`.
- **Dados:** `dados/incidentes.csv`, `dados/clientes_telecom.csv`, `dados/pedidos.csv` e `dados/metas_cidades.csv`.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Com `pedidos.csv`, crie séries temporais de receita diária e mensal, barras de receita por canal e boxplot de valor por categoria.
2. [ ] Faça primeiro com `DataFrame.plot()` e depois recrie dois gráficos diretamente com Matplotlib.
3. [ ] Adicione linha de meta mensal e destaque meses abaixo da meta por anotação textual.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Crie uma função reutilizável que receba DataFrame, coluna temporal, métrica e título.
- [ ] Teste a função com dados vazios, uma única data e categorias desconhecidas.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-017-visualizacao-com-pandas-e-matplotlib.ipynb`:** Filtre somente o canal app, calcule a receita mensal e recrie o gráfico de linha com título que declare uma conclusão desse recorte.
- [ ] **Em `01-exercicios/dia-017-visualizacao-com-pandas-e-matplotlib.ipynb`:** Passe à função reutilizável um DataFrame vazio e outro com uma única data; trate ambos sem produzir gráfico enganoso.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Qual cuidado evita conclusões distorcidas ao trabalhar com **Visualização com pandas e Matplotlib**?

- [ ] A) Substituir valores ausentes pelo maior valor disponível.
- [ ] B) Manter a granularidade correta e conferir o efeito de filtros, agrupamentos e junções.
- [ ] C) Somar todas as colunas numéricas independentemente do significado.
- [ ] D) Arredondar os valores antes de analisar diferenças.
- [ ] E) Usar apenas as primeiras linhas como representação de toda a base.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Qual verificação é mais útil para encontrar problemas que uma média geral pode esconder em **Visualização com pandas e Matplotlib**?

- [ ] A) Ordenar as colunas pelo tamanho do nome.
- [ ] B) Trocar as cores do gráfico até a tendência ficar mais visível.
- [ ] C) Excluir categorias pequenas antes de examiná-las.
- [ ] D) Duplicar a base e repetir o mesmo cálculo.
- [ ] E) Comparar segmentos, distribuições, valores extremos e grupos com poucos registros.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene um fluxo de análise para uma atividade de **Visualização com pandas e Matplotlib**.

- A) Comunicar a conclusão, as limitações e a ação sugerida.
- B) Preparar os dados sem perder a granularidade necessária.
- C) Inspecionar a estrutura e a qualidade dos dados.
- D) Calcular e visualizar as evidências relevantes.
- E) Definir a pergunta que precisa ser respondida.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`

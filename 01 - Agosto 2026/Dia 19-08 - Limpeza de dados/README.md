<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 13 — Limpeza de dados — 19/08/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Limpeza de dados.
- **Competência sugerida:** Limpeza de dados.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Limpeza de dados** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Python`.
- **Próximo marco do perfil:** Dia 20 — Engenharia de Software | Análise de Dados | Python e Power BI.

> [!abstract] Resultado concreto do dia
> Concluir **Limpeza de dados** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Limpeza de dados.
- **Pasta/arquivo principal:** `01-exercicios/dia-013-limpeza-de-dados.ipynb`.
- **Dados:** `dados/incidentes.csv`, `dados/clientes_telecom.csv`, `dados/pedidos.csv` e `dados/metas_cidades.csv`.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Produza um relatório inicial de ausentes, duplicados, tipos incorretos e categorias inconsistentes.
2. [ ] Padronize textos, converta tipos e trate duplicados com uma regra explícita.
3. [ ] Escolha uma estratégia para cada campo ausente, salve `dados_limpos.csv` e registre o antes/depois em poucas linhas.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Compare duas estratégias para um campo ausente apenas se a escolha inicial ainda não estiver clara.
- [ ] Não remova valores extremos por regra automática neste dia; apenas identifique casos suspeitos e preserve-os.
- [ ] IQR e z-score serão estudados com base estatística no Dia 31.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] Após o Dia 31, volte a este notebook e compare IQR e z-score em uma cópia dos dados.
- [ ] Teste uma categoria com espaços e capitalização diferente usando a mesma função de padronização.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Qual cuidado evita conclusões distorcidas ao trabalhar com **Limpeza de dados**?

- [ ] A) Manter a granularidade correta e conferir o efeito de filtros, agrupamentos e junções.
- [ ] B) Somar todas as colunas numéricas independentemente do significado.
- [ ] C) Arredondar os valores antes de analisar diferenças.
- [ ] D) Usar apenas as primeiras linhas como representação de toda a base.
- [ ] E) Substituir valores ausentes pelo maior valor disponível.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Qual verificação é mais útil para encontrar problemas que uma média geral pode esconder em **Limpeza de dados**?

- [ ] A) Trocar as cores do gráfico até a tendência ficar mais visível.
- [ ] B) Excluir categorias pequenas antes de examiná-las.
- [ ] C) Duplicar a base e repetir o mesmo cálculo.
- [ ] D) Comparar segmentos, distribuições, valores extremos e grupos com poucos registros.
- [ ] E) Ordenar as colunas pelo tamanho do nome.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene um fluxo de análise para uma atividade de **Limpeza de dados**.

- A) Preparar os dados sem perder a granularidade necessária.
- B) Inspecionar a estrutura e a qualidade dos dados.
- C) Definir a pergunta que precisa ser respondida.
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

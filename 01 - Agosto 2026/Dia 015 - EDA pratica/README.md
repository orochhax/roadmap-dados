<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 15 — EDA prática — 21/08/2026
> [!abstract] Resultado concreto do dia
> Concluir **EDA prática** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** EDA prática.
- **Pasta/arquivo principal:** `semana-03/dia-015-eda-pratica/` (pasta do projeto).
- **Dados:** `dados/incidentes.csv`, `dados/clientes_telecom.csv`, `dados/pedidos.csv` e `dados/metas_cidades.csv`.

### Passo a passo completo
1. [ ] Escolha `clientes_telecom.csv` e escreva antes da análise cinco perguntas de negócio sobre churn, chamados, plano, mensalidade e NPS.
2. [ ] Faça inspeção estrutural, qualidade, estatísticas e distribuição do alvo; não gere gráficos antes das perguntas.
3. [ ] Crie pelo menos seis análises segmentadas: churn por plano, cidade, atraso, faixa de NPS, chamados e tempo de cliente.
4. [ ] Produza quatro gráficos úteis, cada um com título que declare a conclusão e um parágrafo de interpretação.
5. [ ] Entregue `eda_clientes.ipynb` e `resumo_executivo.md` com três achados, duas limitações e duas ações sugeridas.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Aplique a técnica central de **EDA prática** a uma segunda coluna, grupo ou recorte dos dados e compare o que mudou.
- [ ] Introduza uma cópia dos dados com um problema controlado — valor ausente, duplicado ou outlier — e verifique como ele afeta o resultado.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. Antes de tirar conclusões em **EDA prática**, qual é a prática mais confiável?

- [ ] A) Inspecionar estrutura, tipos, granularidade, valores ausentes e possíveis duplicidades.
- [ ] B) Começar pelo gráfico mais bonito e escolher os dados depois.
- [ ] C) Remover todas as linhas incompletas sem medir o impacto.
- [ ] D) Calcular médias antes de entender o que cada linha representa.
- [ ] E) Considerar os nomes das colunas suficientes para validar os dados.

2. Qual cuidado evita conclusões distorcidas ao trabalhar com **EDA prática**?

- [ ] A) Arredondar os valores antes de analisar diferenças.
- [ ] B) Usar apenas as primeiras linhas como representação de toda a base.
- [ ] C) Substituir valores ausentes pelo maior valor disponível.
- [ ] D) Manter a granularidade correta e conferir o efeito de filtros, agrupamentos e junções.
- [ ] E) Somar todas as colunas numéricas independentemente do significado.

3. Qual verificação é mais útil para encontrar problemas que uma média geral pode esconder em **EDA prática**?

- [ ] A) Duplicar a base e repetir o mesmo cálculo.
- [ ] B) Comparar segmentos, distribuições, valores extremos e grupos com poucos registros.
- [ ] C) Ordenar as colunas pelo tamanho do nome.
- [ ] D) Trocar as cores do gráfico até a tendência ficar mais visível.
- [ ] E) Excluir categorias pequenas antes de examiná-las.

4. Como uma análise de **EDA prática** deve ser apresentada para apoiar uma decisão?

- [ ] A) Mostrando todas as tabelas produzidas, sem priorizar uma conclusão.
- [ ] B) Omitindo incertezas para transmitir mais confiança.
- [ ] C) Usando apenas termos técnicos, sem explicar o impacto.
- [ ] D) Escolhendo a recomendação mais popular, mesmo sem evidência.
- [ ] E) Ligando evidências à pergunta de negócio, com limitações e uma ação recomendada.

5. Ordene um fluxo de análise para uma atividade de **EDA prática**.

- A) Definir a pergunta que precisa ser respondida.
- B) Preparar os dados sem perder a granularidade necessária.
- C) Comunicar a conclusão, as limitações e a ação sugerida.
- D) Calcular e visualizar as evidências relevantes.
- E) Inspecionar a estrutura e a qualidade dos dados.

**Ordem:** `__ → __ → __ → __ → __`

6. Ordene a preparação de uma visualização ou entrega sobre **EDA prática**.

- A) Identificar o público e a decisão que será apoiada.
- B) Selecionar a métrica e o recorte adequados.
- C) Apresentar a mensagem principal e o próximo passo.
- D) Revisar rótulos, escalas e possíveis interpretações enganosas.
- E) Escolher o tipo de visual compatível com a comparação.

**Ordem:** `__ → __ → __ → __ → __`

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Alterações registradas em commit e enviadas ao GitHub.

**Autoavaliação do dia:** `__/5`  
**Evidência:** link do commit, notebook, consulta, imagem ou gravação.

> [!project] Projeto semanal — Auditoria de Dados de Clientes e Risco de Cancelamento
> **Desafio:** Auditar uma base imperfeita de clientes, corrigir problemas de qualidade e investigar quais sinais merecem ser estudados como possíveis fatores de risco de cancelamento.
>
> **Deve reutilizar:** Python, NumPy, pandas e validações.
>
> **Entregáveis obrigatórios:**
> - [ ] notebook reexecutável e tabela antes/depois da limpeza;
> - [ ] dicionário de dados com definição das variáveis;
> - [ ] cinco perguntas de negócio sobre churn, chamados, atraso, plano e satisfação;
> - [ ] seis análises segmentadas e quatro gráficos comentados;
> - [ ] lista de variáveis candidatas e variáveis proibidas por risco de leakage;
> - [ ] relatório com achados, limitações e próximas hipóteses;
>
> **Defesa:** diferenciar associação de causalidade e justificar por que nenhum achado exploratório prova sozinho que um cliente irá cancelar.
>
> **Nota mínima recomendada:** `6/10`.

> [!check] Critério para avançar
> Você consegue transformar uma auditoria de dados em hipóteses claras para um futuro modelo, sem antecipar conclusões?

---

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** EDA prática.
- **Competência sugerida:** Análise Exploratória de Dados (EDA).
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Análise Exploratória de Dados (EDA)** na seção Competências. Se a entrega estiver revisada e representar bem seu trabalho, considere incluí-la em Projetos ou Destaques.
- **Título atual recomendado:** `Engenharia de Software | Python`.
- **Próximo marco do perfil:** Dia 20 — Engenharia de Software | Análise de Dados | Python e Power BI.

---

## Anotações pessoais



### Conceitos estudados


### Dúvidas


### Erros encontrados e correções


### Aprendizado principal


### Próxima ação

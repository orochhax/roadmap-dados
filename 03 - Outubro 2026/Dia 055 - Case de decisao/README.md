<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 55 — Case de decisão — 16/10/2026
> [!abstract] Resultado concreto do dia
> Concluir **Case de decisão** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Case de decisão.
- **Pasta/arquivo principal:** `semana-11/dia-055-case-de-decisao/` (pasta do projeto).
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Passo a passo completo
1. [ ] Monte tabela com cliente, probabilidade, limiar, decisão e custo esperado.
2. [ ] Crie três políticas: conservadora, equilibrada e agressiva; calcule volume de ações e custo.
3. [ ] Analise desempenho por cidade, plano e faixa de mensalidade.
4. [ ] Defina regra de revisão humana para casos próximos ao limiar.
5. [ ] Apresente decisão em uma página, incluindo quem não deve receber ação automatizada.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Faça uma alteração controlada em uma feature, modelo, hiperparâmetro ou limiar de **Case de decisão** e compare usando a mesma validação.
- [ ] Separe alguns erros do modelo por grupo ou tipo de caso e registre onde o desempenho piora e o que investigar.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. Qual prática evita vazamento de dados em uma atividade de **Case de decisão**?

- [ ] A) Separar treino e teste antes de ajustar transformações, selecionar variáveis ou treinar o modelo.
- [ ] B) Normalizar toda a base antes da separação para usar mais informação.
- [ ] C) Escolher variáveis depois de observar o desempenho no teste.
- [ ] D) Duplicar exemplos raros antes de separar os conjuntos.
- [ ] E) Usar a variável-alvo para preencher valores ausentes de todas as colunas.

2. Como escolher uma métrica adequada para avaliar **Case de decisão**?

- [ ] A) Escolhendo a métrica que produz o maior número.
- [ ] B) Trocando de métrica depois de ver qual favorece o modelo.
- [ ] C) Avaliando apenas o tempo de treinamento do algoritmo.
- [ ] D) Considerando o tipo de problema, o desbalanceamento e o custo dos diferentes erros para o negócio.
- [ ] E) Usando sempre acurácia, pois ela serve para qualquer problema.

3. Qual procedimento fornece uma comparação mais confiável entre modelos em **Case de decisão**?

- [ ] A) Comparar somente a quantidade de parâmetros dos algoritmos.
- [ ] B) Usar o mesmo protocolo de validação, ajustar decisões no treino e reservar o teste para a avaliação final.
- [ ] C) Testar cada modelo em uma divisão diferente dos dados.
- [ ] D) Escolher pelo desempenho no conjunto usado para treinar.
- [ ] E) Consultar repetidamente o teste durante cada ajuste.

4. Antes de usar um modelo de **Case de decisão** em uma decisão real, o que deve ser analisado?

- [ ] A) Somente a métrica média do melhor experimento.
- [ ] B) A aparência dos gráficos de treinamento, sem examinar dados.
- [ ] C) A complexidade do nome do algoritmo escolhido.
- [ ] D) A quantidade de linhas de código usada para criar o modelo.
- [ ] E) Erros por segmento, estabilidade, explicabilidade e impacto dos falsos positivos e falsos negativos.

5. Ordene um fluxo de modelagem para **Case de decisão**.

- A) Definir o problema, a população, o alvo e a métrica.
- B) Ajustar o pré-processamento apenas com os dados de treino.
- C) Avaliar, analisar erros e relacionar o modelo à decisão.
- D) Treinar um baseline e modelos candidatos.
- E) Separar os dados conforme o contexto do problema.

**Ordem:** `__ → __ → __ → __ → __`

6. Ordene uma seleção responsável de modelo em **Case de decisão**.

- A) Estabelecer um baseline simples e reproduzível.
- B) Ajustar hiperparâmetros sem consultar o conjunto de teste.
- C) Documentar limitações, segmentos frágeis e regras de uso.
- D) Avaliar uma vez no teste após fechar as escolhas.
- E) Comparar candidatos com o mesmo protocolo de validação.

**Ordem:** `__ → __ → __ → __ → __`

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Alterações registradas em commit e enviadas ao GitHub.

**Autoavaliação do dia:** `__/5`  
**Evidência:** link do commit, notebook, consulta, imagem ou gravação.

> [!todo] PUBLICAR NO LINKEDIN — projeto prioritário do portfólio
> - [ ] Publique somente após README, resultados e limitações estarem revisados.
> - [ ] Inclua problema, abordagem, principal evidência, decisão e link do GitHub.
> - [ ] **Ângulo sugerido:** mostrar por que o limiar 0,5 não é automático e como custos dos erros mudam a política.

> [!project] Projeto semanal — Política de acionamento por probabilidade
> **Desafio:** Criar uma política que decide quem receberá uma intervenção com base em probabilidades e custo dos erros.
>
> **Deve reutilizar:** Classificação, regressão logística, limiar, calibração e desbalanceamento.
>
> **Entregáveis obrigatórios:**
> - [ ] curvas e métricas;
> - [ ] função de custo;
> - [ ] limiar escolhido;
> - [ ] análise de segmentos;
> - [ ] parecer de risco;
>
> **Defesa:** demonstração de cinco minutos e resposta a três perguntas técnicas.
>
> **Nota mínima recomendada:** `6/10`.

> [!check] Critério para avançar
> Você consegue defender o limiar do modelo com custo e não apenas usar 0,5?

---

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Case de decisão.
- **Competência sugerida:** Machine Learning para tomada de decisão.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Machine Learning para tomada de decisão** na seção Competências. Se a entrega estiver revisada e representar bem seu trabalho, considere incluí-la em Projetos ou Destaques.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

---

## Anotações pessoais



### Conceitos estudados


### Dúvidas


### Erros encontrados e correções


### Aprendizado principal


### Próxima ação

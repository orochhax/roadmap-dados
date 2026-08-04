<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 59 — Seleção de modelo — 22/10/2026
> [!abstract] Resultado concreto do dia
> Concluir **Seleção de modelo** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Seleção de modelo.
- **Pasta/arquivo principal:** `semana-12/dia-059-selecao-de-modelo.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Passo a passo completo
1. [ ] Crie tabela única com todos os modelos já treinados, mesma validação e métricas.
2. [ ] Defina critérios de escolha antes de olhar o vencedor: custo, recall, calibração, tempo, explicabilidade.
3. [ ] Use teste ou bootstrap para verificar estabilidade da diferença entre os dois melhores.
4. [ ] Escolha modelo campeão e um challenger.
5. [ ] Escreva decisão com trade-offs, não apenas ranking.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Faça uma alteração controlada em uma feature, modelo, hiperparâmetro ou limiar de **Seleção de modelo** e compare usando a mesma validação.
- [ ] Separe alguns erros do modelo por grupo ou tipo de caso e registre onde o desempenho piora e o que investigar.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Crie tabela única com todos os modelos já treinados, mesma validação e métricas.

   **Pergunta:** Qual prática evita vazamento de dados em uma atividade de **Seleção de modelo**?

- [ ] A) Usar a variável-alvo para preencher valores ausentes de todas as colunas.
- [ ] B) Separar treino e teste antes de ajustar transformações, selecionar variáveis ou treinar o modelo.
- [ ] C) Normalizar toda a base antes da separação para usar mais informação.
- [ ] D) Escolher variáveis depois de observar o desempenho no teste.
- [ ] E) Duplicar exemplos raros antes de separar os conjuntos.

2. **Referência — atividade 2:** Defina critérios de escolha antes de olhar o vencedor: custo, recall, calibração, tempo, explicabilidade.

   **Pergunta:** Como escolher uma métrica adequada para avaliar **Seleção de modelo**?

- [ ] A) Usando sempre acurácia, pois ela serve para qualquer problema.
- [ ] B) Escolhendo a métrica que produz o maior número.
- [ ] C) Trocando de métrica depois de ver qual favorece o modelo.
- [ ] D) Avaliando apenas o tempo de treinamento do algoritmo.
- [ ] E) Considerando o tipo de problema, o desbalanceamento e o custo dos diferentes erros para o negócio.

3. **Referência — atividade 3:** Use teste ou bootstrap para verificar estabilidade da diferença entre os dois melhores.

   **Pergunta:** Qual procedimento fornece uma comparação mais confiável entre modelos em **Seleção de modelo**?

- [ ] A) Consultar repetidamente o teste durante cada ajuste.
- [ ] B) Comparar somente a quantidade de parâmetros dos algoritmos.
- [ ] C) Usar o mesmo protocolo de validação, ajustar decisões no treino e reservar o teste para a avaliação final.
- [ ] D) Testar cada modelo em uma divisão diferente dos dados.
- [ ] E) Escolher pelo desempenho no conjunto usado para treinar.

4. **Referência — atividade 4:** Escolha modelo campeão e um challenger.

   **Pergunta:** Antes de usar um modelo de **Seleção de modelo** em uma decisão real, o que deve ser analisado?

- [ ] A) Erros por segmento, estabilidade, explicabilidade e impacto dos falsos positivos e falsos negativos.
- [ ] B) Somente a métrica média do melhor experimento.
- [ ] C) A aparência dos gráficos de treinamento, sem examinar dados.
- [ ] D) A complexidade do nome do algoritmo escolhido.
- [ ] E) A quantidade de linhas de código usada para criar o modelo.

5. **Referência — atividade 5:** Escreva decisão com trade-offs, não apenas ranking.

   **Pergunta:** Ordene um fluxo de modelagem para **Seleção de modelo**.

- A) Definir o problema, a população, o alvo e a métrica.
- B) Ajustar o pré-processamento apenas com os dados de treino.
- C) Avaliar, analisar erros e relacionar o modelo à decisão.
- D) Treinar um baseline e modelos candidatos.
- E) Separar os dados conforme o contexto do problema.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene uma seleção responsável de modelo em **Seleção de modelo**.

- A) Ajustar hiperparâmetros sem consultar o conjunto de teste.
- B) Comparar candidatos com o mesmo protocolo de validação.
- C) Documentar limitações, segmentos frágeis e regras de uso.
- D) Avaliar uma vez no teste após fechar as escolhas.
- E) Estabelecer um baseline simples e reproduzível.

**Ordem:** `__ → __ → __ → __ → __`

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Alterações registradas em commit e enviadas ao GitHub.

**Autoavaliação do dia:** `__/5`  

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Seleção de modelo.
- **Competência sugerida:** Seleção de modelos.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Seleção de modelos** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

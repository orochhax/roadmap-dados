<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 52 — Limiar e custo — 13/10/2026
> [!abstract] Resultado concreto do dia
> Concluir **Limiar e custo** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Limiar e custo.
- **Pasta/arquivo principal:** `semana-11/dia-052-limiar-e-custo.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Passo a passo completo
1. [ ] Calcule previsões para limiares 0.2, 0.3, 0.5, 0.7 e 0.8.
2. [ ] Para cada limiar, registre TP, FP, FN, TN, precision, recall e custo total.
3. [ ] Use custos definidos: FN=R$500, FP=R$20, TP=R$80 de campanha e benefício esperado de R$300.
4. [ ] Escolha o limiar de menor custo respeitando recall mínimo de 70%.
5. [ ] Crie gráfico custo versus limiar e escreva recomendação executiva.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Faça uma alteração controlada em uma feature, modelo, hiperparâmetro ou limiar de **Limiar e custo** e compare usando a mesma validação.
- [ ] Separe alguns erros do modelo por grupo ou tipo de caso e registre onde o desempenho piora e o que investigar.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Calcule previsões para limiares 0.2, 0.3, 0.5, 0.7 e 0.8.

   **Pergunta:** Qual prática evita vazamento de dados em uma atividade de **Limiar e custo**?

- [ ] A) Escolher variáveis depois de observar o desempenho no teste.
- [ ] B) Duplicar exemplos raros antes de separar os conjuntos.
- [ ] C) Usar a variável-alvo para preencher valores ausentes de todas as colunas.
- [ ] D) Separar treino e teste antes de ajustar transformações, selecionar variáveis ou treinar o modelo.
- [ ] E) Normalizar toda a base antes da separação para usar mais informação.

2. **Referência — atividade 2:** Para cada limiar, registre TP, FP, FN, TN, precision, recall e custo total.

   **Pergunta:** Como escolher uma métrica adequada para avaliar **Limiar e custo**?

- [ ] A) Avaliando apenas o tempo de treinamento do algoritmo.
- [ ] B) Considerando o tipo de problema, o desbalanceamento e o custo dos diferentes erros para o negócio.
- [ ] C) Usando sempre acurácia, pois ela serve para qualquer problema.
- [ ] D) Escolhendo a métrica que produz o maior número.
- [ ] E) Trocando de métrica depois de ver qual favorece o modelo.

3. **Referência — atividade 3:** Use custos definidos: FN=R$500, FP=R$20, TP=R$80 de campanha e benefício esperado de R$300.

   **Pergunta:** Qual procedimento fornece uma comparação mais confiável entre modelos em **Limiar e custo**?

- [ ] A) Testar cada modelo em uma divisão diferente dos dados.
- [ ] B) Escolher pelo desempenho no conjunto usado para treinar.
- [ ] C) Consultar repetidamente o teste durante cada ajuste.
- [ ] D) Comparar somente a quantidade de parâmetros dos algoritmos.
- [ ] E) Usar o mesmo protocolo de validação, ajustar decisões no treino e reservar o teste para a avaliação final.

4. **Referência — atividade 4:** Escolha o limiar de menor custo respeitando recall mínimo de 70%.

   **Pergunta:** Antes de usar um modelo de **Limiar e custo** em uma decisão real, o que deve ser analisado?

- [ ] A) A complexidade do nome do algoritmo escolhido.
- [ ] B) A quantidade de linhas de código usada para criar o modelo.
- [ ] C) Erros por segmento, estabilidade, explicabilidade e impacto dos falsos positivos e falsos negativos.
- [ ] D) Somente a métrica média do melhor experimento.
- [ ] E) A aparência dos gráficos de treinamento, sem examinar dados.

5. **Referência — atividade 5:** Crie gráfico custo versus limiar e escreva recomendação executiva.

   **Pergunta:** Ordene um fluxo de modelagem para **Limiar e custo**.

- A) Definir o problema, a população, o alvo e a métrica.
- B) Ajustar o pré-processamento apenas com os dados de treino.
- C) Avaliar, analisar erros e relacionar o modelo à decisão.
- D) Treinar um baseline e modelos candidatos.
- E) Separar os dados conforme o contexto do problema.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene uma seleção responsável de modelo em **Limiar e custo**.

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

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Limiar e custo.
- **Competência sugerida:** Limiar de decisão e análise de custo.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Limiar de decisão e análise de custo** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

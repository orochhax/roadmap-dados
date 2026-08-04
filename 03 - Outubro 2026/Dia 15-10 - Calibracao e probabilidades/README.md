<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 53 — Calibração e probabilidades — 14/10/2026
> [!abstract] Resultado concreto do dia
> Concluir **Calibração e probabilidades** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Calibração e probabilidades.
- **Pasta/arquivo principal:** `semana-11/dia-053-calibracao-e-probabilidades.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Passo a passo completo
1. [ ] Crie gráfico de calibração e calcule Brier Score para regressão logística e modelo de árvore.
2. [ ] Agrupe probabilidades em decis e compare previsão média com frequência real.
3. [ ] Aplique `CalibratedClassifierCV` com métodos sigmoid e isotonic.
4. [ ] Compare discriminação e calibração antes/depois.
5. [ ] Explique por que uma probabilidade mal calibrada prejudica política de crédito ou retenção.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Faça uma alteração controlada em uma feature, modelo, hiperparâmetro ou limiar de **Calibração e probabilidades** e compare usando a mesma validação.
- [ ] Separe alguns erros do modelo por grupo ou tipo de caso e registre onde o desempenho piora e o que investigar.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Crie gráfico de calibração e calcule Brier Score para regressão logística e modelo de árvore.

   **Pergunta:** Qual prática evita vazamento de dados em uma atividade de **Calibração e probabilidades**?

- [ ] A) Duplicar exemplos raros antes de separar os conjuntos.
- [ ] B) Usar a variável-alvo para preencher valores ausentes de todas as colunas.
- [ ] C) Separar treino e teste antes de ajustar transformações, selecionar variáveis ou treinar o modelo.
- [ ] D) Normalizar toda a base antes da separação para usar mais informação.
- [ ] E) Escolher variáveis depois de observar o desempenho no teste.

2. **Referência — atividade 2:** Agrupe probabilidades em decis e compare previsão média com frequência real.

   **Pergunta:** Como escolher uma métrica adequada para avaliar **Calibração e probabilidades**?

- [ ] A) Considerando o tipo de problema, o desbalanceamento e o custo dos diferentes erros para o negócio.
- [ ] B) Usando sempre acurácia, pois ela serve para qualquer problema.
- [ ] C) Escolhendo a métrica que produz o maior número.
- [ ] D) Trocando de métrica depois de ver qual favorece o modelo.
- [ ] E) Avaliando apenas o tempo de treinamento do algoritmo.

3. **Referência — atividade 3:** Aplique `CalibratedClassifierCV` com métodos sigmoid e isotonic.

   **Pergunta:** Qual procedimento fornece uma comparação mais confiável entre modelos em **Calibração e probabilidades**?

- [ ] A) Escolher pelo desempenho no conjunto usado para treinar.
- [ ] B) Consultar repetidamente o teste durante cada ajuste.
- [ ] C) Comparar somente a quantidade de parâmetros dos algoritmos.
- [ ] D) Usar o mesmo protocolo de validação, ajustar decisões no treino e reservar o teste para a avaliação final.
- [ ] E) Testar cada modelo em uma divisão diferente dos dados.

4. **Referência — atividade 4:** Compare discriminação e calibração antes/depois.

   **Pergunta:** Antes de usar um modelo de **Calibração e probabilidades** em uma decisão real, o que deve ser analisado?

- [ ] A) A quantidade de linhas de código usada para criar o modelo.
- [ ] B) Erros por segmento, estabilidade, explicabilidade e impacto dos falsos positivos e falsos negativos.
- [ ] C) Somente a métrica média do melhor experimento.
- [ ] D) A aparência dos gráficos de treinamento, sem examinar dados.
- [ ] E) A complexidade do nome do algoritmo escolhido.

5. **Referência — atividade 5:** Explique por que uma probabilidade mal calibrada prejudica política de crédito ou retenção.

   **Pergunta:** Ordene um fluxo de modelagem para **Calibração e probabilidades**.

- A) Ajustar o pré-processamento apenas com os dados de treino.
- B) Avaliar, analisar erros e relacionar o modelo à decisão.
- C) Definir o problema, a população, o alvo e a métrica.
- D) Treinar um baseline e modelos candidatos.
- E) Separar os dados conforme o contexto do problema.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene uma seleção responsável de modelo em **Calibração e probabilidades**.

- A) Ajustar hiperparâmetros sem consultar o conjunto de teste.
- B) Documentar limitações, segmentos frágeis e regras de uso.
- C) Estabelecer um baseline simples e reproduzível.
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

- **Conhecimento praticado hoje:** Calibração e probabilidades.
- **Competência sugerida:** Calibração de modelos.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Calibração de modelos** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 51 — Regressão logística — 12/10/2026
> [!abstract] Resultado concreto do dia
> Concluir **Regressão logística** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Regressão logística.
- **Pasta/arquivo principal:** `01-exercicios/dia-051-regressao-logistica.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Passo a passo completo
1. [ ] Implemente regressão logística em dados sintéticos e interprete probabilidade e log-odds em nível conceitual.
2. [ ] Treine no churn com pipeline completa e obtenha probabilidades, não apenas classes.
3. [ ] Interprete sinal e magnitude de cinco coeficientes após padronização.
4. [ ] Compare regressão logística com `DummyClassifier` e regra simples.
5. [ ] Teste multicolinearidade e regularização; documente estabilidade dos coeficientes.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/dia-051-regressao-logistica.ipynb`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/dia-051-regressao-logistica.ipynb`:** Treine a logística com C=0,1 e C=10 no mesmo split e compare cinco coeficientes padronizados.
- [ ] **Em `01-exercicios/dia-051-regressao-logistica.ipynb`:** Avalie probabilidades no grupo chamados_90d>=3 e compare a média com o grupo chamados_90d<3.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Implemente regressão logística em dados sintéticos e interprete probabilidade e log-odds em nível conceitual.

   **Pergunta:** Qual prática evita vazamento de dados em uma atividade de **Regressão logística**?

- [ ] A) Normalizar toda a base antes da separação para usar mais informação.
- [ ] B) Escolher variáveis depois de observar o desempenho no teste.
- [ ] C) Duplicar exemplos raros antes de separar os conjuntos.
- [ ] D) Usar a variável-alvo para preencher valores ausentes de todas as colunas.
- [ ] E) Separar treino e teste antes de ajustar transformações, selecionar variáveis ou treinar o modelo.

2. **Referência — atividade 2:** Treine no churn com pipeline completa e obtenha probabilidades, não apenas classes.

   **Pergunta:** Como escolher uma métrica adequada para avaliar **Regressão logística**?

- [ ] A) Trocando de métrica depois de ver qual favorece o modelo.
- [ ] B) Avaliando apenas o tempo de treinamento do algoritmo.
- [ ] C) Considerando o tipo de problema, o desbalanceamento e o custo dos diferentes erros para o negócio.
- [ ] D) Usando sempre acurácia, pois ela serve para qualquer problema.
- [ ] E) Escolhendo a métrica que produz o maior número.

3. **Referência — atividade 3:** Interprete sinal e magnitude de cinco coeficientes após padronização.

   **Pergunta:** Qual procedimento fornece uma comparação mais confiável entre modelos em **Regressão logística**?

- [ ] A) Usar o mesmo protocolo de validação, ajustar decisões no treino e reservar o teste para a avaliação final.
- [ ] B) Testar cada modelo em uma divisão diferente dos dados.
- [ ] C) Escolher pelo desempenho no conjunto usado para treinar.
- [ ] D) Consultar repetidamente o teste durante cada ajuste.
- [ ] E) Comparar somente a quantidade de parâmetros dos algoritmos.

4. **Referência — atividade 4:** Compare regressão logística com `DummyClassifier` e regra simples.

   **Pergunta:** Antes de usar um modelo de **Regressão logística** em uma decisão real, o que deve ser analisado?

- [ ] A) A aparência dos gráficos de treinamento, sem examinar dados.
- [ ] B) A complexidade do nome do algoritmo escolhido.
- [ ] C) A quantidade de linhas de código usada para criar o modelo.
- [ ] D) Erros por segmento, estabilidade, explicabilidade e impacto dos falsos positivos e falsos negativos.
- [ ] E) Somente a métrica média do melhor experimento.

5. **Referência — atividade 5:** Teste multicolinearidade e regularização; documente estabilidade dos coeficientes.

   **Pergunta:** Ordene um fluxo de modelagem para **Regressão logística**.

- A) Definir o problema, a população, o alvo e a métrica.
- B) Separar os dados conforme o contexto do problema.
- C) Avaliar, analisar erros e relacionar o modelo à decisão.
- D) Treinar um baseline e modelos candidatos.
- E) Ajustar o pré-processamento apenas com os dados de treino.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene uma seleção responsável de modelo em **Regressão logística**.

- A) Documentar limitações, segmentos frágeis e regras de uso.
- B) Ajustar hiperparâmetros sem consultar o conjunto de teste.
- C) Comparar candidatos com o mesmo protocolo de validação.
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

- **Conhecimento praticado hoje:** Regressão logística.
- **Competência sugerida:** Regressão logística.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Regressão logística** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 42 — Separação e vazamento — 29/09/2026
> [!abstract] Resultado concreto do dia
> Concluir **Separação e vazamento** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Separação e vazamento.
- **Pasta/arquivo principal:** `semana-09/dia-042-separacao-e-vazamento.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Passo a passo completo
1. [ ] Separe treino, validação e teste com proporção 60/20/20 e `random_state` fixo.
2. [ ] Repita a separação de forma estratificada e compare proporção de churn em cada conjunto.
3. [ ] Crie três features com leakage proposital, como `data_cancelamento`, `motivo_cancelamento` e `status_atual`; demonstre o aumento artificial da métrica.
4. [ ] Remova o leakage e registre a queda de desempenho como evidência de correção.
5. [ ] Escreva um checklist de 10 perguntas para detectar vazamento antes da modelagem.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Faça uma alteração controlada em uma feature, modelo, hiperparâmetro ou limiar de **Separação e vazamento** e compare usando a mesma validação.
- [ ] Separe alguns erros do modelo por grupo ou tipo de caso e registre onde o desempenho piora e o que investigar.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Separe treino, validação e teste com proporção 60/20/20 e `random_state` fixo.

   **Pergunta:** Qual prática evita vazamento de dados em uma atividade de **Separação e vazamento**?

- [ ] A) Escolher variáveis depois de observar o desempenho no teste.
- [ ] B) Duplicar exemplos raros antes de separar os conjuntos.
- [ ] C) Usar a variável-alvo para preencher valores ausentes de todas as colunas.
- [ ] D) Separar treino e teste antes de ajustar transformações, selecionar variáveis ou treinar o modelo.
- [ ] E) Normalizar toda a base antes da separação para usar mais informação.

2. **Referência — atividade 2:** Repita a separação de forma estratificada e compare proporção de churn em cada conjunto.

   **Pergunta:** Como escolher uma métrica adequada para avaliar **Separação e vazamento**?

- [ ] A) Avaliando apenas o tempo de treinamento do algoritmo.
- [ ] B) Considerando o tipo de problema, o desbalanceamento e o custo dos diferentes erros para o negócio.
- [ ] C) Usando sempre acurácia, pois ela serve para qualquer problema.
- [ ] D) Escolhendo a métrica que produz o maior número.
- [ ] E) Trocando de métrica depois de ver qual favorece o modelo.

3. **Referência — atividade 3:** Crie três features com leakage proposital, como `data_cancelamento`, `motivo_cancelamento` e `status_atual`; demonstre o aumento artificial da métrica.

   **Pergunta:** Qual procedimento fornece uma comparação mais confiável entre modelos em **Separação e vazamento**?

- [ ] A) Testar cada modelo em uma divisão diferente dos dados.
- [ ] B) Escolher pelo desempenho no conjunto usado para treinar.
- [ ] C) Consultar repetidamente o teste durante cada ajuste.
- [ ] D) Comparar somente a quantidade de parâmetros dos algoritmos.
- [ ] E) Usar o mesmo protocolo de validação, ajustar decisões no treino e reservar o teste para a avaliação final.

4. **Referência — atividade 4:** Remova o leakage e registre a queda de desempenho como evidência de correção.

   **Pergunta:** Antes de usar um modelo de **Separação e vazamento** em uma decisão real, o que deve ser analisado?

- [ ] A) A complexidade do nome do algoritmo escolhido.
- [ ] B) A quantidade de linhas de código usada para criar o modelo.
- [ ] C) Erros por segmento, estabilidade, explicabilidade e impacto dos falsos positivos e falsos negativos.
- [ ] D) Somente a métrica média do melhor experimento.
- [ ] E) A aparência dos gráficos de treinamento, sem examinar dados.

5. **Referência — atividade 5:** Escreva um checklist de 10 perguntas para detectar vazamento antes da modelagem.

   **Pergunta:** Ordene um fluxo de modelagem para **Separação e vazamento**.

- A) Definir o problema, a população, o alvo e a métrica.
- B) Avaliar, analisar erros e relacionar o modelo à decisão.
- C) Separar os dados conforme o contexto do problema.
- D) Treinar um baseline e modelos candidatos.
- E) Ajustar o pré-processamento apenas com os dados de treino.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene uma seleção responsável de modelo em **Separação e vazamento**.

- A) Estabelecer um baseline simples e reproduzível.
- B) Comparar candidatos com o mesmo protocolo de validação.
- C) Documentar limitações, segmentos frágeis e regras de uso.
- D) Avaliar uma vez no teste após fechar as escolhas.
- E) Ajustar hiperparâmetros sem consultar o conjunto de teste.

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

- **Conhecimento praticado hoje:** Separação e vazamento.
- **Competência sugerida:** Separação de dados e prevenção de vazamento.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Separação de dados e prevenção de vazamento** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

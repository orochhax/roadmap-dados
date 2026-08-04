<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 38 — Teste A/B — 23/09/2026
> [!abstract] Resultado concreto do dia
> Concluir **Teste A/B** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Teste A/B.
- **Pasta/arquivo principal:** `01-exercicios/dia-038-teste-a-b.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/incidentes.csv` e dados sintéticos gerados no notebook com seed 42.

### Passo a passo completo
1. [ ] Defina experimento A/B de uma oferta de retenção: unidade, população, métrica primária, guardrails, duração e critério de parada.
2. [ ] Gere dados sintéticos de 2.000 clientes por grupo com taxas 10% e 11,5%; calcule diferença, IC e teste.
3. [ ] Calcule tamanho de amostra aproximado para detectar aumento mínimo de 1,5 ponto percentual.
4. [ ] Simule peeking diário e explique como aumenta falso positivo.
5. [ ] Crie relatório de decisão: lançar, repetir ou abandonar, justificando risco e impacto.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/dia-038-teste-a-b.ipynb`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/dia-038-teste-a-b.ipynb`:** Refaça o cálculo de tamanho de amostra para efeito mínimo de 0,5 ponto percentual em vez de 1,5 ponto.
- [ ] **Em `01-exercicios/dia-038-teste-a-b.ipynb`:** Execute a simulação de peeking em 30 verificações diárias e conte quantas vezes a regra pararia antes da amostra planejada.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Defina experimento A/B de uma oferta de retenção: unidade, população, métrica primária, guardrails, duração e critério de parada.

   **Pergunta:** Ao estudar **Teste A/B**, por que uma única medida-resumo pode ser insuficiente?

- [ ] A) Porque a mediana sempre substitui qualquer outra medida.
- [ ] B) Porque gráficos tornam cálculos estatísticos desnecessários.
- [ ] C) Porque distribuições diferentes podem ter a mesma média e esconder dispersão, assimetria ou valores extremos.
- [ ] D) Porque médias só podem ser usadas com dados de texto.
- [ ] E) Porque toda análise exige exatamente cinco métricas.

2. **Referência — atividade 2:** Gere dados sintéticos de 2.000 clientes por grupo com taxas 10% e 11,5%; calcule diferença, IC e teste.

   **Pergunta:** Qual interpretação estatística é mais responsável em uma análise de **Teste A/B**?

- [ ] A) Avaliar tamanho do efeito, incerteza, pressupostos e relevância prática em conjunto.
- [ ] B) Tratar qualquer valor-p pequeno como prova de grande impacto.
- [ ] C) Considerar correlação suficiente para afirmar causalidade.
- [ ] D) Escolher a hipótese depois de observar os dados.
- [ ] E) Ignorar o tamanho da amostra quando a média parece convincente.

3. **Referência — atividade 3:** Calcule tamanho de amostra aproximado para detectar aumento mínimo de 1,5 ponto percentual.

   **Pergunta:** Qual situação ameaça mais a validade de uma conclusão sobre **Teste A/B**?

- [ ] A) Um gráfico com título curto.
- [ ] B) Uma média apresentada com duas casas decimais.
- [ ] C) Um arquivo salvo em uma pasta específica do projeto.
- [ ] D) Uma amostra enviesada que não representa adequadamente a população de interesse.
- [ ] E) Uma tabela com colunas em ordem diferente.

4. **Referência — atividade 4:** Simule peeking diário e explique como aumenta falso positivo.

   **Pergunta:** Como usar evidência de **Teste A/B** em uma decisão real?

- [ ] A) Repetir testes até surgir uma conclusão favorável.
- [ ] B) Combinar a estimativa e sua incerteza com custos, riscos e consequências das alternativas.
- [ ] C) Escolher automaticamente a opção com a maior média observada.
- [ ] D) Eliminar a incerteza arredondando os números.
- [ ] E) Tomar a decisão apenas pelo sinal positivo ou negativo.

5. **Referência — atividade 5:** Crie relatório de decisão: lançar, repetir ou abandonar, justificando risco e impacto.

   **Pergunta:** Ordene um estudo estatístico relacionado a **Teste A/B**.

- A) Coletar e verificar a qualidade dos dados.
- B) Definir população, amostra, métrica e método.
- C) Formular a pergunta e a hipótese antes da análise.
- D) Interpretar a evidência com pressupostos e limitações.
- E) Estimar efeitos e quantificar a incerteza.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene as etapas de um experimento controlado ligado a **Teste A/B**.

- A) Definir hipótese, métrica principal e regra de decisão.
- B) Decidir com base no efeito, no risco e na relevância prática.
- C) Distribuir aleatoriamente as unidades entre os grupos.
- D) Estimar a diferença entre grupos e sua incerteza.
- E) Verificar equilíbrio e integridade da coleta.

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

- **Conhecimento praticado hoje:** Teste A/B.
- **Competência sugerida:** Testes A/B.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Testes A/B** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

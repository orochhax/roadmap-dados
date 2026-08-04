<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 49 — Feature engineering para regressão — 08/10/2026
> [!abstract] Resultado concreto do dia
> Concluir **Feature engineering para regressão** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Feature engineering para regressão.
- **Pasta/arquivo principal:** `semana-10/dia-049-feature-engineering-para-regressao.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Passo a passo completo
1. [ ] Crie features de data: mês, dia da semana, fim de semana e dias desde primeira compra.
2. [ ] Crie transformações `log1p` para variável assimétrica e interações entre desconto e canal.
3. [ ] Agrupe categorias raras com limiar explícito e documente impacto.
4. [ ] Construa cada feature dentro da pipeline para evitar diferenças entre treino e inferência.
5. [ ] Faça ablação: remova grupos de features e registre quanto cada grupo muda a métrica.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Faça uma alteração controlada em uma feature, modelo, hiperparâmetro ou limiar de **Feature engineering para regressão** e compare usando a mesma validação.
- [ ] Separe alguns erros do modelo por grupo ou tipo de caso e registre onde o desempenho piora e o que investigar.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. Qual prática evita vazamento de dados em uma atividade de **Feature engineering para regressão**?

- [ ] A) Usar a variável-alvo para preencher valores ausentes de todas as colunas.
- [ ] B) Separar treino e teste antes de ajustar transformações, selecionar variáveis ou treinar o modelo.
- [ ] C) Normalizar toda a base antes da separação para usar mais informação.
- [ ] D) Escolher variáveis depois de observar o desempenho no teste.
- [ ] E) Duplicar exemplos raros antes de separar os conjuntos.

2. Como escolher uma métrica adequada para avaliar **Feature engineering para regressão**?

- [ ] A) Usando sempre acurácia, pois ela serve para qualquer problema.
- [ ] B) Escolhendo a métrica que produz o maior número.
- [ ] C) Trocando de métrica depois de ver qual favorece o modelo.
- [ ] D) Avaliando apenas o tempo de treinamento do algoritmo.
- [ ] E) Considerando o tipo de problema, o desbalanceamento e o custo dos diferentes erros para o negócio.

3. Qual procedimento fornece uma comparação mais confiável entre modelos em **Feature engineering para regressão**?

- [ ] A) Consultar repetidamente o teste durante cada ajuste.
- [ ] B) Comparar somente a quantidade de parâmetros dos algoritmos.
- [ ] C) Usar o mesmo protocolo de validação, ajustar decisões no treino e reservar o teste para a avaliação final.
- [ ] D) Testar cada modelo em uma divisão diferente dos dados.
- [ ] E) Escolher pelo desempenho no conjunto usado para treinar.

4. Antes de usar um modelo de **Feature engineering para regressão** em uma decisão real, o que deve ser analisado?

- [ ] A) Erros por segmento, estabilidade, explicabilidade e impacto dos falsos positivos e falsos negativos.
- [ ] B) Somente a métrica média do melhor experimento.
- [ ] C) A aparência dos gráficos de treinamento, sem examinar dados.
- [ ] D) A complexidade do nome do algoritmo escolhido.
- [ ] E) A quantidade de linhas de código usada para criar o modelo.

5. Ordene um fluxo de modelagem para **Feature engineering para regressão**.

- A) Definir o problema, a população, o alvo e a métrica.
- B) Avaliar, analisar erros e relacionar o modelo à decisão.
- C) Separar os dados conforme o contexto do problema.
- D) Treinar um baseline e modelos candidatos.
- E) Ajustar o pré-processamento apenas com os dados de treino.

**Ordem:** `__ → __ → __ → __ → __`

6. Ordene uma seleção responsável de modelo em **Feature engineering para regressão**.

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
**Evidência:** link do commit, notebook, consulta, imagem ou gravação.

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Feature engineering para regressão.
- **Competência sugerida:** Feature Engineering.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Feature Engineering** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

---

## Anotações pessoais



### Conceitos estudados


### Dúvidas


### Erros encontrados e correções


### Aprendizado principal


### Próxima ação

<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 57 — Random Forest — 20/10/2026
> [!abstract] Resultado concreto do dia
> Concluir **Random Forest** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Random Forest.
- **Pasta/arquivo principal:** `semana-12/dia-057-random-forest.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Passo a passo completo
1. [ ] Treine Random Forest variando número de árvores, profundidade e número de features.
2. [ ] Compare variância de uma árvore única com a floresta em cinco seeds.
3. [ ] Calcule importância por impureza e permutation importance; compare rankings.
4. [ ] Meça tempo e tamanho do modelo.
5. [ ] Escolha configuração considerando desempenho, estabilidade e custo de inferência.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Faça uma alteração controlada em uma feature, modelo, hiperparâmetro ou limiar de **Random Forest** e compare usando a mesma validação.
- [ ] Separe alguns erros do modelo por grupo ou tipo de caso e registre onde o desempenho piora e o que investigar.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. Qual prática evita vazamento de dados em uma atividade de **Random Forest**?

- [ ] A) Escolher variáveis depois de observar o desempenho no teste.
- [ ] B) Duplicar exemplos raros antes de separar os conjuntos.
- [ ] C) Usar a variável-alvo para preencher valores ausentes de todas as colunas.
- [ ] D) Separar treino e teste antes de ajustar transformações, selecionar variáveis ou treinar o modelo.
- [ ] E) Normalizar toda a base antes da separação para usar mais informação.

2. Como escolher uma métrica adequada para avaliar **Random Forest**?

- [ ] A) Avaliando apenas o tempo de treinamento do algoritmo.
- [ ] B) Considerando o tipo de problema, o desbalanceamento e o custo dos diferentes erros para o negócio.
- [ ] C) Usando sempre acurácia, pois ela serve para qualquer problema.
- [ ] D) Escolhendo a métrica que produz o maior número.
- [ ] E) Trocando de métrica depois de ver qual favorece o modelo.

3. Qual procedimento fornece uma comparação mais confiável entre modelos em **Random Forest**?

- [ ] A) Testar cada modelo em uma divisão diferente dos dados.
- [ ] B) Escolher pelo desempenho no conjunto usado para treinar.
- [ ] C) Consultar repetidamente o teste durante cada ajuste.
- [ ] D) Comparar somente a quantidade de parâmetros dos algoritmos.
- [ ] E) Usar o mesmo protocolo de validação, ajustar decisões no treino e reservar o teste para a avaliação final.

4. Antes de usar um modelo de **Random Forest** em uma decisão real, o que deve ser analisado?

- [ ] A) A complexidade do nome do algoritmo escolhido.
- [ ] B) A quantidade de linhas de código usada para criar o modelo.
- [ ] C) Erros por segmento, estabilidade, explicabilidade e impacto dos falsos positivos e falsos negativos.
- [ ] D) Somente a métrica média do melhor experimento.
- [ ] E) A aparência dos gráficos de treinamento, sem examinar dados.

5. Ordene um fluxo de modelagem para **Random Forest**.

- A) Avaliar, analisar erros e relacionar o modelo à decisão.
- B) Ajustar o pré-processamento apenas com os dados de treino.
- C) Separar os dados conforme o contexto do problema.
- D) Treinar um baseline e modelos candidatos.
- E) Definir o problema, a população, o alvo e a métrica.

**Ordem:** `__ → __ → __ → __ → __`

6. Ordene uma seleção responsável de modelo em **Random Forest**.

- A) Documentar limitações, segmentos frágeis e regras de uso.
- B) Comparar candidatos com o mesmo protocolo de validação.
- C) Ajustar hiperparâmetros sem consultar o conjunto de teste.
- D) Avaliar uma vez no teste após fechar as escolhas.
- E) Estabelecer um baseline simples e reproduzível.

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

- **Conhecimento praticado hoje:** Random Forest.
- **Competência sugerida:** Random Forest.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Random Forest** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

---

## Anotações pessoais



### Conceitos estudados


### Dúvidas


### Erros encontrados e correções


### Aprendizado principal


### Próxima ação

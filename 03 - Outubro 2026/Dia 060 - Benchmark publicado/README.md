<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 60 — Benchmark publicado — 23/10/2026
> [!abstract] Resultado concreto do dia
> Concluir **Benchmark publicado** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Benchmark publicado.
- **Pasta/arquivo principal:** `semana-12/dia-060-benchmark-publicado/` (pasta do projeto).
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.

### Passo a passo completo
1. [ ] Organize benchmark em script ou notebook reproduzível com configuração central.
2. [ ] Execute no mínimo Dummy, logística, árvore, Random Forest e boosting.
3. [ ] Salve métricas em CSV, gráficos em pasta e parâmetros em JSON.
4. [ ] Crie README com tabela de resultados e três conclusões.
5. [ ] Faça release `v0.1.0` no GitHub e grave apresentação técnica de cinco minutos.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Faça uma alteração controlada em uma feature, modelo, hiperparâmetro ou limiar de **Benchmark publicado** e compare usando a mesma validação.
- [ ] Separe alguns erros do modelo por grupo ou tipo de caso e registre onde o desempenho piora e o que investigar.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. Qual prática evita vazamento de dados em uma atividade de **Benchmark publicado**?

- [ ] A) Separar treino e teste antes de ajustar transformações, selecionar variáveis ou treinar o modelo.
- [ ] B) Normalizar toda a base antes da separação para usar mais informação.
- [ ] C) Escolher variáveis depois de observar o desempenho no teste.
- [ ] D) Duplicar exemplos raros antes de separar os conjuntos.
- [ ] E) Usar a variável-alvo para preencher valores ausentes de todas as colunas.

2. Como escolher uma métrica adequada para avaliar **Benchmark publicado**?

- [ ] A) Escolhendo a métrica que produz o maior número.
- [ ] B) Trocando de métrica depois de ver qual favorece o modelo.
- [ ] C) Avaliando apenas o tempo de treinamento do algoritmo.
- [ ] D) Considerando o tipo de problema, o desbalanceamento e o custo dos diferentes erros para o negócio.
- [ ] E) Usando sempre acurácia, pois ela serve para qualquer problema.

3. Qual procedimento fornece uma comparação mais confiável entre modelos em **Benchmark publicado**?

- [ ] A) Comparar somente a quantidade de parâmetros dos algoritmos.
- [ ] B) Usar o mesmo protocolo de validação, ajustar decisões no treino e reservar o teste para a avaliação final.
- [ ] C) Testar cada modelo em uma divisão diferente dos dados.
- [ ] D) Escolher pelo desempenho no conjunto usado para treinar.
- [ ] E) Consultar repetidamente o teste durante cada ajuste.

4. Antes de usar um modelo de **Benchmark publicado** em uma decisão real, o que deve ser analisado?

- [ ] A) Somente a métrica média do melhor experimento.
- [ ] B) A aparência dos gráficos de treinamento, sem examinar dados.
- [ ] C) A complexidade do nome do algoritmo escolhido.
- [ ] D) A quantidade de linhas de código usada para criar o modelo.
- [ ] E) Erros por segmento, estabilidade, explicabilidade e impacto dos falsos positivos e falsos negativos.

5. Ordene um fluxo de modelagem para **Benchmark publicado**.

- A) Ajustar o pré-processamento apenas com os dados de treino.
- B) Avaliar, analisar erros e relacionar o modelo à decisão.
- C) Definir o problema, a população, o alvo e a métrica.
- D) Treinar um baseline e modelos candidatos.
- E) Separar os dados conforme o contexto do problema.

**Ordem:** `__ → __ → __ → __ → __`

6. Ordene uma seleção responsável de modelo em **Benchmark publicado**.

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
**Evidência:** link do commit, notebook, consulta, imagem ou gravação.

> [!project] Projeto semanal — Seleção de Modelo para Campanha de Retenção com Orçamento Limitado
> **Desafio:** Comparar árvores e ensembles para selecionar clientes de uma campanha de retenção limitada por orçamento, maximizando retorno esperado e controlando falsos positivos.
>
> **Deve reutilizar:** Todo o fluxo de ML das semanas 9–12, calibração, limiar e custo dos erros.
>
> **Entregáveis obrigatórios:**
> - [ ] orçamento, custo por contato, valor esperado de retenção e capacidade máxima definidos;
> - [ ] protocolo de comparação com validação consistente;
> - [ ] tabela de métricas técnicas, custo, retorno esperado, tempo e complexidade;
> - [ ] simulação Top-N para pelo menos três tamanhos de campanha;
> - [ ] explicabilidade e análise de segmentos;
> - [ ] recomendação final justificando modelo, limiar e quantidade de clientes acionados;
>
> **Defesa:** mostrar por que o melhor modelo de negócio pode não ser o modelo com maior AUC e como a restrição orçamentária muda a decisão.
>
> **Nota mínima recomendada:** `6/10`.

> [!check] Critério para avançar
> Você consegue selecionar um modelo com base no retorno esperado da campanha, e não apenas em uma métrica isolada?

---

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Benchmark publicado.
- **Competência sugerida:** Benchmark de modelos.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Benchmark de modelos** na seção Competências. Se a entrega estiver revisada e representar bem seu trabalho, considere incluí-la em Projetos ou Destaques.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

---

## Anotações pessoais



### Conceitos estudados


### Dúvidas


### Erros encontrados e correções


### Aprendizado principal


### Próxima ação

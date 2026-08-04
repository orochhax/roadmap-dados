<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 43 — Pré-processamento com Pipeline — 30/09/2026
> [!abstract] Resultado concreto do dia
> Concluir **Pré-processamento com Pipeline** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Pré-processamento com Pipeline.
- **Pasta/arquivo principal:** `semana-09/dia-043-pre-processamento-com-pipeline.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.
- **Regra:** antes de executar qualquer cálculo ou código importante, anote o resultado que espera obter.

### Passo a passo completo
1. [ ] Identifique colunas numéricas, categóricas e ordinais do conjunto de churn.
2. [ ] Construa `ColumnTransformer` com imputação, padronização e one-hot encoding.
3. [ ] Encapsule transformação e modelo em `Pipeline`; confirme que `fit` ocorre apenas no treino.
4. [ ] Teste categorias inéditas no conjunto de validação usando `handle_unknown='ignore'`.
5. [ ] Salve e recarregue a pipeline; compare previsões antes e depois para garantir igualdade.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Faça uma alteração controlada em uma feature, modelo, hiperparâmetro ou limiar de **Pré-processamento com Pipeline** e compare usando a mesma validação.
- [ ] Separe alguns erros do modelo por grupo ou tipo de caso e registre onde o desempenho piora e o que investigar.

### Perguntas de checagem
1. Por que transformações devem ser ajustadas apenas no treino e encapsuladas em pipeline?

**Resposta:**

2. Em qual exercício de **Pré-processamento com Pipeline** uma implementação errada poderia parecer correta? Dê um exemplo com entrada, saída errada e saída esperada.

**Resposta:**

3. Qual caso de borda você testou, por que ele importa e qual evidência comprova que foi tratado?

**Resposta:**

4. Como o conhecimento de **Pré-processamento com Pipeline** seria usado para apoiar uma decisão real em dados ou IA?

**Resposta:**

5. Que vazamento ou escolha de validação poderia produzir um resultado artificialmente bom neste dia?

**Resposta:**

6. Qual troca entre métricas mudaria a decisão de negócio e por quê?

**Resposta:**

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Commit realizado com mensagem no formato `dia-043: pre-processamento-com-pipeline`.

**Autoavaliação do dia:** `__/5`  
**Evidência:** link do commit, notebook, consulta, imagem ou gravação.

---

## Anotações pessoais

### Resultado esperado antes de executar


### Conceitos estudados


### Dúvidas


### Erros encontrados e correções


### Aprendizado principal


### Próxima ação

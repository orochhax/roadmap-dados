<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 41 — Definição do problema — 28/09/2026
> [!abstract] Resultado concreto do dia
> Concluir **Definição do problema** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Definição do problema.
- **Pasta/arquivo principal:** `semana-09/dia-041-definicao-do-problema.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.
- **Regra:** antes de executar qualquer cálculo ou código importante, anote o resultado que espera obter.

### Passo a passo completo
1. [ ] Escolha um problema binário usando `clientes_telecom.csv`: prever churn nos próximos 30 dias; escreva alvo, unidade de previsão e horizonte temporal.
2. [ ] Defina quem usará a previsão, qual ação será tomada e qual erro é mais caro.
3. [ ] Liste 15 variáveis possíveis e classifique cada uma como disponível, indisponível, sensível ou potencial leakage.
4. [ ] Crie baseline de negócio: prever todos como não churn e comparar com regra simples `chamados_90d >= 3`.
5. [ ] Escreva `problem_statement.md` com objetivo, restrições, métrica primária, métricas secundárias e critério de sucesso.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Faça uma alteração controlada em uma feature, modelo, hiperparâmetro ou limiar de **Definição do problema** e compare usando a mesma validação.
- [ ] Separe alguns erros do modelo por grupo ou tipo de caso e registre onde o desempenho piora e o que investigar.

### Perguntas de checagem
1. Como transformar um pedido vago em alvo, unidade de análise, horizonte e ação mensurável?

**Resposta:**

2. Em qual exercício de **Definição do problema** uma implementação errada poderia parecer correta? Dê um exemplo com entrada, saída errada e saída esperada.

**Resposta:**

3. Qual caso de borda você testou, por que ele importa e qual evidência comprova que foi tratado?

**Resposta:**

4. Como o conhecimento de **Definição do problema** seria usado para apoiar uma decisão real em dados ou IA?

**Resposta:**

5. Que vazamento ou escolha de validação poderia produzir um resultado artificialmente bom neste dia?

**Resposta:**

6. Qual troca entre métricas mudaria a decisão de negócio e por quê?

**Resposta:**

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Commit realizado com mensagem no formato `dia-041: definicao-do-problema`.

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

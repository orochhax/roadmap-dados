<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 27 — Funções de janela — 08/09/2026
> [!abstract] Resultado concreto do dia
> Concluir **Funções de janela** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Funções de janela.
- **Pasta/arquivo principal:** `semana-06/dia-027-funcoes-de-janela.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.
- **Regra:** antes de executar qualquer cálculo ou código importante, anote o resultado que espera obter.

### Passo a passo completo
1. [ ] Use `ROW_NUMBER`, `RANK` e `DENSE_RANK` para ranquear incidentes por impacto dentro de cada cidade; explique diferenças em empates.
2. [ ] Calcule média móvel de sete dias, soma acumulada e diferença para o evento anterior com `LAG`.
3. [ ] Use `LEAD` para calcular tempo até o próximo incidente da mesma cidade.
4. [ ] Selecione o top 3 por cidade sem perder empates relevantes.
5. [ ] Compare uma solução com função de janela a outra com `GROUP BY` e explique por que elas respondem perguntas diferentes.

### Verificação prática sem consulta
- [ ] Escreva do zero uma consulta que use o principal recurso de **Funções de janela** e responda uma pergunta nova.
- [ ] Valide o resultado por contagem manual em uma amostra de 5–10 linhas ou por pandas.
- [ ] Explique a granularidade do resultado e o risco de duplicação.

### Perguntas de checagem
1. Qual a diferença entre agregar linhas e usar uma função de janela sem perder granularidade?

**Resposta:**

2. Em qual exercício de **Funções de janela** uma implementação errada poderia parecer correta? Dê um exemplo com entrada, saída errada e saída esperada.

**Resposta:**

3. Qual caso de borda você testou, por que ele importa e qual evidência comprova que foi tratado?

**Resposta:**

4. Como o conhecimento de **Funções de janela** seria usado para apoiar uma decisão real em dados ou IA?

**Resposta:**

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Commit realizado com mensagem no formato `dia-027: funcoes-de-janela`.

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

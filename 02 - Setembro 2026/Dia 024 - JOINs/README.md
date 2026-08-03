<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 24 — JOINs — 03/09/2026
> [!abstract] Resultado concreto do dia
> Concluir **JOINs** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** JOINs.
- **Pasta/arquivo principal:** `semana-05/dia-024-joins.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.
- **Regra:** antes de executar qualquer cálculo ou código importante, anote o resultado que espera obter.

### Passo a passo completo
1. [ ] Crie tabelas `clientes`, `planos`, `chamados` e `pagamentos` com chaves primárias e estrangeiras; importe dados do kit.
2. [ ] Escreva um `INNER JOIN` para clientes com plano, um `LEFT JOIN` para encontrar clientes sem pagamentos e um anti-join para planos sem clientes.
3. [ ] Crie um caso muitos-para-muitos acidental duplicando chaves; meça como isso infla soma de mensalidade.
4. [ ] Corrija o problema agregando antes do join ou validando cardinalidade.
5. [ ] Desenhe em Mermaid ou texto o relacionamento entre as quatro tabelas e anote a granularidade de cada uma.

### Verificação prática sem consulta
- [ ] Escreva do zero uma consulta que use o principal recurso de **JOINs** e responda uma pergunta nova.
- [ ] Valide o resultado por contagem manual em uma amostra de 5–10 linhas ou por pandas.
- [ ] Explique a granularidade do resultado e o risco de duplicação.

### Perguntas de checagem
1. Qual a diferença entre `INNER`, `LEFT`, `RIGHT` e `FULL JOIN`, e como detectar multiplicação de linhas?

**Resposta:**

2. Em qual exercício de **JOINs** uma implementação errada poderia parecer correta? Dê um exemplo com entrada, saída errada e saída esperada.

**Resposta:**

3. Qual caso de borda você testou, por que ele importa e qual evidência comprova que foi tratado?

**Resposta:**

4. Como o conhecimento de **JOINs** seria usado para apoiar uma decisão real em dados ou IA?

**Resposta:**

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] O diário registra erro principal, correção, aprendizado e próxima lacuna.
- [ ] Commit realizado com mensagem no formato `dia-024: joins`.

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

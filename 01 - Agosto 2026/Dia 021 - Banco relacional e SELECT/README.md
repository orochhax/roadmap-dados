<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 21 — Banco relacional e SELECT — 31/08/2026
> [!abstract] Resultado concreto do dia
> Concluir **Banco relacional e SELECT** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Banco relacional e SELECT.
- **Pasta/arquivo principal:** `semana-05/dia-021-banco-relacional-e-select.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.
- **Regra:** antes de executar qualquer cálculo ou código importante, anote o resultado que espera obter.

### Passo a passo completo
1. [ ] Instale PostgreSQL ou use DuckDB; crie banco `roadmap_ds` e tabela `incidentes` com chave primária e tipos apropriados.
2. [ ] Importe `incidentes.csv` e execute 12 consultas `SELECT`: todas as colunas; colunas específicas; alias; `DISTINCT`; limite; ordenação crescente/decrescente; expressão calculada; concatenação; `COALESCE`; `CAST`; `CASE`; contagem total.
3. [ ] Antes de cada consulta, escreva em comentário quantas linhas e colunas espera receber.
4. [ ] Crie uma consulta que calcule `impacto = duracao_min * clientes_afetados` e liste os cinco maiores.
5. [ ] Salve tudo em `03-sql/dia21/select_basico.sql` e exporte os resultados principais para CSV.

### Verificação prática sem consulta
- [ ] Escreva do zero uma consulta que use o principal recurso de **Banco relacional e SELECT** e responda uma pergunta nova.
- [ ] Valide o resultado por contagem manual em uma amostra de 5–10 linhas ou por pandas.
- [ ] Explique a granularidade do resultado e o risco de duplicação.

### Perguntas de checagem
1. Qual a função de chave primária e chave estrangeira, e por que normalização importa?

**Resposta:**

2. Em qual exercício de **Banco relacional e SELECT** uma implementação errada poderia parecer correta? Dê um exemplo com entrada, saída errada e saída esperada.

**Resposta:**

3. Qual caso de borda você testou, por que ele importa e qual evidência comprova que foi tratado?

**Resposta:**

4. Como o conhecimento de **Banco relacional e SELECT** seria usado para apoiar uma decisão real em dados ou IA?

**Resposta:**

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Commit realizado com mensagem no formato `dia-021: banco-relacional-e-select`.

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

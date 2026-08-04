<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 22 — Filtros e funções — 01/09/2026
> [!abstract] Resultado concreto do dia
> Concluir **Filtros e funções** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Filtros e funções.
- **Pasta/arquivo principal:** `semana-05/dia-022-filtros-e-funcoes.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.
- **Regra:** antes de executar qualquer cálculo ou código importante, anote o resultado que espera obter.

### Passo a passo completo
1. [ ] Escreva 15 consultas usando `WHERE`: igualdade, diferença, maior/menor, `BETWEEN`, `IN`, `LIKE`, `IS NULL`, `AND`, `OR` e `NOT`.
2. [ ] Crie filtros de negócio: P1 não resolvido; incidentes acima de 120 minutos; cidades com mais de 100 clientes afetados; causas contendo `fibra`.
3. [ ] Use funções de texto para padronizar cidade, funções numéricas para arredondar impacto e funções nulas para substituir valores ausentes.
4. [ ] Construa três consultas logicamente equivalentes com parênteses diferentes e explique por que uma delas retorna linhas erradas.
5. [ ] Teste limites exatos 50/51, 120/121 e datas de início/fim; registre os casos inclusivos e exclusivos.

### Verificação prática sem consulta
- [ ] Escreva do zero uma consulta que use o principal recurso de **Filtros e funções** e responda uma pergunta nova.
- [ ] Valide o resultado por contagem manual em uma amostra de 5–10 linhas ou por pandas.
- [ ] Explique a granularidade do resultado e o risco de duplicação.

### Perguntas de checagem
1. Como `NULL` se comporta em filtros SQL e por que `= NULL` não funciona como esperado?

**Resposta:**

2. Em qual exercício de **Filtros e funções** uma implementação errada poderia parecer correta? Dê um exemplo com entrada, saída errada e saída esperada.

**Resposta:**

3. Qual caso de borda você testou, por que ele importa e qual evidência comprova que foi tratado?

**Resposta:**

4. Como o conhecimento de **Filtros e funções** seria usado para apoiar uma decisão real em dados ou IA?

**Resposta:**

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Commit realizado com mensagem no formato `dia-022: filtros-e-funcoes`.

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

# Agregacoes + JOINs

**Data de estudo:** 18/09/2026  
**Carga planejada:** 4 a 5 horas

## Como estudar

Você pode escolher vídeo, documentação, site ou IA. Pesquise os nomes abaixo, faça uma primeira tentativa sem solução pronta e guarde evidência executável.

## Assuntos para pesquisar

### Bloco 1 — Agregacoes

Pesquise exatamente:

- `Agregacoes Python explicado passo a passo`
- `Agregacoes Python exercícios práticos`

Depois siga o [guia e os enunciados deste bloco](<modulos/01-e29/README.md>). Tente os exercícios antes de procurar uma implementação completa.

### Bloco 2 — JOINs

Pesquise exatamente:

- `JOINs SQL para análise de dados explicado passo a passo`
- `JOINs SQL para análise de dados exercícios práticos`

Depois siga o [guia e os enunciados deste bloco](<modulos/02-e30/README.md>). Tente os exercícios antes de procurar uma implementação completa.

## Integração

Explique com suas palavras como os blocos se conectam em um fluxo de dados ou decisão. Execute um caso comum e um caso de borda de cada bloco e registre comandos, saídas e dúvidas nas evidências.

## Publicação da semana no LinkedIn

- **Tema específico:** como agregações e JOINs transformam tabelas de clientes, incidentes e pagamentos em uma métrica reconciliada.
- **Tipo:** progresso.
- **Formato:** carrossel técnico com diagrama simples das tabelas, trecho da consulta, resultado e conferência manual.
- **Artefato/evidência exigida:** `dia-023-agregacoes.sql` e `dia-024-joins.sql` executados, contagem antes/depois do JOIN, chaves sem correspondência identificadas e uma métrica conferida em amostra pequena.

### Roteiro para preencher

- **Pergunta:** [qual métrica ou lista a consulta responde?]
- **Tabelas e grão:** [o que representa uma linha em cada tabela?]
- **JOIN escolhido:** [INNER, LEFT ou outro e por que preserva o conjunto correto?]
- **Agregação:** [qual agrupamento e denominador foram usados?]
- **Resultado verificável:** [valor, consulta e saída que o comprovam]
- **Conferência:** [qual amostra foi calculada manualmente?]
- **Caso de borda:** [chave ausente, duplicada ou valor nulo e tratamento]

### Limitação obrigatória

Declare que a consulta foi testada em uma base pequena e que ainda não comprova desempenho, modelagem dimensional completa ou comportamento em escala.

### Cuidado contra afirmações falsas

Não declare domínio avançado de SQL nem otimização sem plano de execução e benchmark. Não esconda linhas perdidas por JOIN. A publicação não libera Competências ou headline antes do marco central.

### Checklist de publicação

- [ ] Executei as consultas e salvei o resultado usado no post.
- [ ] Registrei grão, chave e tipo de JOIN.
- [ ] Conferi contagens antes/depois e linhas sem correspondência.
- [ ] Recalculei manualmente uma métrica.
- [ ] Removi dados sensíveis e testei o link compartilhado.
- [ ] **URL publicada:**
- [ ] **Data da publicação:**

## Concluído quando

- [ ] Estudei todos os assuntos e concluí os enunciados dos blocos sem copiar uma solução completa.
- [ ] Executei os artefatos, testei casos de borda e registrei resultados verificáveis.
- [ ] Expliquei a conexão entre os blocos, a decisão tomada e pelo menos uma limitação concreta.

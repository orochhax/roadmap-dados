# Agregacoes + JOINs

**Data de estudo:** 18/09/2026  
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Agregacoes

#### O que pesquisar
- `Agregacoes Python explicado passo a passo`
- `Agregacoes Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-agregacoes`](<atividades/01-agregacoes/>)

#### Aula guiada — Curso MySQL

- [ ] #13 — **SELECT, parte 3** (29:11).
- Depois da aula, use o conjunto de dados do roadmap; exemplos copiados da base do curso não contam como prática.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-agregacoes/dia-023-agregacoes.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

#### O que fazer

- [ ] Escreva uma consulta de resumo que contenha `COUNT`, `SUM`, `AVG`, `MIN` e `MAX` para a tabela de incidentes, em vez de repetir uma consulta isolada para cada função.
- [ ] Agrupe por cidade, causa e severidade; calcule quantidade, duração média, clientes totais e percentual resolvido.
- [ ] Use `HAVING` para manter apenas cidades com pelo menos cinco incidentes e duração média acima de 60.

- [ ] Calcule taxa de resolução com proteção contra divisão por zero e compare resultado com pandas.
- [ ] **Em `atividades/01-agregacoes/dia-023-agregacoes.sql`:** Agrupe por cidade e mantenha apenas grupos com pelo menos 10 incidentes e duração média acima de 90 minutos.
- [ ] **Em `atividades/01-agregacoes/dia-023-agregacoes.sql`:** Escolha uma cidade do resultado e confira em outra consulta COUNT, SUM(duracao_min) e AVG(duracao_min) sem usar o agrupamento final.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

### Atividade 2 — JOINs

#### O que pesquisar
- `JOINs SQL para análise de dados explicado passo a passo`
- `JOINs SQL para análise de dados exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-joins`](<atividades/02-joins/>)

#### O que você precisa entender

Um anti-join retorna linhas sem correspondência. Antes de combinar tabelas, declare se cada chave é única e confira a quantidade de linhas.

```sql
SELECT c.id
FROM clientes AS c
LEFT JOIN pagamentos AS p ON p.cliente_id = c.id
WHERE p.cliente_id IS NULL;
```

**Erro comum:** juntar duas tabelas com várias linhas por cliente e somar valores duplicados; agregue antes ou valide a cardinalidade.

#### Aulas guiadas — Curso MySQL

- [ ] #14 — **Modelo Relacional** (40:25).
- [ ] #15 — **Chaves Estrangeiras e JOIN** (40:44).
- **Carga:** 1h21. As duas aulas cobrem o necessário para a prática abaixo.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-joins/dia-024-joins.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

#### O que fazer

- [ ] Crie tabelas `clientes`, `planos`, `chamados` e `pagamentos` com chaves primárias e estrangeiras; importe dados do kit.
- [ ] Como o `INNER JOIN` simples já foi praticado no curso, escreva um `LEFT JOIN` para encontrar clientes sem pagamentos e um anti-join para planos sem clientes.
- [ ] Crie um caso muitos-para-muitos acidental duplicando chaves; meça como isso infla soma de mensalidade.

- [ ] Corrija o problema agregando antes do join ou validando cardinalidade.
- [ ] Desenhe em Mermaid ou texto o relacionamento entre as quatro tabelas e anote a granularidade de cada uma.
- [ ] **Em `atividades/02-joins/dia-024-joins.sql`:** Conte linhas e clientes distintos antes e depois do join com pagamentos para revelar qualquer multiplicação de registros.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

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

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

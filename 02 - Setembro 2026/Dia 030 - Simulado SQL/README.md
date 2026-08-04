<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 30 — Simulado SQL — 11/09/2026
> [!abstract] Resultado concreto do dia
> Concluir **Simulado SQL** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Simulado SQL.
- **Pasta/arquivo principal:** `semana-06/dia-030-simulado-sql/` (pasta do projeto).
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

### Passo a passo completo
1. [ ] Resolva um simulado cronometrado com 20 questões: cinco filtros, quatro agregações, quatro joins, três CTEs, duas janelas e duas datas.
2. [ ] Use os arquivos `simulado_sql_perguntas.md` e `simulado_sql_respostas.sql`; não abra respostas durante os primeiros 90 minutos.
3. [ ] Para cada questão, marque tempo, confiança de 1–5 e se precisou consultar documentação.
4. [ ] Escolha as cinco piores respostas e reescreva do zero no fim do dia.
5. [ ] Crie uma folha de erros com categoria, causa, correção e regra que evitará repetição.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Escreva uma consulta adicional sobre **Simulado SQL** que responda a uma pergunta de negócio diferente usando as mesmas tabelas.
- [ ] Crie uma consulta de validação para conferir nulos, duplicidades, cardinalidade ou totais antes de aceitar o resultado principal.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. Antes de escrever uma consulta de **Simulado SQL**, o que deve ser definido primeiro?

- [ ] A) A pergunta de negócio, a métrica e a granularidade que cada linha da saída deve representar.
- [ ] B) A quantidade máxima de linhas que caberá na tela.
- [ ] C) A ordem alfabética dos nomes das tabelas.
- [ ] D) O uso obrigatório de todas as colunas disponíveis.
- [ ] E) A formatação visual da tabela final antes dos cálculos.

2. Qual cuidado é essencial ao usar junções em uma atividade de **Simulado SQL**?

- [ ] A) Juntar tabelas por qualquer coluna com o mesmo tipo.
- [ ] B) Remover duplicidades depois da junção sem investigar a origem.
- [ ] C) Selecionar todas as colunas para garantir que nada seja perdido.
- [ ] D) Conferir as chaves e a cardinalidade para evitar perda ou multiplicação indevida de linhas.
- [ ] E) Usar sempre `INNER JOIN`, independentemente da pergunta.

3. Como valores NULL devem ser tratados em consultas relacionadas a **Simulado SQL**?

- [ ] A) Ignorando-os, pois bancos relacionais os convertem sozinhos.
- [ ] B) De acordo com o significado do campo, distinguindo ausência de dado de um valor numérico ou textual válido.
- [ ] C) Sempre como zero, porque simplifica as agregações.
- [ ] D) Sempre como texto vazio, mesmo em colunas numéricas.
- [ ] E) Excluindo automaticamente todas as linhas que contenham `NULL`.

4. Qual verificação aumenta mais a confiança em uma consulta de **Simulado SQL**?

- [ ] A) Executar a consulta apenas uma vez sem mensagem de erro.
- [ ] B) Adicionar `ORDER BY` para que os números pareçam organizados.
- [ ] C) Limitar a saída a dez linhas e assumir que o restante está correto.
- [ ] D) Trocar nomes de aliases sem conferir os valores calculados.
- [ ] E) Comparar contagens e totais, inspecionar amostras e validar a lógica em partes menores.

5. Ordene a construção de uma consulta para **Simulado SQL**.

- A) Definir a pergunta, a métrica e a granularidade.
- B) Montar filtros e junções da base da consulta.
- C) Identificar tabelas, campos e chaves necessárias.
- D) Aplicar agregações, janelas ou transformações necessárias.
- E) Validar contagens, totais e algumas linhas manualmente.

**Ordem:** `__ → __ → __ → __ → __`

6. Ordene a investigação de uma consulta incorreta em **Simulado SQL**.

- A) Reproduzir o problema com um recorte pequeno.
- B) Executar separadamente cada etapa ou CTE.
- C) Executar a consulta completa e registrar a causa do erro.
- D) Corrigir a etapa que altera os dados indevidamente.
- E) Conferir chaves, duplicidades, filtros e contagens.

**Ordem:** `__ → __ → __ → __ → __`

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Alterações registradas em commit e enviadas ao GitHub.

**Autoavaliação do dia:** `__/5`  
**Evidência:** link do commit, notebook, consulta, imagem ou gravação.

> [!todo] PUBLICAR NO LINKEDIN — projeto prioritário do portfólio
> - [ ] Publique somente após README, resultados e limitações estarem revisados.
> - [ ] Inclua problema, abordagem, principal evidência, decisão e link do GitHub.
> - [ ] **Ângulo sugerido:** mostrar como SQL analítico revela quando clientes abandonam, quais cohorts retêm melhor e onde está a receita.

> [!project] Projeto semanal — Cohorts, retenção e receita
> **Desafio:** Analisar aquisição, retenção e receita de clientes ao longo do tempo usando SQL analítico.
>
> **Deve reutilizar:** SQL básico, CTEs, janelas, datas e cohorts.
>
> **Entregáveis obrigatórios:**
> - [ ] consultas reproduzíveis;
> - [ ] matriz de cohort;
> - [ ] ranking de segmentos;
> - [ ] explicação de limitações;
>
> **Defesa:** demonstração de cinco minutos e resposta a três perguntas técnicas.
>
> **Nota mínima recomendada:** `6/10`.

> [!check] Critério para avançar
> Você consegue resolver JOINs, CTEs, datas, cohorts e janelas sob limite de tempo?

---

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Simulado SQL.
- **Competência sugerida:** SQL analítico.
- **Ação recomendada:** Após concluir todas as atividades do dia, atualize o título profissional e adicione ou reforce **SQL analítico** na seção Competências. Se a entrega estiver revisada e apresentável, inclua-a também em Projetos ou Destaques.
- **Novo título sugerido:** `Engenharia de Software | Análise de Dados | Python, SQL e Power BI`.
- **Próximo marco do perfil:** Dia 65 — Engenharia de Software | Ciência de Dados | Python, SQL, Power BI e Machine Learning.

---

## Anotações pessoais



### Conceitos estudados


### Dúvidas


### Erros encontrados e correções


### Aprendizado principal


### Próxima ação

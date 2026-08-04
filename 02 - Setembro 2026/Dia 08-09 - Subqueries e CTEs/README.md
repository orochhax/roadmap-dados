<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 26 — Subqueries e CTEs — 07/09/2026
> [!abstract] Resultado concreto do dia
> Concluir **Subqueries e CTEs** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Subqueries e CTEs.
- **Pasta/arquivo principal:** `semana-06/dia-026-subqueries-e-ctes.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

### Passo a passo completo
1. [ ] Escreva uma subquery escalar para comparar cada incidente à duração média geral.
2. [ ] Escreva uma subquery correlacionada para identificar incidentes acima da média de sua própria cidade.
3. [ ] Reescreva ambas usando CTEs e compare legibilidade.
4. [ ] Crie uma sequência de três CTEs: dados válidos → métricas por cidade → ranking final.
5. [ ] Introduza um filtro em posição errada e demonstre como ele altera o denominador de uma taxa.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Escreva uma consulta adicional sobre **Subqueries e CTEs** que responda a uma pergunta de negócio diferente usando as mesmas tabelas.
- [ ] Crie uma consulta de validação para conferir nulos, duplicidades, cardinalidade ou totais antes de aceitar o resultado principal.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Escreva uma subquery escalar para comparar cada incidente à duração média geral.

   **Pergunta:** Antes de escrever uma consulta de **Subqueries e CTEs**, o que deve ser definido primeiro?

- [ ] A) A quantidade máxima de linhas que caberá na tela.
- [ ] B) A ordem alfabética dos nomes das tabelas.
- [ ] C) O uso obrigatório de todas as colunas disponíveis.
- [ ] D) A formatação visual da tabela final antes dos cálculos.
- [ ] E) A pergunta de negócio, a métrica e a granularidade que cada linha da saída deve representar.

2. **Referência — atividade 2:** Escreva uma subquery correlacionada para identificar incidentes acima da média de sua própria cidade.

   **Pergunta:** Qual cuidado é essencial ao usar junções em uma atividade de **Subqueries e CTEs**?

- [ ] A) Remover duplicidades depois da junção sem investigar a origem.
- [ ] B) Selecionar todas as colunas para garantir que nada seja perdido.
- [ ] C) Conferir as chaves e a cardinalidade para evitar perda ou multiplicação indevida de linhas.
- [ ] D) Usar sempre `INNER JOIN`, independentemente da pergunta.
- [ ] E) Juntar tabelas por qualquer coluna com o mesmo tipo.

3. **Referência — atividade 3:** Reescreva ambas usando CTEs e compare legibilidade.

   **Pergunta:** Como valores NULL devem ser tratados em consultas relacionadas a **Subqueries e CTEs**?

- [ ] A) De acordo com o significado do campo, distinguindo ausência de dado de um valor numérico ou textual válido.
- [ ] B) Sempre como zero, porque simplifica as agregações.
- [ ] C) Sempre como texto vazio, mesmo em colunas numéricas.
- [ ] D) Excluindo automaticamente todas as linhas que contenham `NULL`.
- [ ] E) Ignorando-os, pois bancos relacionais os convertem sozinhos.

4. **Referência — atividade 4:** Crie uma sequência de três CTEs: dados válidos → métricas por cidade → ranking final.

   **Pergunta:** Qual verificação aumenta mais a confiança em uma consulta de **Subqueries e CTEs**?

- [ ] A) Adicionar `ORDER BY` para que os números pareçam organizados.
- [ ] B) Limitar a saída a dez linhas e assumir que o restante está correto.
- [ ] C) Trocar nomes de aliases sem conferir os valores calculados.
- [ ] D) Comparar contagens e totais, inspecionar amostras e validar a lógica em partes menores.
- [ ] E) Executar a consulta apenas uma vez sem mensagem de erro.

5. **Referência — atividade 5:** Introduza um filtro em posição errada e demonstre como ele altera o denominador de uma taxa.

   **Pergunta:** Ordene a construção de uma consulta para **Subqueries e CTEs**.

- A) Validar contagens, totais e algumas linhas manualmente.
- B) Identificar tabelas, campos e chaves necessárias.
- C) Montar filtros e junções da base da consulta.
- D) Aplicar agregações, janelas ou transformações necessárias.
- E) Definir a pergunta, a métrica e a granularidade.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene a investigação de uma consulta incorreta em **Subqueries e CTEs**.

- A) Reproduzir o problema com um recorte pequeno.
- B) Conferir chaves, duplicidades, filtros e contagens.
- C) Executar separadamente cada etapa ou CTE.
- D) Executar a consulta completa e registrar a causa do erro.
- E) Corrigir a etapa que altera os dados indevidamente.

**Ordem:** `__ → __ → __ → __ → __`

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Alterações registradas em commit e enviadas ao GitHub.

**Autoavaliação do dia:** `__/5`  

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Subqueries e CTEs.
- **Competência sugerida:** CTEs e subqueries em SQL.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **CTEs e subqueries em SQL** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python e Power BI`.
- **Próximo marco do perfil:** Dia 30 — Engenharia de Software | Análise de Dados | Python, SQL e Power BI.

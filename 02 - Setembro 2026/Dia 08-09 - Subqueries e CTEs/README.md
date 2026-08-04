<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 26 — Subqueries e CTEs — 07/09/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Subqueries e CTEs.
- **Competência sugerida:** CTEs e subqueries em SQL.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **CTEs e subqueries em SQL** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python e Power BI`.
- **Próximo marco do perfil:** Dia 30 — Engenharia de Software | Análise de Dados | Python, SQL e Power BI.

> [!abstract] Resultado concreto do dia
> Concluir **Subqueries e CTEs** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Subqueries e CTEs.
- **Pasta/arquivo principal:** `01-exercicios/dia-026-subqueries-e-ctes.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Escreva uma subquery escalar para comparar cada incidente à duração média geral.
2. [ ] Escreva uma subquery correlacionada para identificar incidentes acima da média de sua própria cidade.
3. [ ] Reescreva ambas usando CTEs e compare legibilidade.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Crie uma sequência de três CTEs: dados válidos → métricas por cidade → ranking final.
- [ ] Introduza um filtro em posição errada e demonstre como ele altera o denominador de uma taxa.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-026-subqueries-e-ctes.sql`:** Crie uma CTE que filtre P1/P2, outra que agregue impacto por cidade e uma terceira que retorne as três cidades de maior impacto.
- [ ] **Em `01-exercicios/dia-026-subqueries-e-ctes.sql`:** Mova o filtro de resolvido entre a primeira e a segunda CTE e registre como o denominador da taxa muda nas duas versões.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Qual cuidado é essencial ao usar junções em uma atividade de **Subqueries e CTEs**?

- [ ] A) Remover duplicidades depois da junção sem investigar a origem.
- [ ] B) Selecionar todas as colunas para garantir que nada seja perdido.
- [ ] C) Conferir as chaves e a cardinalidade para evitar perda ou multiplicação indevida de linhas.
- [ ] D) Usar sempre `INNER JOIN`, independentemente da pergunta.
- [ ] E) Juntar tabelas por qualquer coluna com o mesmo tipo.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Como valores NULL devem ser tratados em consultas relacionadas a **Subqueries e CTEs**?

- [ ] A) De acordo com o significado do campo, distinguindo ausência de dado de um valor numérico ou textual válido.
- [ ] B) Sempre como zero, porque simplifica as agregações.
- [ ] C) Sempre como texto vazio, mesmo em colunas numéricas.
- [ ] D) Excluindo automaticamente todas as linhas que contenham `NULL`.
- [ ] E) Ignorando-os, pois bancos relacionais os convertem sozinhos.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene a construção de uma consulta para **Subqueries e CTEs**.

- A) Validar contagens, totais e algumas linhas manualmente.
- B) Identificar tabelas, campos e chaves necessárias.
- C) Montar filtros e junções da base da consulta.
- D) Aplicar agregações, janelas ou transformações necessárias.
- E) Definir a pergunta, a métrica e a granularidade.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`

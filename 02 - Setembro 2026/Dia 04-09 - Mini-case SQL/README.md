<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 25 — Mini-case SQL — 04/09/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Mini-case SQL.
- **Competência sugerida:** SQL aplicado a negócios.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **SQL aplicado a negócios** na seção Competências. Se a entrega estiver revisada e representar bem seu trabalho, considere incluí-la em Projetos ou Destaques.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python e Power BI`.
- **Próximo marco do perfil:** Dia 30 — Engenharia de Software | Análise de Dados | Python, SQL e Power BI.

> [!abstract] Resultado concreto do dia
> Concluir **Mini-case SQL** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 4–5 horas; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Mini-case SQL.
- **Pasta/arquivo principal:** `projeto-semanal/docs/case_sql_semana05.md`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Escolha três das cinco perguntas do mini-case e responda usando apenas `SELECT`, filtros, agregações e JOINs já estudados.
2. [ ] Valide um indicador em pandas ou por uma segunda consulta mais simples.
3. [ ] Entregue `case_sql_semana05.md` com pergunta, consulta, resultado, interpretação e uma limitação para cada resposta.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Responda as outras duas perguntas somente se as três primeiras estiverem claras.
- [ ] CTEs e subqueries não são requisito deste dia; elas serão ensinadas no Dia 26.
- [ ] Otimização e plano de execução são desafios posteriores.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `projeto-semanal/docs/case_sql_semana05.md`:** Calcule churn por cidade somente para cidades com pelo menos 30 clientes e ordene pela maior taxa.
- [ ] **Em `projeto-semanal/docs/case_sql_semana05.md`:** Reproduza em pandas a contagem e a taxa da primeira cidade do ranking usando exatamente o mesmo filtro SQL.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Qual cuidado é essencial ao usar junções em uma atividade de **Mini-case SQL**?

- [ ] A) Juntar tabelas por qualquer coluna com o mesmo tipo.
- [ ] B) Remover duplicidades depois da junção sem investigar a origem.
- [ ] C) Selecionar todas as colunas para garantir que nada seja perdido.
- [ ] D) Conferir as chaves e a cardinalidade para evitar perda ou multiplicação indevida de linhas.
- [ ] E) Usar sempre `INNER JOIN`, independentemente da pergunta.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Como valores NULL devem ser tratados em consultas relacionadas a **Mini-case SQL**?

- [ ] A) Ignorando-os, pois bancos relacionais os convertem sozinhos.
- [ ] B) De acordo com o significado do campo, distinguindo ausência de dado de um valor numérico ou textual válido.
- [ ] C) Sempre como zero, porque simplifica as agregações.
- [ ] D) Sempre como texto vazio, mesmo em colunas numéricas.
- [ ] E) Excluindo automaticamente todas as linhas que contenham `NULL`.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene a construção de uma consulta para **Mini-case SQL**.

- A) Montar filtros e junções da base da consulta.
- B) Identificar tabelas, campos e chaves necessárias.
- C) Validar contagens, totais e algumas linhas manualmente.
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



---

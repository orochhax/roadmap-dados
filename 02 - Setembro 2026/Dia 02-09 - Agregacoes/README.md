<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 23 — Agregações — 02/09/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Agregações.
- **Competência sugerida:** Agregações em SQL.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Agregações em SQL** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python e Power BI`.
- **Próximo marco do perfil:** Dia 30 — Engenharia de Software | Análise de Dados | Python, SQL e Power BI.

> [!abstract] Resultado concreto do dia
> Concluir **Agregações** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Agregações.
- **Pasta/arquivo principal:** `01-exercicios/dia-023-agregacoes.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Escreva consultas com `COUNT`, `SUM`, `AVG`, `MIN` e `MAX` para a tabela de incidentes.
2. [ ] Agrupe por cidade, causa e severidade; calcule quantidade, duração média, clientes totais e percentual resolvido.
3. [ ] Use `HAVING` para manter apenas cidades com pelo menos cinco incidentes e duração média acima de 60.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Calcule taxa de resolução com proteção contra divisão por zero e compare resultado com pandas.
- [ ] Crie uma tabela de validação manual para duas cidades e confirme os agregados linha por linha.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-023-agregacoes.sql`:** Agrupe por cidade e mantenha apenas grupos com pelo menos 10 incidentes e duração média acima de 90 minutos.
- [ ] **Em `01-exercicios/dia-023-agregacoes.sql`:** Escolha uma cidade do resultado e confira em outra consulta COUNT, SUM(duracao_min) e AVG(duracao_min) sem usar o agrupamento final.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Qual cuidado é essencial ao usar junções em uma atividade de **Agregações**?

- [ ] A) Conferir as chaves e a cardinalidade para evitar perda ou multiplicação indevida de linhas.
- [ ] B) Usar sempre `INNER JOIN`, independentemente da pergunta.
- [ ] C) Juntar tabelas por qualquer coluna com o mesmo tipo.
- [ ] D) Remover duplicidades depois da junção sem investigar a origem.
- [ ] E) Selecionar todas as colunas para garantir que nada seja perdido.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Como valores NULL devem ser tratados em consultas relacionadas a **Agregações**?

- [ ] A) Sempre como texto vazio, mesmo em colunas numéricas.
- [ ] B) Excluindo automaticamente todas as linhas que contenham `NULL`.
- [ ] C) Ignorando-os, pois bancos relacionais os convertem sozinhos.
- [ ] D) De acordo com o significado do campo, distinguindo ausência de dado de um valor numérico ou textual válido.
- [ ] E) Sempre como zero, porque simplifica as agregações.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene a construção de uma consulta para **Agregações**.

- A) Validar contagens, totais e algumas linhas manualmente.
- B) Identificar tabelas, campos e chaves necessárias.
- C) Definir a pergunta, a métrica e a granularidade.
- D) Aplicar agregações, janelas ou transformações necessárias.
- E) Montar filtros e junções da base da consulta.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`

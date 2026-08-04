<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 28 — Datas e análise temporal — 09/09/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Datas e análise temporal.
- **Competência sugerida:** Análise temporal com SQL.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Análise temporal com SQL** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python e Power BI`.
- **Próximo marco do perfil:** Dia 30 — Engenharia de Software | Análise de Dados | Python, SQL e Power BI.

> [!abstract] Resultado concreto do dia
> Concluir **Datas e análise temporal** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Datas e análise temporal.
- **Pasta/arquivo principal:** `01-exercicios/dia-028-datas-e-analise-temporal.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Converta colunas de texto em data/hora e extraia ano, mês, semana, dia da semana e hora.
2. [ ] Calcule incidentes e duração média por dia, semana e mês.
3. [ ] Meça tempo entre abertura e fechamento e classifique SLA em `no prazo` ou `atrasado`.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Crie calendário completo e faça `LEFT JOIN` para exibir dias sem eventos com zero.
- [ ] Teste virada de mês, ano bissexto, horário nulo e eventos abertos; documente decisões.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-028-datas-e-analise-temporal.sql`:** Gere um calendário de 01/07/2026 a 31/07/2026 e mostre zero nos dias sem incidentes.
- [ ] **Em `01-exercicios/dia-028-datas-e-analise-temporal.sql`:** Inclua na análise um evento sem data de fechamento e classifique-o separadamente, sem calcular uma duração falsa.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Qual cuidado é essencial ao usar junções em uma atividade de **Datas e análise temporal**?

- [ ] A) Conferir as chaves e a cardinalidade para evitar perda ou multiplicação indevida de linhas.
- [ ] B) Usar sempre `INNER JOIN`, independentemente da pergunta.
- [ ] C) Juntar tabelas por qualquer coluna com o mesmo tipo.
- [ ] D) Remover duplicidades depois da junção sem investigar a origem.
- [ ] E) Selecionar todas as colunas para garantir que nada seja perdido.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Como valores NULL devem ser tratados em consultas relacionadas a **Datas e análise temporal**?

- [ ] A) Sempre como texto vazio, mesmo em colunas numéricas.
- [ ] B) Excluindo automaticamente todas as linhas que contenham `NULL`.
- [ ] C) Ignorando-os, pois bancos relacionais os convertem sozinhos.
- [ ] D) De acordo com o significado do campo, distinguindo ausência de dado de um valor numérico ou textual válido.
- [ ] E) Sempre como zero, porque simplifica as agregações.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene a construção de uma consulta para **Datas e análise temporal**.

- A) Montar filtros e junções da base da consulta.
- B) Identificar tabelas, campos e chaves necessárias.
- C) Definir a pergunta, a métrica e a granularidade.
- D) Aplicar agregações, janelas ou transformações necessárias.
- E) Validar contagens, totais e algumas linhas manualmente.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`

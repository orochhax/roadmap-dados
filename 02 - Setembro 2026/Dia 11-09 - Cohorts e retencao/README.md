<!-- Estrutura reformulada por domínio. Nenhuma atividade foi resolvida. -->

## Dia 29 — Cohorts e retenção — 10/09/2026

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Cohorts e retenção.
- **Competência sugerida:** Análise de cohorts e retenção.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Análise de cohorts e retenção** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python e Power BI`.
- **Próximo marco do perfil:** Dia 30 — Engenharia de Software | Análise de Dados | Python, SQL e Power BI.

> [!abstract] Resultado concreto do dia
> Concluir **Cohorts e retenção** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Rota adaptativa do dia

- **Obrigatório:** conclua somente o Núcleo essencial.
- **Reforço:** comece por um item apenas se ainda não atingir o critério de avanço.
- **Desafio:** é opcional e nunca impede seguir para o próximo dia.
- **Limite sugerido:** 2h30–3h30; se ultrapassar muito, divida a tarefa sem copiar respostas.
- **Fonte de prioridade:** se o arquivo de exercício tiver mais enunciados, este README define quais são obrigatórios.

### Preparação
- **Assunto central:** Cohorts e retenção.
- **Pasta/arquivo principal:** `01-exercicios/dia-029-cohorts-e-retencao.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

### Núcleo essencial

> Estes são os únicos itens obrigatórios do dia.

1. [ ] Defina coorte como mês da primeira compra ou ativação; calcule o mês inicial de cada cliente.
2. [ ] Crie tabela com `cohort_month`, `period_number`, clientes ativos e taxa de retenção.
3. [ ] Monte matriz de retenção do mês 0 ao mês 5 e valide manualmente uma coorte pequena com cinco clientes.

### Reforço direcionado

> Faça primeiro um único item desta seção se o núcleo ainda não estiver claro. Pare quando corrigir a lacuna.

- [ ] Compare retenção por canal de aquisição ou plano.
- [ ] Escreva três conclusões e uma cautela sobre coortes pequenas.

### Desafio opcional

> Faça somente se o núcleo estiver correto, a autoavaliação for 3 ou mais e ainda houver tempo e energia.

- [ ] **Em `01-exercicios/dia-029-cohorts-e-retencao.sql`:** Calcule a matriz de retenção somente para clientes adquiridos pelo site e limite a cohorts com pelo menos 20 clientes no mês 0.
- [ ] **Em `01-exercicios/dia-029-cohorts-e-retencao.sql`:** Selecione cinco clientes de uma coorte e liste os meses em que ficaram ativos antes de conferir a taxa agregada.

### Checagem rápida

> Nas questões 1–2, marque `[x]` em uma única alternativa. Na questão 3, escreva a sequência correta usando as letras A–E. A checagem não substitui executar o código.

1. **Referência:** conceito e implementação do Núcleo essencial deste dia.

   **Pergunta:** Qual cuidado é essencial ao usar junções em uma atividade de **Cohorts e retenção**?

- [ ] A) Usar sempre `INNER JOIN`, independentemente da pergunta.
- [ ] B) Juntar tabelas por qualquer coluna com o mesmo tipo.
- [ ] C) Remover duplicidades depois da junção sem investigar a origem.
- [ ] D) Selecionar todas as colunas para garantir que nada seja perdido.
- [ ] E) Conferir as chaves e a cardinalidade para evitar perda ou multiplicação indevida de linhas.

2. **Referência:** execução, testes e variação de dados do Núcleo essencial.

   **Pergunta:** Como valores NULL devem ser tratados em consultas relacionadas a **Cohorts e retenção**?

- [ ] A) Excluindo automaticamente todas as linhas que contenham `NULL`.
- [ ] B) Ignorando-os, pois bancos relacionais os convertem sozinhos.
- [ ] C) De acordo com o significado do campo, distinguindo ausência de dado de um valor numérico ou textual válido.
- [ ] D) Sempre como zero, porque simplifica as agregações.
- [ ] E) Sempre como texto vazio, mesmo em colunas numéricas.

3. **Referência:** fluxo completo do Núcleo essencial deste dia.

   **Pergunta:** Ordene a construção de uma consulta para **Cohorts e retenção**.

- A) Identificar tabelas, campos e chaves necessárias.
- B) Montar filtros e junções da base da consulta.
- C) Aplicar agregações, janelas ou transformações necessárias.
- D) Validar contagens, totais e algumas linhas manualmente.
- E) Definir a pergunta, a métrica e a granularidade.

**Ordem:** `__ → __ → __ → __ → __`

### Critério de avanço

- [ ] O Núcleo essencial foi executado ou produzido do início ao fim.
- [ ] Acertei pelo menos duas das três perguntas sem consulta.
- [ ] Alterei uma entrada, parâmetro ou hipótese e entendi o efeito no resultado.
- [ ] Consigo explicar o objetivo, a lógica principal e um erro ou limitação conhecida.

> Se todos os itens acima estiverem marcados, avance. Reforço e desafio não são requisitos. Faça commit quando encerrar uma unidade útil, sem usar o commit como prova de compreensão.

**Autoavaliação do dia:** `__/5`

<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 29 — Cohorts e retenção — 10/09/2026
> [!abstract] Resultado concreto do dia
> Concluir **Cohorts e retenção** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Cohorts e retenção.
- **Pasta/arquivo principal:** `01-exercicios/dia-029-cohorts-e-retencao.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

### Passo a passo completo
1. [ ] Defina coorte como mês da primeira compra ou ativação; calcule o mês inicial de cada cliente.
2. [ ] Crie tabela com `cohort_month`, `period_number`, clientes ativos e taxa de retenção.
3. [ ] Monte matriz de retenção do mês 0 ao mês 5 e valide manualmente uma coorte pequena com cinco clientes.
4. [ ] Compare retenção por canal de aquisição ou plano.
5. [ ] Escreva três conclusões e uma cautela sobre coortes pequenas.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/dia-029-cohorts-e-retencao.sql`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/dia-029-cohorts-e-retencao.sql`:** Calcule a matriz de retenção somente para clientes adquiridos pelo site e limite a cohorts com pelo menos 20 clientes no mês 0.
- [ ] **Em `01-exercicios/dia-029-cohorts-e-retencao.sql`:** Selecione cinco clientes de uma coorte e liste os meses em que ficaram ativos antes de conferir a taxa agregada.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Defina coorte como mês da primeira compra ou ativação; calcule o mês inicial de cada cliente.

   **Pergunta:** Antes de escrever uma consulta de **Cohorts e retenção**, o que deve ser definido primeiro?

- [ ] A) A formatação visual da tabela final antes dos cálculos.
- [ ] B) A pergunta de negócio, a métrica e a granularidade que cada linha da saída deve representar.
- [ ] C) A quantidade máxima de linhas que caberá na tela.
- [ ] D) A ordem alfabética dos nomes das tabelas.
- [ ] E) O uso obrigatório de todas as colunas disponíveis.

2. **Referência — atividade 2:** Crie tabela com `cohort_month`, `period_number`, clientes ativos e taxa de retenção.

   **Pergunta:** Qual cuidado é essencial ao usar junções em uma atividade de **Cohorts e retenção**?

- [ ] A) Usar sempre `INNER JOIN`, independentemente da pergunta.
- [ ] B) Juntar tabelas por qualquer coluna com o mesmo tipo.
- [ ] C) Remover duplicidades depois da junção sem investigar a origem.
- [ ] D) Selecionar todas as colunas para garantir que nada seja perdido.
- [ ] E) Conferir as chaves e a cardinalidade para evitar perda ou multiplicação indevida de linhas.

3. **Referência — atividade 3:** Monte matriz de retenção do mês 0 ao mês 5 e valide manualmente uma coorte pequena com cinco clientes.

   **Pergunta:** Como valores NULL devem ser tratados em consultas relacionadas a **Cohorts e retenção**?

- [ ] A) Excluindo automaticamente todas as linhas que contenham `NULL`.
- [ ] B) Ignorando-os, pois bancos relacionais os convertem sozinhos.
- [ ] C) De acordo com o significado do campo, distinguindo ausência de dado de um valor numérico ou textual válido.
- [ ] D) Sempre como zero, porque simplifica as agregações.
- [ ] E) Sempre como texto vazio, mesmo em colunas numéricas.

4. **Referência — atividade 4:** Compare retenção por canal de aquisição ou plano.

   **Pergunta:** Qual verificação aumenta mais a confiança em uma consulta de **Cohorts e retenção**?

- [ ] A) Comparar contagens e totais, inspecionar amostras e validar a lógica em partes menores.
- [ ] B) Executar a consulta apenas uma vez sem mensagem de erro.
- [ ] C) Adicionar `ORDER BY` para que os números pareçam organizados.
- [ ] D) Limitar a saída a dez linhas e assumir que o restante está correto.
- [ ] E) Trocar nomes de aliases sem conferir os valores calculados.

5. **Referência — atividade 5:** Escreva três conclusões e uma cautela sobre coortes pequenas.

   **Pergunta:** Ordene a construção de uma consulta para **Cohorts e retenção**.

- A) Identificar tabelas, campos e chaves necessárias.
- B) Montar filtros e junções da base da consulta.
- C) Aplicar agregações, janelas ou transformações necessárias.
- D) Validar contagens, totais e algumas linhas manualmente.
- E) Definir a pergunta, a métrica e a granularidade.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene a investigação de uma consulta incorreta em **Cohorts e retenção**.

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

- **Conhecimento praticado hoje:** Cohorts e retenção.
- **Competência sugerida:** Análise de cohorts e retenção.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Análise de cohorts e retenção** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python e Power BI`.
- **Próximo marco do perfil:** Dia 30 — Engenharia de Software | Análise de Dados | Python, SQL e Power BI.

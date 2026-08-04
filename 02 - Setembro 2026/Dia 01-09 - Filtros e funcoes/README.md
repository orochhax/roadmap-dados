<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 22 — Filtros e funções — 01/09/2026
> [!abstract] Resultado concreto do dia
> Concluir **Filtros e funções** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Filtros e funções.
- **Pasta/arquivo principal:** `01-exercicios/dia-022-filtros-e-funcoes.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

### Passo a passo completo
1. [ ] Resolva as 15 consultas numeradas com `WHERE` em `01-exercicios/dia-022-filtros-e-funcoes.sql`; cada filtro e seus dados já estão definidos no arquivo.
2. [ ] Crie filtros de negócio: P1 não resolvido; incidentes acima de 120 minutos; cidades com mais de 100 clientes afetados; causas contendo `fibra`.
3. [ ] Use funções de texto para padronizar cidade, funções numéricas para arredondar impacto e funções nulas para substituir valores ausentes.
4. [ ] Construa três consultas logicamente equivalentes com parênteses diferentes e explique por que uma delas retorna linhas erradas.
5. [ ] Teste limites exatos 50/51, 120/121 e datas de início/fim; registre os casos inclusivos e exclusivos.

### Exercícios extras
> Os enunciados também estão preparados em `01-exercicios/dia-022-filtros-e-funcoes.sql`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/dia-022-filtros-e-funcoes.sql`:** Escreva uma consulta para incidentes de Salvador ou Ilhéus, com duração entre 51 e 120 minutos e causa contendo 'fibra'.
- [ ] **Em `01-exercicios/dia-022-filtros-e-funcoes.sql`:** Crie uma consulta que conte duração nula, cidade nula e ids duplicados; mantenha cada contagem em uma coluna identificada.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Resolva as 15 consultas numeradas com `WHERE` em `01-exercicios/dia-022-filtros-e-funcoes.sql`.

   **Pergunta:** Antes de escrever uma consulta de **Filtros e funções**, o que deve ser definido primeiro?

- [ ] A) A ordem alfabética dos nomes das tabelas.
- [ ] B) O uso obrigatório de todas as colunas disponíveis.
- [ ] C) A formatação visual da tabela final antes dos cálculos.
- [ ] D) A pergunta de negócio, a métrica e a granularidade que cada linha da saída deve representar.
- [ ] E) A quantidade máxima de linhas que caberá na tela.

2. **Referência — atividade 2:** Crie filtros de negócio: P1 não resolvido; incidentes acima de 120 minutos; cidades com mais de 100 clientes afetados; causas contendo `fibra`.

   **Pergunta:** Qual cuidado é essencial ao usar junções em uma atividade de **Filtros e funções**?

- [ ] A) Selecionar todas as colunas para garantir que nada seja perdido.
- [ ] B) Conferir as chaves e a cardinalidade para evitar perda ou multiplicação indevida de linhas.
- [ ] C) Usar sempre `INNER JOIN`, independentemente da pergunta.
- [ ] D) Juntar tabelas por qualquer coluna com o mesmo tipo.
- [ ] E) Remover duplicidades depois da junção sem investigar a origem.

3. **Referência — atividade 3:** Use funções de texto para padronizar cidade, funções numéricas para arredondar impacto e funções nulas para substituir valores ausentes.

   **Pergunta:** Como valores NULL devem ser tratados em consultas relacionadas a **Filtros e funções**?

- [ ] A) Sempre como zero, porque simplifica as agregações.
- [ ] B) Sempre como texto vazio, mesmo em colunas numéricas.
- [ ] C) Excluindo automaticamente todas as linhas que contenham `NULL`.
- [ ] D) Ignorando-os, pois bancos relacionais os convertem sozinhos.
- [ ] E) De acordo com o significado do campo, distinguindo ausência de dado de um valor numérico ou textual válido.

4. **Referência — atividade 4:** Construa três consultas logicamente equivalentes com parênteses diferentes e explique por que uma delas retorna linhas erradas.

   **Pergunta:** Qual verificação aumenta mais a confiança em uma consulta de **Filtros e funções**?

- [ ] A) Limitar a saída a dez linhas e assumir que o restante está correto.
- [ ] B) Trocar nomes de aliases sem conferir os valores calculados.
- [ ] C) Comparar contagens e totais, inspecionar amostras e validar a lógica em partes menores.
- [ ] D) Executar a consulta apenas uma vez sem mensagem de erro.
- [ ] E) Adicionar `ORDER BY` para que os números pareçam organizados.

5. **Referência — atividade 5:** Teste limites exatos 50/51, 120/121 e datas de início/fim; registre os casos inclusivos e exclusivos.

   **Pergunta:** Ordene a construção de uma consulta para **Filtros e funções**.

- A) Definir a pergunta, a métrica e a granularidade.
- B) Validar contagens, totais e algumas linhas manualmente.
- C) Identificar tabelas, campos e chaves necessárias.
- D) Aplicar agregações, janelas ou transformações necessárias.
- E) Montar filtros e junções da base da consulta.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene a investigação de uma consulta incorreta em **Filtros e funções**.

- A) Executar separadamente cada etapa ou CTE.
- B) Conferir chaves, duplicidades, filtros e contagens.
- C) Corrigir a etapa que altera os dados indevidamente.
- D) Executar a consulta completa e registrar a causa do erro.
- E) Reproduzir o problema com um recorte pequeno.

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

- **Conhecimento praticado hoje:** Filtros e funções.
- **Competência sugerida:** SQL.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **SQL** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python e Power BI`.
- **Próximo marco do perfil:** Dia 30 — Engenharia de Software | Análise de Dados | Python, SQL e Power BI.

<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 27 — Funções de janela — 08/09/2026
> [!abstract] Resultado concreto do dia
> Concluir **Funções de janela** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Funções de janela.
- **Pasta/arquivo principal:** `semana-06/dia-027-funcoes-de-janela.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

### Passo a passo completo
1. [ ] Use `ROW_NUMBER`, `RANK` e `DENSE_RANK` para ranquear incidentes por impacto dentro de cada cidade; explique diferenças em empates.
2. [ ] Calcule média móvel de sete dias, soma acumulada e diferença para o evento anterior com `LAG`.
3. [ ] Use `LEAD` para calcular tempo até o próximo incidente da mesma cidade.
4. [ ] Selecione o top 3 por cidade sem perder empates relevantes.
5. [ ] Compare uma solução com função de janela a outra com `GROUP BY` e explique por que elas respondem perguntas diferentes.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Escreva uma consulta adicional sobre **Funções de janela** que responda a uma pergunta de negócio diferente usando as mesmas tabelas.
- [ ] Crie uma consulta de validação para conferir nulos, duplicidades, cardinalidade ou totais antes de aceitar o resultado principal.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Use `ROW_NUMBER`, `RANK` e `DENSE_RANK` para ranquear incidentes por impacto dentro de cada cidade; explique diferenças em empates.

   **Pergunta:** Antes de escrever uma consulta de **Funções de janela**, o que deve ser definido primeiro?

- [ ] A) A ordem alfabética dos nomes das tabelas.
- [ ] B) O uso obrigatório de todas as colunas disponíveis.
- [ ] C) A formatação visual da tabela final antes dos cálculos.
- [ ] D) A pergunta de negócio, a métrica e a granularidade que cada linha da saída deve representar.
- [ ] E) A quantidade máxima de linhas que caberá na tela.

2. **Referência — atividade 2:** Calcule média móvel de sete dias, soma acumulada e diferença para o evento anterior com `LAG`.

   **Pergunta:** Qual cuidado é essencial ao usar junções em uma atividade de **Funções de janela**?

- [ ] A) Selecionar todas as colunas para garantir que nada seja perdido.
- [ ] B) Conferir as chaves e a cardinalidade para evitar perda ou multiplicação indevida de linhas.
- [ ] C) Usar sempre `INNER JOIN`, independentemente da pergunta.
- [ ] D) Juntar tabelas por qualquer coluna com o mesmo tipo.
- [ ] E) Remover duplicidades depois da junção sem investigar a origem.

3. **Referência — atividade 3:** Use `LEAD` para calcular tempo até o próximo incidente da mesma cidade.

   **Pergunta:** Como valores NULL devem ser tratados em consultas relacionadas a **Funções de janela**?

- [ ] A) Sempre como zero, porque simplifica as agregações.
- [ ] B) Sempre como texto vazio, mesmo em colunas numéricas.
- [ ] C) Excluindo automaticamente todas as linhas que contenham `NULL`.
- [ ] D) Ignorando-os, pois bancos relacionais os convertem sozinhos.
- [ ] E) De acordo com o significado do campo, distinguindo ausência de dado de um valor numérico ou textual válido.

4. **Referência — atividade 4:** Selecione o top 3 por cidade sem perder empates relevantes.

   **Pergunta:** Qual verificação aumenta mais a confiança em uma consulta de **Funções de janela**?

- [ ] A) Limitar a saída a dez linhas e assumir que o restante está correto.
- [ ] B) Trocar nomes de aliases sem conferir os valores calculados.
- [ ] C) Comparar contagens e totais, inspecionar amostras e validar a lógica em partes menores.
- [ ] D) Executar a consulta apenas uma vez sem mensagem de erro.
- [ ] E) Adicionar `ORDER BY` para que os números pareçam organizados.

5. **Referência — atividade 5:** Compare uma solução com função de janela a outra com `GROUP BY` e explique por que elas respondem perguntas diferentes.

   **Pergunta:** Ordene a construção de uma consulta para **Funções de janela**.

- A) Definir a pergunta, a métrica e a granularidade.
- B) Montar filtros e junções da base da consulta.
- C) Identificar tabelas, campos e chaves necessárias.
- D) Aplicar agregações, janelas ou transformações necessárias.
- E) Validar contagens, totais e algumas linhas manualmente.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene a investigação de uma consulta incorreta em **Funções de janela**.

- A) Conferir chaves, duplicidades, filtros e contagens.
- B) Executar separadamente cada etapa ou CTE.
- C) Reproduzir o problema com um recorte pequeno.
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

- **Conhecimento praticado hoje:** Funções de janela.
- **Competência sugerida:** Funções de janela em SQL.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Funções de janela em SQL** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python e Power BI`.
- **Próximo marco do perfil:** Dia 30 — Engenharia de Software | Análise de Dados | Python, SQL e Power BI.

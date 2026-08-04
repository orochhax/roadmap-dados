<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 23 — Agregações — 02/09/2026
> [!abstract] Resultado concreto do dia
> Concluir **Agregações** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Agregações.
- **Pasta/arquivo principal:** `semana-05/dia-023-agregacoes.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

### Passo a passo completo
1. [ ] Escreva consultas com `COUNT`, `SUM`, `AVG`, `MIN` e `MAX` para a tabela de incidentes.
2. [ ] Agrupe por cidade, causa e severidade; calcule quantidade, duração média, clientes totais e percentual resolvido.
3. [ ] Use `HAVING` para manter apenas cidades com pelo menos cinco incidentes e duração média acima de 60.
4. [ ] Calcule taxa de resolução com proteção contra divisão por zero e compare resultado com pandas.
5. [ ] Crie uma tabela de validação manual para duas cidades e confirme os agregados linha por linha.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Escreva uma consulta adicional sobre **Agregações** que responda a uma pergunta de negócio diferente usando as mesmas tabelas.
- [ ] Crie uma consulta de validação para conferir nulos, duplicidades, cardinalidade ou totais antes de aceitar o resultado principal.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Escreva consultas com `COUNT`, `SUM`, `AVG`, `MIN` e `MAX` para a tabela de incidentes.

   **Pergunta:** Antes de escrever uma consulta de **Agregações**, o que deve ser definido primeiro?

- [ ] A) O uso obrigatório de todas as colunas disponíveis.
- [ ] B) A formatação visual da tabela final antes dos cálculos.
- [ ] C) A pergunta de negócio, a métrica e a granularidade que cada linha da saída deve representar.
- [ ] D) A quantidade máxima de linhas que caberá na tela.
- [ ] E) A ordem alfabética dos nomes das tabelas.

2. **Referência — atividade 2:** Agrupe por cidade, causa e severidade; calcule quantidade, duração média, clientes totais e percentual resolvido.

   **Pergunta:** Qual cuidado é essencial ao usar junções em uma atividade de **Agregações**?

- [ ] A) Conferir as chaves e a cardinalidade para evitar perda ou multiplicação indevida de linhas.
- [ ] B) Usar sempre `INNER JOIN`, independentemente da pergunta.
- [ ] C) Juntar tabelas por qualquer coluna com o mesmo tipo.
- [ ] D) Remover duplicidades depois da junção sem investigar a origem.
- [ ] E) Selecionar todas as colunas para garantir que nada seja perdido.

3. **Referência — atividade 3:** Use `HAVING` para manter apenas cidades com pelo menos cinco incidentes e duração média acima de 60.

   **Pergunta:** Como valores NULL devem ser tratados em consultas relacionadas a **Agregações**?

- [ ] A) Sempre como texto vazio, mesmo em colunas numéricas.
- [ ] B) Excluindo automaticamente todas as linhas que contenham `NULL`.
- [ ] C) Ignorando-os, pois bancos relacionais os convertem sozinhos.
- [ ] D) De acordo com o significado do campo, distinguindo ausência de dado de um valor numérico ou textual válido.
- [ ] E) Sempre como zero, porque simplifica as agregações.

4. **Referência — atividade 4:** Calcule taxa de resolução com proteção contra divisão por zero e compare resultado com pandas.

   **Pergunta:** Qual verificação aumenta mais a confiança em uma consulta de **Agregações**?

- [ ] A) Trocar nomes de aliases sem conferir os valores calculados.
- [ ] B) Comparar contagens e totais, inspecionar amostras e validar a lógica em partes menores.
- [ ] C) Executar a consulta apenas uma vez sem mensagem de erro.
- [ ] D) Adicionar `ORDER BY` para que os números pareçam organizados.
- [ ] E) Limitar a saída a dez linhas e assumir que o restante está correto.

5. **Referência — atividade 5:** Crie uma tabela de validação manual para duas cidades e confirme os agregados linha por linha.

   **Pergunta:** Ordene a construção de uma consulta para **Agregações**.

- A) Validar contagens, totais e algumas linhas manualmente.
- B) Identificar tabelas, campos e chaves necessárias.
- C) Definir a pergunta, a métrica e a granularidade.
- D) Aplicar agregações, janelas ou transformações necessárias.
- E) Montar filtros e junções da base da consulta.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene a investigação de uma consulta incorreta em **Agregações**.

- A) Reproduzir o problema com um recorte pequeno.
- B) Conferir chaves, duplicidades, filtros e contagens.
- C) Executar separadamente cada etapa ou CTE.
- D) Corrigir a etapa que altera os dados indevidamente.
- E) Executar a consulta completa e registrar a causa do erro.

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

- **Conhecimento praticado hoje:** Agregações.
- **Competência sugerida:** Agregações em SQL.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Agregações em SQL** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python e Power BI`.
- **Próximo marco do perfil:** Dia 30 — Engenharia de Software | Análise de Dados | Python, SQL e Power BI.

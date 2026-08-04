<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 24 — JOINs — 03/09/2026
> [!abstract] Resultado concreto do dia
> Concluir **JOINs** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** JOINs.
- **Pasta/arquivo principal:** `semana-05/dia-024-joins.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

### Passo a passo completo
1. [ ] Crie tabelas `clientes`, `planos`, `chamados` e `pagamentos` com chaves primárias e estrangeiras; importe dados do kit.
2. [ ] Escreva um `INNER JOIN` para clientes com plano, um `LEFT JOIN` para encontrar clientes sem pagamentos e um anti-join para planos sem clientes.
3. [ ] Crie um caso muitos-para-muitos acidental duplicando chaves; meça como isso infla soma de mensalidade.
4. [ ] Corrija o problema agregando antes do join ou validando cardinalidade.
5. [ ] Desenhe em Mermaid ou texto o relacionamento entre as quatro tabelas e anote a granularidade de cada uma.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Escreva uma consulta adicional sobre **JOINs** que responda a uma pergunta de negócio diferente usando as mesmas tabelas.
- [ ] Crie uma consulta de validação para conferir nulos, duplicidades, cardinalidade ou totais antes de aceitar o resultado principal.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Crie tabelas `clientes`, `planos`, `chamados` e `pagamentos` com chaves primárias e estrangeiras; importe dados do kit.

   **Pergunta:** Antes de escrever uma consulta de **JOINs**, o que deve ser definido primeiro?

- [ ] A) A formatação visual da tabela final antes dos cálculos.
- [ ] B) A pergunta de negócio, a métrica e a granularidade que cada linha da saída deve representar.
- [ ] C) A quantidade máxima de linhas que caberá na tela.
- [ ] D) A ordem alfabética dos nomes das tabelas.
- [ ] E) O uso obrigatório de todas as colunas disponíveis.

2. **Referência — atividade 2:** Escreva um `INNER JOIN` para clientes com plano, um `LEFT JOIN` para encontrar clientes sem pagamentos e um anti-join para planos sem clientes.

   **Pergunta:** Qual cuidado é essencial ao usar junções em uma atividade de **JOINs**?

- [ ] A) Usar sempre `INNER JOIN`, independentemente da pergunta.
- [ ] B) Juntar tabelas por qualquer coluna com o mesmo tipo.
- [ ] C) Remover duplicidades depois da junção sem investigar a origem.
- [ ] D) Selecionar todas as colunas para garantir que nada seja perdido.
- [ ] E) Conferir as chaves e a cardinalidade para evitar perda ou multiplicação indevida de linhas.

3. **Referência — atividade 3:** Crie um caso muitos-para-muitos acidental duplicando chaves; meça como isso infla soma de mensalidade.

   **Pergunta:** Como valores NULL devem ser tratados em consultas relacionadas a **JOINs**?

- [ ] A) Excluindo automaticamente todas as linhas que contenham `NULL`.
- [ ] B) Ignorando-os, pois bancos relacionais os convertem sozinhos.
- [ ] C) De acordo com o significado do campo, distinguindo ausência de dado de um valor numérico ou textual válido.
- [ ] D) Sempre como zero, porque simplifica as agregações.
- [ ] E) Sempre como texto vazio, mesmo em colunas numéricas.

4. **Referência — atividade 4:** Corrija o problema agregando antes do join ou validando cardinalidade.

   **Pergunta:** Qual verificação aumenta mais a confiança em uma consulta de **JOINs**?

- [ ] A) Comparar contagens e totais, inspecionar amostras e validar a lógica em partes menores.
- [ ] B) Executar a consulta apenas uma vez sem mensagem de erro.
- [ ] C) Adicionar `ORDER BY` para que os números pareçam organizados.
- [ ] D) Limitar a saída a dez linhas e assumir que o restante está correto.
- [ ] E) Trocar nomes de aliases sem conferir os valores calculados.

5. **Referência — atividade 5:** Desenhe em Mermaid ou texto o relacionamento entre as quatro tabelas e anote a granularidade de cada uma.

   **Pergunta:** Ordene a construção de uma consulta para **JOINs**.

- A) Definir a pergunta, a métrica e a granularidade.
- B) Identificar tabelas, campos e chaves necessárias.
- C) Validar contagens, totais e algumas linhas manualmente.
- D) Aplicar agregações, janelas ou transformações necessárias.
- E) Montar filtros e junções da base da consulta.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene a investigação de uma consulta incorreta em **JOINs**.

- A) Reproduzir o problema com um recorte pequeno.
- B) Executar separadamente cada etapa ou CTE.
- C) Executar a consulta completa e registrar a causa do erro.
- D) Corrigir a etapa que altera os dados indevidamente.
- E) Conferir chaves, duplicidades, filtros e contagens.

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

- **Conhecimento praticado hoje:** JOINs.
- **Competência sugerida:** JOINs em SQL.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **JOINs em SQL** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python e Power BI`.
- **Próximo marco do perfil:** Dia 30 — Engenharia de Software | Análise de Dados | Python, SQL e Power BI.

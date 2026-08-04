<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 21 — Banco relacional e SELECT — 31/08/2026
> [!abstract] Resultado concreto do dia
> Concluir **Banco relacional e SELECT** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Banco relacional e SELECT.
- **Pasta/arquivo principal:** `semana-05/dia-021-banco-relacional-e-select.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

### Passo a passo completo
1. [ ] Instale PostgreSQL ou use DuckDB; crie banco `roadmap_ds` e tabela `incidentes` com chave primária e tipos apropriados.
2. [ ] Importe `incidentes.csv` e execute 12 consultas `SELECT`: todas as colunas; colunas específicas; alias; `DISTINCT`; limite; ordenação crescente/decrescente; expressão calculada; concatenação; `COALESCE`; `CAST`; `CASE`; contagem total.
3. [ ] Antes de cada consulta, escreva em comentário quantas linhas e colunas espera receber.
4. [ ] Crie uma consulta que calcule `impacto = duracao_min * clientes_afetados` e liste os cinco maiores.
5. [ ] Salve tudo em `03-sql/dia21/select_basico.sql` e exporte os resultados principais para CSV.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Escreva uma consulta adicional sobre **Banco relacional e SELECT** que responda a uma pergunta de negócio diferente usando as mesmas tabelas.
- [ ] Crie uma consulta de validação para conferir nulos, duplicidades, cardinalidade ou totais antes de aceitar o resultado principal.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. Antes de escrever uma consulta de **Banco relacional e SELECT**, o que deve ser definido primeiro?

- [ ] A) A quantidade máxima de linhas que caberá na tela.
- [ ] B) A ordem alfabética dos nomes das tabelas.
- [ ] C) O uso obrigatório de todas as colunas disponíveis.
- [ ] D) A formatação visual da tabela final antes dos cálculos.
- [ ] E) A pergunta de negócio, a métrica e a granularidade que cada linha da saída deve representar.

2. Qual cuidado é essencial ao usar junções em uma atividade de **Banco relacional e SELECT**?

- [ ] A) Remover duplicidades depois da junção sem investigar a origem.
- [ ] B) Selecionar todas as colunas para garantir que nada seja perdido.
- [ ] C) Conferir as chaves e a cardinalidade para evitar perda ou multiplicação indevida de linhas.
- [ ] D) Usar sempre `INNER JOIN`, independentemente da pergunta.
- [ ] E) Juntar tabelas por qualquer coluna com o mesmo tipo.

3. Como valores NULL devem ser tratados em consultas relacionadas a **Banco relacional e SELECT**?

- [ ] A) De acordo com o significado do campo, distinguindo ausência de dado de um valor numérico ou textual válido.
- [ ] B) Sempre como zero, porque simplifica as agregações.
- [ ] C) Sempre como texto vazio, mesmo em colunas numéricas.
- [ ] D) Excluindo automaticamente todas as linhas que contenham `NULL`.
- [ ] E) Ignorando-os, pois bancos relacionais os convertem sozinhos.

4. Qual verificação aumenta mais a confiança em uma consulta de **Banco relacional e SELECT**?

- [ ] A) Adicionar `ORDER BY` para que os números pareçam organizados.
- [ ] B) Limitar a saída a dez linhas e assumir que o restante está correto.
- [ ] C) Trocar nomes de aliases sem conferir os valores calculados.
- [ ] D) Comparar contagens e totais, inspecionar amostras e validar a lógica em partes menores.
- [ ] E) Executar a consulta apenas uma vez sem mensagem de erro.

5. Ordene a construção de uma consulta para **Banco relacional e SELECT**.

- A) Definir a pergunta, a métrica e a granularidade.
- B) Identificar tabelas, campos e chaves necessárias.
- C) Montar filtros e junções da base da consulta.
- D) Validar contagens, totais e algumas linhas manualmente.
- E) Aplicar agregações, janelas ou transformações necessárias.

**Ordem:** `__ → __ → __ → __ → __`

6. Ordene a investigação de uma consulta incorreta em **Banco relacional e SELECT**.

- A) Conferir chaves, duplicidades, filtros e contagens.
- B) Executar separadamente cada etapa ou CTE.
- C) Reproduzir o problema com um recorte pequeno.
- D) Corrigir a etapa que altera os dados indevidamente.
- E) Executar a consulta completa e registrar a causa do erro.

**Ordem:** `__ → __ → __ → __ → __`

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Alterações registradas em commit e enviadas ao GitHub.

**Autoavaliação do dia:** `__/5`  
**Evidência:** link do commit, notebook, consulta, imagem ou gravação.

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Banco relacional e SELECT.
- **Competência sugerida:** Bancos de dados relacionais e SQL.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Bancos de dados relacionais e SQL** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python e Power BI`.
- **Próximo marco do perfil:** Dia 30 — Engenharia de Software | Análise de Dados | Python, SQL e Power BI.

---

## Anotações pessoais



### Conceitos estudados


### Dúvidas


### Erros encontrados e correções


### Aprendizado principal


### Próxima ação

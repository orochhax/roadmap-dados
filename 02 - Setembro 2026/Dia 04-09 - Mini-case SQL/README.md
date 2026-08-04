<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 25 — Mini-case SQL — 04/09/2026
> [!abstract] Resultado concreto do dia
> Concluir **Mini-case SQL** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Mini-case SQL.
- **Pasta/arquivo principal:** `semana-05/dia-025-mini-case-sql/` (pasta do projeto).
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

### Passo a passo completo
1. [ ] Responda em SQL: quais cidades concentram churn; quais planos têm maior ticket; quais clientes abriram mais chamados; qual canal arrecadou mais; quais clientes estão inadimplentes.
2. [ ] Crie uma consulta única com CTEs ou subconsultas para gerar uma tabela executiva por cidade.
3. [ ] Exporte o resultado e reproduza dois indicadores em pandas para validação cruzada.
4. [ ] Otimize uma consulta removendo `SELECT *`, filtros tardios e joins desnecessários; compare o plano de execução quando disponível.
5. [ ] Entregue `case_sql_semana05.md` com pergunta, consulta, resultado, interpretação e limitação para cada análise.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Escreva uma consulta adicional sobre **Mini-case SQL** que responda a uma pergunta de negócio diferente usando as mesmas tabelas.
- [ ] Crie uma consulta de validação para conferir nulos, duplicidades, cardinalidade ou totais antes de aceitar o resultado principal.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. **Referência — atividade 1:** Responda em SQL: quais cidades concentram churn; quais planos têm maior ticket; quais clientes abriram mais chamados; qual canal arrecadou mais; quais clientes estão inadimplentes.

   **Pergunta:** Antes de escrever uma consulta de **Mini-case SQL**, o que deve ser definido primeiro?

- [ ] A) A pergunta de negócio, a métrica e a granularidade que cada linha da saída deve representar.
- [ ] B) A quantidade máxima de linhas que caberá na tela.
- [ ] C) A ordem alfabética dos nomes das tabelas.
- [ ] D) O uso obrigatório de todas as colunas disponíveis.
- [ ] E) A formatação visual da tabela final antes dos cálculos.

2. **Referência — atividade 2:** Crie uma consulta única com CTEs ou subconsultas para gerar uma tabela executiva por cidade.

   **Pergunta:** Qual cuidado é essencial ao usar junções em uma atividade de **Mini-case SQL**?

- [ ] A) Juntar tabelas por qualquer coluna com o mesmo tipo.
- [ ] B) Remover duplicidades depois da junção sem investigar a origem.
- [ ] C) Selecionar todas as colunas para garantir que nada seja perdido.
- [ ] D) Conferir as chaves e a cardinalidade para evitar perda ou multiplicação indevida de linhas.
- [ ] E) Usar sempre `INNER JOIN`, independentemente da pergunta.

3. **Referência — atividade 3:** Exporte o resultado e reproduza dois indicadores em pandas para validação cruzada.

   **Pergunta:** Como valores NULL devem ser tratados em consultas relacionadas a **Mini-case SQL**?

- [ ] A) Ignorando-os, pois bancos relacionais os convertem sozinhos.
- [ ] B) De acordo com o significado do campo, distinguindo ausência de dado de um valor numérico ou textual válido.
- [ ] C) Sempre como zero, porque simplifica as agregações.
- [ ] D) Sempre como texto vazio, mesmo em colunas numéricas.
- [ ] E) Excluindo automaticamente todas as linhas que contenham `NULL`.

4. **Referência — atividade 4:** Otimize uma consulta removendo `SELECT *`, filtros tardios e joins desnecessários; compare o plano de execução quando disponível.

   **Pergunta:** Qual verificação aumenta mais a confiança em uma consulta de **Mini-case SQL**?

- [ ] A) Executar a consulta apenas uma vez sem mensagem de erro.
- [ ] B) Adicionar `ORDER BY` para que os números pareçam organizados.
- [ ] C) Limitar a saída a dez linhas e assumir que o restante está correto.
- [ ] D) Trocar nomes de aliases sem conferir os valores calculados.
- [ ] E) Comparar contagens e totais, inspecionar amostras e validar a lógica em partes menores.

5. **Referência — atividade 5:** Entregue `case_sql_semana05.md` com pergunta, consulta, resultado, interpretação e limitação para cada análise.

   **Pergunta:** Ordene a construção de uma consulta para **Mini-case SQL**.

- A) Montar filtros e junções da base da consulta.
- B) Identificar tabelas, campos e chaves necessárias.
- C) Validar contagens, totais e algumas linhas manualmente.
- D) Aplicar agregações, janelas ou transformações necessárias.
- E) Definir a pergunta, a métrica e a granularidade.

**Ordem:** `__ → __ → __ → __ → __`

6. **Referência — fluxo completo do dia:** atividades 1 a 5 do passo a passo exibido acima.

   **Pergunta:** Ordene a investigação de uma consulta incorreta em **Mini-case SQL**.

- A) Reproduzir o problema com um recorte pequeno.
- B) Conferir chaves, duplicidades, filtros e contagens.
- C) Executar a consulta completa e registrar a causa do erro.
- D) Corrigir a etapa que altera os dados indevidamente.
- E) Executar separadamente cada etapa ou CTE.

**Ordem:** `__ → __ → __ → __ → __`

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Alterações registradas em commit e enviadas ao GitHub.

**Autoavaliação do dia:** `__/5`  

> [!project] Projeto semanal — Banco comercial e consultas de decisão
> **Desafio:** Modelar um pequeno banco de clientes, pedidos e pagamentos e responder perguntas comerciais reais com SQL.
>
> **Deve reutilizar:** Python/pandas anteriores e SQL básico.
>
> **Entregáveis obrigatórios:**
> - [ ] script de criação e carga;
> - [ ] 15 consultas comentadas;
> - [ ] validação de JOINs e duplicidades;
> - [ ] memorando com três decisões;
>
> **Defesa:** demonstração de cinco minutos e resposta a três perguntas técnicas.
>
> **Nota mínima recomendada:** `6/10`.

> [!check] Critério para avançar
> Você consegue responder perguntas de negócio combinando várias tabelas e validar se não duplicou valores?

---

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** Mini-case SQL.
- **Competência sugerida:** SQL aplicado a negócios.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **SQL aplicado a negócios** na seção Competências. Se a entrega estiver revisada e representar bem seu trabalho, considere incluí-la em Projetos ou Destaques.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python e Power BI`.
- **Próximo marco do perfil:** Dia 30 — Engenharia de Software | Análise de Dados | Python, SQL e Power BI.

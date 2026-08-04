<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 28 — Datas e análise temporal — 09/09/2026
> [!abstract] Resultado concreto do dia
> Concluir **Datas e análise temporal** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Datas e análise temporal.
- **Pasta/arquivo principal:** `semana-06/dia-028-datas-e-analise-temporal.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.

### Passo a passo completo
1. [ ] Converta colunas de texto em data/hora e extraia ano, mês, semana, dia da semana e hora.
2. [ ] Calcule incidentes e duração média por dia, semana e mês.
3. [ ] Meça tempo entre abertura e fechamento e classifique SLA em `no prazo` ou `atrasado`.
4. [ ] Crie calendário completo e faça `LEFT JOIN` para exibir dias sem eventos com zero.
5. [ ] Teste virada de mês, ano bissexto, horário nulo e eventos abertos; documente decisões.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Escreva uma consulta adicional sobre **Datas e análise temporal** que responda a uma pergunta de negócio diferente usando as mesmas tabelas.
- [ ] Crie uma consulta de validação para conferir nulos, duplicidades, cardinalidade ou totais antes de aceitar o resultado principal.

### Perguntas de checagem

> Nas questões 1–4, marque `[x]` em uma única alternativa. Nas questões 5–6, escreva a sequência correta usando as letras A–E.

1. Antes de escrever uma consulta de **Datas e análise temporal**, o que deve ser definido primeiro?

- [ ] A) O uso obrigatório de todas as colunas disponíveis.
- [ ] B) A formatação visual da tabela final antes dos cálculos.
- [ ] C) A pergunta de negócio, a métrica e a granularidade que cada linha da saída deve representar.
- [ ] D) A quantidade máxima de linhas que caberá na tela.
- [ ] E) A ordem alfabética dos nomes das tabelas.

2. Qual cuidado é essencial ao usar junções em uma atividade de **Datas e análise temporal**?

- [ ] A) Conferir as chaves e a cardinalidade para evitar perda ou multiplicação indevida de linhas.
- [ ] B) Usar sempre `INNER JOIN`, independentemente da pergunta.
- [ ] C) Juntar tabelas por qualquer coluna com o mesmo tipo.
- [ ] D) Remover duplicidades depois da junção sem investigar a origem.
- [ ] E) Selecionar todas as colunas para garantir que nada seja perdido.

3. Como valores NULL devem ser tratados em consultas relacionadas a **Datas e análise temporal**?

- [ ] A) Sempre como texto vazio, mesmo em colunas numéricas.
- [ ] B) Excluindo automaticamente todas as linhas que contenham `NULL`.
- [ ] C) Ignorando-os, pois bancos relacionais os convertem sozinhos.
- [ ] D) De acordo com o significado do campo, distinguindo ausência de dado de um valor numérico ou textual válido.
- [ ] E) Sempre como zero, porque simplifica as agregações.

4. Qual verificação aumenta mais a confiança em uma consulta de **Datas e análise temporal**?

- [ ] A) Trocar nomes de aliases sem conferir os valores calculados.
- [ ] B) Comparar contagens e totais, inspecionar amostras e validar a lógica em partes menores.
- [ ] C) Executar a consulta apenas uma vez sem mensagem de erro.
- [ ] D) Adicionar `ORDER BY` para que os números pareçam organizados.
- [ ] E) Limitar a saída a dez linhas e assumir que o restante está correto.

5. Ordene a construção de uma consulta para **Datas e análise temporal**.

- A) Montar filtros e junções da base da consulta.
- B) Identificar tabelas, campos e chaves necessárias.
- C) Definir a pergunta, a métrica e a granularidade.
- D) Aplicar agregações, janelas ou transformações necessárias.
- E) Validar contagens, totais e algumas linhas manualmente.

**Ordem:** `__ → __ → __ → __ → __`

6. Ordene a investigação de uma consulta incorreta em **Datas e análise temporal**.

- A) Reproduzir o problema com um recorte pequeno.
- B) Executar separadamente cada etapa ou CTE.
- C) Conferir chaves, duplicidades, filtros e contagens.
- D) Executar a consulta completa e registrar a causa do erro.
- E) Corrigir a etapa que altera os dados indevidamente.

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

- **Conhecimento praticado hoje:** Datas e análise temporal.
- **Competência sugerida:** Análise temporal com SQL.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Análise temporal com SQL** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise de Dados | Python e Power BI`.
- **Próximo marco do perfil:** Dia 30 — Engenharia de Software | Análise de Dados | Python, SQL e Power BI.

---

## Anotações pessoais



### Conceitos estudados


### Dúvidas


### Erros encontrados e correções


### Aprendizado principal


### Próxima ação

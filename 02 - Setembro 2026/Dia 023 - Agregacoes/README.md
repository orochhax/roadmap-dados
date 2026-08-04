<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 23 — Agregações — 02/09/2026
> [!abstract] Resultado concreto do dia
> Concluir **Agregações** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Agregações.
- **Pasta/arquivo principal:** `semana-05/dia-023-agregacoes.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.
- **Regra:** antes de executar qualquer cálculo ou código importante, anote o resultado que espera obter.

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
1. Qual a diferença entre `WHERE` e `HAVING`, e como uma agregação pode contar registros duplicados?

**Resposta:**

2. Em qual exercício de **Agregações** uma implementação errada poderia parecer correta? Dê um exemplo com entrada, saída errada e saída esperada.

**Resposta:**

3. Qual caso de borda você testou, por que ele importa e qual evidência comprova que foi tratado?

**Resposta:**

4. Como o conhecimento de **Agregações** seria usado para apoiar uma decisão real em dados ou IA?

**Resposta:**

5. Qual é a granularidade da sua saída e como ela pode mudar por causa de filtros, agregações ou joins?

**Resposta:**

6. Como você tornaria a consulta mais legível e verificável sem alterar o resultado?

**Resposta:**

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Commit realizado com mensagem no formato `dia-023: agregacoes`.

**Autoavaliação do dia:** `__/5`  
**Evidência:** link do commit, notebook, consulta, imagem ou gravação.

---

## Anotações pessoais

### Resultado esperado antes de executar


### Conceitos estudados


### Dúvidas


### Erros encontrados e correções


### Aprendizado principal


### Próxima ação

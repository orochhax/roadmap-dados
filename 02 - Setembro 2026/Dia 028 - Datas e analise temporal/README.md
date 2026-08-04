<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 28 — Datas e análise temporal — 09/09/2026
> [!abstract] Resultado concreto do dia
> Concluir **Datas e análise temporal** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Datas e análise temporal.
- **Pasta/arquivo principal:** `semana-06/dia-028-datas-e-analise-temporal.sql`.
- **Dados:** Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.
- **Regra:** antes de executar qualquer cálculo ou código importante, anote o resultado que espera obter.

### Passo a passo completo
1. [ ] Converta colunas de texto em data/hora e extraia ano, mês, semana, dia da semana e hora.
2. [ ] Calcule incidentes e duração média por dia, semana e mês.
3. [ ] Meça tempo entre abertura e fechamento e classifique SLA em `no prazo` ou `atrasado`.
4. [ ] Crie calendário completo e faça `LEFT JOIN` para exibir dias sem eventos com zero.
5. [ ] Teste virada de mês, ano bissexto, horário nulo e eventos abertos; documente decisões.

### Verificação prática sem consulta
- [ ] Escreva do zero uma consulta que use o principal recurso de **Datas e análise temporal** e responda uma pergunta nova.
- [ ] Valide o resultado por contagem manual em uma amostra de 5–10 linhas ou por pandas.
- [ ] Explique a granularidade do resultado e o risco de duplicação.

### Perguntas de checagem
1. Como fuso horário, datas incompletas e janelas móveis podem distorcer uma análise?

**Resposta:**

2. Em qual exercício de **Datas e análise temporal** uma implementação errada poderia parecer correta? Dê um exemplo com entrada, saída errada e saída esperada.

**Resposta:**

3. Qual caso de borda você testou, por que ele importa e qual evidência comprova que foi tratado?

**Resposta:**

4. Como o conhecimento de **Datas e análise temporal** seria usado para apoiar uma decisão real em dados ou IA?

**Resposta:**

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Commit realizado com mensagem no formato `dia-028: datas-e-analise-temporal`.

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

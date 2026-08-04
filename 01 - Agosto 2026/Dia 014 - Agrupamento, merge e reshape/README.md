<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 14 — Agrupamento, merge e reshape — 20/08/2026
> [!abstract] Resultado concreto do dia
> Concluir **Agrupamento, merge e reshape** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Agrupamento, merge e reshape.
- **Pasta/arquivo principal:** `semana-03/dia-014-agrupamento-merge-e-reshape.ipynb`.
- **Dados:** `dados/incidentes.csv`, `dados/clientes_telecom.csv`, `dados/pedidos.csv` e `dados/metas_cidades.csv`.
- **Regra:** antes de executar qualquer cálculo ou código importante, anote o resultado que espera obter.

### Passo a passo completo
1. [ ] Com `incidentes.csv` e `metas_cidades.csv`, calcule por `groupby` quantidade, média, mediana, soma de clientes e percentual resolvido por cidade.
2. [ ] Faça `merge` `inner`, `left` e `outer`; anote quantas linhas resultam e identifique cidades sem correspondência.
3. [ ] Crie uma tabela dinâmica com cidade nas linhas, severidade nas colunas e duração média nos valores.
4. [ ] Transforme dados largos em longos com `melt` e volte ao formato largo com `pivot`.
5. [ ] Provoque uma chave duplicada em `metas_cidades.csv`, observe o aumento de linhas e crie uma validação para impedir merge muitos-para-muitos acidental.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Aplique a técnica central de **Agrupamento, merge e reshape** a uma segunda coluna, grupo ou recorte dos dados e compare o que mudou.
- [ ] Introduza uma cópia dos dados com um problema controlado — valor ausente, duplicado ou outlier — e verifique como ele afeta o resultado.

### Perguntas de checagem
1. Como escolher entre `merge`, `concat`, `groupby` e `pivot`, e qual risco existe em chaves não únicas?

**Resposta:**

2. Em qual exercício de **Agrupamento, merge e reshape** uma implementação errada poderia parecer correta? Dê um exemplo com entrada, saída errada e saída esperada.

**Resposta:**

3. Qual caso de borda você testou, por que ele importa e qual evidência comprova que foi tratado?

**Resposta:**

4. Como o conhecimento de **Agrupamento, merge e reshape** seria usado para apoiar uma decisão real em dados ou IA?

**Resposta:**

5. Qual decisão sobre estrutura ou qualidade dos dados mais influencia a confiabilidade desta análise?

**Resposta:**

6. Como você confirmaria que o resultado não depende apenas de uma coluna ou recorte conveniente?

**Resposta:**

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Commit realizado com mensagem no formato `dia-014: agrupamento-merge-e-reshape`.

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

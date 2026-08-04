<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 127 — TCC: fatores e motor de ranking — 26/01/2027
> [!abstract] Resultado concreto do dia
> Construir fatores auditáveis e um ranking separado para ações, ETFs e FIIs.

### Passo a passo completo
1. [ ] Calcule retornos, momentum, volatilidade, drawdown, liquidez, consistência e correlações usando somente janelas anteriores à decisão.
2. [ ] Padronize os fatores dentro de cada classe e trate outliers sem usar o período futuro.
3. [ ] Construa um score quantitativo simples e documente pesos, sinal esperado e justificativa de cada fator.
4. [ ] Crie alvos futuros para classificação/regressão e implemente ao menos regressão logística e um modelo de árvore/boosting.
5. [ ] Gere ranking A–E por classe, Precision@K, retorno dos Top-K, turnover e estabilidade entre rebalanceamentos.
6. [ ] Produza explicabilidade global e exemplos de ativos bem/mal classificados.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Adicione um teste de robustez ou sensibilidade ainda não previsto em **TCC: fatores e motor de ranking** e defina antes o critério de aceitação.
- [ ] Formule uma objeção técnica forte ao resultado e indique qual artefato ou evidência deverá respondê-la.

### Perguntas de checagem
1. Por que o ranking deve ser separado por classe?

**Resposta:**

2. Um ranking estável é necessariamente um ranking bom?

**Resposta:**

3. Como Precision@K se conecta à seleção de uma carteira?

**Resposta:**

4. Qual fator tem maior risco de estar apenas ajustado ao passado?

**Resposta:**

5. Qual risco, viés ou limitação poderia enfraquecer mais a conclusão deste dia?

**Resposta:**

6. Qual é a evidência mínima necessária para outra pessoa reproduzir e contestar o resultado?

**Resposta:**

### Critério objetivo para marcar como concluído
- [ ] Baseline e modelos usam o mesmo protocolo temporal.
- [ ] Ranking reproduzível para cada data e classe.
- [ ] Features possuem ficha de disponibilidade temporal.
- [ ] Resultados incluem falhas, não apenas o melhor período.
- [ ] Commit: `dia-127: fatores-e-motor-quantitativo-de-ranking`.

**Autoavaliação do dia:** `__/5`  
**Evidência:** tabela de fatores, ranking, métricas e commit.

---

## Anotações pessoais

### Resultado esperado antes de executar


### Conceitos estudados


### Dúvidas


### Erros encontrados e correções


### Aprendizado principal


### Próxima ação

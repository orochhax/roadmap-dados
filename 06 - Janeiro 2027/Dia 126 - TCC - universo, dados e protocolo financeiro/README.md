<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 126 — TCC: universo, dados e protocolo financeiro — 25/01/2027
> [!abstract] Resultado concreto do dia
> Congelar o universo e criar uma base versionada cuja disponibilidade temporal possa ser auditada.

### Preparação
- **Pasta/arquivo principal:** `13-tcc-final/portfolio-intelligence-lab/`.
- **Unidade de análise:** ativo × data de rebalanceamento.
- **Classes obrigatórias:** ações, ETFs e FIIs.

### Passo a passo completo
1. [ ] Defina o universo mínimo por classe, critérios de inclusão, período histórico e frequência de rebalanceamento.
2. [ ] Crie tabela de ativos com `ticker`, classe, segmento, data inicial, data final e regra de elegibilidade.
3. [ ] Importe preços ajustados, volume/liquidez, proventos e indicadores disponíveis; preserve a camada bruta.
4. [ ] Crie dicionário de dados e coluna `disponivel_em` para indicadores que não surgem no mesmo dia do período de referência.
5. [ ] Gere relatório automático de ausentes, duplicados, gaps, ativos sem histórico suficiente e datas inconsistentes.
6. [ ] Defina baselines, protocolo walk-forward, custos, métricas e critérios de sucesso antes de testar modelos.

### Exercícios extras
> Você pode consultar suas anotações e o código já feito; o objetivo é avançar com uma variação nova, não refazer a atividade.

- [ ] Adicione um teste de robustez ou sensibilidade ainda não previsto em **TCC: universo, dados e protocolo financeiro** e defina antes o critério de aceitação.
- [ ] Formule uma objeção técnica forte ao resultado e indique qual artefato ou evidência deverá respondê-la.

### Perguntas de checagem
1. Qual informação estaria disponível na data real de cada decisão?

**Resposta:**

2. Como você evitará selecionar hoje apenas ativos que sobreviveram?

**Resposta:**

3. Qual é o benchmark mais simples que o projeto precisa superar?

**Resposta:**

4. Que resultado faria você concluir que o ranking não funciona?

**Resposta:**

5. Qual risco, viés ou limitação poderia enfraquecer mais a conclusão deste dia?

**Resposta:**

6. Qual é a evidência mínima necessária para outra pessoa reproduzir e contestar o resultado?

**Resposta:**

### Critério objetivo para marcar como concluído
- [ ] Dados brutos preservados e versionados.
- [ ] Universo e regras de elegibilidade documentados.
- [ ] Protocolo definido antes da modelagem.
- [ ] Pelo menos três testes automáticos de qualidade aprovados.
- [ ] Commit: `dia-126: universo-dados-e-protocolo-financeiro`.

**Autoavaliação do dia:** `__/5`  
**Evidência:** relatório de qualidade, dicionário, protocolo e commit.

---

## Anotações pessoais

### Resultado esperado antes de executar


### Conceitos estudados


### Dúvidas


### Erros encontrados e correções


### Aprendizado principal


### Próxima ação

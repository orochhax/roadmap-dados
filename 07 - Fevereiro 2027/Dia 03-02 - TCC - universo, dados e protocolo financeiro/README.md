<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 126 — TCC: universo, dados e protocolo financeiro — 25/01/2027
> [!abstract] Resultado concreto do dia
> Congelar o universo e criar uma base versionada cuja disponibilidade temporal possa ser auditada.

### Preparação
- **Pasta/arquivo principal:** `01-exercicios/roteiro_tcc.md`.
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
> Os enunciados também estão preparados em `01-exercicios/roteiro_tcc.md`. Faça exatamente estes dois itens.

- [ ] **Em `01-exercicios/roteiro_tcc.md`:** Teste o protocolo removendo ativos com menos de 252 pregões e registre quantos permanecem por classe.
- [ ] **Em `01-exercicios/roteiro_tcc.md`:** Formule a objeção 'disponivel_em ainda permite olhar o futuro?' e indique a validação temporal que deverá respondê-la.

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
- [ ] Alterações registradas em commit e enviadas ao GitHub.

**Autoavaliação do dia:** `__/5`  

---

### Conquista para o LinkedIn

> [!tip] Libere esta conquista somente depois de concluir as atividades do dia e conseguir explicar o conhecimento com suas próprias palavras.

- **Conhecimento praticado hoje:** TCC: universo, dados e protocolo financeiro.
- **Competência sugerida:** Análise de dados financeiros.
- **Ação recomendada:** Mantenha o título atual e adicione ou reforce **Análise de dados financeiros** na seção Competências.
- **Título atual recomendado:** `Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa`.
- **Próximo marco do perfil:** Dia 130 — revisão final do título, Sobre, Competências, Projetos e Destaques.

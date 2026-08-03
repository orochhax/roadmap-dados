<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 55 — Case de decisão — 16/10/2026
> [!abstract] Resultado concreto do dia
> Concluir **Case de decisão** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Case de decisão.
- **Pasta/arquivo principal:** `semana-11/dia-055-case-de-decisao/` (pasta do projeto).
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.
- **Regra:** antes de executar qualquer cálculo ou código importante, anote o resultado que espera obter.

### Passo a passo completo
1. [ ] Monte tabela com cliente, probabilidade, limiar, decisão e custo esperado.
2. [ ] Crie três políticas: conservadora, equilibrada e agressiva; calcule volume de ações e custo.
3. [ ] Analise desempenho por cidade, plano e faixa de mensalidade.
4. [ ] Defina regra de revisão humana para casos próximos ao limiar.
5. [ ] Apresente decisão em uma página, incluindo quem não deve receber ação automatizada.

### Verificação prática sem consulta
- [ ] Treine ou avalie novamente o componente central de **Case de decisão** em um notebook limpo.
- [ ] Mude seed, limiar ou uma feature e registre se a conclusão permanece estável.
- [ ] Explique qual erro técnico produziria uma métrica artificialmente boa.

### Perguntas de checagem
1. Como converter uma probabilidade prevista em política operacional auditável?

**Resposta:**

2. Em qual exercício de **Case de decisão** uma implementação errada poderia parecer correta? Dê um exemplo com entrada, saída errada e saída esperada.

**Resposta:**

3. Qual caso de borda você testou, por que ele importa e qual evidência comprova que foi tratado?

**Resposta:**

4. Como o conhecimento de **Case de decisão** seria usado para apoiar uma decisão real em dados ou IA?

**Resposta:**

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] O diário registra erro principal, correção, aprendizado e próxima lacuna.
- [ ] Commit realizado com mensagem no formato `dia-055: case-de-decisao`.

**Autoavaliação do dia:** `__/5`  
**Evidência:** link do commit, notebook, consulta, imagem ou gravação.

> [!todo] PUBLICAR NO LINKEDIN — projeto prioritário do portfólio
> - [ ] Publique somente após README, resultados e limitações estarem revisados.
> - [ ] Inclua problema, abordagem, principal evidência, decisão e link do GitHub.
> - [ ] **Ângulo sugerido:** mostrar por que o limiar 0,5 não é automático e como custos dos erros mudam a política.

> [!project] Projeto semanal — Política de acionamento por probabilidade
> **Desafio:** Criar uma política que decide quem receberá uma intervenção com base em probabilidades e custo dos erros.
>
> **Deve reutilizar:** Classificação, regressão logística, limiar, calibração e desbalanceamento.
>
> **Entregáveis obrigatórios:**
> - [ ] curvas e métricas;
> - [ ] função de custo;
> - [ ] limiar escolhido;
> - [ ] análise de segmentos;
> - [ ] parecer de risco;
>
> **Defesa:** demonstração de cinco minutos e resposta a três perguntas técnicas.
>
> **Nota mínima recomendada:** `6/10`.

> [!check] Critério para avançar
> Você consegue defender o limiar do modelo com custo e não apenas usar 0,5?

---

---

## Anotações pessoais

### Resultado esperado antes de executar


### Conceitos estudados


### Dúvidas


### Erros encontrados e correções


### Aprendizado principal


### Próxima ação

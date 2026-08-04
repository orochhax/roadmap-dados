<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 42 — Separação e vazamento — 29/09/2026
> [!abstract] Resultado concreto do dia
> Concluir **Separação e vazamento** produzindo um artefato executável e evidências de que você compreendeu o assunto.

### Preparação
- **Assunto central:** Separação e vazamento.
- **Pasta/arquivo principal:** `semana-09/dia-042-separacao-e-vazamento.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/pedidos.csv` e bases derivadas pelo seu pipeline.
- **Regra:** antes de executar qualquer cálculo ou código importante, anote o resultado que espera obter.

### Passo a passo completo
1. [ ] Separe treino, validação e teste com proporção 60/20/20 e `random_state` fixo.
2. [ ] Repita a separação de forma estratificada e compare proporção de churn em cada conjunto.
3. [ ] Crie três features com leakage proposital, como `data_cancelamento`, `motivo_cancelamento` e `status_atual`; demonstre o aumento artificial da métrica.
4. [ ] Remova o leakage e registre a queda de desempenho como evidência de correção.
5. [ ] Escreva um checklist de 10 perguntas para detectar vazamento antes da modelagem.

### Verificação prática sem consulta
- [ ] Treine ou avalie novamente o componente central de **Separação e vazamento** em um notebook limpo.
- [ ] Mude seed, limiar ou uma feature e registre se a conclusão permanece estável.
- [ ] Explique qual erro técnico produziria uma métrica artificialmente boa.

### Perguntas de checagem
1. Quais informações configuram data leakage e por que a separação deve respeitar tempo ou grupos?

**Resposta:**

2. Em qual exercício de **Separação e vazamento** uma implementação errada poderia parecer correta? Dê um exemplo com entrada, saída errada e saída esperada.

**Resposta:**

3. Qual caso de borda você testou, por que ele importa e qual evidência comprova que foi tratado?

**Resposta:**

4. Como o conhecimento de **Separação e vazamento** seria usado para apoiar uma decisão real em dados ou IA?

**Resposta:**

### Critério objetivo para marcar como concluído
- [ ] Todos os exercícios obrigatórios foram executados; nenhum item foi marcado apenas por leitura.
- [ ] O artefato executa do início ao fim sem edição manual oculta.
- [ ] Há pelo menos um caso normal, um caso de borda e um caso inválido documentados.
- [ ] Commit realizado com mensagem no formato `dia-042: separacao-e-vazamento`.

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

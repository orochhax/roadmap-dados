# Enunciado — tracking plan do autoatendimento de internet

## Cenário real

Clientes usam o aplicativo para vincular o modem, executar diagnóstico e resolver falhas sem ligar para o suporte. Produto quer medir ativação, mas os eventos atuais têm nomes livres, duplicatas e até e-mail em propriedades. Você criará o contrato antes da análise.

## Entradas

- fixture `EVENTOS_EXEMPLO` em [validar_tracking_plan.py](validar_tracking_plan.py), que deve ser ampliada para pelo menos 20 eventos;
- eventos permitidos: `account_created`, `modem_linked`, `diagnostic_started`, `diagnostic_finished`, `solution_viewed`, `issue_resolved`, `support_contacted` e `app_opened`;
- campos-base: `event_id`, `event_name`, `occurred_at`, `user_id`, `anonymous_id`, `session_id`, `schema_version` e `properties`.

## Saídas

- `tracking_plan.json` com definição, gatilho, propriedades obrigatórias, tipos, dono e versão de cada evento;
- `eventos_validos.jsonl` e `eventos_rejeitados.jsonl`;
- `relatorio_tracking.json` com métricas de qualidade;
- [evidências](../03-evidencias/README.md) com árvore de métricas e decisão.

## Regras obrigatórias

1. Use nomes no passado e a lista canônica; não aceite sinônimos silenciosamente.
2. `event_id` deve ser único; repetição idêntica é deduplicada e repetição conflitante é rejeitada.
3. `occurred_at` deve ser ISO 8601 com fuso; eventos muito futuros são rejeitados.
4. Exija `session_id` e ao menos uma identidade (`user_id` ou `anonymous_id`).
5. Proíba em propriedades: e-mail, telefone, CPF, senha, conteúdo de mensagem e endereço completo.
6. Valide propriedades específicas: diagnóstico precisa de `diagnostic_id`; resolução precisa de `issue_type` e `resolution_channel`.
7. Preserve a versão do schema e rejeite versão desconhecida.
8. Defina North Star, três métricas de entrada e duas guardrails antes de calcular qualquer resultado.

## Casos de borda obrigatórios

- mesmo `event_id` repetido com payload igual;
- mesmo `event_id` com payload diferente;
- usuário anônimo que se identifica depois;
- evento fora de ordem por atraso de rede;
- timestamp futuro;
- propriedade proibida com e-mail;
- versão de schema desconhecida;
- sessão sem evento inicial.

## Métricas

- taxa de eventos válidos;
- taxa de duplicidade e de conflito;
- violações por regra e por versão;
- cobertura do tracking plan: eventos observados documentados / eventos observados;
- percentual de sessões com sequência mínima mensurável.

## Critério de aceite

- [ ] O validador processa pelo menos 20 eventos e nunca encerra por causa de uma linha ruim.
- [ ] Os oito casos de borda têm esperado e observado.
- [ ] Nenhuma PII proibida aparece nas saídas válidas.
- [ ] Duplicatas idênticas não inflam contagens e conflitos ficam auditáveis.
- [ ] A North Star, entradas e guardrails formam uma árvore coerente e não incentivam apenas mais cliques.


# Enunciado — experimento da nova jornada de diagnóstico

## Cenário real

O aplicativo da operadora reduziu de seis para três telas o diagnóstico de internet. Produto quer lançar a nova jornada se ela aumentar resolução sem atendente, mas acompanha várias métricas diariamente e já sugeriu parar assim que “der significativo”. Você deverá estabelecer um protocolo defensável.

## Entradas

Gere `experimento_diagnostico.csv` com seed 42 e pelo menos 4.000 usuários, um registro por usuário:

- `user_id`, `group` (`control`/`treatment`) e `assignment_date`;
- `resolved_without_agent` como métrica primária binária;
- `support_contacted` como guardrail binária;
- `time_to_resolution_min` como métrica secundária;
- `pre_period_self_service_rate` como covariável anterior ao experimento;
- `city` e `device_os` apenas para auditoria, não para procurar um “segmento vencedor”.

Crie também uma cópia com SRM proposital, removendo parte de um grupo, para provar que o teste detecta o problema.

## Saídas

- [analisar_experimento.py](analisar_experimento.py) completo;
- `resultado_experimento.json` com protocolo, checagens, estimativas e decisão;
- `simulacao_peeking.csv` com pelo menos 500 experimentos sem efeito;
- [evidências](../03-evidencias/README.md) preenchidas.

## Regras obrigatórias

1. Antes de gerar/analisar o resultado, fixe alfa, poder, MDE de 1,5 ponto percentual, amostra, métrica primária, guardrail e regra de parada.
2. Teste SRM por qui-quadrado contra a alocação esperada 50/50.
3. Calcule efeito absoluto, relativo, IC95% e teste para a primária.
4. Corrija a família das três métricas com Holm-Bonferroni e compare com p-valores brutos.
5. Aplique CUPED somente com a covariável pré-experimento; registre `theta`, variância antes/depois e redução percentual.
6. Analise o resultado apenas se o teste de SRM não acusar falha; na cópia defeituosa, bloqueie a decisão.
7. Simule peeking diário ingênuo em dados sem efeito e compare sua taxa de falso positivo com uma regra sequencial previamente escolhida.
8. Não troque métrica primária, segmento ou regra depois de olhar o resultado.

## Casos de borda obrigatórios

- SRM proposital;
- covariável constante, que não reduz variância;
- valores ausentes na covariável pré-período;
- usuário duplicado em dois grupos;
- guardrail piora enquanto a primária melhora;
- p-valor bruto significativo que deixa de ser após correção;
- efeito significativo abaixo do MDE;
- dia sem observações em um grupo.

## Métricas

- p-valor de SRM;
- efeito, IC95% e p-valor bruto/ajustado;
- redução de variância e largura do IC com/sem CUPED;
- taxa de falso positivo em 500 simulações com peeking e com regra sequencial;
- custo esperado de lançar e de não lançar, usando valores definidos antes.

## Critério de aceite

- [ ] A decisão é bloqueada na base com SRM e duplicidade entre grupos.
- [ ] CUPED não usa nenhuma informação posterior à atribuição.
- [ ] A correção de multiplicidade é aplicada à família declarada.
- [ ] A simulação demonstra numericamente o risco do peeking.
- [ ] A conclusão usa efeito, incerteza, MDE e guardrail, não apenas `p < 0,05`.


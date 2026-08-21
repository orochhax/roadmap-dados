# Teste A/B

## Aprenda agora

Defina antes da coleta: unidade de randomização, métrica primária, guardrail, efeito mínimo relevante e tamanho da amostra. *Peeking* é testar repetidamente e parar ao primeiro resultado favorável.

```python
efeito_observado = conversao_b - conversao_a
decisao = "lançar" if limite_inferior_ic > efeito_minimo else "não lançar"
```

**Erro comum:** escolher métrica, segmento ou duração depois de olhar o resultado.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-038-teste-a-b.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/incidentes.csv` e dados sintéticos gerados no notebook com seed 42.

## Núcleo essencial

1. [ ] Defina um experimento A/B com unidade, população, métrica primária, guardrail e duração.
2. [ ] Analise uma amostra sintética com diferença, intervalo de confiança e teste de hipótese.
3. [ ] Escreva uma decisão entre lançar, repetir ou abandonar, citando efeito, incerteza e risco.

## Prática obrigatória

- [ ] Calcule o tamanho de amostra para efeitos mínimos de 1,5 e 0,5 ponto percentual e explique por que o segundo exige mais observações.
- [ ] **Em `01-exercicios/dia-038-teste-a-b.ipynb`:** Execute a simulação de peeking em 30 verificações diárias e conte quantas vezes a regra pararia antes da amostra planejada.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

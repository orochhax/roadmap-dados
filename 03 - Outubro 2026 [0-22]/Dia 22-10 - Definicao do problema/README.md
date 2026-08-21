# Definição do problema

## Aprenda agora

Em aprendizado supervisionado, cada linha tem uma unidade de previsão, um alvo e um instante em que a decisão será tomada. *Leakage* é qualquer informação indisponível nesse instante.

```python
problema = {
    "unidade": "cliente",
    "alvo": "cancelará em até 30 dias",
    "momento_da_previsao": "fim do mês atual",
}
```

**Erro comum:** usar `data_cancelamento` ou `motivo_cancelamento` para prever um cancelamento que ainda não ocorreu.

## Aula guiada — Curso em Vídeo IA

- [ ] Assista à aula #12 — **Você sabe o que é Machine Learning?** (15:10).
- Use-a como introdução ao bloco de Machine Learning; ela substitui parte do estudo conceitual do dia, mas não reduz o Núcleo essencial.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-041-definicao-do-problema.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

## Núcleo essencial

1. [ ] Escolha um problema binário usando `clientes_telecom.csv`: prever churn nos próximos 30 dias; escreva alvo, unidade de previsão e horizonte temporal.
2. [ ] Defina quem usará a previsão, qual ação será tomada e qual erro é mais caro.
3. [ ] Liste 15 variáveis possíveis e classifique cada uma como disponível, indisponível, sensível ou potencial leakage.

## Prática obrigatória

- [ ] Crie baseline de negócio: prever todos como não churn e comparar com regra simples `chamados_90d >= 3`.
- [ ] Escreva `problem_statement.md` com objetivo, restrições, métrica primária, métricas secundárias e critério de sucesso.
- [ ] **Em `01-exercicios/dia-041-definicao-do-problema.ipynb`:** Altere no problem statement o custo de falso negativo de R$500 para R$800 e revise somente métrica primária e critério de sucesso afetados.
- [ ] **Em `01-exercicios/dia-041-definicao-do-problema.ipynb`:** Classifique status_atual, data_cancelamento e motivo_cancelamento como leakage e escreva em que momento cada coluna fica disponível.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

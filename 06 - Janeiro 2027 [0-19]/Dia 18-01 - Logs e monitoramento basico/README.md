# Logs e monitoramento básico

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-099-logs-e-monitoramento-basico.py`.
- **Entradas:** 20 requisições locais e schema de log. **Fallback local:** latências determinísticas em `baseline_monitoramento.json`.

## Aprenda agora

- **Definição:** log estruturado usa campos; p50 é a mediana e p95 cobre 95% das latências; drift é mudança da distribuição de entrada, previsão ou desempenho.
- **Exemplo mínimo:** grave `timestamp, request_id, status, latency_ms, model_version`; salve em `baseline_monitoramento.json` probabilidades, volume e janela de referência.
- **Erro comum:** registrar dados pessoais ou alertar sem baseline, janela e limite definidos.

## Núcleo essencial

1. [ ] Adicione logs de requisição com tempo, status e versão sem registrar dados sensíveis.
2. [ ] Meça contagem, latência e erros em 20 requisições válidas e cinco inválidas.
3. [ ] Defina um alerta conceitual e escreva um runbook curto para investigá-lo.

## Prática obrigatória

- [ ] Gere `baseline_monitoramento.json`, compare uma amostra alterada e registre o sinal de drift junto das métricas operacionais.
- [ ] **Em `01-exercicios/dia-099-logs-e-monitoramento-basico.py`:** simule 50 requisições com 200 ms adicionais, compare p50 e p95 e confirme que dez payloads inválidos são contados sem conteúdo sensível nos logs.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-099-logs-e-monitoramento-basico.py` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

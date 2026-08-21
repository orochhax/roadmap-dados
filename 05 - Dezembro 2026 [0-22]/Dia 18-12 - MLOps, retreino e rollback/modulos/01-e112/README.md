# MLOps introdutório

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-104-mlops-introdutorio.py`.
- **Entradas:** `dados/clientes_telecom.csv`, run IDs do MLflow, `01-exercicios/politica_promocao.md` e `01-exercicios/model_card.md`.
- **Saídas obrigatórias:** modelo inicial, modelo retreinado, histórico de promoção e `deployment_events.jsonl` com rollback.

## Aprenda agora

- **Definição:** drift de dados muda entradas; de previsão muda scores; de conceito muda a relação com o alvo. PSI compara proporções: `Σ(a-e)ln(a/e)`.
- **Exemplo mínimo:** leia `baseline_monitoramento.json`; sem ele, gere baseline local da amostra. Defina alerta, responsável e ação de rollback.
- **Erro comum:** retreinar automaticamente por qualquer PSI sem confirmar qualidade, impacto e atraso do rótulo.
- **Retreinamento real:** exige executar novamente `.fit()` com um lote diferente; apenas descrever o processo não atende.
- **Rollback comprovado:** exige restaurar a versão anterior, recarregá-la e executar uma previsão de verificação.

## Núcleo essencial

1. [ ] Treine e registre no MLflow um modelo inicial como champion, incluindo versão dos dados, seed, métricas, latência e artefato.
2. [ ] Crie um novo lote rotulado, execute um novo `.fit()` e registre o modelo retreinado como challenger em outra run.
3. [ ] Antes de comparar, preencha um gate de promoção com métrica mínima, tolerância de degradação e limite de latência; não altere esses limites depois de ver os resultados.
4. [ ] Registre champion e challenger e controle o modelo ativo por alias ou ponteiro versionado.
5. [ ] Aponte temporariamente para o challenger, injete uma queda controlada de performance e execute rollback para o champion anterior.
6. [ ] Recarregue o modelo restaurado, faça uma previsão de verificação e grave `deployment_events.jsonl` com versões, motivo, decisão e resultado.
7. [ ] Complete o model card com uso, métricas, gatilho de retreinamento, limitações, aprovação e responsável.

## Atualização do LinkedIn — após concluir

- **Evidência exigida:** duas runs reais, novo `.fit()`, gate preenchido, promoção simulada, rollback e recarga da versão anterior.
- **Competências:** adicione **MLOps** e **Monitoramento de modelos**.
- **Sobre:** acrescente uma frase concreta sobre pipelines reproduzíveis com rastreamento, monitoramento, retreinamento e rollback usando MLflow.
- **Headline:** mantenha a atual até o marco de currículo e narrativa.

## Prática obrigatória

- [ ] **Em `01-exercicios/dia-104-mlops-introdutorio.py`:** Defina alerta de drift quando PSI superar 0,20 e registre quem revisa e em quanto tempo.
- [ ] **Em `01-exercicios/dia-104-mlops-introdutorio.py`:** Simule challenger 2% melhor na métrica, mas 4 vezes mais lento; aplique os critérios do model card para decidir.

## Concluído quando

- [ ] Retreinamento, gate, promoção e rollback foram executados e registrados com identificadores de versão.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

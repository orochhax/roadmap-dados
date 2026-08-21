# Arquitetura e entrevista

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/perguntas_entrevista.md`.
- **Entradas:** diagrama, métricas, logs, run IDs do MLflow, histórico do modelo ativo, `deployment_events.jsonl` e `01-exercicios/perguntas_entrevista.md`.

## Aprenda agora

- **Definição:** diagrama de arquitetura mostra componentes e fluxo; health check prova disponibilidade; fallback e rollback limitam falhas. Resposta técnica precisa de evidência.
- **Exemplo mínimo:** desenhe entrada→validação→modelo→resposta→log e responda uma pergunta em “decisão, motivo, trade-off, evidência”.
- **Erro comum:** citar ferramenta sem explicar responsabilidade, falha e alternativa.

## Núcleo essencial

1. [ ] Desenhe a arquitetura final com dados, pipeline, MLflow, modelo ativo, API, monitoramento e caminho de rollback.
2. [ ] Responda as perguntas 1–8 de `perguntas_entrevista.md` sem consulta na primeira tentativa.
3. [ ] Revise somente as respostas em que a confiança ficou abaixo de 3.
4. [ ] Entregue o projeto reproduzível com checklist técnico e limitações.

## Prática obrigatória

- [ ] **Em `01-exercicios/perguntas_entrevista.md`:** Adapte a arquitetura para crescimento de 10 GB para 1 TB por dia e identifique os dois componentes que precisam mudar.
- [ ] **Em `01-exercicios/perguntas_entrevista.md`:** Simule indisponibilidade do serviço de modelo e explique health check, fallback e procedimento de rollback.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/perguntas_entrevista.md` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

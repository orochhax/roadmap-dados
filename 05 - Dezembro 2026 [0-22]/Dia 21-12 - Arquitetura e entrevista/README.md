# Arquitetura e entrevista

**Data de estudo:** 21/12/2026  
**Carga planejada:** 2 a 4 horas

## Atividades do dia

### Atividade 1 — Arquitetura e entrevista

#### O que pesquisar
- `Arquitetura e entrevista Python explicado passo a passo`
- `Arquitetura e entrevista Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-arquitetura-e-entrevista`](<atividades/01-arquitetura-e-entrevista/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-arquitetura-e-entrevista/perguntas_entrevista.md`.
- **Entradas:** diagrama, métricas, logs, run IDs do MLflow, histórico do modelo ativo, `deployment_events.jsonl` e `atividades/01-arquitetura-e-entrevista/perguntas_entrevista.md`.

#### O que você precisa entender

- **Definição:** diagrama de arquitetura mostra componentes e fluxo; health check prova disponibilidade; fallback e rollback limitam falhas. Resposta técnica precisa de evidência.
- **Exemplo mínimo:** desenhe entrada→validação→modelo→resposta→log e responda uma pergunta em “decisão, motivo, trade-off, evidência”.
- **Erro comum:** citar ferramenta sem explicar responsabilidade, falha e alternativa.

#### O que fazer

- [ ] Desenhe a arquitetura final com dados, pipeline, MLflow, modelo ativo, API, monitoramento e caminho de rollback.
- [ ] Responda as perguntas 1–8 de `perguntas_entrevista.md` sem consulta na primeira tentativa.
- [ ] Revise somente as respostas em que a confiança ficou abaixo de 3.
- [ ] Entregue o projeto reproduzível com checklist técnico e limitações.

- [ ] **Em `atividades/01-arquitetura-e-entrevista/perguntas_entrevista.md`:** Adapte a arquitetura para crescimento de 10 GB para 1 TB por dia e identifique os dois componentes que precisam mudar.
- [ ] **Em `atividades/01-arquitetura-e-entrevista/perguntas_entrevista.md`:** Simule indisponibilidade do serviço de modelo e explique health check, fallback e procedimento de rollback.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

# Entrega do pipeline

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/roteiro_atividades.md`.
- **Entradas:** `dados/pedidos.csv`, schema, configuração e regras. **Fallback local:** Python com DuckDB/Parquet.

## Aprenda agora

- **Definição:** entrega de pipeline exige contrato entre etapas: fonte, schema, chave, saída, regra de reexecução e evidência de auditoria.
- **Exemplo mínimo:** tabela `etapa | entrada | saída | linhas | hash | status | duração`; uma execução completa preenche todas as linhas.
- **Erro comum:** validar cada script isolado sem testar o fluxo integral e uma falha controlada.

## Núcleo essencial

1. [ ] Empacote pipeline da semana com script de execução única.
2. [ ] Adicione validações de esquema, unicidade, nulos e limites.
3. [ ] Produza tabela de auditoria com data, status, linhas de entrada, saída e erro.
4. [ ] Rode duas vezes e com dados novos para provar idempotência/incremento correto.

## Prática obrigatória

- [ ] **Em `01-exercicios/roteiro_atividades.md`:** execute a pipeline com uma linha duplicada e registre na auditoria quantas linhas foram rejeitadas.
- [ ] Publique README de arquitetura, execução, testes, regras de reexecução e limitações.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/roteiro_atividades.md` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

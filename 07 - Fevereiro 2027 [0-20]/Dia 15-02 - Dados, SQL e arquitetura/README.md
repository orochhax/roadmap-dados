# Dados, SQL e arquitetura

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-117-dados-sql-e-arquitetura.ipynb`.
- **Entradas:** `product_brief.md`, fonte escolhida e schema. **Fallback local:** DuckDB e fixture válida/nula/duplicada.

## Manifesto de entradas

- **Obrigatórias:** `product_brief.md`, dataset local, schema e chave de negócio.
- **Fallback local:** use fixture com casos válido, nulo e duplicado; registre que é amostra de desenvolvimento.

## Aprenda agora

- **Definição:** contrato de arquitetura fixa fonte, schema, granularidade, transformação e consumidor; cada tipo de produto pede um fluxo coerente.
- **Exemplo mínimo:** preditivo: tabela→features→modelo; forecasting: série→cortes→previsão; analítico: SQL→métrica→painel; RAG: corpus→índice→resposta avaliada.
- **Erro comum:** exigir SQL, API ou modelo quando não servem à decisão escolhida.

## Núcleo essencial

1. [ ] Crie ou revise esquema SQL e pipeline de formação da base.
2. [ ] Adicione testes de qualidade e dicionário.
3. [ ] Desenhe arquitetura de execução e deploy.

## Prática obrigatória

- [ ] **Em `01-exercicios/dia-117-dados-sql-e-arquitetura.ipynb`:** Remova cliente_id de uma cópia da entrada e faça a checagem de qualidade impedir a formação da base.
- [ ] **Em `01-exercicios/dia-117-dados-sql-e-arquitetura.ipynb`:** documente uma única instrução de reprodução, execute-a duas vezes e confirme que a segunda execução não duplica linhas nem artefatos.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-117-dados-sql-e-arquitetura.ipynb` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

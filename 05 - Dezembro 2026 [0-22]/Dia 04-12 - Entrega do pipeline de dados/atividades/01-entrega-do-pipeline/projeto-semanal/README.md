# Projeto — Pipeline ETL reprodutível

## Manifesto de entradas

- **Obrigatórias:** fonte local, schema, chave, configuração e regras de qualidade.
- **Saídas:** camadas raw/clean/analytics, logs e tabela de auditoria.
- **Fallback local:** use CSV/Parquet e DuckDB; orquestrador ou nuvem não são requisitos.

## Entregas obrigatórias
1. Implemente ingestão, validação, transformação e publicação.
2. Prove idempotência com duas execuções da mesma entrada.
3. Registre contagens, hashes, duração e status por etapa.
4. Simule uma falha, aplique o runbook e registre a recuperação.

## Concluído quando

- A execução integral produz a mesma saída para a mesma entrada.
- Uma entrada inválida falha ou vai para quarentena com motivo.
- Logs e documentação permitem localizar a origem de cada tabela.

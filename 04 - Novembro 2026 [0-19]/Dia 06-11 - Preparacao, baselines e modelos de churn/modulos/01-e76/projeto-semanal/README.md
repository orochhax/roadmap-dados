# Projeto — Preparação para modelagem

## Manifesto de entradas

- **Obrigatórias:** `dados/clientes_telecom.csv`, consulta SQL, dicionário, alvo e data de corte.
- **Saídas:** base modelável, relatório de qualidade e pipeline de preparação.
- **Fallback local:** use SQLite/DuckDB e os arquivos versionados quando não houver banco externo.

## Núcleo essencial

1. [ ] Declare unidade, alvo, corte temporal e ação de negócio.
2. [ ] Valide schema, chaves, nulos, duplicatas e joins.
3. [ ] Implemente imputação, codificação e escala ajustadas somente no treino.

## Prática obrigatória

- [ ] Registre riscos de leakage e sugestões de features sem implementá-las.

## Concluído quando

- [ ] Uma linha da base representa exatamente a unidade declarada.
- [ ] Os testes de qualidade passam ou registram rejeições justificadas.
- [ ] O pipeline transforma treino e validação sem usar informação indevida.

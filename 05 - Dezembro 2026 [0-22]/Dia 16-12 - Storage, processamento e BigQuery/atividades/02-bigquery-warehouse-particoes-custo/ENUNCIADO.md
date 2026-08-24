# Enunciado — Warehouse de eventos de rede no BigQuery

## Cenário real

Os lotes do Cloud Storage precisam alimentar indicadores diários de uso e degradação de rede. Analistas querem consultar poucos dias sem escanear todo o histórico, e a equipe de dados precisa repetir uma carga corrigida sem criar duplicatas.

## Entradas

Use os arquivos válidos produzidos na atividade de Cloud e GCP prático com o schema mínimo:

- `event_id STRING`;
- `event_timestamp TIMESTAMP`;
- `ingestion_date DATE`;
- `customer_id_hash STRING`;
- `cell_id STRING`;
- `event_type STRING`;
- `duration_ms INT64`;
- `bytes_down INT64`;
- `region STRING`.

Inclua duplicata de `event_id`, valor nulo em campo obrigatório, data atrasada e valor negativo para exercitar qualidade. Não use identificadores reais.

## Saídas obrigatórias

Em `consultas_bigquery.sql`, escreva blocos identificados para:

1. criar datasets `staging` e `curated` na mesma região do bucket;
2. criar uma tabela baseline não particionada e uma tabela curated particionada por data do evento;
3. configurar clustering e `require_partition_filter` com justificativa;
4. carregar staging e rejeitar/quarentenar registros inválidos;
5. deduplicar e fazer `MERGE` incremental idempotente em curated;
6. reconciliar origem, staging, rejeitados e curated;
7. calcular tráfego e eventos por dia/região;
8. identificar células degradadas em janela móvel de sete dias;
9. comparar uma consulta sem poda com uma consulta otimizada equivalente;
10. consultar metadados de jobs e estimar custo.

## Regras

- Não use `SELECT *` nas consultas avaliadas.
- Declare explicitamente o schema e a timezone usada para derivar a data.
- Toda consulta de curated deve filtrar a coluna de partição.
- Escolha clustering a partir dos filtros/agregações reais, não por hábito.
- A carga repetida do mesmo lote deve terminar com a mesma quantidade e conteúdo.
- Valide unicidade de `event_id`, nulos, domínio de `event_type` e valores não negativos.
- Use dry run antes de consultas potencialmente caras.
- Parametrize projeto e datasets; não coloque credenciais no SQL.

## Casos de borda obrigatórios

- lote vazio;
- `event_id` duplicado no mesmo lote e entre dias;
- evento atrasado cuja data difere da ingestão;
- timestamp inválido e timezone na virada do dia;
- `cell_id` ou `event_type` desconhecido;
- duração/bytes negativos;
- filtro que não permite poda de partição;
- repetição completa da carga.

## Métricas

- qualidade: contagem por etapa, duplicatas, nulos, inválidos e diferença de reconciliação;
- custo: bytes processados/faturados e estimativa monetária por consulta;
- desempenho: duração e slot milliseconds quando disponíveis;
- otimização: redução percentual de bytes entre baseline e consulta particionada/clusterizada equivalente.

## Critério de aceite

A soma `curated + rejeitados` deve reconciliar com os registros únicos da origem segundo a regra documentada, curated deve ter zero `event_id` duplicado e a repetição do `MERGE` não pode mudar contagens. A consulta otimizada deve retornar o mesmo resultado da baseline e reduzir bytes processados em pelo menos 50% no benchmark com várias partições. Se o volume de laboratório não demonstrar clustering, explique isso sem inventar ganho e use estimativa/dry run para discutir escala.

## Restrições

Não copie um script SQL completo. Consulte cada comando, escreva a sua versão no arquivo inicial e remova tabelas de laboratório ao encerrar, se elas não forem necessárias à atividade de orquestração e Airflow real.

# Enunciado — Pipeline diário observável de eventos de telecom

## Cenário real

Todos os dias um lote é publicado no prefixo do Cloud Storage. Até 07:00, os dados válidos precisam estar no BigQuery; arquivo ausente, schema inválido ou quebra de qualidade deve interromper a publicação. Uma falha transitória pode ser repetida, mas um reprocessamento jamais pode duplicar eventos.

## Entradas

Reutilize:

- bucket e padrão `raw/event_date=AAAA-MM-DD/` do N23;
- manifesto com linhas, bytes e checksum;
- SQL de staging, validação e `MERGE` do N24;
- conexões Airflow para GCP configuradas fora do código.

A data processada deve vir do `data_interval`, não do relógio atual da máquina.

## Saídas obrigatórias

Substitua o placeholder de `dag_telecom.py` por uma DAG que contenha tarefas equivalentes a:

1. validar configuração e intervalo;
2. aguardar/localizar arquivo e manifesto da data lógica;
3. conferir tamanho, checksum e schema;
4. carregar uma staging identificada pela data/run;
5. executar verificações de qualidade;
6. fazer `MERGE` idempotente em curated;
7. reconciliar contagens e publicar métricas;
8. mover ou registrar lote inválido para quarentena;
9. limpar staging temporária com regra segura de execução.

Produza também grafo da DAG, logs redigidos, duração por tarefa e instruções de execução local.

## Regras

- O arquivo deve importar sem realizar rede, ler credenciais ou executar consultas.
- Defina `start_date`, agenda, `catchup`, retries, atraso e timeout conscientemente.
- Use templating/data interval para caminhos e partições; não use `datetime.now()` para escolher dados.
- Use conexões/identidade padrão, nunca chave ou segredo no código.
- Retry atende falha transitória; dado inválido deve falhar ou ir para quarentena sem repetição inútil.
- Cada tarefa deve ser pequena, observável e idempotente.
- Não passe datasets por XCom; passe referências e metadados pequenos.
- Uma falha de qualidade impede a publicação curated.

## Casos de borda obrigatórios

- arquivo atrasado ou ausente;
- falha transitória simulada que é recuperada por retry;
- checksum ou schema inválido sem retry infinito;
- segunda execução da mesma data;
- backfill de pelo menos dois intervalos históricos;
- falha depois da carga de staging e antes do `MERGE`;
- tarefa limpa/rodada novamente fora de ordem;
- credencial/conexão ausente com erro compreensível.

## Métricas

- confiabilidade: sucesso por execução, retries, falhas por tipo e duplicatas após rerun;
- qualidade: reconciliação de linhas, rejeitados e testes aprovados;
- tempo: duração por tarefa, duração total, data freshness e atraso contra 07:00;
- custo: bytes carregados/processados e estimativa por execução.

## Critério de aceite

A DAG deve passar no teste de importação/DagBag, mostrar dependências corretas e concluir um lote válido. A falha transitória simulada deve se recuperar, o lote inválido não pode chegar a curated, executar duas vezes a mesma data deve manter contagem/hash e o backfill de dois dias deve carregar apenas as partições correspondentes. Nenhuma credencial pode aparecer em código ou log. Se um requisito falhar, a DAG não está pronta para produção.

## Restrições

Não copie uma DAG completa nem esconda o fluxo em uma única tarefa Python. Pesquise operadores e conceitos individualmente e implemente no arquivo inicial.

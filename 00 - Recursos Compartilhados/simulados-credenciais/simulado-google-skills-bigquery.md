# Simulado autoral — Google Skills e BigQuery

Este simulado prepara para os laboratórios e para o formato de Challenge Lab do skill badge de BigQuery. Ele não reproduz tarefas oficiais e não concede uma Google Cloud Certification.

## O que este simulado mede

- **Parte A:** dez conceitos necessários para trabalhar com segurança, granularidade e custo;
- **Parte B:** qualidade do laboratório de BigQuery já concluído no roadmap;
- **Parte C:** execução autônoma de uma variante cronometrada, sem instruções passo a passo.

## Regras

- Tempo: 25 minutos para a Parte A e 45 minutos para a Parte C.
- Faça a primeira tentativa sem consulta.
- Responda em `respostas-google-skills-bigquery.md`.
- Não abra um laboratório que consome créditos antes de deixar ambiente, arquivos e cronômetro preparados.
- Este arquivo não contém respostas nem gabarito. Envie a tentativa, o SQL e o registro de execução para correção.

## Cenário

Uma empresa carrega eventos de atendimento no BigQuery. A tabela cresce diariamente, algumas consultas leem todas as colunas, os custos não são acompanhados e uma carga duplicou parte dos eventos. O gestor quer uma tabela confiável por cidade e dia, com volume, tempo médio e taxa de reincidência.

## Parte A — dez conceitos essenciais

1. Diferencie projeto, dataset e tabela e explique onde cobrança, localização e permissão entram nessa hierarquia.
2. Proponha o menor conjunto de permissões para alguém que precisa consultar tabelas, mas não criar nem apagar dados.
3. Compare autodetecção e esquema explícito ao carregar um CSV usado por uma métrica importante.
4. Explique como seleção de colunas e dry run ajudam a prevenir uma consulta desnecessariamente cara.
5. Diferencie particionamento e clustering e dê um filtro que poderia aproveitar cada estratégia.
6. Uma função foi aplicada sobre a coluna de partição no `WHERE`. Qual risco de desempenho você investigaria e que evidência procuraria?
7. Um `JOIN` dobrou a quantidade de linhas e a soma. Quais granularidades, chaves e contagens você verificaria primeiro?
8. Compare substituição total e carga incremental considerando idempotência, atraso, correção retroativa e custo.
9. Defina a granularidade da tabela diária do cenário e descreva o numerador e o denominador da taxa de reincidência.
10. Diferencie skill badge de Google Cloud Certification e explique quais evidências podem ser publicadas sem expor projeto, conta ou credencial.

## Parte B — laboratório existente como pré-requisito

Use o SQL e as conferências produzidos em [BigQuery, partições e custo](<../../07 - Fevereiro 2027 [0-12]/Dia 23-02 - Storage, processamento e BigQuery/atividades/02-bigquery-warehouse-particoes-custo/>). Não repita o laboratório completo.

Antes da variante, confirme que já possui:

- carga ou consulta de uma fonte com esquema conhecido;
- staging e tabela analítica com granularidade declarada;
- deduplicação ou carga idempotente;
- partição e, quando justificado, clustering;
- dry run, bytes processados e estimativa de custo registrados;
- ao menos uma métrica reconciliada por consulta independente;
- SQL salvo sem credenciais ou identificadores sensíveis.

Se um desses itens ainda não existe, termine a atividade de BigQuery antes de iniciar o cronômetro.

## Parte C — Challenge Lab variante, 45 minutos

### Preparação

Trabalhe em dataset de treinamento e preserve a entrega original. Sorteie uma variante ou peça à IA apenas para escolher `A`, `B` ou `C`, sem fornecer solução:

- **A — carga repetida:** um lote foi carregado duas vezes e contém ocorrências legítimas parecidas;
- **B — contrato alterado:** um campo usado por uma métrica chegou com tipo ou nome incompatível;
- **C — custo inesperado:** uma consulta retorna o valor correto, mas ignora a estratégia de partição e lê dados demais.

### Objetivos entregues ao candidato

1. Inspecione as tabelas e declare a granularidade antes de transformar.
2. Identifique o problema correspondente à variante com uma consulta de diagnóstico.
3. Produza uma tabela diária confiável por cidade sem perder ocorrências legítimas.
4. Calcule volume, tempo médio e taxa de reincidência com definições explícitas.
5. Use filtro de partição utilizável e registre dry run ou bytes estimados antes da consulta final.
6. Reconcilie uma métrica por uma segunda consulta de estrutura diferente.
7. Salve o SQL e um registro com hipótese, evidência, correção, bytes, resultado e limitação.
8. Remova ou encerre apenas os recursos temporários criados para a variante, conforme as regras do ambiente.

Ao fim de 45 minutos, pare e registre o estado mesmo que nem todos os objetivos tenham sido concluídos. Não esconda trabalho realizado depois do cronômetro.

## Rubrica de correção — sem respostas

| Critério | Pontos |
|---|---:|
| Conceitos de recursos, permissão, granularidade e custo | 20 |
| Diagnóstico correto da variante | 15 |
| SQL, joins, deduplicação e definições de métricas | 25 |
| Partição, bytes processados e controle de custo | 20 |
| Reconciliação, registro da execução e limpeza | 15 |
| Comunicação de decisão e limitação | 5 |
| **Total** | **100** |

### Falhas críticas

- publicar credencial, token ou identificador sensível;
- executar consulta relevante sem estimativa quando a ferramenta permitia conferência;
- manter indicador duplicado por `JOIN` sem diagnóstico;
- apagar ocorrência legítima para fazer a contagem fechar;
- deixar recurso temporário ativo contrariando o enunciado;
- chamar skill badge de Google Cloud Certification.

Prontidão recomendada: 80 pontos ou mais, nenhuma falha crítica e pelo menos seis dos oito objetivos concluídos dentro do tempo.

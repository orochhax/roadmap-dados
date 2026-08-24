# Avaliação de prontidão — dbt Fundamentals

Esta avaliação verifica os fundamentos necessários para concluir o curso oficial e defender o projeto dbt já construído no roadmap. Ela não reproduz uma avaliação oficial e não é a certificação profissional `dbt Analytics Engineering Certification Exam`.

## O que esta avaliação mede

- **Parte A:** doze decisões conceituais e de diagnóstico;
- **Parte B:** qualidade do projeto existente no dia 16/12;
- **Parte C:** investigação cronometrada de três falhas inseridas em uma cópia descartável desse projeto.

Não construa um segundo projeto dbt. A avaliação reutiliza sources, modelos, testes, documentação, snapshot e incremental já obrigatórios.

## Regras

- Tempo: 40 minutos para a Parte A e 60 minutos para a Parte C.
- Faça a primeira tentativa sem consulta.
- Responda em `respostas-dbt-fundamentals.md`.
- Justifique decisões com o projeto do roadmap, sem copiar definições.
- Este arquivo não contém respostas nem gabarito. Envie respostas, log de diagnóstico e artefato para correção.

## Cenário

Um time mantém transformações de pedidos, pagamentos e clientes. Alterações quebram métricas sem aviso, ninguém conhece todas as dependências e uma execução completa ficou cara. O projeto dbt foi criado para separar fontes, staging e marts, testar contratos e documentar lineage.

## Parte A — doze cenários de prontidão

1. Explique qual problema dbt resolve nesse cenário e cite uma responsabilidade importante que continua fora do dbt.
2. Diferencie `source`, `seed`, `model`, `snapshot` e `test` usando um exemplo curto do projeto do roadmap.
3. Explique por que `source()` e `ref()` contribuem para dependências, ordem de execução e lineage, em vez de apenas substituir nomes de tabelas.
4. Proponha a granularidade de staging, intermediate e marts e explique um sinal de que uma camada foi criada sem necessidade.
5. Compare `view`, `table`, `incremental` e `ephemeral` por custo, persistência, atualização e uso.
6. Um incremental produz valor diferente de um `full-refresh`. Quais filtros, chave única, registros atualizados e estado anterior você investigaria?
7. Diferencie teste genérico e singular e explique por que um teste aprovado não prova sozinho que a regra de negócio está correta.
8. Um teste de relacionamento falhou para 37 pagamentos. Liste hipóteses em ordem de investigação, sem escrever a correção pronta.
9. O total do mart está 4% acima da fonte. Como granularidade, duplicidade e cardinalidade de `JOIN` entram no diagnóstico?
10. Explique como documentação de modelo, documentação de coluna, testes e lineage atendem perguntas diferentes de um revisor.
11. O projeto funciona em desenvolvimento e falha em produção. Quais diferenças de target, schema, permissão, variável e dado devem ser comparadas sem expor segredos?
12. Diferencie conclusão do dbt Fundamentals e aprovação na certificação profissional paga. Que evidência prática deve acompanhar o curso no LinkedIn?

## Parte B — projeto aplicado já existente

Use o trabalho concluído em [dbt e Analytics Engineering](<../../05 - Dezembro 2026 [0-22]/Dia 16-12 - Storage, processamento e BigQuery/atividades/03-dbt-e-analytics-engineering/>). Não recrie o projeto.

Antes do diagnóstico, confirme uma execução verde que possua:

- `source()` e `ref()` formando o DAG;
- staging e marts com granularidade descrita;
- testes genéricos e singulares;
- documentação e lineage gerados;
- snapshot demonstrado com mudança controlada;
- incremental executado duas vezes sem duplicar dados;
- reconciliação de contagem e uma métrica monetária;
- `dbt build` final sem falhas.

Guarde o log dessa execução como baseline. Ele permitirá provar que as falhas da Parte C foram introduzidas depois.

## Parte C — diagnóstico de três falhas, 60 minutos

### Preparação pelo avaliador

1. Crie uma branch ou cópia descartável do projeto; preserve a versão verde.
2. Peça à IA ou a outra pessoa para inserir **exatamente três falhas**, uma de cada grupo abaixo, sem revelar arquivo, linha ou correção:
   - **dependência ou contrato:** `source()`, `ref()`, nome, coluna ou tipo;
   - **qualidade ou granularidade:** teste, chave, cardinalidade ou regra de negócio;
   - **estado ou execução:** incremental, snapshot, materialization, target ou variável de ambiente.
3. A pessoa que inserir as falhas deve guardar a lista fora da visão do candidato até o final.

Não autorize a remoção de testes apenas para obter uma execução verde. Nenhuma credencial real deve ser inserida.

### Trabalho do candidato

Para cada falha:

1. execute o menor comando que produza evidência útil;
2. registre sintoma, primeira hipótese e evidência observada;
3. localize a causa sem reescrever o projeto inteiro;
4. faça a menor correção sustentável;
5. adicione ou reaproveite uma verificação que impediria regressão;
6. execute `dbt build` e reconcilie a métrica principal ao final.

Preencha uma tabela no arquivo de respostas:

| Falha | Sintoma | Hipótese | Evidência | Causa | Correção | Teste de regressão | Minutos |
|---|---|---|---|---|---|---|---:|
| 1 |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |  |

Ao chegar a 60 minutos, pare e registre o estado. Compare então seu diagnóstico com a lista guardada pelo avaliador. Trabalho posterior deve ser identificado como revisão.

## Fechamento

Sem abrir o código, explique em até três minutos:

1. como um pedido percorre o DAG até o mart;
2. qual das três falhas tinha maior risco para o negócio;
3. qual teste existente não detectaria essa falha e por quê.

## Rubrica de correção — sem respostas

| Critério | Pontos |
|---|---:|
| Conceitos, camadas, granularidade e dependências | 15 |
| Testes, documentação, ambientes e materializações | 15 |
| Diagnóstico baseado em evidência | 25 |
| Correções mínimas e testes de regressão | 20 |
| `dbt build`, idempotência e reconciliação final | 15 |
| Clareza do registro e do fechamento | 10 |
| **Total** | **100** |

### Falhas críticas

- versionar senha, token ou arquivo de credencial;
- remover teste ou dado para esconder uma falha;
- manter mart sem granularidade definida;
- aceitar métrica duplicada por `JOIN`;
- declarar conclusão com `dbt build` final em falha;
- chamar dbt Fundamentals de certificação profissional.

Prontidão recomendada: 80 pontos ou mais, nenhuma falha crítica e pelo menos duas das três falhas corrigidas dentro do tempo.

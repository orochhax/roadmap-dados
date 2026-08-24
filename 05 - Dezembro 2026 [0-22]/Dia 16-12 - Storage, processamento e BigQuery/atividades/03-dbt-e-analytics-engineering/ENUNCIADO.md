# Enunciado — dbt e Analytics Engineering

## Cenário

A empresa fictícia **VivaCommerce** recebe arquivos de clientes e pedidos de um sistema legado. Analistas montam métricas diretamente nas tabelas brutas e chegam a resultados diferentes. Sua missão é criar uma camada analítica pequena, testada, documentada e reproduzível.

Os CSVs deste diretório são sintéticos e não representam pessoas ou empresas reais. Há problemas intencionais de espaços, caixa de texto, repetição e mudança cadastral. Descubra-os antes de decidir como tratar cada um.

## Restrições

- Faça a primeira implementação local com DuckDB.
- Não procure um repositório pronto para este enunciado.
- Não salve senha, token, chave JSON nem conteúdo de arquivo `.env` no Git.
- Não apague silenciosamente um registro problemático: documente a regra e a quantidade afetada.
- Um teste só conta como evidência quando você consegue explicar qual risco ele reduz.

## Etapa 1 — preparar e conhecer as fontes

1. Crie um ambiente virtual e instale `dbt-core` e `dbt-duckdb`.
2. Copie `profiles.example.yml` para o local esperado pelo dbt e substitua os `TODO` necessários.
3. Execute `dbt debug` e guarde o resultado sem caminhos ou dados sensíveis.
4. Execute `dbt seed` para carregar `clientes_raw.csv` e `pedidos_raw.csv`.
5. Faça um perfil das fontes: linhas, chaves distintas, nulos, duplicidades, domínios de texto e intervalos de data/valor.
6. Registre cada problema encontrado e a decisão de tratamento.

## Etapa 2 — organizar o projeto

Complete os scaffolds com esta separação:

- `models/sources.yml`: declaração das fontes físicas e descrições;
- `models/staging/`: renomeação, conversão de tipos, padronização e deduplicação;
- `models/marts/dim_clientes.sql`: uma linha válida por cliente no estado atual;
- `models/marts/fct_vendas.sql`: grão explícito de um pedido e colunas necessárias às métricas;
- arquivos YAML próximos aos modelos: documentação de tabelas/colunas e testes.

Use `source()` ao ler uma fonte declarada e `ref()` ao depender de outro modelo. Não escreva nomes físicos de staging ou marts diretamente nas consultas dependentes.

## Etapa 3 — contrato e testes

Implemente testes genéricos adequados para:

- chaves que devem ser únicas e preenchidas;
- relacionamento entre pedido e cliente;
- domínio conhecido de status;
- campos essenciais das métricas.

Crie também pelo menos dois testes singulares:

1. uma regra financeira que você consiga justificar;
2. uma regra temporal ou de consistência entre colunas.

Antes de corrigir o pipeline, provoque ou preserve uma falha controlada, execute `dbt test`, explique a mensagem e só então implemente o tratamento. O objetivo é mostrar que o teste detecta risco real.

## Etapa 4 — documentação e lineage

1. Descreva cada modelo, seu grão e as colunas usadas como chave ou métrica.
2. Execute `dbt docs generate` e `dbt docs serve`.
3. Capture o DAG completo da fonte ao mart.
4. Escolha uma coluna, simule uma mudança e explique quais modelos seriam afetados.

## Etapa 5 — histórico com snapshot

Use `snapshots/snap_clientes.sql` para manter o histórico de uma mudança cadastral.

1. Justifique a estratégia escolhida (`check` ou `timestamp`).
2. Execute o snapshot no estado inicial.
3. Altere de forma controlada um cliente na seed e execute novamente.
4. Consulte o histórico e registre as linhas que comprovam a mudança.
5. Reverta somente a alteração controlada feita por você ao encerrar a demonstração.

## Etapa 6 — carga incremental e idempotência

Escolha um modelo em que processamento incremental faça sentido e implemente:

- materialização incremental;
- `unique_key` coerente com o grão;
- filtro dentro de `is_incremental()`;
- estratégia para registro atualizado ou reprocessado.

Execute duas vezes sem mudar a entrada e prove que a segunda execução não cria duplicidades. Depois acrescente um pedido sintético e demonstre o comportamento incremental.

## Etapa 7 — desenho para BigQuery

Sem precisar migrar o projeto agora, escreva nas evidências:

- método de autenticação adequado para estudo local e para produção;
- projeto, dataset e localização;
- modelos que seriam `view`, `table` ou `incremental`;
- coluna de partição e possíveis colunas de clustering;
- como usar dry run, limite de bytes e ambiente separado para controlar custo;
- como adaptar o `profile` sem versionar credenciais.

## Consultas de validação obrigatórias

Produza consultas que respondam, sem registrar os resultados neste enunciado:

1. receita válida por mês;
2. quantidade de pedidos por status;
3. ticket médio por segmento;
4. clientes sem pedido e pedidos sem cliente;
5. diferença entre linhas brutas, linhas de staging e linhas da fato.

## Entregáveis

- projeto dbt preenchido e versionável;
- seeds sintéticas;
- modelos de fontes, staging e marts;
- testes genéricos e singulares;
- snapshot e um modelo incremental;
- documentação gerada e captura do lineage;
- o próprio artefato preenchido com comandos, resultados, decisões e limitações.

## Critérios de conclusão

- O projeto executa localmente desde um ambiente limpo seguindo minhas instruções.
- `dbt run` e `dbt test` terminam com sucesso no estado final.
- Cada modelo tem grão e propósito documentados.
- Há evidência de uma falha detectada, de um snapshot e de idempotência incremental.
- O desenho do BigQuery considera segurança, custo e desempenho.
- Consigo explicar as decisões sem ler uma resposta pronta.

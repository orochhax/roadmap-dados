# Data card — Telecom Customer Intelligence

## Fontes imutáveis

| Arquivo | Papel inicial | Linhas esperadas |
|---|---|---:|
| ../../dados/clientes_telecom.csv | alvo de churn e atributos de cliente | 600 |
| ../../dados/clientes.csv | dimensão de cliente | 600 |
| ../../dados/planos.csv | dimensão de plano | 6 |
| ../../dados/chamados.csv | eventos de suporte | 2.577 |
| ../../dados/pagamentos.csv | eventos financeiros | 6.391 |
| ../../dados/incidentes.csv | eventos operacionais | 240 |
| ../../dados/metas_cidades.csv | metas por cidade | 5 |

Confirme contagens e hashes durante a execução; não os copie como resultado
sem validar.

## Unidade e tempo

- unidade analítica de Product Analytics: cliente, cohort ou cidade/período;
- unidade de ML: cliente em uma data de decisão explícita;
- unidade causal: cidade-semana;
- data de corte: TODO definir antes de criar features;
- horizonte do churn: TODO definir sem olhar o resultado.

## Alvo e disponibilidade

Para cada coluna usada no modelo, registre:

| Coluna | Origem | Disponível na decisão? | Tratamento | Risco |
|---|---|---|---|---|
| TODO | TODO | TODO | TODO | TODO |

Campos como data_cancelamento, motivo_cancelamento e status posterior são
candidatos evidentes a vazamento e não devem entrar como features.

## Intervenção causal

Crie um arquivo versionado com cidade, data de início e descrição da política.
Se a intervenção for simulada, identifique-a como sintética e registre seed e
gerador. Não altere incidentes para fabricar um efeito favorável.

## Qualidade e ética

- validar chaves, FKs, datas, duplicatas, nulos e valores impossíveis;
- não tratar cidade, plano ou canal como justificativa automática para negar
  atendimento;
- publicar métricas por segmentos apenas com tamanho de amostra;
- registrar que os dados são sintéticos e não contêm pessoas reais.

## Split

- Product Analytics: período completo com cortes visíveis;
- causal: pré e pós definidos antes da estimação;
- ML: treino, validação e teste em ordem temporal;
- monitoramento: janela posterior separada do desenvolvimento.

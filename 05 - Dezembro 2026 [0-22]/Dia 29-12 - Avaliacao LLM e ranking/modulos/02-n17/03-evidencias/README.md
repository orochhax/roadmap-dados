# Evidências — N17: ranking e recomendação

## Exercício 1 — Reranking de entity matching

## Dados e prevenção de vazamento

- origem dos candidatos:
- quantidade de consultas e pares por divisão:
- prova de que `record_id` não atravessa divisões:
- features disponíveis no momento da decisão:
- features recusadas por vazamento:

## Modelagem reproduzível

- fórmula e pesos da regra baseline:
- versão/parâmetros do XGBoost:
- seed, hardware e comandos:
- limiares de `match`, `review` e `no_match` definidos na validação:

## Resultados no teste

| método | MRR | NDCG@5 | Recall@1 | precisão automática | cobertura | P95 |
|---|---:|---:|---:|---:|---:|---:|
| regra ponderada |  |  |  |  |  |  |
| XGBRanker |  |  |  |  |  |  |

## Diagnóstico

- importância das features:
- falhas causadas pelo gerador:
- falhas causadas pelo ranker:
- casos de empate/margem baixa:
- impacto estimado por mil consultas:

## Decisão

- método aprovado:
- percentuais esperados de automação e revisão:
- maior risco remanescente:
- condição que exigiria rollback:

---

## Exercício 2 — Recomendador com feedback implícito

### Dados e corte temporal

- origem/licença ou geração dos eventos:
- intervalo de datas por divisão:
- quantidade de usuários, itens e interações:
- pesos atribuídos a cada `event_type`:
- verificação de que features e popularidade não usam o futuro:

### Métodos

- regra e desempate do baseline de popularidade:
- segunda abordagem escolhida e justificativa:
- itens já vistos excluídos do top-k:
- política para usuário novo:
- política para item novo:

### Resultados

| método | Precision@10 | Recall@10 | NDCG@10 | cobertura | P95 |
|---|---:|---:|---:|---:|---:|
| popularidade |  |  |  |  |  |
| conteúdo ou colaborativo |  |  |  |  |  |

Registre separadamente os resultados de cold start e usuários com pouco histórico.

### Casos de borda e decisão

- empate de popularidade:
- catálogo vazio/menos de dez elegíveis:
- interação repetida:
- usuário ou item novo:
- método recomendado e evidência:
- limitação do feedback implícito:

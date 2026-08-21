# Evidências — N16: embeddings para entity matching

## Modelo e representação

- identificador/revisão/licença do modelo:
- campos e ordem usados no texto composto:
- dimensão e normalização dos vetores:
- biblioteca/índice vetorial:
- CPU/GPU, RAM e tamanho do lote:

## Protocolo

- conjuntos reutilizados do N14/N15:
- definição dos hard negatives:
- parâmetros escolhidos somente na validação:
- comandos reproduzíveis:

## Qualidade e custo

| método | Recall@1 | Recall@5 | MRR | NDCG@5 | consulta P95 | memória índice |
|---|---:|---:|---:|---:|---:|---:|
| TF-IDF |  |  |  |  |  |  |
| embedding |  |  |  |  |  |  |
| híbrido |  |  |  |  |  |  |

Registre também tempo de indexação, throughput e resultados por idioma/alias/domínio ausente.

## Hard negatives

Para cada erro relevante, anote entidade correta, concorrente recuperado, scores, posição e possível causa. Evite expor dados pessoais.

## Decisão

- abordagem aprovada:
- ganho mensurável versus custo adicional:
- comportamento que exige revisão humana:
- limitação do modelo multilíngue:

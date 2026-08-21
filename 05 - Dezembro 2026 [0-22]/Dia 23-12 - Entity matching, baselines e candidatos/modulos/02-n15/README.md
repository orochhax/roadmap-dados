# Entity matching II: blocking e geração escalável de candidatos

## Objetivo

Evitar a comparação cartesiana entre cada registro recebido e todo o cadastro. Você construirá um gerador de candidatos em múltiplas passagens, medindo quanto trabalho ele elimina sem descartar a entidade verdadeira. Essa etapa transforma os baselines do N14 em um desenho capaz de crescer para milhões de empresas.

## Pesquise estes nomes exatos

1. `record linkage blocking candidate generation explained`
2. `blocking keys exact match multiple passes record linkage`
3. `sorted neighbourhood indexing record linkage`
4. `TF-IDF nearest neighbors candidate generation sparse matrix`
5. `blocking pair completeness pairs quality reduction ratio`
6. `candidate recall at k entity resolution`
7. `deduplication connected components transitive closure risk`
8. `entity resolution blocking missing values common names`

## Conceitos essenciais

- **Blocking:** restringe quais pares podem ser comparados com regras baratas.
- **Passagens múltiplas:** unem candidatos produzidos por chaves diferentes.
- **Pair completeness:** proporção dos pares verdadeiros preservados pelo blocking.
- **Reduction ratio:** proporção do produto cartesiano que deixou de ser avaliada.
- **Recall@k de candidatos:** frequência com que a entidade correta aparece entre os primeiros `k` candidatos.

## Entrega obrigatória

Use os dados e funções de normalização do N14. Siga [o enunciado](<01-exercicios/ENUNCIADO.md>) em `01-exercicios/gerar_candidatos.py` e registre os experimentos em [evidências](<03-evidencias/README.md>).

O arquivo de candidatos aprovado será a entrada dos embeddings no N16 e do reranking no N17.

## LinkedIn

Após concluir, adicione: **Entity Resolution**, **Geração de candidatos** e **Otimização de algoritmos**.

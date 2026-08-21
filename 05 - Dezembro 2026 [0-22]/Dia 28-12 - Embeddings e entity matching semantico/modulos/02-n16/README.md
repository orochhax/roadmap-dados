# Entity matching III: embeddings multilíngues e hard negatives

## Objetivo

Avaliar se representações semânticas recuperam empresas que os métodos lexicais não encontram, como traduções, aliases e nomes comerciais muito diferentes. Você comparará embeddings congelados com o TF-IDF do N14, usará os candidatos do N15 e medirá não apenas qualidade, mas também latência, memória e custo de reprocessamento.

## Pesquise estes nomes exatos

1. `SentenceTransformer encode normalize_embeddings cosine similarity`
2. `multilingual sentence transformers semantic similarity`
3. `multilingual E5 query passage prefix embeddings`
4. `FAISS IndexFlatIP cosine similarity normalized vectors`
5. `hard negative mining semantic similarity entity matching`
6. `Recall at k MRR retrieval evaluation`
7. `embedding batch size latency memory benchmark`
8. `semantic similarity lexical features hybrid retrieval`

## Conceitos essenciais

- **Bi-encoder:** gera vetores separadamente e permite indexar o cadastro.
- **Hard negative:** empresa errada, mas muito parecida com a correta.
- **Busca vetorial:** recupera vizinhos próximos no espaço de embeddings.
- **Recuperação híbrida:** combina sinais semânticos e lexicais.
- **Custo de indexação:** tempo e memória necessários para atualizar o catálogo.

## Entrega obrigatória

Execute o [enunciado](<01-exercicios/ENUNCIADO.md>) em `01-exercicios/matching_semantico.py`. Registre versão exata do modelo, formato do texto composto e benchmark em [evidências](<03-evidencias/README.md>).

## LinkedIn

Após concluir, adicione: **Embeddings**, **Busca semântica** e **Sentence Transformers**.

# Embeddings e busca semantica + Entity matching III: embeddings, hard negatives e multilinguismo

**Data de estudo:** 28/12/2026  
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Embeddings e busca semantica

#### O que pesquisar
- `Embeddings e busca semantica IA generativa aplicada explicado passo a passo`
- `Embeddings e busca semantica IA generativa aplicada exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `projeto-assistente-suporte-ia`](<../../projetos/assistente-suporte-ia/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `projetos/assistente-suporte-ia/src/assistente_suporte_ia/busca_semantica.py`.
- **Dados:** os 15 documentos de `projetos/assistente-suporte-ia/data/corpus/`.

#### Diagnóstico de base

- [ ] Confirme agora, em `projetos/assistente-suporte-ia/governanca/gate-fundamentos.md`, autonomia 3/5 ou maior em Python, SQL, estatística e ML: script testado, consulta com JOIN/agregação, cálculo interpretado e pipeline com baseline.
- Use as lacunas encontradas para planejar uma revisão posterior; elas não substituem as atividades obrigatórias de LLM/RAG.

#### O que você precisa entender

- **Definição:** embedding é um vetor semântico; similaridade cosseno é `(a·b)/(|a||b|)` e varia de -1 a 1.
- **Exemplo mínimo:** calcule o cosseno de três vetores pequenos e confira que textos equivalentes ficam acima dos não relacionados; use vetores locais simulados se não houver modelo.
- **Erro comum:** comparar vetores de modelos diferentes ou interpretar similaridade alta como prova de verdade.

#### O que fazer

- [ ] Gere embeddings para os 15 documentos fornecidos ou use vetores simulados para entender o fluxo.
- [ ] Calcule similaridade cosseno entre uma consulta e os documentos.
- [ ] Compare busca por palavra-chave e semântica em cinco perguntas.

- [ ] **Em `projetos/assistente-suporte-ia/src/assistente_suporte_ia/busca_semantica.py`:** compare palavra-chave e cosseno para 'a luz LOS ficou vermelha' e registre os três documentos retornados por cada busca.
- [ ] **No mesmo arquivo:** teste 'qual a previsão do tempo amanhã?', aplique um limiar que permita declarar a consulta fora do domínio e registre um falso positivo ou falso negativo observado.

#### Como validar

- O diagnóstico está registrado e o artefato obrigatório de LLM/RAG foi executado com a saída exigida.
- Um caso de borda ou erro foi testado, com resultado esperado e observado registrados.
- A entrega explica o resultado, a decisão tomada e uma limitação concreta.

### Atividade 2 — Entity matching III: embeddings, hard negatives e multilinguismo

#### O que pesquisar
- `sentence transformers similarity`
- `hard negative mining`
- `multilingual embeddings`
- `embedding latency`

**Arquivos da atividade:** [abrir a pasta `02-entity-matching-iii-embeddings-hard`](<atividades/02-entity-matching-iii-embeddings-hard/>)

#### Objetivo

Avaliar se representações semânticas recuperam empresas que os métodos lexicais não encontram, como traduções, aliases e nomes comerciais muito diferentes. Você comparará embeddings congelados com o TF-IDF da atividade de normalização e baseline, usará os candidatos da atividade de blocking e medirá não apenas qualidade, mas também latência, memória e custo de reprocessamento.

#### Termos complementares para pesquisar

1. `SentenceTransformer encode normalize_embeddings cosine similarity`
2. `multilingual sentence transformers semantic similarity`
3. `multilingual E5 query passage prefix embeddings`
4. `FAISS IndexFlatIP cosine similarity normalized vectors`
5. `hard negative mining semantic similarity entity matching`
6. `Recall at k MRR retrieval evaluation`
7. `embedding batch size latency memory benchmark`
8. `semantic similarity lexical features hybrid retrieval`

#### O que você precisa entender

- **Bi-encoder:** gera vetores separadamente e permite indexar o cadastro.
- **Hard negative:** empresa errada, mas muito parecida com a correta.
- **Busca vetorial:** recupera vizinhos próximos no espaço de embeddings.
- **Recuperação híbrida:** combina sinais semânticos e lexicais.
- **Custo de indexação:** tempo e memória necessários para atualizar o catálogo.

#### O que fazer

Execute o [enunciado](<atividades/02-entity-matching-iii-embeddings-hard/ENUNCIADO.md>) em `atividades/02-entity-matching-iii-embeddings-hard/matching_semantico.py`. Registre versão exata do modelo, formato do texto composto e benchmark no próprio artefato.

#### LinkedIn

Após concluir, adicione: **Embeddings**, **Busca semântica** e **Sentence Transformers**.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

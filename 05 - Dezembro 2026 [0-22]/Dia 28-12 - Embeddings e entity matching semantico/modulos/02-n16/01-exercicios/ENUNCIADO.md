# Enunciado — Recuperação semântica de empresas multilíngues

## Cenário real

O baseline lexical encontra nomes parecidos, mas falha quando um ticket usa tradução, alias ou nome comercial. Você deve medir se um modelo de embeddings multilíngue melhora a recuperação sem confundir concorrentes, subsidiárias e empresas de nomes semelhantes.

## Entradas

Use:

- o cadastro canônico do N14;
- os registros recebidos e o teste congelado;
- o arquivo de candidatos do N15;
- um conjunto identificado de hard negatives, sem alterar os rótulos do teste.

Crie uma representação textual documentada a partir de nome, domínio, país e cidade. Campo ausente deve ter tratamento explícito; não use `true_entity_id` na representação.

## Saídas obrigatórias

`matching_semantico.py` deve produzir:

1. embeddings do cadastro em lotes e metadados da versão do modelo;
2. top-k de um baseline TF-IDF e do modelo semântico;
3. uma terceira execução híbrida que combine sinais lexicais e semânticos;
4. arquivo com `record_id`, `candidate_entity_id`, posição, scores e método;
5. métricas globais e por fatia;
6. benchmark de indexação e consulta;
7. análise específica de hard negatives e resultados multilíngues.

## Regras

- Use um modelo multilíngue aberto e registre o identificador e a revisão utilizados.
- Normalize vetores quando a métrica escolhida exigir.
- Defina o texto composto e os pesos híbridos usando apenas treino/validação.
- Compare os métodos no mesmo conjunto de candidatos e no mesmo teste.
- Meça a indexação separadamente da consulta.
- Não conclua que embeddings são melhores apenas por exemplos escolhidos.
- Registre CPU/GPU, tamanho do lote, dimensão, memória e tempo.

## Casos de borda obrigatórios

- alias sem nenhuma palavra em comum com o nome jurídico;
- nome idêntico em países diferentes;
- matriz e subsidiária com descrições próximas;
- domínio presente no texto, mas nome muito diferente;
- registro apenas com nome curto;
- mistura de idiomas e caracteres não ASCII;
- hard negative mais similar semanticamente que a entidade correta;
- registro `no_match`.

## Métricas

- principais: Recall@1, Recall@5 e MRR;
- apoio: NDCG@5, precisão após limiar, recall de hard negatives, latência P50/P95, throughput, memória do índice e tempo de indexação;
- fatias: idioma, domínio ausente, alias e tamanho do nome.

## Critério de aceite

Embeddings só entram no pipeline se o método semântico ou híbrido elevar Recall@1 ou MRR em pelo menos 0,05 sobre TF-IDF, sem reduzir Recall@5 abaixo de 0,95 e dentro de um orçamento de latência definido antes do teste. Se perder, mantenha o baseline lexical e documente o custo evitado. Analise pelo menos dez hard negatives ou todos os disponíveis.

## Restrições

Não ajuste prompts, pesos ou texto composto com base no teste. O arquivo inicial não contém solução; implemente e explique cada etapa.

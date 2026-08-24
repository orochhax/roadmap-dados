# Entity Matching Lab

Projeto obrigatório de NLP, recuperação e ranking para reconciliar empresas com
nomes, aliases e domínios inconsistentes.

Documentos: [dados](data_card.md), [backlog](backlog.md),
[apresentação em inglês](docs/presentation-en.md) e
[versão em inglês](README.en.md).

## Problema e usuário

- **Problema:** ligar cada registro recebido a uma empresa canônica ou
  encaminhá-lo para revisão.
- **Usuário:** equipe de cadastro mestre, CRM ou operações comerciais.
- **Risco principal:** aceitar uma empresa parecida como se fosse a mesma.

## Dados

Construa duas fontes versionadas:

1. empresas_canonicas.csv, com id, nome, domínio, país e atributos permitidos;
2. registros_ruidosos.csv, com variantes, erros, aliases, domínios ausentes e
   rótulo verdadeiro separado para avaliação.

O gerador deve ter seed e perturbações documentadas. Inclua acentos,
abreviações, lookalikes, homônimos e exemplos multilíngues. Não ajuste as
perturbações para favorecer um método.

## Baselines

1. domínio exato normalizado;
2. nome exato normalizado;
3. fuzzy matching com limiar declarado.

## Abordagens

- TF-IDF de caracteres;
- blocking/candidate generation;
- embeddings;
- ranker supervisionado simples para candidatos;
- revisão humana para baixa confiança.

Compare obrigatoriamente embeddings com alternativas mais baratas. Não use LLM
como árbitro sem conjunto de teste, orçamento e registro dos erros.

## Métricas

- precisão, recall e F1 por par;
- recall@K da geração de candidatos;
- MRR ou precisão@1 do ranking;
- redução do espaço de candidatos;
- latência e custo por mil registros;
- slices por acento, abreviação, domínio, lookalike e idioma.

## Testes

Teste normalização, estabilidade do gerador, labels, blocking recall, ausência
de pares do teste no treino, ordenação, determinismo e política de revisão.

## Artefatos

- gerador e manifesto;
- benchmark de regras, fuzzy, TF-IDF, embeddings e ranking;
- catálogo de falsos positivos/negativos;
- CLI ou API de matching;
- relatório de custo, latência e decisão;
- README em dois idiomas e apresentação em inglês.

## Concluído quando

- Os splits são por entidade, não por linha aleatória.
- O baseline está implementado e preservado no benchmark.
- Candidate recall e ranking são avaliados separadamente.
- Há slices e análise manual dos erros mais caros.
- O sistema pode devolver revisão, sem forçar todo registro a casar.
- Comando, testes e artefatos são reproduzíveis.
- README.en.md e docs/presentation-en.md contêm resultados reais.

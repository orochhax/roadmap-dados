# Evidências — N13: NER multilíngue

## Corpus e anotação

- origem e licença dos textos:
- guia usado para decidir limites e tipos:
- contagem de documentos/entidades por divisão, idioma e rótulo:
- resultado da validação de offsets:
- tratamento de dados pessoais:

## Execução reproduzível

- Python, spaCy e modelo utilizados:
- seed e comando de treino:
- comando de avaliação:
- hash ou versão do conjunto anotado:

## Resultados

| abordagem | precisão exata | recall exato | F1 exato | latência P95 |
|---|---:|---:|---:|---:|
| regras/dicionário |  |  |  |  |
| NER spaCy |  |  |  |  |

Inclua tabelas adicionais por `ORG`, `DOMAIN`, `PRODUCT`, `LOCATION` e por idioma.

## Catálogo de erros

Registre pelo menos oito casos anonimizados e classifique cada um como: limite incorreto, tipo incorreto, entidade perdida, entidade espúria, ambiguidade ou problema de anotação.

## Decisão para o próximo módulo

- o extrator está apto a fornecer candidatos para entity matching?
- quais tipos/idiomas exigem revisão humana?
- qual diferença foi observada entre o baseline e o NER?
- qual melhoria será testada sem tocar no conjunto de teste?

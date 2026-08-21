# Evidências — N14: baselines de entity matching

## Dados e verdade de referência

- origem/licença ou geração dos registros:
- quantidade de entidades, registros e casos `no_match`:
- como os pares verdadeiros foram verificados:
- regra de divisão entre validação e teste:

## Normalização documentada

Liste cada transformação, sua justificativa e um exemplo antes/depois. Registre separadamente as regras para nomes e domínios.

## Execução

- versões de Python, pandas, scikit-learn e RapidFuzz:
- seed e comandos:
- limiares escolhidos na validação:

## Resultados no teste congelado

| método | precisão automática | recall | F1 | revisão | falso merge | latência P95 |
|---|---:|---:|---:|---:|---:|---:|
| igualdade exata |  |  |  |  |  |  |
| fuzzy |  |  |  |  |  |  |
| TF-IDF de caracteres |  |  |  |  |  |  |

## Erros relevantes

Inclua exemplos anonimizados de falso merge, falso split, `no_match` incorreto e caso enviado corretamente para revisão. Explique qual campo ou regra causou cada erro.

## Recomendação

- método e limiares recomendados:
- risco de negócio que permanece:
- situações que exigem revisão humana:
- hipótese que será levada à geração de candidatos do N15:

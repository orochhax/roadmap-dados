# NER multilíngue para extrair empresas, domínios, produtos e localidades

## Objetivo

Adicionar ao **Assistente de Suporte IA** uma etapa que localiza entidades mencionadas pelo cliente. A saída servirá como entrada para o entity matching: por exemplo, `Acme Brasil`, `acme.com.br` e `Salvador` precisam manter seus limites de caracteres e tipos corretos para que o registro canônico seja encontrado depois.

Você avaliará correspondência exata de entidade, não apenas acerto por token, e investigará diferenças entre português, inglês e espanhol.

## Pesquise estes nomes exatos

1. `named entity recognition span start end offsets`
2. `BIO IOB2 tagging named entity recognition`
3. `spaCy EntityRuler rule based NER baseline`
4. `spaCy custom NER DocBin training data`
5. `spaCy Scorer ents_p ents_r ents_f`
6. `multilingual NER Portuguese Spanish English`
7. `Unicode normalization character offsets NLP`
8. `NER boundary error type error error analysis`

## Conceitos que você deve dominar

- **Entidade:** trecho com significado definido, como empresa, domínio, produto ou localidade.
- **Span:** intervalo `início:fim` que aponta para os caracteres exatos no texto.
- **BIO/IOB2:** convenção que marca começo, continuação e exterior de uma entidade.
- **F1 por entidade:** só considera correta uma previsão com limite e tipo compatíveis.
- **Análise por idioma:** impede que um bom resultado médio esconda falhas em uma língua.

## Entrega obrigatória

Siga [o enunciado](<01-exercicios/ENUNCIADO.md>) no arquivo `01-exercicios/avaliar_ner.py` e documente a execução em [evidências](<03-evidencias/README.md>). Preserve os textos originais para não invalidar os offsets anotados.

## LinkedIn

Depois de concluir e conseguir defender a avaliação, adicione: **Reconhecimento de Entidades Nomeadas (NER)**, **spaCy** e **NLP multilíngue**.

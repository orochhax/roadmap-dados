# Enunciado — Extrator de entidades para tickets multilíngues

## Cenário real

Depois de classificar o ticket, o Assistente de Suporte precisa reconhecer qual empresa, domínio, produto e localidade foram citados. A equipe de cadastro usará esses trechos para procurar entidades canônicas. Um limite errado (`Acme` em vez de `Acme Brasil Ltda.`) pode gerar um vínculo incorreto.

## Entradas

Crie um arquivo JSONL anotado com pelo menos:

- `document_id`;
- `language`: `pt`, `en` ou `es`;
- `text`: texto original, sem alteração após a anotação;
- `entities`: lista de objetos com `start`, `end` e `label`.

Use os rótulos `ORG`, `DOMAIN`, `PRODUCT` e `LOCATION`. Inclua documentos sem entidade e pelo menos 20 entidades de cada tipo no conjunto total. Separe treino, validação e teste; expressões quase duplicadas não podem cruzar as divisões.

## Saídas obrigatórias

O arquivo `avaliar_ner.py` deverá gerar:

1. validação dos offsets e rótulos da entrada;
2. resultado de um baseline baseado em regras, dicionário ou expressões regulares;
3. resultado de um pipeline NER treinado ou adaptado com spaCy;
4. previsões JSONL com texto, entidades reais e previstas;
5. tabela de precisão, recall e F1 por tipo e por idioma;
6. relatório de erros de limite, tipo, entidade perdida e entidade inventada;
7. latência P50/P95 por documento.

## Regras

- Compare os métodos no mesmo teste congelado.
- Faça todas as transformações de texto antes da anotação; depois dela, preserve os índices.
- Não use uma lista construída com entidades observadas no teste.
- Uma entidade só é acerto exato quando `start`, `end` e `label` coincidirem.
- Resultados parciais por token podem ser usados apenas como diagnóstico.
- A análise deve separar pelo menos os três idiomas e os quatro tipos.
- Documente seed, versão do modelo e versão dos dados.

## Casos de borda obrigatórios

- texto sem nenhuma entidade;
- domínio com subdomínio, hífen ou sufixo de país;
- nome com acento e caracteres Unicode;
- entidades vizinhas ou sobrepostas;
- empresa com nome igual a uma palavra comum;
- organização desconhecida e produto escrito com erro;
- texto que mistura dois idiomas.

## Métricas

- principal: F1 exato por entidade;
- apoio: precisão e recall por tipo, F1 por idioma, taxa de entidades espúrias e latência P95;
- qualidade de dados: quantidade de offsets inválidos deve ser zero antes da avaliação.

## Critério de aceite

O pipeline só pode seguir para o entity matching se superar o F1 do baseline em pelo menos 0,05, tiver recall mínimo de 0,60 para `ORG` e `DOMAIN` e não apresentar diferença maior que 0,20 entre o melhor e o pior idioma. Caso não cumpra, entregue uma decisão de não promoção com pelo menos oito erros categorizados e uma hipótese testável para o próximo ciclo.

## Restrições

Não copie um treinamento pronto nem use o conjunto de teste para ampliar dicionários. Pesquise cada conceito separadamente e implemente no arquivo fornecido.

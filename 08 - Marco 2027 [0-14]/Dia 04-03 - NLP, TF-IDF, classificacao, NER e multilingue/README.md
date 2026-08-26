# NLP clássico: normalização, TF-IDF e classificação de texto + NLP aplicado: NER, dados multilíngues e análise de erros

**Data de estudo:** 04/03/2027
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — NLP clássico: normalização, TF-IDF e classificação de texto

#### O que pesquisar
- `NLP preprocessing português`
- `TF-IDF character n-grams`
- `TfidfVectorizer Pipeline`
- `text classification error analysis`

#### Aulas guiadas — NLP clássico com Codebasics

- [ ] Assista a [**NLP Pipeline: NLP Tutorial For Beginners In Python - S1 E6**](https://www.youtube.com/watch?v=S3EId9uatxI) (26min02s).
- [ ] Assista a [**Stemming and Lemmatization: NLP Tutorial For Beginners - S1 E10**](https://www.youtube.com/watch?v=HHAilAC3cXw) (16min46s).
- [ ] Assista a [**Named Entity Recognition (NER): NLP Tutorial For Beginners - S1 E12**](https://www.youtube.com/watch?v=2XUhKpH0p4M) (22min34s).
- [ ] Assista a [**Text Representation Using TF-IDF: NLP Tutorial For Beginners - S2 E6**](https://www.youtube.com/watch?v=ATK6fm3cYfI) (36min18s).
- Carga total de vídeo: 1h41min40s. A prática abaixo acrescenta classificação, análise multilíngue, métricas e análise de erros; não é necessário assistir ao restante da playlist neste dia.

**Arquivos da atividade:** [abrir a pasta `01-nlp-classico-normalizacao-tf-idf`](<atividades/01-nlp-classico-normalizacao-tf-idf/>)

#### Objetivo

Construir o primeiro componente do **Assistente de Suporte IA**: um classificador que recebe o texto de um ticket em português, inglês ou espanhol e sugere a fila correta. Você aprenderá a transformar texto em números com TF-IDF, criar um baseline honesto, evitar vazamento de dados e decidir quando o modelo deve se abster em vez de encaminhar um chamado com baixa confiança.

Ao terminar, você deve conseguir explicar por que acurácia isolada engana em classes desbalanceadas e como erros de roteamento afetam a operação.

#### Termos complementares para pesquisar

Faça as pesquisas na ordem abaixo e registre as fontes utilizadas no cabeçalho ou na documentação de `atividades/01-nlp-classico-normalizacao-tf-idf/classificador_tickets.py`:

1. `scikit-learn DummyClassifier most_frequent baseline`
2. `scikit-learn TfidfVectorizer word analyzer char_wb ngram_range`
3. `scikit-learn Pipeline text classification LogisticRegression`
4. `train test split duplicate text data leakage`
5. `multiclass classification macro F1 per class recall confusion matrix`
6. `predict_proba confidence threshold abstention classification`
7. `NLP text normalization accents Portuguese multilingual`
8. `text classification error analysis taxonomy`

#### O que você precisa compreender

- **TF-IDF:** dá mais peso a termos úteis para distinguir documentos e menos peso a termos muito comuns.
- **N-gramas de palavras e caracteres:** capturam expressões e variações como erros de digitação, abreviações e flexões.
- **Baseline:** solução simples usada como referência; um modelo novo só é útil se trouxer ganho mensurável.
- **Vazamento:** ocorre quando informações do teste influenciam o treino, deixando a avaliação artificialmente otimista.
- **Abstenção:** encaminhamento para revisão humana quando a confiança é insuficiente.

#### O que fazer

Leia [o enunciado completo](<atividades/01-nlp-classico-normalizacao-tf-idf/ENUNCIADO.md>) e implemente em `atividades/01-nlp-classico-normalizacao-tf-idf/classificador_tickets.py`. Registre dados, comandos, métricas, erros e decisão no próprio artefato.

O resultado desta atividade será reutilizado na Atividade 2 — NER, avaliação por entidade e dados multilíngues — e, depois, no produto de entity matching.

#### LinkedIn

Somente após executar e explicar o trabalho, adicione: **Processamento de Linguagem Natural (NLP)**, **Scikit-learn** e **Classificação de texto**.

### Atividade 2 — NLP aplicado: NER, dados multilíngues e análise de erros

#### O que pesquisar
- `named entity recognition`
- `BIO tagging`
- `multilingual NLP`
- `entity-level F1`

**Arquivos da atividade:** [abrir a pasta `02-nlp-aplicado-ner-dados-multilingues`](<atividades/02-nlp-aplicado-ner-dados-multilingues/>)

#### Objetivo

Adicionar ao **Assistente de Suporte IA** uma etapa que localiza entidades mencionadas pelo cliente. A saída servirá como entrada para o entity matching: por exemplo, `Acme Brasil`, `acme.com.br` e `Salvador` precisam manter seus limites de caracteres e tipos corretos para que o registro canônico seja encontrado depois.

Você avaliará correspondência exata de entidade, não apenas acerto por token, e investigará diferenças entre português, inglês e espanhol.

#### Termos complementares para pesquisar

1. `named entity recognition span start end offsets`
2. `BIO IOB2 tagging named entity recognition`
3. `spaCy EntityRuler rule based NER baseline`
4. `spaCy custom NER DocBin training data`
5. `spaCy Scorer ents_p ents_r ents_f`
6. `multilingual NER Portuguese Spanish English`
7. `Unicode normalization character offsets NLP`
8. `NER boundary error type error error analysis`

#### Conceitos que você deve dominar

- **Entidade:** trecho com significado definido, como empresa, domínio, produto ou localidade.
- **Span:** intervalo `início:fim` que aponta para os caracteres exatos no texto.
- **BIO/IOB2:** convenção que marca começo, continuação e exterior de uma entidade.
- **F1 por entidade:** só considera correta uma previsão com limite e tipo compatíveis.
- **Análise por idioma:** impede que um bom resultado médio esconda falhas em uma língua.

#### O que fazer

Siga [o enunciado](<atividades/02-nlp-aplicado-ner-dados-multilingues/ENUNCIADO.md>) no arquivo `atividades/02-nlp-aplicado-ner-dados-multilingues/avaliar_ner.py` e documente a execução no próprio artefato. Preserve os textos originais para não invalidar os offsets anotados.

#### LinkedIn

Depois de concluir e conseguir defender a avaliação, adicione: **Reconhecimento de Entidades Nomeadas (NER)**, **spaCy** e **NLP multilíngue**.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

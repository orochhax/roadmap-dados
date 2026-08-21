# NLP clássico para triagem de tickets: normalização, TF-IDF e classificação

## Objetivo

Construir o primeiro componente do **Assistente de Suporte IA**: um classificador que recebe o texto de um ticket em português, inglês ou espanhol e sugere a fila correta. Você aprenderá a transformar texto em números com TF-IDF, criar um baseline honesto, evitar vazamento de dados e decidir quando o modelo deve se abster em vez de encaminhar um chamado com baixa confiança.

Ao terminar, você deve conseguir explicar por que acurácia isolada engana em classes desbalanceadas e como erros de roteamento afetam a operação.

## Pesquise estes nomes exatos

Faça as pesquisas na ordem abaixo e registre as fontes utilizadas em `03-evidencias/README.md`:

1. `scikit-learn DummyClassifier most_frequent baseline`
2. `scikit-learn TfidfVectorizer word analyzer char_wb ngram_range`
3. `scikit-learn Pipeline text classification LogisticRegression`
4. `train test split duplicate text data leakage`
5. `multiclass classification macro F1 per class recall confusion matrix`
6. `predict_proba confidence threshold abstention classification`
7. `NLP text normalization accents Portuguese multilingual`
8. `text classification error analysis taxonomy`

## O que você precisa compreender

- **TF-IDF:** dá mais peso a termos úteis para distinguir documentos e menos peso a termos muito comuns.
- **N-gramas de palavras e caracteres:** capturam expressões e variações como erros de digitação, abreviações e flexões.
- **Baseline:** solução simples usada como referência; um modelo novo só é útil se trouxer ganho mensurável.
- **Vazamento:** ocorre quando informações do teste influenciam o treino, deixando a avaliação artificialmente otimista.
- **Abstenção:** encaminhamento para revisão humana quando a confiança é insuficiente.

## Entrega obrigatória

Leia [o enunciado completo](<01-exercicios/ENUNCIADO.md>) e implemente em `01-exercicios/classificador_tickets.py`. Registre dados, comandos, métricas, erros e decisão em [evidências](<03-evidencias/README.md>).

O resultado desta sessão será reutilizado no N13 para extrair entidades citadas nos tickets e, depois, no produto de entity matching.

## LinkedIn

Somente após executar e explicar o trabalho, adicione: **Processamento de Linguagem Natural (NLP)**, **Scikit-learn** e **Classificação de texto**.

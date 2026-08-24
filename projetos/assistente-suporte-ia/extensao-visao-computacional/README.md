# Extensão obrigatória — Triagem visual de campo

Esta extensão adiciona uma tarefa de visão computacional ao projeto de suporte
sem fingir que ela e o RAG são o mesmo modelo. A aplicação terá duas entradas:

- texto: consulta ao assistente RAG existente;
- imagem: classificação ou detecção de anomalia para triagem de campo.

Consulte também o [projeto de suporte](../README.md), o
[data card](data_card.md), o [backlog](backlog.md), a
[apresentação em inglês](docs/presentation-en.md) e a
[versão em inglês](README.en.md).

## Problema e usuário

- **Problema:** priorizar imagens de cabos ou equipamentos com possível defeito.
- **Usuário:** supervisor de manutenção de campo.
- **Decisão:** encaminhar para inspeção urgente, fila normal ou revisão humana.

O modelo não autoriza reparo automaticamente e não substitui inspeção técnica.

## Dados

Use a categoria cable do conjunto MVTec AD ou outra fonte pública equivalente
aprovada no roadmap. Antes do download, registre URL, versão, licença, data,
hash, classes e restrições em data_card.md. Versione apenas uma amostra permitida
ou um manifesto; não faça commit de arquivos grandes sem necessidade.

## Baseline

Implemente um baseline barato antes da rede neural:

- descritores simples de imagem com regressão logística ou k-NN; ou
- embeddings congelados com classificador linear.

## Modelo PyTorch

Implemente transfer learning compacto com MobileNetV3 ou ResNet18. Congele o
protocolo de split e métricas antes de treinar. Augmentation é permitido apenas
no treino.

## Métricas

- PR-AUC;
- recall da classe defeito;
- macro-F1 e matriz de confusão;
- calibração ou confiança por faixa;
- latência de inferência em CPU;
- erros por subtipo disponível.

## Testes

Teste leitura e shape, normalização, separação sem duplicatas, augmentation
somente em treino, seed, saída do modelo, inferência em CPU e política de
revisão.

## Artefatos

- manifesto e protocolo de dados;
- baseline e benchmark PyTorch;
- modelo e model card;
- galeria de falsos positivos/negativos;
- explicação visual, como Grad-CAM, sem tratá-la como prova causal;
- rota ou CLI separada da rota RAG;
- apresentação em inglês.

## Concluído quando

- Baseline e modelo usam exatamente o mesmo teste.
- O split impede duplicatas ou imagens relacionadas em lados diferentes.
- A inferência funciona em CPU com comando documentado.
- Limiares e revisão humana refletem o custo dos erros.
- A galeria mostra erros, não somente acertos.
- A interface deixa claro que texto e imagem são tarefas independentes.
- Testes passam e métricas reconciliam com artefatos.
- README.en.md e docs/presentation-en.md contêm resultados reais.

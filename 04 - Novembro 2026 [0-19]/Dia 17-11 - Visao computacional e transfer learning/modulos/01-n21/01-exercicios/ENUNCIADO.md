# Enunciado — Triagem visual de defeitos em ativos de telecom

## Cenário real

Técnicos enviam fotos durante inspeções de campo. A operação quer priorizar imagens com indícios de dano e separar defeitos por categoria. Você usará um conjunto público de defeitos industriais como proxy e avaliará se transfer learning supera uma referência simples sem memorizar objetos ou fundos.

## Entradas

Organize imagens e metadados com:

- `image_id`, `asset_or_group_id`, `captured_at` quando disponível;
- caminho da imagem;
- classe `normal` ou uma categoria de defeito;
- origem e licença.

Escolha um conjunto público com pelo menos três classes totais. Se várias fotos pertencem ao mesmo objeto/lote, preserve `asset_or_group_id` para divisão por grupo. Explique por que os dados são apenas um proxy de telecom.

## Saídas obrigatórias

`classificar_defeitos.py` deverá gerar:

1. auditoria de imagens corrompidas, dimensões e distribuição das classes;
2. divisão por grupo entre treino, validação e teste;
3. baseline de classe majoritária ou features simples;
4. modelo pré-treinado com backbone congelado;
5. experimento controlado de fine-tuning parcial;
6. métricas, matriz de confusão e previsões do teste;
7. exemplos Grad-CAM de acertos e erros;
8. latência, tamanho do modelo e recomendação de uso.

## Regras

- Augmentation ocorre somente no treino; validação/teste usam transformações determinísticas.
- Fotos do mesmo ativo, sequência ou lote não podem atravessar divisões.
- Registre pesos pré-treinados e versões do PyTorch/Torchvision.
- Escolha arquitetura, épocas e camadas descongeladas pela validação.
- Trate desbalanceamento e compare sempre com o baseline.
- Grad-CAM não substitui métricas nem garante que o modelo aprendeu o defeito certo.
- Não coloque dataset ou checkpoint pesado no Git.

## Casos de borda obrigatórios

- arquivo corrompido ou formato não suportado;
- imagem muito escura, borrada ou rotacionada;
- resolução e proporção incomuns;
- classe rara;
- fundo que aparece apenas em uma classe;
- foto sem o ativo ou com vários ativos;
- imagem fora do domínio do conjunto de treino.

## Métricas

- principal: macro-F1;
- segurança: recall da classe de defeito mais crítico;
- apoio: precisão/recall por classe, balanced accuracy, matriz de confusão, latência P95 e tamanho do modelo;
- fatias: iluminação, resolução e origem/grupo quando disponíveis.

## Critério de aceite

O protótipo só é aprovado para uma triagem controlada se melhorar o macro-F1 do baseline em pelo menos 0,10, atingir recall mínimo de 0,80 para o defeito crítico definido previamente e respeitar o orçamento local de latência. A inspeção Grad-CAM deve mostrar pelo menos cinco acertos e cinco erros; se o modelo se apoiar em fundo ou marca d'água, rejeite a implantação mesmo com métrica alta.

## Restrições

Não treine a partir do zero nem copie um notebook completo. Implemente o pipeline no arquivo inicial e diferencie claramente evidência do proxy e expectativa no cenário de telecom.

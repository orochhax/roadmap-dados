# Visão computacional II: localizar defeitos com detecção e segmentação

## Objetivo

Ir além da classe global do N21 e localizar a região danificada. Você comparará caixas delimitadoras e máscaras em um cenário de inspeção de ativos, implementará métricas geométricas e aprenderá a avaliar corretamente imagens sem objeto, múltiplas ocorrências e diferentes limiares de confiança.

## Pesquise estes nomes exatos

1. `object detection versus semantic instance segmentation`
2. `COCO bounding box annotation format xywh category_id`
3. `intersection over union bounding boxes implementation`
4. `COCO mean average precision mAP 50 95`
5. `Dice coefficient binary segmentation masks`
6. `empty mask IoU Dice edge case`
7. `precision recall confidence threshold object detection`
8. `torchvision object detection finetuning tutorial`

## Conceitos essenciais

- **Detecção:** prevê classe e caixa para cada objeto.
- **Segmentação:** atribui pixels à região de interesse.
- **IoU:** mede a interseção dividida pela união.
- **mAP:** resume precisão/recall em limiares e classes.
- **Dice:** mede sobreposição de máscaras e precisa de regra explícita para máscaras vazias.

## Entrega obrigatória

Implemente e teste o avaliador solicitado no [enunciado](<01-exercicios/ENUNCIADO.md>) usando `01-exercicios/avaliar_segmentacao.py`. Documente dados, convenções e resultados em [evidências](<03-evidencias/README.md>).

## LinkedIn

Depois de concluir, adicione: **Detecção de objetos**, **Segmentação de imagens** e **Avaliação de visão computacional**.

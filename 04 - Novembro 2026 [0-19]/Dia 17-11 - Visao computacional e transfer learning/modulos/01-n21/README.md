# Visão computacional I: classificação de defeitos com transfer learning

## Objetivo

Criar um protótipo para apoiar inspeções de caixas, conectores e outros ativos de telecom. A partir de uma foto, o sistema deverá distinguir condição normal de tipos de defeito. Como um conjunto público pode representar defeitos industriais em vez de ativos de telecom, você também terá de documentar a diferença entre o proxy acadêmico e o uso real.

## Pesquise estes nomes exatos

1. `PyTorch transfer learning image classification tutorial ResNet18`
2. `torchvision ImageFolder Dataset DataLoader`
3. `torchvision transforms v2 data augmentation`
4. `freeze backbone fine tune classifier PyTorch`
5. `image dataset leakage same object train test`
6. `multiclass macro F1 confusion matrix imbalanced images`
7. `Grad-CAM PyTorch image classification explanation`
8. `MVTec AD dataset license industrial defects`

## Conceitos essenciais

- **Transfer learning:** reutiliza features aprendidas em muitas imagens.
- **Backbone congelado:** evita atualizar inicialmente a maior parte da rede.
- **Data augmentation:** cria variações plausíveis apenas durante o treino.
- **Leakage visual:** fotos do mesmo objeto/local em treino e teste inflam a métrica.
- **Grad-CAM:** destaca regiões que influenciaram a classe, mas não prova causalidade.

## Entrega obrigatória

Implemente o [enunciado](<01-exercicios/ENUNCIADO.md>) em `01-exercicios/classificar_defeitos.py` e preencha [evidências](<03-evidencias/README.md>). Não versione pesos grandes nem imagens sem licença.

## LinkedIn

Depois de validar o protótipo, adicione: **Visão computacional**, **Transfer Learning** e **Torchvision**.

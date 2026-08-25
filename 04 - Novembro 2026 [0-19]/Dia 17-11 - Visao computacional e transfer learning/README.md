# Visão computacional I: classificação e transfer learning

**Data de estudo:** 17/11/2026  
**Carga planejada:** 2 a 4 horas

## Aula selecionada no YouTube

- [ ] **Redes Neurais Convolucionais com PyTorch | Visão Computacional | Deep Learning #2** — [abrir no YouTube](https://www.youtube.com/watch?v=doT7koXt9vw).

**Recorte deste dia:** de 00:00 até 1:50:06, passando por imagens, CIFAR-10, pré-processamento, DataLoader, MLP, GPU, CrossEntropyLoss, treinamento e avaliação. Não assista ao restante hoje.

**Carga de vídeo selecionada:** aproximadamente 1h50.

**Prática obrigatória:** execute o enunciado local de classificação e transfer learning. O vídeo usa classificação no CIFAR-10 e não substitui a comparação entre modelo congelado, fine-tuning e baseline exigida na atividade.

## Atividades do dia

### Atividade 1 — Visão computacional I: classificação e transfer learning

#### O que pesquisar
- `PyTorch transfer learning`
- `torchvision transforms`
- `image classification PR-AUC`
- `Grad-CAM`

**Arquivos da atividade:** [abrir a pasta `01-visao-computacional-i-classificacao`](<atividades/01-visao-computacional-i-classificacao/>)

#### Objetivo

Criar um protótipo para apoiar inspeções de caixas, conectores e outros ativos de telecom. A partir de uma foto, o sistema deverá distinguir condição normal de tipos de defeito. Como um conjunto público pode representar defeitos industriais em vez de ativos de telecom, você também terá de documentar a diferença entre o proxy acadêmico e o uso real.

#### Termos complementares para pesquisar

1. `PyTorch transfer learning image classification tutorial ResNet18`
2. `torchvision ImageFolder Dataset DataLoader`
3. `torchvision transforms v2 data augmentation`
4. `freeze backbone fine tune classifier PyTorch`
5. `image dataset leakage same object train test`
6. `multiclass macro F1 confusion matrix imbalanced images`
7. `Grad-CAM PyTorch image classification explanation`
8. `MVTec AD dataset license industrial defects`

#### O que você precisa entender

- **Transfer learning:** reutiliza features aprendidas em muitas imagens.
- **Backbone congelado:** evita atualizar inicialmente a maior parte da rede.
- **Data augmentation:** cria variações plausíveis apenas durante o treino.
- **Leakage visual:** fotos do mesmo objeto/local em treino e teste inflam a métrica.
- **Grad-CAM:** destaca regiões que influenciaram a classe, mas não prova causalidade.

#### O que fazer

Implemente o [enunciado](<atividades/01-visao-computacional-i-classificacao/ENUNCIADO.md>) em `atividades/01-visao-computacional-i-classificacao/classificar_defeitos.py` e preencha registro no próprio artefato. Não versione pesos grandes nem imagens sem licença.

#### LinkedIn

Depois de validar o protótipo, adicione: **Visão computacional**, **Transfer Learning** e **Torchvision**.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

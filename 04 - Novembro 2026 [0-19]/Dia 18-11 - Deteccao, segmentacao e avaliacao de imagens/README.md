# Visão computacional II: detecção, segmentação, IoU, mAP e Dice

**Data de estudo:** 18/11/2026  
**Carga planejada:** 2 a 4 horas

## Continuação da aula selecionada

- [ ] **Redes Neurais Convolucionais com PyTorch | Visão Computacional | Deep Learning #2** — [abrir no YouTube a partir de 1:50:06](https://www.youtube.com/watch?v=doT7koXt9vw&t=6606s).

**Recorte deste dia:** de 1:50:06 até o fim, cobrindo intuição de convolução, criação, treino, avaliação e uso da CNN em imagens próprias.

**Carga de vídeo selecionada:** aproximadamente 1h01.

**Limite da aula:** este recorte ensina CNN para classificação, mas não cobre todo o conteúdo de detecção e segmentação. A prática local com bounding boxes, IoU, mAP, máscaras e Dice continua integralmente obrigatória.

## Atividades do dia

### Atividade 1 — Visão computacional II: detecção, segmentação, IoU, mAP e Dice

#### O que pesquisar
- `object detection vs segmentation`
- `IoU`
- `mAP`
- `Dice coefficient`

**Arquivos da atividade:** [abrir a pasta `01-visao-computacional-ii-deteccao`](<atividades/01-visao-computacional-ii-deteccao/>)

#### Objetivo

Ir além da classe global produzida na atividade de visão computacional e transfer learning e localizar a região danificada. Você comparará caixas delimitadoras e máscaras em um cenário de inspeção de ativos, implementará métricas geométricas e aprenderá a avaliar corretamente imagens sem objeto, múltiplas ocorrências e diferentes limiares de confiança.

#### Termos complementares para pesquisar

1. `object detection versus semantic instance segmentation`
2. `COCO bounding box annotation format xywh category_id`
3. `intersection over union bounding boxes implementation`
4. `COCO mean average precision mAP 50 95`
5. `Dice coefficient binary segmentation masks`
6. `empty mask IoU Dice edge case`
7. `precision recall confidence threshold object detection`
8. `torchvision object detection finetuning tutorial`

#### O que você precisa entender

- **Detecção:** prevê classe e caixa para cada objeto.
- **Segmentação:** atribui pixels à região de interesse.
- **IoU:** mede a interseção dividida pela união.
- **mAP:** resume precisão/recall em limiares e classes.
- **Dice:** mede sobreposição de máscaras e precisa de regra explícita para máscaras vazias.

#### O que fazer

Implemente e teste o avaliador solicitado no [enunciado](<atividades/01-visao-computacional-ii-deteccao/ENUNCIADO.md>) usando `atividades/01-visao-computacional-ii-deteccao/avaliar_segmentacao.py`. Documente dados, convenções e resultados no próprio artefato.

#### LinkedIn

Depois de concluir, adicione: **Detecção de objetos**, **Segmentação de imagens** e **Avaliação de visão computacional**.

## Entrega real de portfólio

**Intelligent Support Operations — triagem visual**

Siga o [brief do projeto](<../../projetos/assistente-suporte-ia/extensao-visao-computacional/README.md>). A entrega precisa ter problema e usuário definidos, data card, dados reproduzíveis, baseline, métricas escolhidas antes do resultado, análise de erros, testes, README em português e inglês e apresentação de 2–3 minutos em inglês. Documente também resultados negativos.

## Publicação da semana no LinkedIn

- **Tema específico:** avaliação de uma triagem visual que localiza defeitos em ativos, comparando baseline, detecção e segmentação sem esconder erros.
- **Tipo:** entrega.
- **Formato:** carrossel visual com sobreposições de verdade e previsão, acompanhado de uma tabela curta de métricas.
- **Artefato/evidência exigida:** `atividades/01-visao-computacional-ii-deteccao/avaliar_segmentacao.py` executado, evidências preenchidas, teste manual de IoU/Dice, resultados por classe/tamanho, latência em CPU e imagens cuja licença permita publicação.

### Roteiro para preencher

- **Problema operacional:** [qual defeito precisa ser localizado e qual erro é mais caro?]
- **Dataset e licença:** [qual fonte foi usada e por que as imagens podem ser mostradas?]
- **Baseline e modelos avaliados:** [quais abordagens foram comparadas no mesmo split?]
- **Resultado verificável:** [mAP, AP50, IoU, Dice, recall crítico ou latência, com caminho da evidência]
- **Erro visual:** [qual imagem representa o erro mais importante e o que ele ensina?]
- **Decisão:** [protótipo aceito, rejeitado ou encaminhado para revisão humana, e por quê?]
- **Link:** [repositório, relatório ou demonstração conferidos]

### Limitação obrigatória

Declare a diferença entre o conjunto de imagens usado e ativos reais de telecom, incluindo o risco de mudança de domínio.

### Cuidado contra afirmações falsas

Não chame um experimento com dados públicos ou proxy de sistema implantado em campo. Não publique imagens, anotações ou pesos sem licença. Esta publicação não antecipa Competências nem alteração de headline.

### Checklist de publicação

- [ ] Validei o split por ativo/grupo e os testes manuais de IoU e Dice.
- [ ] Recalculei as métricas exibidas e mantive o baseline visível.
- [ ] Selecionei exemplos de erro representativos, sem escolher apenas acertos.
- [ ] Confirmei licença e ausência de dados sensíveis em todas as imagens.
- [ ] Registrei latência, decisão operacional e limitação de domínio.
- [ ] **URL publicada:**
- [ ] **Data da publicação:**

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

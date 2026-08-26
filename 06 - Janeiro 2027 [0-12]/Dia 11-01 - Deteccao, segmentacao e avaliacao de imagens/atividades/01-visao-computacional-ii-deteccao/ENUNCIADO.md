# Enunciado — Localização de danos em equipamentos de rede

## Cenário real

Uma classificação `com defeito` não informa ao técnico onde está o problema. Você precisa avaliar um protótipo que delimita e segmenta corrosão, trinca ou componente danificado em fotos de inspeção. Um falso negativo pode atrasar manutenção; caixas ou máscaras imprecisas reduzem a utilidade em campo.

## Entradas

Use um conjunto público com caixas/máscaras de defeitos ou anote um pequeno conjunto licenciado. Registre:

- imagens com `image_id` e `asset_or_group_id`;
- caixas em formato COCO e suas categorias;
- máscaras binárias ou polígonos com dimensão conhecida;
- previsões com classe, confiança, caixa e/ou máscara.

Inclua imagens sem defeito, com um defeito e com múltiplos defeitos. Separe por ativo/grupo para evitar leakage.

## Saídas obrigatórias

`avaliar_segmentacao.py` deverá produzir:

1. validação de caixas, máscaras, dimensões e categorias;
2. implementação própria e testada de IoU para caixas e Dice para máscaras;
3. baseline geométrico simples documentado;
4. avaliação das previsões de um detector e de um segmentador adaptados ou pré-treinados;
5. mAP, IoU e Dice agregados e por classe/tamanho;
6. análise de limiares de confiança;
7. imagens de erro com verdade e previsão sobrepostas;
8. latência e recomendação operacional.

## Regras

- Declare a convenção das caixas (`xyxy` ou `xywh`) e converta explicitamente.
- Caixa inválida, com área negativa ou fora da imagem, deve ser rejeitada ou corrigida com log.
- Defina antes do teste como IoU/Dice tratam duas máscaras vazias.
- Faça o pareamento entre previsões e verdade sem contar o mesmo objeto duas vezes.
- Escolha confiança e IoU na validação.
- Calcule resultados por classe e por objeto pequeno/médio/grande.
- Não reporte somente exemplos visuais; inclua o conjunto inteiro.

## Casos de borda obrigatórios

- caixa e máscara idênticas à verdade;
- nenhuma sobreposição;
- sobreposição parcial calculável à mão;
- verdade vazia e previsão vazia;
- falso positivo em imagem sem defeito;
- duas previsões para o mesmo objeto;
- objeto cortado na borda da imagem;
- máscara com dimensão diferente da imagem.

## Métricas

- detecção: mAP@[0.50:0.95], AP50, precisão e recall por classe;
- segmentação: Dice e IoU médios por classe;
- operação: recall do defeito crítico, falso positivo por imagem e latência P95;
- fatias: tamanho do objeto, iluminação e origem do ativo.

## Critério de aceite

Primeiro, os testes manuais de IoU/Dice devem produzir exatamente os valores esperados. Para recomendar o protótipo, exija recall mínimo de 0,85 no defeito crítico, AP50 e Dice superiores ao baseline e latência dentro do limite definido antes do teste. Se as metas não forem alcançadas, entregue a ferramenta de avaliação e rejeite a aplicação, indicando se o problema é anotação, detecção, segmentação ou mudança de domínio.

## Restrições

Não copie uma função completa de métricas. Bibliotecas podem ser usadas depois para conferir sua implementação. Não versione imagens ou pesos sem licença.

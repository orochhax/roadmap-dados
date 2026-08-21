# Evidências — N21: classificação visual de defeitos

## Dataset e adequação ao problema

- nome, URL, versão e licença:
- classes e quantidade de imagens:
- definição de `asset_or_group_id`:
- como duplicatas e imagens corrompidas foram tratadas:
- diferenças entre o dataset proxy e ativos reais de telecom:

## Ambiente e treinamento

- hardware e versões de Python/PyTorch/Torchvision:
- pesos pré-treinados:
- seed, transformações e comando:
- camadas congeladas/descongeladas:

## Resultados congelados

| abordagem | macro-F1 | recall crítico | balanced accuracy | P95 | tamanho |
|---|---:|---:|---:|---:|---:|
| baseline |  |  |  |  |  |
| backbone congelado |  |  |  |  |  |
| fine-tuning parcial |  |  |  |  |  |

## Auditoria visual

Para cinco acertos e cinco erros, registre classe real, previsão, confiança, interpretação cautelosa do Grad-CAM e possível artefato do conjunto.

## Decisão

- protótipo aprovado/rejeitado:
- classe/fatia mais fraca:
- risco de mudança de domínio para telecom:
- dado real que seria necessário antes de um piloto:

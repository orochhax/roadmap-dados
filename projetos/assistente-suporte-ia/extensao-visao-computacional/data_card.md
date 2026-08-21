# Data card — Extensão de visão computacional

## Fonte a registrar antes do uso

- nome/versão: TODO;
- URL oficial: TODO;
- licença e permissão de redistribuição: TODO;
- data de acesso: TODO;
- categoria(s): TODO;
- quantidade e tamanho: TODO;
- hash do arquivo ou manifesto: TODO.

Fonte candidata: categoria cable do MVTec AD. Confirme termos e versão em vez
de presumir que todo o conjunto pode ser republicado.

## Unidade e label

- unidade: uma imagem;
- label operacional: normal, possível defeito ou revisão;
- origem do label: TODO;
- subtipos de defeito: TODO;
- grupos relacionados que não podem cruzar splits: TODO.

## Split

Defina treino, validação e teste antes do tuning. Imagens duplicadas, derivações
da mesma imagem ou grupos do mesmo objeto devem ficar no mesmo split.

## Transformações

| Transformação | Treino | Validação/teste | Justificativa |
|---|---|---|---|
| resize/normalização | TODO | TODO | TODO |
| augmentation | TODO | não | TODO |

## Limitações e riscos

- domínio industrial pode diferir de campo telecom real;
- classes e iluminação podem ser artificiais ou controladas;
- explicação visual não prova que o modelo aprendeu a causa correta;
- falso negativo pode atrasar uma inspeção necessária;
- nenhum dado de pessoa ou local sensível deve ser publicado.

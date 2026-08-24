# Causalidade IV: controle sintético e placebos

**Data de estudo:** 07/10/2026  
**Carga planejada:** 2 a 4 horas

## Atividades do dia

### Atividade 1 — Causalidade IV: controle sintético e placebos

#### O que pesquisar
- `synthetic control method`
- `donor pool`
- `RMSPE pré-tratamento`
- `placebo tests`

**Arquivos da atividade:** [abrir a pasta `01-causalidade-iv-controle-sintetico`](<atividades/01-causalidade-iv-controle-sintetico/>)

#### Objetivo

Construir um contrafactual ponderado para uma única região tratada, avaliar o ajuste antes da intervenção e comparar o gap observado com placebos. O método só será aceito se os doadores reproduzirem bem o pré-período.

#### Termos complementares para pesquisar

- `synthetic control method Abadie donor pool`
- `synthetic control nonnegative weights sum to one`
- `pre treatment RMSPE synthetic control`
- `synthetic control in space placebo test`
- `post pre RMSPE ratio synthetic control`
- `leave one out synthetic control sensitivity`
- `convex hull synthetic control extrapolation`
- `scipy optimize minimize constraints`

#### O que fazer

Leia o [enunciado](<atividades/01-causalidade-iv-controle-sintetico/ENUNCIADO.md>), implemente [controle_sintetico.py](<atividades/01-causalidade-iv-controle-sintetico/controle_sintetico.py>) e registre pesos, placebos e decisão no próprio artefato.

#### Como validar

- o donor pool é definido antes de observar o pós;
- pesos obedecem às restrições e ajustam o pré-período;
- o gap é comparado a placebos e sensibilidades;
- mau ajuste prévio impede uma conclusão forte.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

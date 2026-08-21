# TCC — piloto randomizado simulado e efeito incremental

**Data de estudo:** 21/01/2027  
**Carga planejada:** 4 a 5 horas

## Objetivo do dia

Estimar o efeito incremental da campanha no piloto sintético randomizado e traduzir a incerteza em ganho por 100 contatos e custo por retenção. O ranking de churn ajuda a definir uma população prioritária, mas a comparação causal vem da atribuição aleatória do piloto.

## Assuntos para pesquisar

Pesquise exatamente:

- `intention to treat effect randomized experiment binary outcome`
- `difference in proportions confidence interval randomized trial`
- `incremental gain per 100 treated customers`
- `cost per incremental retained customer`
- `heterogeneous treatment effects subgroup analysis caution`
- `randomized experiment noncompliance ITT versus treatment on treated`

Siga o [guia e o roteiro](<modulos/01-e136/README.md>). Controle sintético e modelos avançados de uplift permanecem fora do escopo.

## Integração

Use o ranking de risco apenas conforme o protocolo congelado para definir elegibilidade ou slices. Preserve a randomização dentro do piloto e relate efeito médio, intervalo e limites; não transforme análise exploratória de slices em regra causal individual.

## Concluído quando

- [ ] O efeito por intenção de tratar foi estimado com intervalo de confiança.
- [ ] Ganho por 100 contatos e custo por retenção usam premissas explícitas.
- [ ] Slices pré-especificados exibem tamanho, efeito e incerteza, e o resultado sintético e os limites de generalização estão visíveis.

# TCC — dados sintéticos, contrato temporal e protocolo

**Data de estudo:** 19/01/2027  
**Carga planejada:** 4 a 5 horas

## Objetivo do dia

Construir e auditar os dois conjuntos do TCC: snapshots temporais para prever churn e um piloto randomizado explicitamente simulado para medir resposta à campanha. O protocolo deve impedir que tratamento, resultado ou informação futura virem features do modelo de risco.

## Assuntos para pesquisar

Pesquise exatamente:

- `synthetic churn dataset temporal customer snapshots`
- `decision timestamp prediction horizon feature availability`
- `data leakage churn model post outcome variables`
- `randomized experiment intention to treat treatment assignment`
- `randomization balance check standardized mean difference`
- `data card synthetic data limitations`

Siga o [guia e o roteiro](<modulos/01-e134/README.md>) e preserve o escopo congelado do TCC.

## Integração

O snapshot preditivo responde quem tem maior risco antes da campanha. O piloto simulado responde quanto a campanha alterou retenção entre grupos randomizados. Mantenha schemas, datas, alvos e métricas separados.

## Concluído quando

- [ ] Os dois datasets têm schema, seed, período, hash e declaração de simulação.
- [ ] A disponibilidade de cada coluna foi comparada com a data de decisão, e os splits temporais e o protocolo do piloto foram congelados.
- [ ] Testes de schema, duplicatas, leakage e randomização têm resultado esperado definido.

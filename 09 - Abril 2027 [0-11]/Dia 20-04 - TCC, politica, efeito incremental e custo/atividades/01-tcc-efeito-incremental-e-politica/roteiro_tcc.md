# TCC — roteiro do efeito incremental sem respostas

> Use o piloto sintético congelado. Preencha métodos e resultados próprios; não apague os enunciados.

## 1. Protocolo herdado

- versão/hash do piloto:
- população elegível:
- unidade de randomização:
- probabilidade de atribuição:
- tratamento e controle:
- desfecho/horizonte:
- estimando primário:
- capacidade de contatos:

## 2. Integridade e equilíbrio

| Verificação | Resultado esperado | Resultado observado | Decisão |
|---|---|---|---|
| IDs únicos |  |  |  |
| atribuição válida |  |  |  |
| desfecho observável |  |  |  |
| contagem por grupo |  |  |  |
| equilíbrio das covariáveis |  |  |  |

Explique por que não rerandomizou após observar desfechos:

<!-- Preencha aqui. -->

## 3. Estimativa principal por intenção de tratar

| Grupo atribuído | N | Retidos | Taxa de retenção |
|---|---:|---:|---:|
| controle |  |  |  |
| tratamento |  |  |  |

- efeito absoluto:
- efeito relativo, se apropriado:
- método do intervalo de confiança:
- limite inferior/superior:
- interpretação sem extrapolar:

## 4. Testes da métrica

Crie casos pequenos com resultado calculável manualmente.

| Caso | Efeito/IC esperado | Resultado observado | Passou? |
|---|---|---|---|
| grupos iguais |  |  |  |
| efeito positivo simples |  |  |  |
| efeito negativo |  |  |  |
| grupo vazio/inválido |  |  |  |

## 5. Ganho e custo

- ganho incremental por 100 contatos e intervalo:
- custo unitário de contato:
- custo total:
- retenções incrementais estimadas:
- custo por retenção incremental:
- regra para efeito zero, negativo ou IC inconclusivo:

## 6. Slices pré-especificados

| Slice | N controle | N tratamento | Efeito | IC | Ganho/100 | Limitação |
|---|---:|---:|---:|---|---:|---|
|  |  |  |  |  |  |  |

- ajuste/alerta para múltiplas comparações:
- slice exploratório que não virará conclusão:

## 7. Política sob capacidade

| Política | Elegibilidade | Contatos | Ganho esperado | Custo | Regra de não execução |
|---|---|---:|---:|---:|---|
| baseline |  |  |  |  |  |
| priorização por risco |  |  |  |  |  |

Explique por que a comparação não estima efeito individual de tratamento:

<!-- Preencha aqui. -->

## 8. Limites de inferência

- o que a randomização simulada permite demonstrar:
- por que não há evidência de impacto em uma operadora real:
- ameaça à validade externa:
- hipótese que exigiria um piloto real:

## Aceite

- ITT, intervalo, ganho/100 e custo foram reconciliados.
- Resultado zero, negativo ou inconclusivo tem tratamento correto.
- Slices exibem N e limites.
- Nenhuma alegação real foi feita com dados simulados.

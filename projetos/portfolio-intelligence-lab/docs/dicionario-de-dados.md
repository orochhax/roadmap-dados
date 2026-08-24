# Dicionário de dados

## Escopo

Uma classe com 10–20 ativos e preços ajustados. Todo campo usado no score precisa ter data de disponibilidade auditável.

## Tabelas mínimas

| Tabela | Campo | Tipo | Regra |
|---|---|---|---|
| ativos | ticker | texto | chave única do ativo |
| ativos | data_inicio | data | primeira data elegível |
| ativos | data_fim | data/nulo | última data elegível |
| precos_ajustados | data | data | data de referência do preço |
| precos_ajustados | ticker | texto | chave para ativos |
| precos_ajustados | preco_ajustado | decimal positivo | preço usado nos retornos |
| precos_ajustados | disponivel_em | data | não pode superar o corte da decisão |
| precos_ajustados | fonte | texto | origem rastreável |
| fatores | momentum | decimal/nulo | retorno da janela congelada |
| fatores | volatilidade | decimal/nulo | desvio dos retornos da janela |
| fatores | score | decimal | combinação padronizada dos dois fatores |
| ranking | posicao | inteiro positivo | ordem do score por data |
| resultados_carteira | estrategia | categoria | pesos_iguais ou top_k |
| resultados_carteira | retorno_liquido | decimal | retorno bruto menos custo |

## Validações

- ticker/data são únicos nos preços;
- preços são positivos;
- `disponivel_em <= data_rebalanceamento` para toda observação usada;
- o universo contém entre 10 e 20 tickers;
- fonte, período e hash do snapshot estão registrados.

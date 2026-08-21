# Metodologia do score quantitativo

## Finalidade

Ordenar ativos de uma única classe com regras transparentes. O score não prevê preço nem recomenda compra ou venda.

## Fatores

- **Momentum:** `preco_t / preco_t-j - 1`, usando somente datas anteriores ao rebalanceamento.
- **Volatilidade:** desvio-padrão dos retornos na janela congelada.
- **Padronização:** z-score calculado transversalmente em cada data.
- **Score:** `z_momentum - z_volatilidade`.

Registre no protocolo o tamanho das janelas, tratamento de ausentes e regra de desempate.

## Uso permitido

- comparar ranking e carteira Top-K com pesos iguais;
- analisar estabilidade, custos, risco e períodos ruins;
- explicar a contribuição dos dois fatores.

## Limitações

- associação histórica não garante retorno;
- universo pequeno e janela escolhida limitam generalização;
- custos e disponibilidade de dados podem alterar conclusões;
- mudanças de regime podem tornar o score instável.

## Evidências

- [ ] cálculo manual de dois ativos em duas datas;
- [ ] teste que altera dados posteriores sem mudar score já calculado;
- [ ] tabela com momentum, volatilidade, score e posição.

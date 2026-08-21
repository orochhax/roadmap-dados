# TCC — efeito incremental e política de retenção

## Objetivo

Avaliar o piloto randomizado simulado sem quebrar a randomização e converter o resultado em uma política de retenção sob capacidade. A unidade causal é o cliente atribuído, e o estimando primário é definido antes de olhar os resultados.

## Preparação

- **Enunciado local:** `01-exercicios/roteiro_tcc.md`.
- **Projeto canônico:** `projetos/telecom-customer-intelligence/`.
- **Entradas:** piloto sintético congelado, protocolo de elegibilidade/randomização, ranking do champion e premissas de custo.
- **Saídas esperadas:** análise em `src/telecom_customer_intelligence/causal.py`, métricas em `outputs/` e política documentada em `docs/`.

## Pesquise exatamente

- `intention to treat randomized experiment binary retention outcome`
- `risk difference confidence interval two proportions`
- `bootstrap confidence interval treatment effect experiment`
- `incremental conversions per 100 contacts`
- `cost effectiveness incremental retained customers`
- `subgroup treatment effect multiple comparisons caution`

## Núcleo essencial

1. [ ] Confira elegibilidade, atribuição, integridade e equilíbrio sem rerandomizar por conveniência.
2. [ ] Calcule o baseline ingênuo da taxa geral e depois o efeito por intenção de tratar.
3. [ ] Produza intervalo de confiança com método declarado e teste casos calculáveis.
4. [ ] Traduza o efeito para ganho incremental por 100 contatos.
5. [ ] Calcule custo por retenção incremental e trate efeito zero/negativo sem divisão enganosa.
6. [ ] Avalie slices pré-especificados de risco e operação, exibindo tamanho e incerteza.
7. [ ] Compare políticas dentro da capacidade sem escolher retrospectivamente o melhor slice.

## Regras de inferência

- A atribuição aleatória simulada sustenta a comparação apenas dentro do universo e gerador sintéticos.
- Análise principal é por intenção de tratar; não descarte quem não recebeu o contato.
- Intervalo que cruza zero impede afirmar efeito positivo conclusivo.
- Slice exploratório não comprova heterogeneidade sem poder e protocolo adequados.
- Não apresente ganho sintético como retenção real, economia real ou impacto de produção.

## Casos de borda

- grupo vazio ou extremamente pequeno;
- ausência de desfecho;
- não conformidade entre atribuição e tratamento recebido;
- efeito zero ou negativo;
- custo por retenção indefinido;
- slice sem poder mínimo;
- capacidade menor que a população elegível.

## Fora do escopo

Controle sintético, causal forest, uplift complexo, múltiplas campanhas adaptativas e qualquer dado real não autorizado.

## Concluído quando

- [ ] Efeito, intervalo, ganho por 100 e custo estão reconciliados.
- [ ] A política respeita capacidade e protocolo.
- [ ] Slices e resultados negativos são apresentados honestamente.
- [ ] Limites da simulação impedem alegação de impacto real.

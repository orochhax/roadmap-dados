# TCC: fatores e motor de ranking

## Preparação
- **Enunciado local:** `01-exercicios/roteiro_tcc.md`.
- **Saídas canônicas:** `projetos/portfolio-intelligence-lab/src/features/fatores.py`, `projetos/portfolio-intelligence-lab/src/ranking/motor_ranking.py` e tabelas em `projetos/portfolio-intelligence-lab/data/processed/`.

## Manifesto de entradas

- **Obrigatórias:** preços ajustados, universo elegível e protocolo de datas.
- **Fallback local:** use a amostra congelada e produza `fatores.parquet` e `ranking.parquet` na pasta canônica.

## Aprenda agora

- **Definição:** momentum pode ser `P_t/P_{t-12}-1`; volatilidade é desvio-padrão dos retornos; z-score é `(x-média)/desvio`; Top-K seleciona os maiores scores.
- **Exemplo mínimo:** padronize fatores por data, inverta o sinal da volatilidade e use `score = z_momentum - z_volatilidade`.
- **Erro comum:** padronizar usando datas diferentes juntas ou calcular retorno de avaliação dentro da feature.

## Núcleo essencial

1. [ ] Calcule dois fatores usando apenas janelas anteriores: momentum e volatilidade.
2. [ ] Padronize os fatores na data de cada rebalanceamento e crie um score simples com pesos documentados.
3. [ ] Gere o ranking por data e confira manualmente dois ativos em dois rebalanceamentos.
4. [ ] Avalie estabilidade do ranking e retorno futuro dos Top-K sem tratar associação como garantia de retorno.

## Prática obrigatória

- [ ] Compare pesos iguais entre fatores com os pesos documentados.

## Concluído quando

- [ ] Os módulos e as tabelas canônicas contêm todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

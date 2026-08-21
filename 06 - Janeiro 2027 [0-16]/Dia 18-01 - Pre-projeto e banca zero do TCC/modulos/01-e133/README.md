# Pré-projeto e banca zero — churn e efeito incremental

## Objetivo

Congelar um TCC mínimo, reproduzível e defensável sobre priorização de campanhas de retenção em telecom. O produto servirá a uma pessoa gerente de retenção que possui capacidade limitada de contatos e precisa equilibrar risco, custo e efeito incremental.

## Preparação

- **Enunciado local:** `01-exercicios/roteiro_atividades.md`.
- **Projeto canônico:** `projetos/telecom-customer-intelligence/`.
- **Saída esperada:** `docs/tcc-pre-projeto.md` dentro do projeto canônico.
- **Dados:** somente dados sintéticos ou públicos permitidos; a simulação deve ser declarada no data card, relatório e apresentação.

## Pesquise exatamente

- `prediction versus causal inference churn retention`
- `decision timestamp target horizon data leakage churn`
- `top K capacity constrained targeting recall at K`
- `randomized controlled trial intention to treat effect`
- `confidence interval difference in proportions`
- `ML project champion challenger rollback`

## Decisões que precisam ser congeladas

1. data em que a campanha decide quem contatar;
2. horizonte em que churn e retenção serão observados;
3. capacidade `K` de contatos por ciclo;
4. custos de contato e definição de retenção;
5. métrica preditiva principal e estimando causal principal;
6. splits temporais e período do piloto simulado;
7. critérios de promoção, retreino e rollback.

## Núcleo essencial

1. [ ] Escreva uma pergunta preditiva e uma pergunta causal, sem misturá-las.
2. [ ] Defina usuário, decisão, data de corte, horizonte e capacidade operacional.
3. [ ] Congele regra de negócio, regressão logística e XGBoost como candidatos preditivos.
4. [ ] Defina um piloto sintético randomizado para estimar resposta ao tratamento e descreva seus limites externos.
5. [ ] Congele PR-AUC, recall@K, calibração, custo por retenção, efeito/IC, ganho por 100 contatos e slices.
6. [ ] Planeje MLflow, testes de schema/leakage/métricas, monitoramento temporal, champion/challenger, retreino e rollback.
7. [ ] Registre explicitamente os itens fora do escopo.

## Banca zero obrigatória

Apresente em oito minutos e responda sem ampliar o projeto:

- Por que alto risco de churn não significa alto efeito da campanha?
- O que exatamente é sintético e o que o TCC não pode afirmar sobre clientes reais?
- Qual informação estará disponível na data de decisão?
- Como a capacidade muda a avaliação do modelo?
- Qual resultado faria você manter a regra de negócio?

## Concluído quando

- [ ] O pré-projeto cabe em duas páginas e não possui decisão estrutural aberta.
- [ ] Predição, experimento e política operacional têm contratos separados.
- [ ] A declaração de dados sintéticos e os limites de inferência estão visíveis.
- [ ] As críticas da banca viraram cortes, testes ou critérios de aceite.

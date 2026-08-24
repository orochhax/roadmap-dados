# TCC — pré-projeto e banca zero sobre retenção incremental

**Data de estudo:** 18/01/2027  
**Carga planejada:** 4 a 5 horas

## Tema congelado

**Do risco de churn ao efeito incremental: priorização de campanhas de retenção em telecom sob restrição de capacidade**

O TCC deve responder duas perguntas diferentes: quem apresenta maior risco de churn e qual efeito incremental uma campanha produz. Prever risco não prova resposta ao tratamento; essa distinção precisa aparecer desde o pré-projeto.

## Atividades do dia

Pesquise exatamente:

- `churn prediction retention campaign capacity constraint`
- `randomized experiment incremental treatment effect retention`
- `PR-AUC recall at K probability calibration churn`
- `cost per retained customer campaign evaluation`
- `machine learning project scope pre registration`

Depois siga o guia e o enunciado disponíveis abaixo e preencha o roteiro sem copiar texto pronto.

### Conteúdo e atividades — Pré-projeto e banca zero — churn e efeito incremental

**Arquivos da atividade:** [abrir a pasta `01-pre-projeto-e-banca-zero-churn-e-efeito`](<atividades/01-pre-projeto-e-banca-zero-churn-e-efeito/>)

#### Objetivo

Congelar um TCC mínimo, reproduzível e defensável sobre priorização de campanhas de retenção em telecom. O produto servirá a uma pessoa gerente de retenção que possui capacidade limitada de contatos e precisa equilibrar risco, custo e efeito incremental.

#### Arquivos e dados

- **Enunciado local:** `atividades/01-pre-projeto-e-banca-zero-churn-e-efeito/roteiro_atividades.md`.
- **Projeto canônico:** `projetos/telecom-customer-intelligence/`.
- **Saída esperada:** `docs/tcc-pre-projeto.md` dentro do projeto canônico.
- **Dados:** somente dados sintéticos ou públicos permitidos; a simulação deve ser declarada no data card, relatório e apresentação.

#### Pesquise exatamente

- `prediction versus causal inference churn retention`
- `decision timestamp target horizon data leakage churn`
- `top K capacity constrained targeting recall at K`
- `randomized controlled trial intention to treat effect`
- `confidence interval difference in proportions`
- `ML project champion challenger rollback`

#### Decisões que precisam ser congeladas

1. data em que a campanha decide quem contatar;
2. horizonte em que churn e retenção serão observados;
3. capacidade `K` de contatos por ciclo;
4. custos de contato e definição de retenção;
5. métrica preditiva principal e estimando causal principal;
6. splits temporais e período do piloto simulado;
7. critérios de promoção, retreino e rollback.

#### O que fazer

- [ ] Escreva uma pergunta preditiva e uma pergunta causal, sem misturá-las.
- [ ] Defina usuário, decisão, data de corte, horizonte e capacidade operacional.
- [ ] Congele regra de negócio, regressão logística e XGBoost como candidatos preditivos.
- [ ] Defina um piloto sintético randomizado para estimar resposta ao tratamento e descreva seus limites externos.
- [ ] Congele PR-AUC, recall@K, calibração, custo por retenção, efeito/IC, ganho por 100 contatos e slices.
- [ ] Planeje MLflow, testes de schema/leakage/métricas, monitoramento temporal, champion/challenger, retreino e rollback.
- [ ] Registre explicitamente os itens fora do escopo.

#### Banca zero obrigatória

Apresente em oito minutos e responda sem ampliar o projeto:

- Por que alto risco de churn não significa alto efeito da campanha?
- O que exatamente é sintético e o que o TCC não pode afirmar sobre clientes reais?
- Qual informação estará disponível na data de decisão?
- Como a capacidade muda a avaliação do modelo?
- Qual resultado faria você manter a regra de negócio?

#### Como validar

- O pré-projeto cabe em duas páginas e não possui decisão estrutural aberta.
- Predição, experimento e política operacional têm contratos separados.
- A declaração de dados sintéticos e os limites de inferência estão visíveis.
- As críticas da banca viraram cortes, testes ou critérios de aceite.

## Escopo obrigatório

- data de decisão, horizonte do churn e capacidade máxima de contatos;
- regra de negócio, regressão logística e XGBoost;
- piloto sintético randomizado, identificado em toda publicação como simulação;
- PR-AUC, recall@K, calibração, custo por retenção, efeito com intervalo de confiança, ganho por 100 contatos e slices;
- MLflow, testes, monitoramento temporal, champion/challenger, retreino e rollback.

## Fora do escopo

Controle sintético, múltiplas nuvens, LLMs, entity matching, forecasting e aplicação grande. Não acrescente esses itens na banca.

## Finalização

Antes de concluir, confirme:

- O pré-projeto separa predição de risco e inferência do efeito da campanha.
- Data de decisão, horizonte, capacidade, métricas e custos foram congelados antes dos resultados.
- Dados e piloto estão descritos honestamente como sintéticos, e a banca zero gerou cortes ou critérios verificáveis sem ampliar o escopo.

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

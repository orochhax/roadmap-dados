# Enunciado — avaliar oferta de retenção não randomizada

## Cenário real

Atendentes ofereceram desconto principalmente a clientes com NPS baixo e muitos chamados. O churn dos que receberam oferta não pode ser comparado diretamente ao restante. Você deverá criar uma amostra observacional reproduzível e avaliar se há comparabilidade suficiente.

## Entradas

- `dados/clientes_telecom.csv`;
- uma tabela `ofertas_retencao.csv` gerada com seed 42, contendo `cliente_id`, `oferta` e `churn_30d`;
- a probabilidade de receber oferta deve depender de variáveis prévias como NPS, chamados, atraso, plano e tempo de cliente, mantendo alguma sobreposição;
- crie uma segunda versão com quase nenhuma sobreposição para testar a falha.

## Saídas

- [propensity_score.py](propensity_score.py) completo;
- `diagnostico_propensity.csv` com score, tratamento, peso, par e inclusão;
- `balanceamento.csv` com SMD antes, após matching e após IPW;
- `estimativas_causais.json` com ATT/ATE, incerteza, ESS e sensibilidades;
- [evidências](../03-evidencias/README.md).

## Regras obrigatórias

1. Declare ATT ou ATE antes do ajuste e faça matching/ponderação coerentes com ele.
2. Use somente variáveis anteriores à oferta; `churn_30d` nunca entra no propensity.
3. Separe geração da amostra e análise para não reajustar o gerador após ver o efeito.
4. Inspecione histogramas/densidades dos scores e identifique suporte comum.
5. Calcule SMD de todas as covariáveis antes e depois; não use p-valor de diferença como diagnóstico principal.
6. Faça matching por vizinho mais próximo com caliper declarado e registre descartes.
7. Calcule pesos estabilizados, ESS e distribuição dos pesos.
8. Repita com trimming em dois limites pré-definidos e compare a estimativa.
9. Compare matching e IPW sem escolher apenas o resultado mais favorável.

## Casos de borda obrigatórios

- score exatamente 0 ou 1;
- peso extremo;
- estrato sem tratado ou sem controle;
- covariável ausente;
- cliente duplicado;
- variável pós-tratamento oferecida como feature;
- caliper que descarta muitos tratados;
- base de baixa sobreposição.

## Métricas

- máximo e mediana do `|SMD|` antes/depois;
- percentual de covariáveis com `|SMD| <= 0,10`;
- tratados/controles retidos no matching;
- peso mínimo, mediano, p99 e máximo;
- ESS por grupo;
- ATT/ATE, IC95% e sensibilidade ao trimming.

## Critério de aceite

- [ ] O resultado ingênuo é comparado a matching e IPW.
- [ ] Todos os diagnósticos são calculados antes da conclusão causal.
- [ ] A base sem overlap é rejeitada ou recebe conclusão fortemente limitada.
- [ ] Pesos infinitos/nulos não passam silenciosamente.
- [ ] A decisão cita balanceamento, ESS, estimativa e confundimento não observado.


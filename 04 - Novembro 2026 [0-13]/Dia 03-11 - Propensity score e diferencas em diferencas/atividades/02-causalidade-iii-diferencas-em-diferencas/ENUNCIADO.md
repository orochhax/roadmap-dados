# Enunciado — rollout regional do diagnóstico automático

## Cenário real

Salvador recebeu um diagnóstico automático em uma data definida; Feira de Santana, Vitória da Conquista e Aracaju ainda usavam o fluxo antigo. Operações quer saber se a duração média dos incidentes caiu por causa do rollout ou por uma melhoria geral da rede.

## Entradas

Gere com seed 42 um painel `painel_incidentes_semanais.csv`:

- cidades `Salvador`, `Feira de Santana`, `Vitória da Conquista` e `Aracaju`;
- 16 semanas, com oito antes e oito depois;
- colunas `cidade`, `semana`, `tratada`, `pos`, `duracao_media`, `volume` e `chuva_mm`;
- apenas Salvador é tratada na semana 9;
- injete efeito conhecido de aproximadamente -12 minutos após o rollout;
- gere uma segunda base com tendência prévia diferente em Salvador.

## Saídas

- [diferencas_em_diferencas.py](diferencas_em_diferencas.py) completo;
- `resultado_did.json` com estimador manual, regressão, IC e decisão;
- `event_study.csv` com coeficientes relativos à intervenção;
- gráfico de médias por grupo e gráfico do estudo de evento;
- registro no próprio artefato.

## Regras obrigatórias

1. Declare unidade, tratamento, data, resultado, comparador e estimando antes da geração.
2. Calcule manualmente o DiD 2x2 e reconcilie com o coeficiente da interação `tratada * pos`.
3. Use dados agregados semanalmente com peso/volume justificado; não misture média de médias sem ponderação.
4. Estime erros robustos agrupados por cidade e reconheça a limitação de poucos clusters.
5. Construa event study com uma semana prévia como referência e coeficientes de leads/lags.
6. Faça um placebo com data falsa no pré-período.
7. Reestime removendo uma cidade doadora por vez.
8. Na base com tendência prévia divergente, recuse a conclusão causal forte.

## Casos de borda obrigatórios

- semana ausente em uma cidade;
- volume igual a zero;
- antecipação uma semana antes do rollout;
- cidade controle recebe política concorrente;
- tendência prévia divergente;
- data de placebo;
- grande diferença de volume entre cidades;
- somente duas cidades disponíveis.

## Métricas

- estimador DiD, IC95% e erro padrão agrupado;
- diferença máxima entre cálculo manual e regressão;
- coeficientes e IC dos leads pré-tratamento;
- efeito do placebo;
- variação do efeito no leave-one-city-out;
- distância entre efeito estimado e efeito injetado na base válida.

## Critério de aceite

- Estimador manual e regressão reconciliam dentro de tolerância declarada.
- O efeito injetado é recuperado aproximadamente na base válida.
- Pretrends, placebo e sensibilidade aparecem antes da conclusão.
- A base inválida produz alerta explícito, não causalidade automática.
- A limitação de poucos clusters é explicada.


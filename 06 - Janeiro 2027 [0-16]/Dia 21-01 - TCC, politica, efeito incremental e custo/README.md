# TCC — piloto randomizado simulado e efeito incremental

**Data de estudo:** 21/01/2027  
**Carga planejada:** 4 a 5 horas

## Objetivo do dia

Estimar o efeito incremental da campanha no piloto sintético randomizado e traduzir a incerteza em ganho por 100 contatos e custo por retenção. O ranking de churn ajuda a definir uma população prioritária, mas a comparação causal vem da atribuição aleatória do piloto.

## Atividades do dia

Pesquise exatamente:

- `intention to treat effect randomized experiment binary outcome`
- `difference in proportions confidence interval randomized trial`
- `incremental gain per 100 treated customers`
- `cost per incremental retained customer`
- `heterogeneous treatment effects subgroup analysis caution`
- `randomized experiment noncompliance ITT versus treatment on treated`

Siga o guia e o roteiro disponíveis abaixo. Controle sintético e modelos avançados de uplift permanecem fora do escopo.

### Conteúdo e atividades — TCC — efeito incremental e política de retenção

**Arquivos da atividade:** [abrir a pasta `01-tcc-efeito-incremental-e-politica`](<atividades/01-tcc-efeito-incremental-e-politica/>)

#### Objetivo

Avaliar o piloto randomizado simulado sem quebrar a randomização e converter o resultado em uma política de retenção sob capacidade. A unidade causal é o cliente atribuído, e o estimando primário é definido antes de olhar os resultados.

#### Arquivos e dados

- **Enunciado local:** `atividades/01-tcc-efeito-incremental-e-politica/roteiro_tcc.md`.
- **Projeto canônico:** `projetos/telecom-customer-intelligence/`.
- **Entradas:** piloto sintético congelado, protocolo de elegibilidade/randomização, ranking do champion e premissas de custo.
- **Saídas esperadas:** análise em `src/telecom_customer_intelligence/causal.py`, métricas em `outputs/` e política documentada em `docs/`.

#### Pesquise exatamente

- `intention to treat randomized experiment binary retention outcome`
- `risk difference confidence interval two proportions`
- `bootstrap confidence interval treatment effect experiment`
- `incremental conversions per 100 contacts`
- `cost effectiveness incremental retained customers`
- `subgroup treatment effect multiple comparisons caution`

#### O que fazer

- [ ] Confira elegibilidade, atribuição, integridade e equilíbrio sem rerandomizar por conveniência.
- [ ] Calcule o baseline ingênuo da taxa geral e depois o efeito por intenção de tratar.
- [ ] Produza intervalo de confiança com método declarado e teste casos calculáveis.
- [ ] Traduza o efeito para ganho incremental por 100 contatos.
- [ ] Calcule custo por retenção incremental e trate efeito zero/negativo sem divisão enganosa.
- [ ] Avalie slices pré-especificados de risco e operação, exibindo tamanho e incerteza.
- [ ] Compare políticas dentro da capacidade sem escolher retrospectivamente o melhor slice.

#### Regras de inferência

- A atribuição aleatória simulada sustenta a comparação apenas dentro do universo e gerador sintéticos.
- Análise principal é por intenção de tratar; não descarte quem não recebeu o contato.
- Intervalo que cruza zero impede afirmar efeito positivo conclusivo.
- Slice exploratório não comprova heterogeneidade sem poder e protocolo adequados.
- Não apresente ganho sintético como retenção real, economia real ou impacto de produção.

#### Casos de borda

- grupo vazio ou extremamente pequeno;
- ausência de desfecho;
- não conformidade entre atribuição e tratamento recebido;
- efeito zero ou negativo;
- custo por retenção indefinido;
- slice sem poder mínimo;
- capacidade menor que a população elegível.

#### Fora do escopo

Controle sintético, causal forest, uplift complexo, múltiplas campanhas adaptativas e qualquer dado real não autorizado.

#### Como validar

- Efeito, intervalo, ganho por 100 e custo estão reconciliados.
- A política respeita capacidade e protocolo.
- Slices e resultados negativos são apresentados honestamente.
- Limites da simulação impedem alegação de impacto real.

## Integração do dia

Use o ranking de risco apenas conforme o protocolo congelado para definir elegibilidade ou slices. Preserve a randomização dentro do piloto e relate efeito médio, intervalo e limites; não transforme análise exploratória de slices em regra causal individual.

## Finalização

Antes de concluir, confirme:

- O efeito por intenção de tratar foi estimado com intervalo de confiança.
- Ganho por 100 contatos e custo por retenção usam premissas explícitas.
- Slices pré-especificados exibem tamanho, efeito e incerteza, e o resultado sintético e os limites de generalização estão visíveis.

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

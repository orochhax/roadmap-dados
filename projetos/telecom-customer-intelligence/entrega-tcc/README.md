# Entrega do TCC — Do risco de churn ao efeito incremental

**Título completo:** Do risco de churn ao efeito incremental: priorização de
campanhas de retenção em telecom sob restrição de capacidade.

Este diretório contém o enunciado e os arquivos iniciais da entrega acadêmica.
Ele reutiliza o problema, os contratos e os dados do
[Telecom Customer Intelligence](../README.md), mas congela um recorte menor e
defensável como TCC. A implementação e os resultados devem ser produzidos pelo
estudante.

Documentos: [data card](data_card.md), [backlog](backlog.md),
[README em inglês](README.en.md) e
[apresentação em inglês](docs/presentation-en.md).

## Regra de honestidade experimental

Os dados de clientes compartilhados são sintéticos. Qualquer atribuição de
campanha, resposta à campanha ou efeito causal criado para este TCC também deve
ser identificado, no arquivo e nos metadados, como **sintético**. O trabalho
demonstra método, reprodutibilidade e limites; ele não prova impacto em uma
operadora real.

É proibido apresentar números de exemplo como resultados executados. Substitua
os TODOs somente após gerar artefatos reproduzíveis.

## Problema, usuário e decisão

- **Problema:** a equipe não consegue contatar todos os clientes com risco de
  churn e precisa escolher uma política de priorização.
- **Usuário:** gerente de retenção de uma operadora de telecomunicações.
- **Decisão:** selecionar até `K` clientes elegíveis em cada data de decisão.
- **Restrição:** capacidade e custo da campanha devem ser definidos antes de
  comparar os métodos.
- **Risco metodológico:** alto risco de churn não significa necessariamente que
  uma ação mudará o comportamento daquele cliente.

## Pergunta de pesquisa

> Sob uma capacidade limitada de contatos, uma política orientada pelo efeito
> incremental esperado produz uma decisão mais útil que uma regra de negócio ou
> uma política baseada apenas no risco de churn?

Antes da análise, registre no relatório:

- hipótese principal e hipótese nula: TODO;
- horizonte do desfecho: TODO;
- capacidade `K` ou percentual da base: TODO;
- custo por contato e valor de uma retenção: TODO;
- métrica primária e critérios de decisão: TODO;
- segmentos de segurança e equidade: TODO.

## Escopo congelado

### Incluído

1. Uma data de decisão por janela e um único horizonte principal de churn.
2. Uma regra de negócio reproduzível.
3. Regressão logística como baseline preditivo.
4. XGBoost como candidato tabular.
5. Um estimador causal simples para resposta heterogênea, com premissas
   documentadas.
6. Quatro políticas comparáveis: aleatória, regra, risco e efeito incremental.
7. Avaliação preditiva, causal, operacional e por segmentos.
8. MLflow, janela de monitoramento, champion/challenger e uma simulação de
   retreinamento e rollback.

### Fora do núcleo do TCC

- LLM, RAG, entity matching ou previsão de tráfego;
- vários métodos causais concorrentes;
- infraestrutura cloud completa, Kubernetes ou pipeline distribuído;
- aplicativo de produção ou dashboard que esconda a metodologia;
- alegações de impacto real a partir dos dados sintéticos.

FastAPI, Docker ou uma visualização simples podem ser demonstrativos separados,
mas não substituem a avaliação acadêmica.

## Dados e protocolo

Consulte o [data card do projeto pai](../data_card.md) e os
[dados compartilhados](../../../dados/README.md). Não altere os CSVs originais.
Crie derivados somente dentro de `data/processed/` e registre comando, versão,
seed e hash.

O protocolo deve produzir:

1. uma tabela de decisão com somente informações disponíveis no instante da
   decisão;
2. splits temporais de treino, validação, teste e monitoramento;
3. um piloto de retenção sintético, com atribuição de tratamento reproduzível;
4. metadados que declarem explicitamente a origem sintética do tratamento e do
   desfecho usado na avaliação causal.

## Fases de implementação

| Fase | Starter | Pergunta que deve responder |
|---|---|---|
| Dados | `src/telecom_retention_thesis/data.py` | O que estava disponível na data de decisão? |
| Modelos | `src/telecom_retention_thesis/models.py` | Quem apresenta risco e quem pode responder à ação? |
| Política | `src/telecom_retention_thesis/policy.py` | Quem será selecionado sem exceder a capacidade? |
| Avaliação | `src/telecom_retention_thesis/evaluation.py` | A conclusão permanece útil em métricas e segmentos definidos antes? |
| Monitoramento | `src/telecom_retention_thesis/monitoring.py` | Quando promover, retreinar ou reverter um modelo? |

As funções iniciais levantam `NotImplementedError` de propósito. Os testes em
`tests/` estão marcados como exercícios e devem ser habilitados gradualmente.

## Baselines e candidatos

- **Aleatório:** amostra elegíveis sem usar o desfecho.
- **Regra de negócio:** combinação simples e documentada de sinais disponíveis.
- **Risco:** probabilidade calibrada de churn, começando por regressão logística.
- **Efeito incremental:** estimativa da diferença esperada entre agir e não agir.

Compare todas as políticas na mesma população, período, capacidade e função de
custo. Não declare vitória porque um modelo é mais complexo.

## Métricas obrigatórias

### Predição de churn

- PR-AUC;
- recall no Top-K;
- Brier score e curva de calibração;
- custo dos falsos positivos e falsos negativos;
- desempenho por pelo menos dois segmentos pré-declarados.

### Efeito e política

- efeito médio/ITT com intervalo de confiança;
- ganho incremental por 100 contatos;
- AUUC ou Qini, se adequado ao desenho escolhido;
- valor líquido esperado da política;
- sensibilidade a capacidade e custo sem escolher parâmetros depois do resultado.

### Operação

- qualidade e atraso dos dados;
- drift de dados e de desempenho;
- versão de dados, código, parâmetros e modelo;
- motivo registrado para manter, promover, retreinar ou reverter.

## Artefatos esperados

- protocolo de pesquisa congelado antes do benchmark;
- data card e manifesto dos derivados;
- código reutilizável e testes;
- registro MLflow dos experimentos selecionados;
- tabelas de métricas e análise de erros;
- relatório acadêmico com limitações e resultados negativos;
- README em português e inglês preenchidos com resultados executados;
- apresentação curta em inglês.

## Como começar

```powershell
python -m pip install -r requirements.txt
python -m pytest -q tests
```

No scaffold inicial, o pytest deve informar testes ignorados. Remova cada
marcação `skip` somente depois de implementar o comportamento correspondente.

## Concluído quando

- Pergunta, hipótese, horizonte, capacidade, custos e métrica primária foram congelados.
- Toda origem sintética está marcada nos dados, metadados e relatório.
- Nenhuma feature usa informação posterior à data de decisão.
- Os splits são temporais e a janela de monitoramento permanece intocada durante o desenvolvimento.
- Regra, regressão logística, XGBoost e estimador incremental foram comparados honestamente.
- As quatro políticas respeitam exatamente a mesma capacidade e população elegível.
- Incerteza, calibração, custo e pelo menos dois segmentos foram avaliados.
- Experimentos, dados e modelos possuem versões reproduzíveis.
- Retreinamento e rollback foram simulados com uma regra pré-definida.
- Código, testes, tabelas, texto e apresentação reconciliam entre si.
- As conclusões não extrapolam os limites dos dados sintéticos.


# TCC — roteiro do benchmark de risco sem respostas

> Implemente no projeto canônico e registre aqui decisões e evidências. Não preencha métricas antes de executar.

## 1. Contrato herdado

- versão/hash dos snapshots:
- data de decisão:
- horizonte:
- splits temporais:
- capacidade `K`:
- features aprovadas:
- features removidas por leakage:

## 2. Hipóteses antes do treino

| Candidato | Hipótese | Vantagem esperada | Custo/risco esperado | Critério para rejeitar |
|---|---|---|---|---|
| regra de negócio |  |  |  |  |
| regressão logística |  |  |  |  |
| XGBoost |  |  |  |  |

## 3. Pipeline e prevenção de leakage

- transformações ajustadas somente no treino:
- categorias desconhecidas:
- nulos:
- desbalanceamento:
- seeds:
- comandos:
- teste que prova que dados futuros não entram:

## 4. Registro no MLflow

| Run ID | Modelo | Versão dos dados | Seed | Parâmetros | Artefatos |
|---|---|---|---:|---|---|
|  | regra |  |  |  |  |
|  | logística |  |  |  |  |
|  | XGBoost |  |  |  |  |

## 5. Resultados de validação

| Modelo | PR-AUC | recall@K | Brier/calibração | latência P95 | observação |
|---|---:|---:|---:|---:|---|
| regra |  |  |  |  |  |
| logística |  |  |  |  |  |
| XGBoost |  |  |  |  |  |

- candidato selecionado antes do teste:
- justificativa:
- limiar/calibração escolhidos:

## 6. Teste temporal congelado

| Modelo final | PR-AUC | recall@K | lift@K | Brier | latência P95 |
|---|---:|---:|---:|---:|---:|
| regra |  |  |  |  |  |
| candidato selecionado |  |  |  |  |  |

## 7. Slices e erros

| Slice | N | positivos | PR-AUC | recall@K | calibração | interpretação cautelosa |
|---|---:|---:|---:|---:|---:|---|
|  |  |  |  |  |  |  |

- falso negativo mais custoso:
- falso positivo mais custoso:
- caso com score alto e incerteza operacional:
- slice sem amostra suficiente:

## 8. Champion/challenger

- champion:
- challenger:
- evidência da escolha:
- três trade-offs:
  1.
  2.
  3.
- gatilho de rollback:

## 9. Limite de interpretação

Explique por que o ranking mede risco e não efeito individual da campanha:

<!-- Preencha aqui. -->

## Aceite

- [ ] Mesmo split, pipeline e métricas para os três candidatos.
- [ ] Teste temporal foi usado apenas após a seleção.
- [ ] MLflow contém runs e artefatos reproduzíveis.
- [ ] Slices exibem tamanho de amostra e limites.

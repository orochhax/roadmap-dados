# Evidências — N20: MLP e MLflow

## Hipóteses antes dos experimentos

1. hipótese sobre arquitetura:
2. hipótese sobre regularização:
3. hipótese sobre desbalanceamento:

## Rastreabilidade

- versão/hash dos dados e divisões reutilizadas:
- versão do Python, PyTorch e MLflow:
- URI do tracking local/remoto sem credenciais:
- comandos para iniciar o MLflow e executar o treino:
- experimento e run IDs:

## Comparação de runs

| run ID | mudança testada | seed | melhor época | PR-AUC val. | recall@10% val. | Brier val. |
|---|---|---:|---:|---:|---:|---:|
|  | baseline linear |  |  |  |  |  |
|  | MLP base |  |  |  |  |  |
|  | regularização |  |  |  |  |  |
|  | desbalanceamento |  |  |  |  |  |

## Resultado final no teste

| modelo | PR-AUC | recall@10% | lift@10% | Brier | P95 | tamanho |
|---|---:|---:|---:|---:|---:|---:|
| linear N19 |  |  |  |  |  |  |
| MLP selecionada |  |  |  |  |  |  |

## Diagnóstico e decisão

- evidência de overfitting/regularização:
- estabilidade entre seeds:
- modelo escolhido e justificativa:
- condição de rollback:
- limitação que os experimentos não resolveram:

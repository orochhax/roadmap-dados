# Evidências — N19: training loop de churn

## Dados e corte temporal

- origem/licença ou geração:
- meses de treino, validação e teste:
- quantidade de clientes/linhas/positivos por divisão:
- features recusadas por vazamento temporal:

## Ambiente

- Python, PyTorch, NumPy e scikit-learn:
- CPU/GPU e RAM:
- seeds:
- comando de execução:

## Verificação do loop

- shapes e dtypes de um lote:
- loss e otimizador:
- quantidade de épocas e critério usado:
- evidência de `train`, `eval` e ausência de gradientes na inferência:

## Resultados

| método | PR-AUC | ROC-AUC | recall@10% | lift@10% | log loss | P95 |
|---|---:|---:|---:|---:|---:|---:|
| baseline |  |  |  |  |  |  |
| linear PyTorch |  |  |  |  |  |  |

Inclua loss de treino/validação por época e resultados por plano, região e tempo de contrato.

## Decisão

- piloto aprovado ou rejeitado:
- sinais de underfitting/overfitting:
- maior risco de vazamento:
- limitação do conjunto de dados:
- hipótese que será testada pela MLP no N20:

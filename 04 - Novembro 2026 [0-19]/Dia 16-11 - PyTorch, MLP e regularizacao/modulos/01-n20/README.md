# PyTorch II: MLP regularizada, desbalanceamento e MLflow

## Objetivo

Descobrir se uma rede neural multicamada melhora a priorização de churn em relação ao modelo linear do N19. Você executará experimentos rastreados, controlará overfitting e desbalanceamento e escolherá um modelo com base no ganho de negócio — não apenas na loss de treino.

## Pesquise estes nomes exatos

1. `PyTorch nn.Sequential MLP binary classification`
2. `ReLU dropout batch normalization tabular data`
3. `Adam weight_decay L2 regularization PyTorch`
4. `BCEWithLogitsLoss pos_weight imbalanced data`
5. `WeightedRandomSampler versus class weights PyTorch`
6. `early stopping validation loss PyTorch checkpoint`
7. `MLflow tracking PyTorch log_params log_metrics log_artifact`
8. `probability calibration Brier score reliability diagram`

## Conceitos essenciais

- **MLP:** combina camadas lineares e ativações para aprender relações não lineares.
- **Regularização:** reduz adaptação excessiva ao treino; inclui dropout, weight decay e early stopping.
- **Desbalanceamento:** positivos raros exigem métricas e tratamento apropriados.
- **Tracking:** registra parâmetros, métricas e artefatos para comparar e reproduzir execuções.
- **Calibração:** verifica se probabilidades previstas correspondem à frequência observada.

## Entrega obrigatória

Implemente o [enunciado](<01-exercicios/ENUNCIADO.md>) em `01-exercicios/treinar_mlp.py`. Execute MLflow de verdade e registre os run IDs e a comparação em [evidências](<03-evidencias/README.md>).

## LinkedIn

Após demonstrar os experimentos, adicione: **PyTorch**, **Redes neurais** e **MLflow**.

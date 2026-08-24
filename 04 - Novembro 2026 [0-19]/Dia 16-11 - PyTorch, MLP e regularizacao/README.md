# PyTorch II: MLP, regularização, desbalanceamento e tracking

**Data de estudo:** 16/11/2026  
**Carga planejada:** 2 a 4 horas

## Atividades do dia

### Atividade 1 — PyTorch II: MLP, regularização, desbalanceamento e tracking

#### O que pesquisar
- `PyTorch MLP`
- `dropout e weight decay`
- `class weights`
- `MLflow PyTorch`

**Arquivos da atividade:** [abrir a pasta `01-pytorch-ii-mlp-regularizacao`](<atividades/01-pytorch-ii-mlp-regularizacao/>)

#### Objetivo

Descobrir se uma rede neural multicamada melhora a priorização de churn em relação ao modelo linear da atividade anterior de PyTorch. Você executará experimentos rastreados, controlará overfitting e desbalanceamento e escolherá um modelo com base no ganho de negócio — não apenas na loss de treino.

#### Termos complementares para pesquisar

1. `PyTorch nn.Sequential MLP binary classification`
2. `ReLU dropout batch normalization tabular data`
3. `Adam weight_decay L2 regularization PyTorch`
4. `BCEWithLogitsLoss pos_weight imbalanced data`
5. `WeightedRandomSampler versus class weights PyTorch`
6. `early stopping validation loss PyTorch checkpoint`
7. `MLflow tracking PyTorch log_params log_metrics log_artifact`
8. `probability calibration Brier score reliability diagram`

#### O que você precisa entender

- **MLP:** combina camadas lineares e ativações para aprender relações não lineares.
- **Regularização:** reduz adaptação excessiva ao treino; inclui dropout, weight decay e early stopping.
- **Desbalanceamento:** positivos raros exigem métricas e tratamento apropriados.
- **Tracking:** registra parâmetros, métricas e artefatos para comparar e reproduzir execuções.
- **Calibração:** verifica se probabilidades previstas correspondem à frequência observada.

#### O que fazer

Implemente o [enunciado](<atividades/01-pytorch-ii-mlp-regularizacao/ENUNCIADO.md>) em `atividades/01-pytorch-ii-mlp-regularizacao/treinar_mlp.py`. Execute MLflow de verdade e registre os run IDs e a comparação no próprio artefato.

#### LinkedIn

Após demonstrar os experimentos, adicione: **PyTorch**, **Redes neurais** e **MLflow**.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

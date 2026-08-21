# PyTorch I: tensores e training loop para risco de churn

## Objetivo

Construir, sem esconder o treinamento atrás de uma função pronta, um classificador linear em PyTorch para o produto **Telecom Customer Intelligence**. O modelo priorizará clientes com risco de cancelar nos próximos 30 dias, respeitando a capacidade limitada da equipe de retenção.

O foco é entender o caminho completo: tensor → lote → saída do modelo → loss → gradiente → atualização → avaliação.

## Pesquise estes nomes exatos

1. `PyTorch tensor shape dtype device broadcasting`
2. `PyTorch custom Dataset __len__ __getitem__`
3. `PyTorch DataLoader batch_size shuffle num_workers`
4. `PyTorch autograd backward computational graph`
5. `optimizer zero_grad backward step PyTorch`
6. `BCEWithLogitsLoss versus sigmoid BCELoss`
7. `model train eval torch no_grad inference`
8. `PR AUC imbalanced binary classification churn`

## Conceitos essenciais

- **Tensor:** estrutura numérica com forma, tipo e dispositivo explícitos.
- **Autograd:** calcula gradientes das operações registradas no grafo.
- **Logit:** saída anterior à probabilidade; `BCEWithLogitsLoss` combina sigmoid e loss com estabilidade.
- **Epoch/lote:** uma passagem completa pelos dados e uma parte processada por atualização.
- **Ranking de risco:** a operação age apenas sobre os clientes de maior score.

## Entrega obrigatória

Implemente o fluxo do [enunciado](<01-exercicios/ENUNCIADO.md>) em `01-exercicios/treino_tensores.py` e preencha [evidências](<03-evidencias/README.md>). Não avance para a MLP do N20 sem conseguir explicar o efeito de `zero_grad()`, `backward()` e `step()`.

## LinkedIn

Quando o treinamento estiver reproduzível e compreendido, adicione: **PyTorch**, **Deep Learning** e **Modelagem preditiva**.

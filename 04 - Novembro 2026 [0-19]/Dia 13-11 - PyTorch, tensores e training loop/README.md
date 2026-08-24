# PyTorch I: tensores, Dataset, DataLoader, autograd e training loop

**Data de estudo:** 13/11/2026  
**Carga planejada:** 2 a 4 horas

## Atividades do dia

### Atividade 1 — PyTorch I: tensores, Dataset, DataLoader, autograd e training loop

#### O que pesquisar
- `PyTorch tensors`
- `Dataset e DataLoader`
- `autograd`
- `training e validation loop`

**Arquivos da atividade:** [abrir a pasta `01-pytorch-i-tensores-dataset-dataloader`](<atividades/01-pytorch-i-tensores-dataset-dataloader/>)

#### Objetivo

Construir, sem esconder o treinamento atrás de uma função pronta, um classificador linear em PyTorch para o produto **Telecom Customer Intelligence**. O modelo priorizará clientes com risco de cancelar nos próximos 30 dias, respeitando a capacidade limitada da equipe de retenção.

O foco é entender o caminho completo: tensor → lote → saída do modelo → loss → gradiente → atualização → avaliação.

#### Termos complementares para pesquisar

1. `PyTorch tensor shape dtype device broadcasting`
2. `PyTorch custom Dataset __len__ __getitem__`
3. `PyTorch DataLoader batch_size shuffle num_workers`
4. `PyTorch autograd backward computational graph`
5. `optimizer zero_grad backward step PyTorch`
6. `BCEWithLogitsLoss versus sigmoid BCELoss`
7. `model train eval torch no_grad inference`
8. `PR AUC imbalanced binary classification churn`

#### O que você precisa entender

- **Tensor:** estrutura numérica com forma, tipo e dispositivo explícitos.
- **Autograd:** calcula gradientes das operações registradas no grafo.
- **Logit:** saída anterior à probabilidade; `BCEWithLogitsLoss` combina sigmoid e loss com estabilidade.
- **Epoch/lote:** uma passagem completa pelos dados e uma parte processada por atualização.
- **Ranking de risco:** a operação age apenas sobre os clientes de maior score.

#### O que fazer

Implemente o fluxo do [enunciado](<atividades/01-pytorch-i-tensores-dataset-dataloader/ENUNCIADO.md>) em `atividades/01-pytorch-i-tensores-dataset-dataloader/treino_tensores.py` e preencha o registro no próprio artefato. Não avance para a atividade de MLP e regularização sem conseguir explicar o efeito de `zero_grad()`, `backward()` e `step()`.

#### LinkedIn

Quando o treinamento estiver reproduzível e compreendido, adicione: **PyTorch**, **Deep Learning** e **Modelagem preditiva**.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

# Enunciado — Experimentos de MLP para retenção de clientes

## Cenário real

O modelo linear do N19 criou uma referência. A equipe quer saber se uma MLP justifica maior complexidade e custo. Você deverá comparar configurações sob o mesmo corte temporal, rastrear cada experimento no MLflow e recomendar um modelo somente se o ganho for estável.

## Entradas

Reutilize exatamente o dataset, features e divisões temporais do N19. Crie uma identificação de versão dos dados. O conjunto de teste continua intocado até a escolha final.

## Saídas obrigatórias

`treinar_mlp.py` deve produzir:

1. baseline linear reproduzido com as mesmas métricas;
2. MLP base com arquitetura e contagem de parâmetros registradas;
3. experimentos controlados de dropout, weight decay e tratamento do desbalanceamento;
4. early stopping com checkpoint da melhor validação;
5. runs reais no MLflow com parâmetros, métricas por época e artefatos;
6. tabela ordenada dos experimentos e seleção baseada na validação;
7. avaliação única do vencedor no teste;
8. curva de calibração, latência e tamanho do modelo.

## Regras

- Altere uma família de decisão por experimento e escreva uma hipótese antes de executá-lo.
- Compare `pos_weight` com uma execução de outra estratégia; não misture técnicas sem medir isoladamente.
- Ajuste normalização apenas no treino.
- Early stopping usa validação, nunca teste.
- Registre arquitetura, learning rate, batch size, seed, épocas, paciência e versão dos dados no MLflow.
- Salve o melhor checkpoint, não apenas o último.
- Se houver GPU, registre também determinismo e dispositivo; a execução em CPU deve continuar possível.

## Casos de borda obrigatórios

- classe positiva ausente em um lote;
- checkpoint inexistente ou incompatível;
- interrupção e reinício de uma execução;
- nulos/infinito na entrada;
- probabilidade extrema ou mal calibrada;
- validação piorando enquanto treino melhora;
- run duplicada com os mesmos parâmetros e seed.

## Métricas

- principal: PR-AUC no teste temporal;
- operação: recall@10%, lift@10%, latência P95 e tamanho do artefato;
- generalização: diferença treino-validação, melhor época e estabilidade entre pelo menos três seeds;
- calibração: Brier score e reliability diagram.

## Critério de aceite

A MLP só substitui o modelo linear se elevar PR-AUC em pelo menos 0,03, não reduzir recall@10%, permanecer dentro do orçamento de latência definido e mostrar ganho consistente nas três seeds. Todas as runs devem aparecer no MLflow e a melhor execução precisa ser reproduzível. Se não houver ganho, escolha formalmente o modelo linear e explique por que a complexidade foi rejeitada.

## Restrições

Não copie uma arquitetura pronta nem escolha o melhor resultado pelo teste. Implemente no arquivo inicial e use o MLflow como sistema de registro, não como captura de tela decorativa.

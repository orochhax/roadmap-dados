# Enunciado — Priorização de clientes com risco de churn

## Cenário real

Uma operadora só consegue contatar 10% da carteira por mês. Você criará um classificador binário para ordenar clientes pelo risco de cancelar nos 30 dias seguintes. O time precisa de uma avaliação temporal: usar informações posteriores ao mês de previsão produziria uma falsa sensação de qualidade.

## Entradas

Use uma tabela `customer_month` com:

- `customer_id_hash` e `reference_month`;
- consumo de dados/minutos, variação de uso e falhas de chamada;
- quantidade de tickets, indisponibilidade e atraso de pagamento;
- tempo de contrato, plano, região e valor mensal;
- `churn_next_30d`, alvo binário observado após o mês de referência.

Use dados públicos ou sintéticos e documente a origem. Não use identificadores pessoais. Garanta vários meses e preserve a ordem temporal.

## Saídas obrigatórias

`treino_tensores.py` deverá gerar:

1. validação de schema, nulos e tipos;
2. divisão temporal entre treino, validação e teste;
3. baseline pela prevalência ou modelo linear já conhecido;
4. `Dataset`, `DataLoader` e modelo linear em PyTorch;
5. training loop explícito com loss média de treino e validação por época;
6. probabilidades e ranking de risco no teste;
7. métricas de qualidade e latência;
8. curvas ou tabela que permitam diagnosticar underfitting/overfitting.

## Regras

- Ajuste imputação e escala somente com o treino.
- Não deixe o mesmo `customer_id_hash` atravessar divisões quando isso revelar seu futuro.
- Defina `float32` para features e formato compatível para o alvo.
- No treino, use explicitamente `zero_grad`, `backward` e `step`.
- Na avaliação, use `model.eval()` e contexto sem gradientes.
- Fixe seeds do Python, NumPy e PyTorch.
- Não escolha épocas ou limiar olhando o teste.
- Salve apenas pesos/artefatos necessários; não versione dados sensíveis ou arquivos grandes.

## Casos de borda obrigatórios

- lote final menor que `batch_size`;
- coluna numérica com nulo ou infinito;
- categoria desconhecida no teste;
- mês sem churn ou com poucos positivos;
- cliente duplicado no mesmo mês;
- entrada com quantidade incorreta de features;
- execução em CPU mesmo se CUDA não estiver disponível.

## Métricas

- principal: PR-AUC;
- decisão operacional: recall entre os 10% de maior risco e lift@10%;
- apoio: ROC-AUC, log loss, prevalência, loss por época e latência P95;
- fatias: plano, região e tempo de contrato.

## Critério de aceite

O modelo só pode ser recomendado para um piloto se superar o baseline em PR-AUC, produzir lift@10% maior que 1 e não apresentar queda superior a 0,15 de recall entre as principais fatias com amostra suficiente. O training loop deve reduzir a loss de treino e produzir resultados reproduzíveis. Se não cumprir, rejeite o piloto e explique se a causa provável é dado, otimização ou generalização.

## Restrições

Não use `Trainer`, Lightning ou uma função pronta de treinamento nesta sessão. O objetivo é implementar e compreender o loop no arquivo inicial, sem receber a solução completa.

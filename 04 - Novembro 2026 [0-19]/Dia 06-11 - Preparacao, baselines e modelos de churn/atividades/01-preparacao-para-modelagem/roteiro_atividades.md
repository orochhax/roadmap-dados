# Preparação para modelagem — roteiro

> Folha de trabalho. Preencha os registros sem apagar os enunciados.

## Entradas

- `dados/clientes_telecom.csv` e `dados/pedidos.csv`.
- Unidade de análise, alvo e data de corte definidos nesta sessão.

## Requisitos principais

1. Defina o corte temporal e os conjuntos de treino, validação e teste.

### Registro 1

<!-- Escreva aqui a saída, o teste e a decisão. -->

2. Construa a pipeline de imputação, codificação e escala com `fit` somente no treino.

### Registro 2

<!-- Escreva aqui a saída, o teste e a decisão. -->

3. Crie um baseline de negócio e um `DummyClassifier`.

### Registro 3

<!-- Escreva aqui a saída, o teste e a decisão. -->

4. Defina métricas técnicas e custo de decisão.

### Registro 4

<!-- Escreva aqui a saída, o teste e a decisão. -->

## Requisitos da atividade

- Registre origem, período, população, exclusões e limitações em `projeto-semanal/docs/data_card.md`.

## Adaptação e verificação

1. Compare a regra `chamados_90d >= 3` com o `DummyClassifier` usando a métrica e o custo definidos.

### Registro obrigatório 1

<!-- Escreva aqui. -->

2. Altere o corte temporal em 30 dias e confirme que nenhuma data posterior entrou no treino.

### Registro obrigatório 2

<!-- Escreva aqui. -->

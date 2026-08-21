# Refatoração de notebook

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/train.py`.
- **Entradas:** notebook indicado e `dados/clientes_telecom.csv`. **Fallback local:** amostra fixa de 100 linhas.

## Aprenda agora

- **Definição:** refatorar muda a estrutura sem mudar o comportamento; `src/` concentra código reutilizável, configuração guarda parâmetros e entrypoint inicia o fluxo.
- **Exemplo mínimo:** mova uma função do notebook para `src/features.py`, importe-a e compare a saída antes e após a mudança.
- **Erro comum:** misturar refatoração com nova lógica sem teste de equivalência.

## Núcleo essencial

1. [ ] Escolha notebook de ML e liste células de configuração, ingestão, funções, treino e apresentação.
2. [ ] Extraia funções para `src/`, parâmetros para `config.yaml` ou módulo e dependências para `requirements.txt`.
3. [ ] Transforme execução principal em script `train.py`.

## Prática obrigatória

- [ ] Execute o fluxo do zero, confirme que o notebook importa as funções sem duplicá-las e compare as métricas com a referência anterior.
- [ ] **Em `01-exercicios/train.py`:** use um caminho de dados inexistente e produza uma mensagem que identifique exatamente o arquivo ausente.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/train.py` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

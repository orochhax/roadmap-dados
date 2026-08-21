# Testes

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-093-testes.py`.
- **Entradas:** módulo indicado e fixture de `dados/clientes_telecom.csv`. **Fallback local:** cinco registros fixos.

## Aprenda agora

- **Definição:** teste unitário verifica uma unidade; integração verifica componentes; regressão preserva um comportamento corrigido. AAA significa Arrange, Act, Assert.
- **Exemplo mínimo:** `def test_total(): assert soma([2,3]) == 5`; execute `python -m pytest -q`.
- **Erro comum:** testar apenas que o código roda ou depender da ordem dos testes.

## Núcleo essencial

1. [ ] Instale `pytest` e escreva testes para validação de dados, feature engineering e métrica de custo.
2. [ ] Crie testes unitários com casos normais, borda e erro.
3. [ ] Escreva um teste de integração do carregamento até previsão.

## Prática obrigatória

- [ ] **Em `01-exercicios/dia-093-testes.py`:** crie fixtures pequenas e teste duração negativa e divisão de custo quando `total=0`.
- [ ] Remova uma coluna obrigatória da fixture de integração, confirme a falha antes da previsão e restaure a correção.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-093-testes.py` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

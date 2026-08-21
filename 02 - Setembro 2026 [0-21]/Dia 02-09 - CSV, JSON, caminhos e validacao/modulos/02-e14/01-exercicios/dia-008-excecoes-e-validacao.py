# Exceções e validação
#
# OBJETIVO
# Validar cada linha sem parar o programa inteiro quando uma delas for inválida.
# Os seis exemplos abaixo trazem duas linhas válidas e quatro erros diferentes.

linhas = [
    {"id": "INC-001", "cidade": "Salvador", "severidade": "P1", "duracao_min": "110", "clientes_afetados": "120"},
    {"id": "INC-002", "cidade": "Recife", "severidade": "P3", "duracao_min": "45", "clientes_afetados": "51"},
    {"id": "INC-003", "cidade": "", "severidade": "P2", "duracao_min": "70", "clientes_afetados": "40"},
    {"id": "INC-004", "cidade": "Fortaleza", "severidade": "PX", "duracao_min": "95", "clientes_afetados": "200"},
    {"id": "INC-005", "cidade": "Maceió", "severidade": "P4", "duracao_min": "-10", "clientes_afetados": "10"},
    {"id": "INC-006", "cidade": "Ilhéus", "severidade": "P2", "duracao_min": "erro", "clientes_afetados": "30"},
]

# EXERCÍCIO 1
# Crie validar_linha(linha). Ela deve RETORNAR uma lista de mensagens de erro:
# - cidade vazia;
# - severidade diferente de P1, P2, P3 ou P4;
# - duração ou clientes que não são inteiros ou são negativos.
# Use try/except apenas ao converter texto para int.
# ESCREVA AQUI:


# EXERCÍCIO 2
# Percorra `linhas`. Separe-as em listas `validas` e `rejeitadas`.
# Guarde em cada rejeitada uma nova chave chamada motivo_rejeicao.
# Resultado esperado: 2 válidas (INC-001, INC-002) e 3 rejeitadas.
# ESCREVA AQUI:


# EXERCÍCIO 3
# Imprima os ids válidos e cada id rejeitado com seu motivo. O programa deve
# chegar até o fim, mesmo com dados inválidos.
# ESCREVA AQUI:


# EXERCÍCIO 4
# Implemente `calcular_taxa(resolvidos, total)`. Trate total zero, texto no lugar
# de número e valores negativos. Teste (82, 100), (0, 0) e ("x", 10).
# ESCREVA AQUI:

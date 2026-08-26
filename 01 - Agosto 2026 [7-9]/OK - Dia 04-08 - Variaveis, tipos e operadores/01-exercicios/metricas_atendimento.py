# COMEÇO GUIADO
# Dados de partida: Valores iniciais já incluídos; use apenas os exercícios indicados no Núcleo essencial.
# Use somente esses dados ou os valores já declarados neste arquivo. Resolva uma tarefa
# por vez, execute e confira a saída antes de seguir para a próxima.

# Variáveis, tipos e operadores
#
# COMO USAR ESTE ARQUIVO
# Os dados de teste já estão preparados. Escreva os cálculos e as validações,
# mas não altere os cenários antes de testar o programa.


# 1. [ ] MÉTRICAS DE ATENDIMENTO
# Para cada cenário, calcule e mostre com duas casas decimais:
# - taxa de resolução em porcentagem;
# - taxa de reincidência em porcentagem;
# - duração média por chamado em minutos.
#
# Valide antes de dividir:
# - nenhum número pode ser negativo;
# - resolvidos não pode ser maior que total_chamados;
# - reincidentes não pode ser maior que resolvidos;
# - quando total_chamados for zero, o programa não pode dividir por zero.

cenario_normal = (100, 82, 12, 3450)
cenario_sem_chamados = (0, 0, 0, 0)
cenario_com_negativo = (-5, 7, 2, 100)

# A ordem de cada tupla é:
# (total_chamados, resolvidos, reincidentes, soma_duracoes_min)

# ESCREVA AQUI:


# 2. [ ] TESTES EXTRAS ESPECÍFICOS
# Execute também estes dois cenários sem modificar os valores:
# - uso comum: calcule as três métricas para (150, 120, 18, 5400);
# - entrada problemática: faça o programa rejeitar (10, 12, 1, 300), pois a
#   quantidade resolvida é maior que o total de chamados.
cenario_extra_comum = (150, 120, 18, 5400)
cenario_extra_problematico = (10, 12, 1, 300)

# ESCREVA AQUI:

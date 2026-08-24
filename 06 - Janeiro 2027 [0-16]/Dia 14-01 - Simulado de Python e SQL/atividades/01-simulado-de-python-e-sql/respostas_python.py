# COMEÇO GUIADO
# Dados de partida: `dados/clientes_telecom.csv`, `dados/pedidos.csv` e fixtures declaradas neste arquivo.
# Use somente esses dados ou os valores já declarados neste arquivo. Resolva uma tarefa
# por vez, execute e confira a saída antes de seguir para a próxima.

# Simulado Python
# Não há soluções prontas. Escreva cada resposta abaixo de ESCREVA AQUI.
# P1–P6 formam o núcleo essencial.


# P1. LISTAS
# A partir das durações abaixo, crie outra lista somente com valores acima de
# 60 e calcule quantos valores foram selecionados.
duracoes_p1 = [15, 80, 45, 120, 30, 75, 200, 60]
# ESCREVA AQUI:

# P2. FUNÇÃO
# Crie classificar_sla(duracao, limite) que retorne "no prazo" quando duração
# for menor ou igual ao limite e "atrasado" nos demais casos. Teste (90, 90)
# e (91, 90).
# ESCREVA AQUI:


# P3. DICIONÁRIOS
# Conte quantos incidentes existem por cidade sem usar pandas.
cidades_p3 = ["Salvador", "Ilhéus", "Salvador", "Eunápolis", "Ilhéus", "Salvador"]
# ESCREVA AQUI:


# P4. ARQUIVOS
# Leia dados/incidentes.csv com csv.DictReader e mostre id e cidade das cinco
# primeiras linhas. Use pathlib para construir o caminho.
# ESCREVA AQUI:


# P5. TRATAMENTO DE ERRO
# Converta cada item para inteiro, guarde válidos e inválidos separadamente e
# não interrompa o laço quando encontrar texto.
valores_p5 = ["10", "7", "erro", "25", "", "42"]
# ESCREVA AQUI:


# P6. PANDAS E FILTRO
# Carregue dados/clientes_telecom.csv e selecione clientes com churn=1,
# nps<=4 e chamados_90d>=3. Mostre somente cliente_id, cidade e plano.
# ESCREVA AQUI:

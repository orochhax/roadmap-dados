# COMEÇO GUIADO
# Dados de partida: Dados pequenos definidos nos próprios exercícios e arquivos criados por você.
# Use somente esses dados ou os valores já declarados neste arquivo. Resolva uma tarefa
# por vez, execute e confira a saída antes de seguir para a próxima.

# Dicionários, `set` e resumo de incidentes
#
# OBJETIVO
# Usar `for`, lista, dicionário e `set` para resumir incidentes. Os dados já
# estão prontos: não crie nem altere a lista antes de fazer os exercícios.
#
# COMO RESPONDER
# Faça um exercício por vez abaixo do respectivo "# ESCREVA AQUI". Execute o
# arquivo após cada um e confira o resultado esperado nos comentários.

incidentes = [
    {"cidade": "Salvador", "causa": "fibra rompida", "severidade": "P1", "duracao_min": 110},
    {"cidade": "Recife", "causa": "wifi lento", "severidade": "P3", "duracao_min": 45},
    {"cidade": "Salvador", "causa": "equipamento aquecendo", "severidade": "P2", "duracao_min": 70},
    {"cidade": "Fortaleza", "causa": "sem conexão", "severidade": "P1", "duracao_min": 95},
    {"cidade": "Recife", "causa": "fibra rompida", "severidade": "P1", "duracao_min": 125},
    {"cidade": "Maceió", "causa": "wifi lento", "severidade": "P4", "duracao_min": 30},
    {"cidade": "Fortaleza", "causa": "queda de energia", "severidade": "P1", "duracao_min": 160},
    {"cidade": "Salvador", "causa": "fibra rompida", "severidade": "P2", "duracao_min": 80},
]

# EXERCÍCIO 1 — ler uma lista de dicionários
# Use `for` para imprimir cidade e causa de cada incidente.
# Resultado: devem aparecer 8 linhas.
# ESCREVA AQUI:

# EXERCÍCIO 2 — contar por cidade
# Crie o dicionário `quantidade_por_cidade`. Use `for` para contar os incidentes
# de cada cidade.
# Resultado esperado: Salvador=3, Recife=2, Fortaleza=2 e Maceió=1.
# ESCREVA AQUI:


# EXERCÍCIO 3 — causas únicas
# Crie o conjunto `causas_unicas` e adicione cada causa com `for`.
# Resultado esperado: 5 causas únicas. "fibra rompida" e "wifi lento" devem
# aparecer somente uma vez no conjunto, mesmo existindo em vários incidentes.
# ESCREVA AQUI:


# EXERCÍCIO 4 — duração total e média
# Com `for`, some `duracao_min` de todos os incidentes. Depois calcule a média.
# Resultado esperado: total=715 minutos e média=89.375 minutos.
# ESCREVA AQUI:


# PRÁTICA OBRIGATÓRIA — média por cidade
# Crie os dicionários necessários para calcular a duração média de cada cidade.
# Resultado esperado: Salvador=86.67, Recife=85.0, Fortaleza=127.5, Maceió=30.0.
# ESCREVA AQUI:

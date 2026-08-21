# Compreensões e funções úteis
#
# OBJETIVO
# Transformar a lista pronta de incidentes usando uma list comprehension e
# funções úteis. Primeiro faça cada resultado com `for`; depois tente a versão
# curta apenas onde o comentário pedir.

incidentes = [
    {"cidade": "Salvador", "prioridade": "P1", "duracao_min": 110},
    {"cidade": "Recife", "prioridade": "P3", "duracao_min": 45},
    {"cidade": "Salvador", "prioridade": "P2", "duracao_min": 70},
    {"cidade": "Fortaleza", "prioridade": "P1", "duracao_min": 95},
    {"cidade": "Recife", "prioridade": "P1", "duracao_min": 125},
    {"cidade": "Maceió", "prioridade": "P4", "duracao_min": 30},
    {"cidade": "Fortaleza", "prioridade": "P1", "duracao_min": 160},
    {"cidade": "Salvador", "prioridade": "P2", "duracao_min": 80},
    {"cidade": "Feira de Santana", "prioridade": "P3", "duracao_min": 55},
    {"cidade": "Ilhéus", "prioridade": "P3", "duracao_min": 75},
    {"cidade": "Salvador", "prioridade": "P4", "duracao_min": 20},
    {"cidade": "Recife", "prioridade": "P2", "duracao_min": 61},
    {"cidade": "Fortaleza", "prioridade": "P3", "duracao_min": 90},
    {"cidade": "Maceió", "prioridade": "P1", "duracao_min": 59},
    {"cidade": "Feira de Santana", "prioridade": "P1", "duracao_min": 140},
    {"cidade": "Ilhéus", "prioridade": "P4", "duracao_min": 40},
    {"cidade": "Salvador", "prioridade": "P3", "duracao_min": 130},
    {"cidade": "Recife", "prioridade": "P2", "duracao_min": 60},
    {"cidade": "Maceió", "prioridade": "P1", "duracao_min": 200},
    {"cidade": "Feira de Santana", "prioridade": "P2", "duracao_min": 100},
]

# EXERCÍCIO 1 — filtro com comprehension
# Crie `incidentes_urgentes` contendo apenas P1 ou P2 com duração acima de 60.
# Resultado esperado: 10 incidentes.
# ESCREVA AQUI:

# EXERCÍCIO 2 — dicionário por comprehension
# Gere `{cidade: total_de_incidentes}` primeiro com laço e depois com dict
# comprehension. Compare os dois resultados.
# ESCREVA AQUI:


# EXERCÍCIO 3 — enumerate, zip, sorted, any e all
# Ordene por duração com `sorted(key=...)` e numere o ranking com `enumerate`.
# Combine as cidades e metas abaixo com `zip`. Use `any` para detectar P1 e `all`
# para validar durações não negativas.
cidades = ["Salvador", "Recife", "Fortaleza", "Maceió"]
metas_min = [90, 80, 100, 60]
# ESCREVA AQUI:

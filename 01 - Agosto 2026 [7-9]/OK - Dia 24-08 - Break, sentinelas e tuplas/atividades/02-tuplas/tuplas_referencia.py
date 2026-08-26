# OBJETIVO
# Consultar dados fixos em tuplas sem alterá-los.

PRIORIDADES_VALIDAS = ("P1", "P2", "P3", "P4")
DURACOES = (110, 45, 70, 95, 125, 30)
maior_90 = 0
# EXERCÍCIO 1
# Mostre a menor e a maior duração.
# ESCREVA AQUI:
maiorValor = max(DURACOES)
menorValor = min(DURACOES)
print(f"Menor:{menorValor}")
print(f"Maior: {maiorValor}")

# EXERCÍCIO 2
# Conte com `for` quantas durações são maiores que 90.
# ESCREVA AQUI:
for i in DURACOES:
    if i > 90:
        maior_90 += 1

print(f"Durações maior que 90: {maior_90}")

# EXERCÍCIO 3
# Informe se "P2" pertence às prioridades válidas e em qual posição aparece.
# ESCREVA AQUI:
for pos, y in enumerate(PRIORIDADES_VALIDAS):
    if y == "P2":
        P2 = True
        posicaoP2 = pos
print(P2)
print(f"Posição de P2: {posicaoP2}")

# SAÍDA ESPERADA
# Menor: 30
# Maior: 125
# Acima de 90: 3
# P2 existe: True
# Posição de P2: 1

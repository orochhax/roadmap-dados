# OBJETIVO
# Ler seis durações com `for`, somar todas e contar quantas são maiores que
# 60 minutos.

# EXERCÍCIO
# 1. Prepare um acumulador para o total e um contador para durações acima de 60.
# 2. Use range para repetir a leitura seis vezes.
# 3. Ao final, imprima o total e a contagem.
# ESCREVA AQUI:
a = 0
b = 0
quantidade_de_duracoes = 6

for x in range(quantidade_de_duracoes):
    x = int(input('Digite um numero:'))
    a += x
    if x > 60:
        b += 1

print("Total:", a)
print("Acima de 60 minutos:", b)

# DADOS DE TESTE — digite nesta ordem
# 110, 45, 70, 95, 125, 30
#
# SAÍDA ESPERADA
# Total: 475
# Acima de 60 minutos: 4

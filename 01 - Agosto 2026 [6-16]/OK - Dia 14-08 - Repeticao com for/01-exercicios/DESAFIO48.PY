#Desafio 048

#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0

for x in range(0,501):
    if x % 2 == 1 and x % 3 == 0:
        soma += x

print("Valor total da soma: ",soma)

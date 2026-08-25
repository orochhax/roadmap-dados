# DESAFIO 075

# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em
# uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

# ESCREVA SUA SOLUÇÃO ABAIXO:
valor_tres = 0
nove = 0
pares = 0

valor = (int(input('Digite um numero:')),
         int(input('Digite um numero:')),
         int(input('Digite um numero:')),
         int(input('Digite um numero:')))

for num in valor:
    if num == 9:
        nove += 1




print(f"Valores da tupla: {valor}")
print(f"O numero 9 apareceu: {nove} vezes.")
print(f"O primeiro valor 3 foi digitado na posição {valor_tres}.")
print(f"Os numeros pares são: {pares}")
# DESAFIO 075

# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

# ESCREVA SUA SOLUÇÃO ABAIXO:
valor_tres = 0
nove = 0
pares = ()

valor = (int(input('Digite um numero:')),
         int(input('Digite um numero:')),
         int(input('Digite um numero:')),
         int(input('Digite um numero:')))

for pos, num in enumerate(valor):
    if num == 9:
        nove += 1

    if num % 2 == 0:
        nova_tupla = (num,)
        pares = pares + nova_tupla

    if num == 3 and valor_tres == 0:
        valor_tres = pos + 1

if valor_tres != 0:
    print(f"O primeiro valor 3 foi digitado na posição :{valor_tres}.")
else:
    print("Não teve o numero três.")


print(f"Valores da tupla: {valor}")
print(f"O numero 9 apareceu: {nove} vezes.")
print(f"Os numeros pares são: {pares}")
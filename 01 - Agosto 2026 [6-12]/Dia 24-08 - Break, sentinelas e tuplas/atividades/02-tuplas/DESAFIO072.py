# DESAFIO 072

# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.

# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

# ESCREVA SUA SOLUÇÃO ABAIXO:

extensos = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte",)

while True:
    indice = int(input("Digite um numero de 0 a 20:"))
    if indice in range(0,21):
        print(f"Seu numero é: {indice} ({extensos[indice]})")
        break
    else:
        print("Opção invalida!")
        continue
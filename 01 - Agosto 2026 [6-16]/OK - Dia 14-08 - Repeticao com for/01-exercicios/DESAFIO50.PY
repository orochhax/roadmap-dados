#Desafio 050

#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0

for x in range(0, 6):
    x = int(input("Digite um numero: "))
    if x % 2 == 0:
        soma += x

print("Valor total da soma é:" ,soma)
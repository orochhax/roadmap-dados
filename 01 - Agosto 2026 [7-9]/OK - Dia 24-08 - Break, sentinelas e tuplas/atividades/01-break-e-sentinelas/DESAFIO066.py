#DESAFIO 066

#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.

#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

x = 0
s = 0
c = 0
while True:
    x = int(input("Digite um numero: "))
    if x == 999:
        break
    s += x
    c += 1
print(f"A soma de todos os numeros: {s}")
print(f"Numero validos digitados: {c}")
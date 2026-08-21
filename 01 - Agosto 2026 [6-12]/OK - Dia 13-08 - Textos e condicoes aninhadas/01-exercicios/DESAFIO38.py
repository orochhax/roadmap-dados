#DESAFIO 38
#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

#1- O primeiro valor é maior
#2- O segundo valor é maior
#3- Não existe valor maior, os dois são iguais

x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))

if x > y:
    print('O primeiro valor é maior.')
elif y > x:
    print('O segundo valor é maior.')
else:
    print('Os valores são iguais.')
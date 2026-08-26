#Desafio 059

#Crie um programa que leia dois valores e mostre um menu na tela:

#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso.

a = int(input("Valor um:"))
b = int(input("Valor dois:"))
resultado = 0
c = 0

while c != 5:
    # Menu
    print("[1] somar")
    print("[2] multiplicar")
    print("[3] maior")
    print("[4] novos números")
    print("[5] sair do programa")
    c = int(input("Menu:"))
    if c == 1:
        print("Resultado:", a + b)
    elif c == 2:
        print("Resultado", a * b)
    elif c == 3:
        if a > b:
            print("Valor um é maior.")
        elif b > a:
            print("Valor dois é maior.")
        else:
            print("Valores são iguais.")
    elif c == 4:
        a = int(input("Insira um novo valor um:"))
        b = int(input("Insira um novo valor dois:"))
    elif c == 5:
        print("Programa encerrando...")
    else:
        print("Opção invalida!")
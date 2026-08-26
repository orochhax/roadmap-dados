import time

#Desafio 046

#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

cronometro = 10

for x in range(10, -1, -1):
    print("Contagem > ", x)
    time.sleep(1)
print("A bomba explodiu!")
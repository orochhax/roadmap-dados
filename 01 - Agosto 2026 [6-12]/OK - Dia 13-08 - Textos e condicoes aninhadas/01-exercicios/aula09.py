#DESAFIO 022

#Crie um programa que leia o nome completo de uma pessoa e mostre:

#1- O nome com todas as letras maiúsculas.
#2- O nome com todas minúsculas.
#3- Quantas letras ao todo (sem considerar espaços).
#4- Quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo:')
print("Seu nome com letras maiúsculas:", nome.upper())
print("Seu nome com letras minúsculas:", nome.lower())
total_letras = len("".join(nome.split()))
print("Quantas letras tem seu nome todo:", total_letras)
separado = nome.split()
print("Quantas letras tem seu primeiro nome:", len(separado[0]))
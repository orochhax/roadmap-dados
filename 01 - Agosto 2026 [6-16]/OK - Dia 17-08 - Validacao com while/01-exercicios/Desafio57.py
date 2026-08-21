#Desafio 057

#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input('Informe o seu sexo (F/M):').upper()
while sexo != "F" and sexo != "M":
    sexo = input('Sexo invalido, digite apenas F ou M:').upper()

print("Seu sexo é:", sexo)
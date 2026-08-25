#DESAFIO 069

#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.

#No final, mostre:

#A) quantas pessoas têm mais de 18 anos.
#B) Quantos homens foram cadastrados.
#C) Quantas mulheres têm menos de 20 anos.
mais_18 = 0
mas = 0 
fem_menor_20 = 0

while True:
    opcao = int(input("Menu:1- Novo cadastro 2- Sair"))
    if opcao == 1:
        idade = int(input("Qual sua idade:"))    
        sexo = input("Qual o seu genero:").strip().lower()
    elif opcao == 2:
        break
    else:
        print("Opção invalida!")
        continue

    if idade > 18:
        mais_18 += 1

    if sexo == "masculino":
        mas += 1

    if idade < 20 and sexo == "feminino":
        fem_menor_20 += 1

print(f"Pessoas com mais de 18 anos: {mais_18}")
print(f"Homens cadastrados: {mas}")
print(f"Mulheres com menos de 20 anos: {fem_menor_20}")
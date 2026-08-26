#DESAFIO 070

#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.

#No final, mostre:

#A) Qual é o total gasto na compra.
#B) Quantos produtos custam mais de R$1000.
#C) Qual é o nome do produto mais barato.

total_compra = 0
mais_1000 = 0
nome_barato = ""
preco_barato = None

while True:
    opcao = int(input("Menu:1- Novo produto 2- Sair"))

    if opcao == 1:
        nome_produto = input("Qual o nome do produto:").strip()
        preco = float(input("Qual o preço do produto:"))
        total_compra += preco
    elif opcao == 2: 
        break
    else:
        print("Opção invalida!")
        continue

    if preco_barato is None:
        preco_barato = preco
        nome_barato = nome_produto
    elif preco < preco_barato:
        preco_barato = preco
        nome_barato = nome_produto

    if preco > 1000:
        mais_1000 += 1

print(f"Total da compra: R${total_compra:.2f}")
print(f"Produtos que custam mais de R$1.000: {mais_1000} unidades.")
print(f"Produto mais barato: {nome_barato}")
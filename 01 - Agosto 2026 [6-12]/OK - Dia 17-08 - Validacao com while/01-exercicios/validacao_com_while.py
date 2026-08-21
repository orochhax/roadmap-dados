# OBJETIVO
# Validar uma prioridade e manter um menu ativo até a opção de saída.

prioridades_validas = ("P1", "P2", "P3", "P4")

# EXERCÍCIO 1
# Leia uma prioridade, normalize com strip().upper() e repita enquanto ela não
# estiver em `prioridades_validas`.
# ESCREVA AQUI:
entrada = input("Qual a prioridade ?").strip().upper()
while entrada not in prioridades_validas:
    entrada = input("Prioridade Invalida, digite novamente?")
    entrada = entrada.strip().upper()

print("Prioridade:", entrada)
# EXERCÍCIO 2
# Crie um menu com estas opções:
# 1 - mostrar prioridade
# 2 - informar outra prioridade
# 3 - sair
# Repita o menu enquanto a opção for diferente de 3.
# ESCREVA AQUI:
menu = 0
while menu != 3:
    print("Menu/" \
    "1- Mostrar prioridade/" \
    "2- Informar outra prioridade/" \
    "3- Sair")
    menu = int(input('Opção:'))
    if menu == 1:
        print("Prioridade:", entrada)
    elif menu == 2:
        entrada = input("Qual a prioridade ?").strip().upper()
        while entrada not in prioridades_validas:
            entrada = input("Prioridade Invalida, digite novamente?")
            entrada = entrada.strip().upper()
    elif menu == 3:
        print("Fechando menu...")
    else:
        print("Opção invalida")
# DADOS DE TESTE
# Prioridades: P0, depois " p2 "
# Opções do menu: 9, 1, 3
#
# SAÍDA ESPERADA
# P0 e a opção 9 são recusados; " p2 " é aceito como P2; a opção 3 encerra.

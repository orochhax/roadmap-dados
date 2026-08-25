# OBJETIVO
# Ler durações até receber -1 e calcular quantidade, total e média sem incluir o sentinela.

# EXERCÍCIO
# 1. Use while True para ler uma duração por vez.
# 2. Interrompa com break quando o valor for -1.
# 3. Acumule apenas durações válidas.
# 4. Calcule a média somente se a quantidade for maior que zero.
# ESCREVA AQUI:

total_minutos = 0
duracao = 0
contador = 0 
media = 0

while True:
    duracao = int(input("Digite a duração em minutos:"))
    if duracao == -1:
        break

    if duracao > 0:
        total_minutos += duracao
        contador += 1

if contador > 0:
    media = total_minutos / contador
else:
    media = "média não disponivel"
print(f"Quantidade: {contador}, total de minutos: {total_minutos}, média: {media}")


    

# DADOS DE TESTE 1
# 110, 45, 70, -1
# SAÍDA ESPERADA: quantidade=3, total=225, média=75.0

# DADOS DE TESTE 2
# -1
# SAÍDA ESPERADA: quantidade=0, total=0, média não disponível
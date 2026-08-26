# OBJETIVO
# Normalizar a descrição de um incidente e comparar duas durações com uma única
# cadeia if/elif/else.

descricao_bruta = "  FIBRA rompida em Salvador  "
duracao_primeiro = 110
duracao_segundo = 95

# EXERCÍCIO 1
# Crie `descricao_normalizada` removendo espaços externos e convertendo o texto
# para letras minúsculas. Depois, informe se a palavra "fibra" está presente.
# ESCREVA AQUI:
descricao_lower = descricao_bruta.lower()
descricao_normalizada = descricao_lower.strip()
print(descricao_normalizada)
print('Contém fibra:', 'fibra' in descricao_normalizada)

# EXERCÍCIO 2
# Compare as duas durações com if/elif/else e imprima exatamente uma mensagem:
# "primeiro maior", "segundo maior" ou "durações iguais".
# ESCREVA AQUI:
x = int(input('Primeiro numero: '))
y = int(input('Segundo numero: '))

if x > y:
    print('primeiro maior')
elif y > x:
    print('segundo maior')
else:
    print('durações iguais')

# DADOS DE TESTE
# 1. 110 e 95  -> primeiro maior
# 2. 45 e 70   -> segundo maior
# 3. 80 e 80   -> durações iguais
#
# SAÍDA ESPERADA PARA OS VALORES INICIAIS
# fibra rompida em salvador
# contém fibra: True
# primeiro maior

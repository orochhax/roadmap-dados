# DESAFIO 077

# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

# ESCREVA SUA SOLUÇÃO ABAIXO:
palavras = (
    "aprender",
    "python",
    "dados",
    "rede",
    "monitoramento",
)

for palavra in palavras:
    vogais = ()
    print(palavra)
    for letra in palavra:
        if letra in ["a", "e", "i", "o", "u"]:
            vogais = vogais + (letra, )
    print(vogais)
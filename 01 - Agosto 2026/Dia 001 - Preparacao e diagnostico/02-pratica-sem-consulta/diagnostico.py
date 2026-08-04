#(1) imprimir nome e objetivo profissional; 
print("Carlos")
print("Cientista de Dados/IA")

#(2) somar 125 e 378; 
soma = 125 + 378
print(soma)

#(3) calcular média de 7.5, 8.0 e 6.5; 
media = (7.5 + 8 + 6.5) / 3
print(media)

#(4) converter 135 minutos em horas e minutos; 
total_minutos = 135
horas = total_minutos // 60 
minutos = total_minutos % 60 
print(total_minutos, "minutos é equivalente a", horas, "horas e", minutos, "minutos.")

#(5) calcular 12% de 850; 
valor = 850 
porc = 12
final = valor * porc / 100
print(final)

#(6) verificar se 37 é par; 
num = 37 
if num % 2 == 0:
    print("Par")
else:
    print("Ímpar")

#(7) comparar 18 e 24 e exibir o maior; 
x = 18 
y = 24 

if x > y:
    print(x)
else:
    print(y)

#(8) contar caracteres de `Data Science`; 
text = "Data Science"
quant = len(text)
print(quant)

#(9) inverter `Vertex`; 
texto = "Vertex"
texto_invertido = texto[::-1]
print(texto_invertido)

#(10) calcular quantos clientes representam 7,5% de uma base de 2.400.
porcetagem = 7.5
base = 2400
print((porcetagem / 100) * base)
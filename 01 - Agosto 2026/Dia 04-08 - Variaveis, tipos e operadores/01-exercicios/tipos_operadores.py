# Dia 002 — Variáveis, tipos e operadores — 04/08/2026
#
# COMO USAR ESTE ARQUIVO
# 1. Leia um enunciado por vez.
# 2. Use primeiro os dados iniciais já fornecidos.
# 3. Escreva sua solução logo abaixo de "ESCREVA AQUI".
# 4. Depois que funcionar, adapte o exercício para receber os valores com input().
# 5. Não há respostas prontas neste arquivo.


# PARTE A — TIPOS DE VARIÁVEIS
# [ ] Declare um int, um float, uma str e um bool e mostre o tipo de cada um
#     com type().

x = 23
y = 10.5
nome = "Carlos"
z = True

print(type(x))
print(type(y))
print(type(nome))
print(type(z))


# PARTE B — 15 EXERCÍCIOS

# 1. [ ] PREÇO COM DESCONTO
# Um produto custa R$ 249,90 e recebeu 15% de desconto. Calcule o valor do
# desconto e o preço final. Mostre os dois valores com duas casas decimais.
preco_ex01 = 249.90
desconto_percentual_ex01 = 15
# ESCREVA AQUI:
desconto = preco_ex01 * 0.15
valor_final = preco_ex01 - desconto
print(valor_final)

# 2. [ ] IMC
# Uma pessoa pesa 78,4 kg e mede 1,75 m. Calcule o IMC e mostre o resultado
# com duas casas decimais.
peso_kg_ex02 = 78.4
altura_m_ex02 = 1.75
# ESCREVA AQUI:
altura_ao_quadrado = altura_m_ex02 * altura_m_ex02
imc = peso_kg_ex02 / altura_ao_quadrado
print(f"{imc:.2f}") # Usei ajuda para ver como colocava 2 casas decimais 

# 3. [ ] CONVERSÃO DE CELSIUS PARA FAHRENHEIT
# Converta 32,5 °C para Fahrenheit e mostre uma frase com as duas temperaturas.
temperatura_celsius_ex03 = 32.5
# ESCREVA AQUI:
f = temperatura_celsius_ex03 * 1.8 + 32
print(temperatura_celsius_ex03, "°C |", f, "Fahrenheit")

# 4. [ ] CONVERSÃO DE KM/H PARA M/S
# Converta 90 km/h para m/s e mostre o resultado com duas casas decimais.
velocidade_kmh_ex04 = 90
# ESCREVA AQUI:
converte = 3.6
conversao = velocidade_kmh_ex04 / converte
print(conversao, "m/s")


# 5. [ ] JUROS SIMPLES
# Um capital de R$ 1.500,00 foi aplicado durante 8 meses a uma taxa de 2% ao
# mês. Calcule somente os juros e depois o valor total acumulado.
capital_ex05 = 1500.00
taxa_mensal_percentual_ex05 = 2
meses_ex05 = 8
# ESCREVA AQUI:
rendimento = capital_ex05 * (taxa_mensal_percentual_ex05 / 100)
redimento_total = rendimento * meses_ex05
valor_final_bruto = capital_ex05 + redimento_total
print(f"R$ {valor_final_bruto:.2f}")

# 6. [ ] COMISSÃO
# Um vendedor realizou R$ 18.500,00 em vendas e recebe comissão de 4,5%.
# Calcule a comissão e mostre o valor formatado em reais.
total_vendas_ex06 = 18500.00
comissao_percentual_ex06 = 4.5
# ESCREVA AQUI:
porcetagem_comissao = comissao_percentual_ex06 / 100
comissao = total_vendas_ex06 * porcetagem_comissao
print(f"R$ {comissao:.2f}")

# 7. [ ] DIVISÃO DE CONTA
# Uma conta de R$ 286,50 será dividida entre 4 pessoas depois de acrescentar
# 10% de gorjeta. Calcule a gorjeta, o total com gorjeta e o valor por pessoa.
conta_ex07 = 286.50
pessoas_ex07 = 4
gorjeta_percentual_ex07 = 10
# ESCREVA AQUI:
gorjeta = conta_ex07 * (gorjeta_percentual_ex07 / 100)
total_com_gorjeta = conta_ex07 + gorjeta
valor_individual_com_gorjeta = total_com_gorjeta / 4 
print(f"Total: R${total_com_gorjeta:.2f}, ficando R${valor_individual_com_gorjeta:.2f} pra cada.")

# 8. [ ] CONSUMO MÉDIO
# Um carro percorreu 540 km usando 45 litros. Calcule o consumo médio em km/l.
distancia_km_ex08 = 540
litros_ex08 = 45
# ESCREVA AQUI:
consumo = distancia_km_ex08 / litros_ex08
print(f"{consumo} Km/L")

# 9. [ ] CUSTO POR CLIENTE
# Uma operação custou R$ 12.600,00 e atendeu 350 clientes. Calcule o custo
# médio por cliente com duas casas decimais.
custo_operacao_ex09 = 12600.00
clientes_ex09 = 350
# ESCREVA AQUI:
custo_medio = custo_operacao_ex09 / clientes_ex09
print(f"Custo medio por cliente: R${custo_medio:.2f}")

# 10. [ ] TAXA DE RESOLUÇÃO
# De 240 chamados recebidos, 198 foram resolvidos. Calcule a taxa de resolução
# em porcentagem e mostre com duas casas decimais.
total_chamados_ex10 = 240
chamados_resolvidos_ex10 = 198
# ESCREVA AQUI:
taxa_resolucao = chamados_resolvidos_ex10 / total_chamados_ex10 * 100
print(f"{taxa_resolucao:.2f}% dos chamados foram resolvidos ")

# 11. [ ] TAXA DE REINCIDÊNCIA
# Entre 198 chamados resolvidos, 27 voltaram a ocorrer. Calcule a taxa de
# reincidência em porcentagem.
resolvidos_ex11 = 198
reincidentes_ex11 = 27
# ESCREVA AQUI:
taxa_reincidencia = reincidentes_ex11 / resolvidos_ex11 * 100
print(f"{taxa_reincidencia:.2f}% dos chamados voltaram a correr ")

# 12. [ ] DURAÇÃO MÉDIA
# A soma da duração de 75 incidentes foi 3.675 minutos. Calcule a duração
# média em minutos.
soma_duracoes_min_ex12 = 3675
quantidade_incidentes_ex12 = 75
# ESCREVA AQUI:
duracao_media = soma_duracoes_min_ex12 / quantidade_incidentes_ex12
print(f"Duração media foi de {duracao_media:.0f} minutos")

# 13. [ ] ARREDONDAMENTO MONETÁRIO
# Sete unidades de um item custam R$ 19,987 cada. Calcule o total, arredonde
# para duas casas decimais e mostre no formato R$ 0,00.
preco_unitario_ex13 = 19.987
quantidade_ex13 = 7
# ESCREVA AQUI:
valor_unidade = preco_unitario_ex13 / quantidade_ex13
print(f"Valor da unidade R${valor_unidade:.2f}")

# 14. [ ] COMPARAÇÃO DE METAS
# A meta era resolver 420 chamados e a equipe resolveu 438. Informe se a meta
# foi atingida, a diferença em chamados e o percentual alcançado da meta.
meta_ex14 = 420
realizado_ex14 = 438
# ESCREVA AQUI:


# 15. [ ] FRASE COM F-STRING
# Usando somente os dados abaixo, produza esta informação em uma frase:
# nome da analista, cidade, quantidade de chamados e duração média com uma casa.
analista_ex15 = "Ana"
cidade_ex15 = "Salvador"
chamados_ex15 = 8
duracao_media_ex15 = 42.5
# ESCREVA AQUI:


# PARTE C — ENTRADAS E VALIDAÇÃO
# [ ] Depois de concluir os 15 exercícios com os dados fornecidos, adapte cada
#     seção para usar input() e converter os valores para int ou float.
# [ ] Em exercícios com divisão, impeça divisor igual a zero.
# [ ] Quando for digitado texto no lugar de número, mostre uma mensagem clara
#     em vez de deixar o programa encerrar com erro sem explicação.


# EXERCÍCIO EXTRA ESPECÍFICO
# 16. [ ] PLANO COM CONSUMO EXCEDENTE
# Uma mensalidade custa R$ 129,90. O cliente consumiu 7 GB adicionais, cobrados
# a R$ 4,50 por GB. Calcule o adicional e o total da fatura e mostre uma f-string.
mensalidade_ex16 = 129.90
gb_adicionais_ex16 = 7
preco_por_gb_ex16 = 4.50
# ESCREVA AQUI:

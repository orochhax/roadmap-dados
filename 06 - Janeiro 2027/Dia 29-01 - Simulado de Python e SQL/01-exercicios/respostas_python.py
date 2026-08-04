# Simulado Python — Dia 123
# Não há soluções prontas. Escreva cada resposta abaixo de ESCREVA AQUI.


# P1. [ ] LISTAS
# A partir das durações abaixo, crie outra lista somente com valores acima de
# 60 e calcule quantos valores foram selecionados.
duracoes_p1 = [15, 80, 45, 120, 30, 75, 200, 60]
# ESCREVA AQUI:


# P2. [ ] FUNÇÃO
# Crie classificar_sla(duracao, limite) que retorne "no prazo" quando duração
# for menor ou igual ao limite e "atrasado" nos demais casos. Teste (90, 90)
# e (91, 90).
# ESCREVA AQUI:


# P3. [ ] DICIONÁRIOS
# Conte quantos incidentes existem por cidade sem usar pandas.
cidades_p3 = ["Salvador", "Ilhéus", "Salvador", "Eunápolis", "Ilhéus", "Salvador"]
# ESCREVA AQUI:


# P4. [ ] ARQUIVOS
# Leia dados/incidentes.csv com csv.DictReader e mostre id e cidade das cinco
# primeiras linhas. Use pathlib para construir o caminho.
# ESCREVA AQUI:


# P5. [ ] TRATAMENTO DE ERRO
# Converta cada item para inteiro, guarde válidos e inválidos separadamente e
# não interrompa o laço quando encontrar texto.
valores_p5 = ["10", "7", "erro", "25", "", "42"]
# ESCREVA AQUI:


# P6. [ ] PANDAS E FILTRO
# Carregue dados/clientes_telecom.csv e selecione clientes com churn=1,
# nps<=4 e chamados_90d>=3. Mostre somente cliente_id, cidade e plano.
# ESCREVA AQUI:


# P7. [ ] PANDAS E AGREGAÇÃO
# Calcule por plano: quantidade de clientes, mensalidade média e taxa de churn.
# Ordene da maior para a menor taxa.
# ESCREVA AQUI:


# P8. [ ] MERGE
# Junte dados/clientes.csv a dados/planos.csv usando plano_id. Valide que a
# quantidade de clientes não aumentou depois do merge.
# ESCREVA AQUI:


# P9. [ ] VALIDAÇÃO
# Crie validar_metricas(total, resolvidos, reincidentes) que rejeite negativos,
# resolvidos acima do total e reincidentes acima de resolvidos. Teste
# (100, 82, 12), (0, 0, 0) e (10, 12, 1).
# ESCREVA AQUI:


# P10. [ ] FUNÇÃO E CUSTO
# Crie calcular_custo(fp, fn, custo_fp, custo_fn) e use os dados abaixo.
fp_p10 = 18
fn_p10 = 7
custo_fp_p10 = 20.0
custo_fn_p10 = 500.0
# ESCREVA AQUI:

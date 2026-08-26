# COMEÇO GUIADO
# Dados de partida: Dados pequenos definidos nos próprios exercícios e arquivos criados por você.
# Use somente esses dados ou os valores já declarados neste arquivo. Resolva uma tarefa
# por vez, execute e confira a saída antes de seguir para a próxima.

# Condicionais e regras de negócio
#
# OBJETIVO
# Complete uma única sequência com `if`, `elif` e `else` para definir a
# prioridade de um chamado. Você já conhece as condições; aqui o foco é a
# ORDEM: quando uma regra for verdadeira, as próximas não podem sobrescrevê-la.
#
# REGRAS (use exatamente nesta ordem)
# 1. risco de segurança: P1
# 2. cidade inteira afetada: P1
# 3. serviço crítico E mais de 100 clientes: P1
# 4. mais de 500 clientes OU duração acima de 180 minutos: P2
# 5. mais de 50 clientes: P3
# 6. todos os demais casos: P4
#
# COMO TRANSFORMAR UMA REGRA EM CÓDIGO
# Cada regra tem duas partes:
#
# 1. A PERGUNTA: o que precisa ser verdadeiro?
# 2. A RESPOSTA: qual prioridade deve ser guardada se for verdadeiro?
#
# Leia assim:
#
# Regra 1: "há risco de segurança?"
#   - variável que responde à pergunta: risco_seguranca
#   - se ela for True, guarde: prioridade = "P1"
#   - início da condição: if risco_seguranca:
#
# Regra 2: "a cidade inteira foi afetada?"
#   - variável: cidade_inteira
#   - se ela for True, guarde: prioridade = "P1"
#   - como é a próxima regra, ela começa com: elif cidade_inteira:
#
# Regra 3: "o serviço é crítico E há mais de 100 clientes?"
#   - as duas partes precisam ser verdadeiras: servico_critico e
#     clientes_afetados > 100
#   - junte as duas perguntas com `and`.
#
# Regra 4: "há mais de 500 clientes OU a duração é maior que 180?"
#   - compare: clientes_afetados > 500
#   - compare: duracao_min > 180
#   - basta uma parte ser verdadeira; junte-as com `or`.
#
# Regra 5: "há mais de 50 clientes?"
#   - compare: clientes_afetados > 50
#
# Regra 6: se todas as perguntas anteriores forem falsas, use `else` e guarde P4.
#
# MODELO DA ESTRUTURA (complete as condições e prioridades):
# if PERGUNTA_DA_REGRA_1:
#     prioridade = "..."
# elif PERGUNTA_DA_REGRA_2:
#     prioridade = "..."
# elif PERGUNTA_DA_REGRA_3:
#     prioridade = "..."
# elif PERGUNTA_DA_REGRA_4:
#     prioridade = "..."
# elif PERGUNTA_DA_REGRA_5:
#     prioridade = "..."
# else:
#     prioridade = "..."
#
# COMO RESPONDER
# 1. Complete somente a parte abaixo de # REGRAS.
# 2. Use `if` na primeira regra, `elif` nas regras seguintes e `else` na última.
# 3. Execute o arquivo. Neste primeiro cenário, a saída esperada é: P1.
# 4. Depois, troque APENAS os cinco valores de entrada pelos cenários de teste
#    prontos no fim do arquivo e execute novamente.

# CENÁRIOS DE TESTE PRONTOS
#
# Quando o primeiro cenário estiver funcionando, substitua os cinco valores do
# início do arquivo por UM bloco abaixo. Não altere as regras. Execute e confira
# se a prioridade impressa é a esperada.
#
# TESTE 1 — risco de segurança; esperado: P1
#clientes_afetados = 10
#duracao_min = 15
#servico_critico = False
#cidade_inteira = False
#risco_seguranca = True
#
# TESTE 2 — cidade inteira afetada; esperado: P1
# clientes_afetados = 10
# duracao_min = 15
# servico_critico = False
# cidade_inteira = True
# risco_seguranca = False
#
# TESTE 3 — limite de 50 clientes; esperado: P4
# clientes_afetados = 50
# duracao_min = 30
# servico_critico = False
# cidade_inteira = False
# risco_seguranca = False
#
# TESTE 4 — primeiro valor acima de 50; esperado: P3
clientes_afetados = 51
duracao_min = 30
servico_critico = False
cidade_inteira = False
risco_seguranca = False
#
# TESTE 5 — serviço crítico com exatamente 100 clientes; esperado: P3
# clientes_afetados = 100
# duracao_min = 30
# servico_critico = True
# cidade_inteira = False
# risco_seguranca = False
#
# TESTE 6 — serviço crítico com 101 clientes; esperado: P1
# clientes_afetados = 101
# duracao_min = 30
# servico_critico = True
# cidade_inteira = False
# risco_seguranca = False
#
#---------------------------------------------------------------------
# REGRAS — complete/corrija esta parte usando uma única cadeia if/elif/else.
# 1. Risco de segurança → P1
if risco_seguranca:
    prioridade = "P1"
#2. Cidade inteira → P1
if cidade_inteira:
    prioridade = "P1"
#3. Serviço crítico e mais de 100 clientes → P1
if servico_critico and clientes_afetados > 100:
    prioridade = "P1"
#4. Mais de 500 clientes OU duração acima de 180 minutos → P2
if clientes_afetados > 500 or duracao_min > 180:
    prioridade = "P2"
#5. Mais de 50 clientes → P3
if clientes_afetados > 50:
    prioridade = "P3"
#6. Demais casos → P4
else:
    prioridade = "P4"

print("Prioridade", prioridade)

#----------------------------------------------------------------------

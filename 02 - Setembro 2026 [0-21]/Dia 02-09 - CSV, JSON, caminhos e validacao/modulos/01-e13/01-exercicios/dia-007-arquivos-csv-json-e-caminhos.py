# Arquivos CSV, JSON e caminhos
#
# DADOS PRONTOS
# - incidentes.csv: 4 incidentes.
# - metas.json: duração máxima aceitável, por cidade.
#
# OBJETIVO
# Leia os dois arquivos sem pandas e monte um relatório. Use `Path(__file__)`
# para obter a pasta deste script; assim ele funciona independente do terminal.

from pathlib import Path
import csv
import json

pasta_atual = Path(__file__).parent
arquivo_incidentes = pasta_atual / "incidentes.csv"
arquivo_metas = pasta_atual / "metas.json"

# EXERCÍCIO 1
# Leia incidentes.csv com csv.DictReader e guarde as linhas em uma lista.
# Resultado esperado: a lista tem 4 dicionários.
# ESCREVA AQUI:


# EXERCÍCIO 2
# Leia metas.json com json.load. Converta duracao_min e clientes_afetados de cada
# incidente para int. Converta resolvido para bool.
# ESCREVA AQUI:


# EXERCÍCIO 3
# Para cada incidente, crie `dentro_da_meta`: True quando a duração for menor ou
# igual à meta da cidade. Imprima id e esse resultado.
# Resultado esperado: INC-001=False, INC-002=True, INC-003=True, INC-004=True.
# ESCREVA AQUI:


# EXERCÍCIO 4 — gravação do relatório
# Grave relatorio_consolidado.csv na pasta 03-evidencias, com todas as colunas
# originais e dentro_da_meta.

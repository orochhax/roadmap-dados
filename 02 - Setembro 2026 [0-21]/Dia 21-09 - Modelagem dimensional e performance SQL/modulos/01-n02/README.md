# Modelo dimensional para operações de telecom

## Objetivo

Projetar um modelo estrela auditável para responder perguntas de incidentes, clientes e planos sem multiplicar métricas em joins. Você praticará grão, chaves substitutas, dimensões conformadas e histórico SCD tipo 2.

## Pesquise exatamente estes nomes

- `Kimball dimensional modeling grain fact dimension`
- `star schema fact table dimension table`
- `surrogate key vs natural key data warehouse`
- `slowly changing dimension type 1 type 2`
- `role playing date dimension`
- `accumulating snapshot fact table`
- `DuckDB CREATE TABLE constraints`

## Trabalho obrigatório

Leia o [enunciado](01-exercicios/ENUNCIADO.md), complete [modelo_estrela.sql](01-exercicios/modelo_estrela.sql) e registre as reconciliações em [Evidências](03-evidencias/README.md).

## Concluído quando

- o grão de cada fato está escrito antes do DDL;
- o histórico de plano não reescreve o passado;
- joins preservam a quantidade e o valor das linhas-fato;
- uma mudança tardia e uma chave desconhecida foram tratadas;
- o modelo responde às perguntas do gerente sem consulta ambígua.


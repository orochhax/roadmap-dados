-- Dia 021 — Banco relacional e SELECT
--
-- DADOS: dados/incidentes.csv
-- TABELA A CRIAR: incidentes
--
-- Não há consultas resolvidas neste arquivo. Antes de cada resposta, escreva
-- em comentário quantas linhas e colunas você acredita que a consulta retornará.


-- PREPARAÇÃO
-- [ ] Crie o banco roadmap_ds no PostgreSQL ou abra um banco DuckDB.
-- [ ] Crie a tabela incidentes escolhendo tipos adequados e id como chave primária.
-- [ ] Importe dados/incidentes.csv sem editar o arquivo original.


-- 1. [ ] TODAS AS COLUNAS
-- Retorne todas as colunas da tabela incidentes.
-- ESCREVA AQUI:


-- 2. [ ] COLUNAS ESPECÍFICAS
-- Retorne somente id, cidade, severidade e duracao_min.
-- ESCREVA AQUI:


-- 3. [ ] ALIAS
-- Retorne id como incidente, cidade como localidade e duracao_min como minutos.
-- ESCREVA AQUI:


-- 4. [ ] VALORES DISTINTOS
-- Liste cada cidade uma única vez.
-- ESCREVA AQUI:


-- 5. [ ] LIMITE
-- Retorne somente as 10 primeiras linhas da tabela.
-- ESCREVA AQUI:


-- 6. [ ] ORDENAÇÃO CRESCENTE E DECRESCENTE
-- Faça uma consulta com menor duração primeiro e outra com maior duração primeiro.
-- Em empates, use id em ordem crescente.
-- ESCREVA AQUI:


-- 7. [ ] EXPRESSÃO CALCULADA
-- Retorne id, duracao_min e uma coluna duracao_horas calculada a partir dos minutos.
-- ESCREVA AQUI:


-- 8. [ ] CONCATENAÇÃO
-- Crie uma coluna rotulo juntando id, cidade e severidade com separadores legíveis.
-- ESCREVA AQUI:


-- 9. [ ] COALESCE
-- Retorne id e observacao, substituindo observação nula por 'sem observação'.
-- ESCREVA AQUI:


-- 10. [ ] CAST
-- Converta duracao_min para um tipo decimal antes de calcular duracao_horas.
-- ESCREVA AQUI:


-- 11. [ ] CASE
-- Crie faixa_duracao com três categorias: até 60, de 61 a 120 e acima de 120.
-- ESCREVA AQUI:


-- 12. [ ] CONTAGEM TOTAL
-- Retorne a quantidade total de linhas da tabela com o alias total_incidentes.
-- ESCREVA AQUI:


-- 13. [ ] IMPACTO E TOP 5
-- Calcule impacto = duracao_min * clientes_afetados e retorne os cinco maiores,
-- exibindo id, cidade, duração, clientes afetados e impacto.
-- ESCREVA AQUI:


-- EXERCÍCIOS EXTRAS ESPECÍFICOS
-- 1. [ ] Liste incidentes P1 não resolvidos, calcule impacto, ordene do maior
-- para o menor e limite a cinco linhas.
-- ESCREVA AQUI:

-- 2. [ ] Compare COUNT(*) com COUNT(DISTINCT id) e conte ids nulos antes de
-- aceitar a importação.
-- ESCREVA AQUI:

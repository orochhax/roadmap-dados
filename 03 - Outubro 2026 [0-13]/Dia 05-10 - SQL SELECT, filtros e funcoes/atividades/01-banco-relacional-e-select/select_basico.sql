-- COMEÇO GUIADO
-- Dados de partida: Tabelas importadas de `dados/clientes.csv`, `planos.csv`, `chamados.csv`, `pagamentos.csv`, `incidentes.csv` e `pedidos.csv`.
-- Use as tabelas já carregadas. Escreva e execute uma consulta por vez; confira as
-- colunas e as linhas retornadas antes de seguir.

-- Banco relacional e SELECT
--
-- DADOS: dados/incidentes.csv
-- TABELA A CRIAR: incidentes
--
-- Não há consultas resolvidas neste arquivo. Antes de cada resposta, escreva
-- em comentário quantas linhas e colunas você acredita que a consulta retornará.
-- NÚCLEO ESSENCIAL: preparação e consultas 2, 3, 5 e 6.


-- PREPARAÇÃO
-- Crie o banco roadmap_ds no PostgreSQL ou abra um banco DuckDB.
-- Crie a tabela incidentes escolhendo tipos adequados e id como chave primária.
-- Importe dados/incidentes.csv sem editar o arquivo original.


-- 2. COLUNAS ESPECÍFICAS
-- Retorne somente id, cidade, severidade e duracao_min.
-- ESCREVA AQUI:


-- 3. ALIAS
-- Retorne id como incidente, cidade como localidade e duracao_min como minutos.
-- ESCREVA AQUI:


-- 5. LIMITE
-- Retorne somente as 10 primeiras linhas da tabela.
-- ESCREVA AQUI:


-- 6. ORDENAÇÃO CRESCENTE E DECRESCENTE
-- Faça uma consulta com menor duração primeiro e outra com maior duração primeiro.
-- Em empates, use id em ordem crescente.
-- ESCREVA AQUI:


-- PRÁTICA OBRIGATÓRIA
-- 1. Liste incidentes P1 não resolvidos, calcule impacto, ordene do maior
-- para o menor e limite a cinco linhas.
-- ESCREVA AQUI:

-- 2. Compare COUNT(*) com COUNT(DISTINCT id) e conte ids nulos antes de
-- aceitar a importação.
-- ESCREVA AQUI:

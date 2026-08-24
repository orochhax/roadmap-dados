-- Starter executavel do mini-case SQL.
--
-- Execute este arquivo no DuckDB a partir da raiz do repositorio para que os
-- caminhos em `dados/` sejam encontrados. A preparacao das views abaixo nao
-- responde as perguntas do case; ela apenas disponibiliza as entradas.

CREATE OR REPLACE VIEW clientes AS
SELECT * FROM read_csv_auto('dados/clientes.csv', header = true);

CREATE OR REPLACE VIEW planos AS
SELECT * FROM read_csv_auto('dados/planos.csv', header = true);

CREATE OR REPLACE VIEW chamados AS
SELECT * FROM read_csv_auto('dados/chamados.csv', header = true);

CREATE OR REPLACE VIEW pagamentos AS
SELECT * FROM read_csv_auto('dados/pagamentos.csv', header = true);

CREATE OR REPLACE VIEW incidentes AS
SELECT * FROM read_csv_auto('dados/incidentes.csv', header = true);

CREATE OR REPLACE VIEW pedidos AS
SELECT * FROM read_csv_auto('dados/pedidos.csv', header = true);

CREATE OR REPLACE VIEW clientes_telecom AS
SELECT * FROM read_csv_auto('dados/clientes_telecom.csv', header = true);

-- Verificacao inicial: confirme apenas se todas as fontes foram carregadas.
SELECT 'clientes' AS tabela, COUNT(*) AS linhas FROM clientes
UNION ALL
SELECT 'planos', COUNT(*) FROM planos
UNION ALL
SELECT 'chamados', COUNT(*) FROM chamados
UNION ALL
SELECT 'pagamentos', COUNT(*) FROM pagamentos
UNION ALL
SELECT 'incidentes', COUNT(*) FROM incidentes
UNION ALL
SELECT 'pedidos', COUNT(*) FROM pedidos
UNION ALL
SELECT 'clientes_telecom', COUNT(*) FROM clientes_telecom;

-- DESAFIO 1
-- Quantos clientes existem por cidade e qual e a mensalidade media?
-- TODO: escreva a consulta sem copiar uma solucao pronta.

-- DESAFIO 2
-- Qual e a receita total e o ticket medio dos pedidos por canal?
-- TODO: escreva a consulta e declare qual coluna representa a receita.

-- DESAFIO 3
-- Qual e o valor pendente e a quantidade de pagamentos pendentes por cidade?
-- TODO: defina o status considerado pendente e confira a cardinalidade do JOIN.

-- DESAFIO 4
-- Quais clientes abriram pelo menos tres chamados e qual foi a duracao total?
-- TODO: use GROUP BY e HAVING e registre como tratou clientes sem chamados.

-- DESAFIO 5
-- Quantos clientes existem em cada plano, incluindo planos sem clientes?
-- TODO: escolha o tipo de JOIN que preserva todos os planos.

-- PRATICA OBRIGATORIA
-- Calcule churn por cidade somente para cidades com pelo menos 30 clientes e
-- ordene pela maior taxa.
-- TODO: declare claramente o denominador da taxa de churn.

-- VALIDACAO
-- TODO: escolha a primeira cidade do ranking e confira contagem e taxa em uma
-- segunda consulta simples antes de reproduzir a mesma verificacao em pandas.

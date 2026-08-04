-- Dia 022 — Filtros e funções
--
-- DADOS: dados/incidentes.csv
-- TABELA: incidentes, criada no exercício anterior
-- Nenhuma consulta está resolvida abaixo.


-- PARTE A — 15 CONSULTAS COM WHERE

-- 1. [ ] IGUALDADE
-- Retorne somente incidentes com severidade igual a P1.
-- ESCREVA AQUI:

-- 2. [ ] DIFERENÇA
-- Retorne incidentes cuja cidade seja diferente de Salvador.
-- ESCREVA AQUI:

-- 3. [ ] MAIOR QUE
-- Retorne incidentes com duração acima de 120 minutos.
-- ESCREVA AQUI:

-- 4. [ ] MENOR OU IGUAL
-- Retorne incidentes com duração menor ou igual a 50 minutos.
-- ESCREVA AQUI:

-- 5. [ ] BETWEEN
-- Retorne durações entre 51 e 120 minutos, incluindo os dois limites.
-- ESCREVA AQUI:

-- 6. [ ] IN
-- Retorne incidentes de Salvador, Ilhéus ou Eunápolis.
-- ESCREVA AQUI:

-- 7. [ ] LIKE
-- Retorne causas que contenham a palavra 'fibra', independentemente do texto ao redor.
-- ESCREVA AQUI:

-- 8. [ ] IS NULL
-- Retorne eventos ainda sem data de fechamento.
-- ESCREVA AQUI:

-- 9. [ ] AND
-- Retorne incidentes P1 que ainda não foram resolvidos.
-- ESCREVA AQUI:

-- 10. [ ] OR
-- Retorne incidentes com mais de 500 clientes afetados OU duração acima de 180.
-- ESCREVA AQUI:

-- 11. [ ] NOT
-- Retorne somente linhas que não estejam marcadas como resolvidas.
-- ESCREVA AQUI:

-- 12. [ ] PARÊNTESES COM AND E OR
-- Retorne P1 ou P2 somente nas cidades Salvador e Feira de Santana.
-- Use parênteses para deixar a precedência explícita.
-- ESCREVA AQUI:

-- 13. [ ] TEXTO E CIDADE
-- Retorne incidentes de Ilhéus cuja causa contenha 'energia'.
-- ESCREVA AQUI:

-- 14. [ ] NÚMERO E STATUS
-- Retorne linhas resolvidas com pelo menos 100 clientes afetados.
-- ESCREVA AQUI:

-- 15. [ ] DATA
-- Retorne incidentes abertos entre 01/07/2026 e 31/07/2026, incluindo o mês inteiro.
-- ESCREVA AQUI:


-- PARTE B — FILTROS DE NEGÓCIO

-- 16. [ ] Liste P1 não resolvidos e ordene pela maior duração.
-- ESCREVA AQUI:

-- 17. [ ] Liste incidentes acima de 120 minutos com id, cidade e causa.
-- ESCREVA AQUI:

-- 18. [ ] Liste incidentes com mais de 100 clientes afetados.
-- ESCREVA AQUI:

-- 19. [ ] Liste causas contendo 'fibra' e padronize cidade para letras maiúsculas.
-- ESCREVA AQUI:


-- PARTE C — FUNÇÕES

-- 20. [ ] Retorne cidade sem espaços nas pontas e em letras maiúsculas.
-- ESCREVA AQUI:

-- 21. [ ] Calcule impacto, arredonde para duas casas e dê alias impacto_arredondado.
-- ESCREVA AQUI:

-- 22. [ ] Substitua observacao nula por 'não informada'.
-- ESCREVA AQUI:


-- PARTE D — PRECEDÊNCIA

-- 23. [ ] Escreva três versões usando cidade, severidade e resolvido. Mantenha
-- os mesmos termos, altere somente os parênteses e compare as contagens.
-- ESCREVA AQUI:


-- PARTE E — LIMITES

-- 24. [ ] Retorne somente durações 50, 51, 120 e 121 para conferir inclusão.
-- ESCREVA AQUI:


-- EXERCÍCIOS EXTRAS ESPECÍFICOS
-- 1. [ ] Consulte Salvador ou Ilhéus, duração entre 51 e 120 e causa com 'fibra'.
-- ESCREVA AQUI:

-- 2. [ ] Conte duração nula, cidade nula e ids duplicados em colunas identificadas.
-- ESCREVA AQUI:

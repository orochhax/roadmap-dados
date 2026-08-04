# Simulado SQL — 20 questões

> Use as tabelas importadas de `dados/`. Não abra respostas durante os primeiros 90 minutos. Este arquivo não contém soluções.

Registre em cada questão: início, fim, confiança de 1–5 e se consultou documentação.

## Filtros — questões 1 a 5

1. [ ] Em `incidentes`, liste id, cidade e duração dos P1 não resolvidos, do mais demorado para o menos demorado.
2. [ ] Liste incidentes com duração entre 51 e 120 minutos nas cidades Salvador ou Ilhéus.
3. [ ] Liste causas contendo `fibra` com mais de 100 clientes afetados.
4. [ ] Em `pagamentos`, liste pagamentos pendentes com vencimento anterior a 01/07/2026.
5. [ ] Em `clientes_telecom`, liste clientes com NPS até 4 e pelo menos três chamados nos últimos 90 dias.

## Agregações — questões 6 a 9

6. [ ] Calcule quantidade, duração média e clientes afetados totais por cidade.
7. [ ] Calcule taxa de resolução por severidade com proteção contra divisão por zero.
8. [ ] Liste planos com pelo menos 20 clientes e mensalidade média acima de R$100.
9. [ ] Calcule valor pago e valor pendente por mês usando `pagamentos`.

## JOINs — questões 10 a 13

10. [ ] Junte `clientes` e `planos` para mostrar cliente, cidade, plano e mensalidade-base.
11. [ ] Encontre clientes sem nenhum pagamento usando `LEFT JOIN`.
12. [ ] Encontre planos sem clientes usando anti-join.
13. [ ] Junte clientes, chamados e pagamentos sem inflar valores; agregue cada tabela na granularidade necessária antes do join final.

## CTEs e subconsultas — questões 14 a 16

14. [ ] Use CTE para calcular duração média por cidade e listar incidentes acima da média da própria cidade.
15. [ ] Use três CTEs: pagamentos válidos, total por cliente e ranking dos cinco maiores totais.
16. [ ] Use subconsulta para listar clientes cuja mensalidade está acima da média do próprio plano.

## Funções de janela — questões 17 e 18

17. [ ] Ranqueie os três incidentes de maior impacto dentro de cada cidade, mantendo empates com `DENSE_RANK`.
18. [ ] Calcule soma acumulada mensal de pagamentos por cliente e o valor do pagamento anterior com `LAG`.

## Datas — questões 19 e 20

19. [ ] Calcule quantidade de incidentes por mês, incluindo ano e mês em colunas separadas.
20. [ ] Calcule dias entre vencimento e pagamento; classifique pendentes separadamente, sem inventar data de quitação.

## Controle do simulado

| Questão | Minutos | Confiança 1–5 | Consultou? | Revisar? |
|---:|---:|---:|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |
| 6 |  |  |  |  |
| 7 |  |  |  |  |
| 8 |  |  |  |  |
| 9 |  |  |  |  |
| 10 |  |  |  |  |
| 11 |  |  |  |  |
| 12 |  |  |  |  |
| 13 |  |  |  |  |
| 14 |  |  |  |  |
| 15 |  |  |  |  |
| 16 |  |  |  |  |
| 17 |  |  |  |  |
| 18 |  |  |  |  |
| 19 |  |  |  |  |
| 20 |  |  |  |  |

## Exercícios extras específicos

1. [ ] Depois do simulado, escreva uma 21ª consulta que encontre os três clientes com maior soma de pagamentos pendentes.
2. [ ] Valide a 21ª consulta comparando quantidade de pagamentos, clientes distintos e soma antes e depois dos joins.

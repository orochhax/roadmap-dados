# Dashboard introdutório

## Aprenda agora

Um dashboard liga cada indicador a uma decisão. No Power BI, uma medida básica pode ser `Incidentes = COUNTROWS(incidentes)`; sem Power BI, produza os mesmos indicadores e filtros no notebook com pandas.

Antes de montar páginas, registre para cada métrica: fórmula, granularidade, filtro temporal e fonte.

**Erro comum:** somar uma métrica já agregada ou misturar filtros diferentes entre o cartão e a tabela de validação.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-019-dashboard-introdutorio.ipynb`.
- **Dados:** `dados/incidentes.csv`, `dados/clientes_telecom.csv`, `dados/pedidos.csv` e `dados/metas_cidades.csv`.

## Núcleo essencial

1. [ ] Defina um público-alvo para o dashboard: gerente de operações de telecom; escreva cinco decisões que ele precisa tomar.
2. [ ] Crie no Power BI ou alternativa quatro indicadores: incidentes, duração média, clientes afetados e percentual dentro da meta.
3. [ ] Adicione filtros de período, cidade e severidade; crie duas páginas: visão executiva e diagnóstico.

## Prática obrigatória

- [ ] Valide cada número do dashboard contra uma consulta ou cálculo em pandas.
- [ ] Escreva `dicionario_metricas.md` com fórmula, fonte, periodicidade e risco de interpretação de cada indicador.
- [ ] **Em `01-exercicios/dia-019-dashboard-introdutorio.ipynb`:** Crie uma tabela de validação dos quatro indicadores somente para severidade P1 e compare com a página executiva sob o mesmo filtro.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

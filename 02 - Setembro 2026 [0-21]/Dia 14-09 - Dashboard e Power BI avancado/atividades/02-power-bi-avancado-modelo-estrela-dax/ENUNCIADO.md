# Enunciado — painel de risco operacional do NOC

## Cenário real

O gerente de operações precisa iniciar a reunião diária sabendo quais cidades e severidades concentram impacto, quais SLAs estão piorando e se o volume aumentou por evento real ou por duplicação no modelo. Você recebeu CSVs usados por equipes diferentes e deverá criar uma versão única no Power BI.

## Entradas

- `dados/incidentes.csv`;
- `dados/metas_cidades.csv`;
- `dados/clientes.csv` para contextualizar base atendida;
- calendário contínuo criado no modelo, cobrindo todo o período das fontes.

## Saídas

- arquivo `telecom_noc.pbix` criado nesta pasta de exercícios;
- [roteiro_power_bi.md](roteiro_power_bi.md) preenchido com modelo, medidas e testes;
- capturas das páginas e exportação do Performance Analyzer referenciadas no próprio artefato.

## Regras obrigatórias

1. Modele dimensões de data, cidade e severidade e fatos no menor grão disponível.
2. Use relacionamentos um-para-muitos e direção única; qualquer exceção precisa ser explicada.
3. Crie medidas: incidentes distintos, clientes afetados, duração média, percentual resolvido, percentual dentro da meta e variação contra período anterior.
4. Use `DIVIDE` nas taxas e defina o que mostrar quando o denominador for zero.
5. Página executiva: quatro KPIs, tendência, ranking de cidades e alerta textual.
6. Página diagnóstica: distribuição por severidade, tabela de incidentes e decomposição da meta.
7. Inclua filtros de período, cidade e severidade que afetem todos os visuais esperados.
8. Valide cada KPI com SQL ou pandas usando exatamente os mesmos filtros.
9. Execute Performance Analyzer e investigue o visual mais lento.
10. Use títulos que expressem conclusão, contraste legível e texto alternativo nos principais visuais.

## Casos de borda obrigatórios

- período sem incidentes;
- cidade presente em incidentes, mas ausente em metas;
- cidade presente em metas, mas sem incidente;
- id de incidente duplicado;
- meta igual a zero;
- seleção de múltiplas cidades com escalas muito diferentes.

## Métricas e conferências

- diferença absoluta entre cada KPI do Power BI e o cálculo externo: deve ser zero, salvo arredondamento documentado;
- número de chaves sem correspondência;
- tempo de cada visual e tempo total da página no Performance Analyzer;
- quantidade de decisões do gerente atendidas pelo painel: pelo menos três, descritas antes da construção.

## Critério de aceite

- O modelo não multiplica incidentes ou clientes por relacionamento ambíguo.
- As seis medidas respondem corretamente aos três filtros.
- Três recortes, incluindo um caso de borda, foram reconciliados externamente.
- O visual mais lento tem hipótese e ação registrada.
- A recomendação diária cita um número do painel e uma limitação.


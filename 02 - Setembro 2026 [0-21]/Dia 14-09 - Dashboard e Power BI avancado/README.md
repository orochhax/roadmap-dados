# Excel analítico, Power Query e Power BI: da reconciliação ao dashboard

**Data de estudo:** 14/09/2026  
**Carga planejada:** 7 a 9 horas

## Atividades do dia

### Atividade 1 — Dashboard introdutorio

#### O que pesquisar
- `Dashboard introdutorio Python explicado passo a passo`
- `Dashboard introdutorio Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-dashboard-introdutorio`](<atividades/01-dashboard-introdutorio/>)

#### O que você precisa entender

Um dashboard liga cada indicador a uma decisão. No Power BI, uma medida básica pode ser `Incidentes = COUNTROWS(incidentes)`; sem Power BI, produza os mesmos indicadores e filtros no notebook com pandas.

Antes de montar páginas, registre para cada métrica: fórmula, granularidade, filtro temporal e fonte.

**Erro comum:** somar uma métrica já agregada ou misturar filtros diferentes entre o cartão e a tabela de validação.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-dashboard-introdutorio/dia-019-dashboard-introdutorio.ipynb`.
- **Dados:** `dados/incidentes.csv`, `dados/clientes_telecom.csv`, `dados/pedidos.csv` e `dados/metas_cidades.csv`.

#### O que fazer

- [ ] Defina um público-alvo para o dashboard: gerente de operações de telecom; escreva cinco decisões que ele precisa tomar.
- [ ] Crie no Power BI ou alternativa quatro indicadores: incidentes, duração média, clientes afetados e percentual dentro da meta.
- [ ] Adicione filtros de período, cidade e severidade; crie duas páginas: visão executiva e diagnóstico.

- [ ] Valide cada número do dashboard contra uma consulta ou cálculo em pandas.
- [ ] Escreva `dicionario_metricas.md` com fórmula, fonte, periodicidade e risco de interpretação de cada indicador.
- [ ] **Em `atividades/01-dashboard-introdutorio/dia-019-dashboard-introdutorio.ipynb`:** Crie uma tabela de validação dos quatro indicadores somente para severidade P1 e compare com a página executiva sob o mesmo filtro.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

### Atividade 2 — Power BI avançado: modelo estrela, DAX e contexto de filtro

#### O que pesquisar
- `Power BI star schema`
- `DAX row context e filter context`
- `CALCULATE`
- `Performance Analyzer`

**Arquivos da atividade:** [abrir a pasta `02-power-bi-avancado-modelo-estrela-dax`](<atividades/02-power-bi-avancado-modelo-estrela-dax/>)

#### Aula guiada — primeiras fórmulas DAX

- [ ] Assista **Curso Básico de Power BI - Aula 3 - Introdução às Fórmulas do Power BI**. [Abrir no YouTube](https://www.youtube.com/watch?v=xx3uYFmsqG4)
- Use a aula como introdução. Na prática, avance para medidas explícitas, contexto de filtro, `CALCULATE`, `DIVIDE`, tabela de datas e validação externa dos resultados.

#### Objetivo

Construir um dashboard que continue correto sob filtros, usando modelo estrela, medidas explícitas e validação externa. O resultado deve ajudar um gerente do NOC a decidir onde atuar, não apenas exibir gráficos.

#### Termos complementares para pesquisar

- `Power BI star schema relationships single direction`
- `DAX row context filter context`
- `DAX CALCULATE context transition`
- `DAX DIVIDE function`
- `DAX time intelligence marked date table`
- `Power BI Performance Analyzer`
- `Power BI DAX Studio server timings`
- `Power BI accessibility color contrast alt text`

#### O que fazer

Leia o [enunciado](<atividades/02-power-bi-avancado-modelo-estrela-dax/ENUNCIADO.md>), preencha [roteiro_power_bi.md](<atividades/02-power-bi-avancado-modelo-estrela-dax/roteiro_power_bi.md>) durante a construção e registre números conferidos no próprio artefato.

#### Como validar

- o modelo usa dimensões e relacionamentos justificados;
- cada KPI é uma medida DAX explícita;
- três recortes foram reconciliados fora do visual;
- o Performance Analyzer foi executado;
- o dashboard sustenta uma decisão e declara uma limitação.

### Atividade 3 — Excel analítico e Power Query

#### O que pesquisar
- `Excel tabela estruturada referências estruturadas`
- `Excel SE SEERRO SOMASES CONT.SES PROCX`
- `Excel tabela dinâmica segmentação de dados`
- `Excel reconciliação de bases valores divergentes`
- `Power Query tipos de dados trim clean remover duplicados`
- `Power Query merge append diferença`
- `Power Query atualização refresh pasta de arquivos`
- `Power Pivot modelo de dados relacionamentos`

**Arquivos da atividade:** [abrir a pasta `03-excel-analitico-e-power-query`](<atividades/03-excel-analitico-e-power-query/>)

#### Aulas guiadas — fórmulas, tabelas e segmentação

- [ ] Assista **Curso Excel #09 - Fórmulas Básicas** (13:18).
- [ ] Assista **Curso Excel #10 - Funções do Excel (Parte 1)** (17:35).
- [ ] Assista **Curso Excel #11 - Funções do Excel (Parte 2)** (14:06).
- [ ] Em [**Curso de Excel - Aula 2 [Formatação, Tabela Dinâmica e Segmentação de Dados]**](https://www.youtube.com/watch?v=jwENtgi8ics), assista de `00:27:15` a `00:56:08`: formatar como tabela, criar tabela dinâmica e usar segmentação de dados.
- **Carga total de vídeo do dia:** aproximadamente 1h50, incluindo a aula de Power BI e as quatro seleções de Excel.
- Use os nomes completos acima para localizar as aulas no YouTube. As aulas fornecem a base; o enunciado local exige reconciliação, Power Query, `Append`, `Merge`, atualização e Modelo de Dados.

#### Objetivo

Transformar arquivos mensais e cadastros imperfeitos em uma base reconciliada e atualizável, usando Excel e Power Query de verdade. O resultado precisa permitir auditoria: cada total do resumo deve voltar às linhas que o formaram e cada divergência deve ter uma classificação.

#### O que fazer

- [ ] Transforme intervalos em tabelas estruturadas e pratique referências que se expandem com novas linhas.
- [ ] Use fórmulas condicionais, agregações por critérios, busca entre tabelas e tratamento de erros em colunas de conferência.
- [ ] Monte uma tabela dinâmica com filtros e segmentações para responder perguntas de negócio.
- [ ] No Power Query, importe os arquivos, corrija tipos, espaços, valores ausentes, duplicidades e erros sem alterar manualmente as fontes.
- [ ] Diferencie `Acrescentar/Append` de `Mesclar/Merge`: una os meses em linhas e enriqueça os pedidos com cadastro em colunas.
- [ ] Reconcilie vendas e recebimentos, classificando correspondências, diferenças de valor e registros ausentes em uma das bases.
- [ ] Carregue tabelas no Modelo de Dados, crie relacionamentos coerentes e explique quando uma tabela única deixa de ser suficiente.
- [ ] Adicione novos dados nas fontes e use `Atualizar Tudo` para provar que o fluxo é repetível.

Leia o [enunciado](<atividades/03-excel-analitico-e-power-query/ENUNCIADO.md>), use os quatro CSVs preparados e preencha [roteiro_excel_power_query.md](<atividades/03-excel-analitico-e-power-query/roteiro_excel_power_query.md>) enquanto constrói sua pasta de trabalho. Salve o arquivo final dentro de `atividades/03-excel-analitico-e-power-query/02-pratica/` e registre conferências no próprio artefato.

#### Marco oficial Microsoft Learn

- [ ] Conclua a trilha gratuita [Prepare data for analysis with Power BI](https://learn.microsoft.com/en-us/training/paths/prepare-data-power-bi/).
- [ ] Faça o [simulado Microsoft Power BI](<../../00 - Recursos Compartilhados/simulados-credenciais/simulado-microsoft-power-bi.md>) sem consultar material durante a tentativa e registre os assuntos que precisa revisar.
- [ ] Use `fechamento_comercial.xlsx`, consultas, reconciliações e resultados desta atividade para provar aplicação prática, em vez de registrar somente a conclusão do curso.

**Distinção importante:** concluir a trilha gera progresso/achievement no Microsoft Learn, mas não equivale à certificação profissional **PL-300**, cuja prova é paga.

#### Como validar

- Usei Excel e Power Query no trabalho prático; o arquivo final abre e suas consultas podem ser atualizadas.
- Apliquei fórmulas, tabela estruturada, tabela dinâmica e pelo menos uma reconciliação linha a linha.
- Fiz `Append`, `Merge`, limpeza, tipagem e tratamento de duplicidades com passos reproduzíveis.
- Modelei relacionamentos no Modelo de Dados e expliquei a granularidade e a chave de cada tabela.
- Acrescentei um novo registro em uma fonte, atualizei tudo e reconferi os totais sem refazer o processo manualmente.
- Registrei duas divergências reais dos dados preparados e a decisão tomada para cada uma.
- Concluí a trilha oficial, fiz o simulado e vinculei o achievement à prática desta atividade sem declarar a certificação PL-300.

## Integração do dia

Explique com suas palavras como Excel, Power Query, modelo de dados e Power BI se conectam do arquivo bruto à decisão gerencial. Execute um caso comum e um caso de borda de cada atividade e registre comandos, saídas e dúvidas no próprio artefato.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

# Case técnico cronometrado — NexoVarejo

## Briefing de negócio

A **NexoVarejo** é uma empresa fictícia que vende itens de tecnologia por loja, marketplace e site. A direção acredita que a receita cresceu no último trimestre de 2026, mas percebeu mais cancelamentos, atraso em entregas e diferença entre números apresentados pelas áreas.

Você tem **4 horas e 30 minutos** para produzir uma análise inicial confiável e recomendar a primeira ação que a direção deve tomar. Os dados são totalmente sintéticos.

## Pergunta principal

> Em qual combinação de mês, canal, região, segmento ou categoria a NexoVarejo deve agir primeiro para melhorar resultado sem aumentar desnecessariamente o risco operacional?

Sua resposta precisa definir o que considera resultado e risco. Não existe uma escolha válida sem regra de cálculo explícita.

## Arquivos recebidos

- `dados/clientes.csv`: cadastro e segmento dos clientes;
- `dados/produtos.csv`: catálogo e custo unitário;
- `dados/pedidos.csv`: itens vendidos, preço, desconto, frete, status e entrega;
- `dados/metas.csv`: metas mensais por canal.

Os arquivos contêm problemas intencionais. Não modifique os CSVs originais. Registre os tratamentos em Power Query, SQL ou Python para que possam ser repetidos.

## Timeboxes obrigatórios

| Etapa | Minutos | Saída mínima ao encerrar |
|---|---:|---|
| Leitura, plano e definições | 15 | hipóteses, grão e métricas propostas |
| Perfil e qualidade dos dados | 30 | inventário de problemas e decisões |
| SQL | 60 | consultas salvas e resultados verificados |
| Python | 50 | script executável, validações e gráficos |
| Excel + Power Query | 45 | arquivo tratado, reconciliação e tabela dinâmica |
| Power BI | 50 | modelo, medidas e página executiva |
| Síntese executiva | 20 | recomendação e limitações |
| **Total** | **270** | entrega completa ou estado registrado |

Use `controle_tempo.md`. Quando um timebox terminar, não esconda o atraso: salve o que existe, registre o motivo e avance.

## Parte 1 — planejamento

Antes de abrir uma ferramenta, escreva:

1. qual é o grão de cada arquivo;
2. quais chaves devem conectar os arquivos;
3. como você definirá receita, margem estimada, ticket e cancelamento;
4. quais status entram ou não em cada métrica;
5. três hipóteses que podem responder à pergunta principal;
6. qual resultado seria suficiente para recomendar uma ação.

## Parte 2 — perfil e qualidade

Verifique pelo menos:

- número de linhas e chaves distintas;
- duplicidades exatas e de chave;
- valores ausentes;
- tipos e intervalos numéricos;
- domínios de status, canal, estado e segmento;
- clientes e produtos sem correspondência;
- datas fora do período esperado;
- consistência entre quantidade, preço, desconto, custo e status.

Crie uma tabela de decisões com: problema, quantidade afetada, tratamento, impacto possível e limitação. Não descarte linha sem justificativa.

## Parte 3 — SQL

Complete `consultas.sql`. Importe os CSVs em DuckDB ou SQLite e produza consultas legíveis para:

1. reconciliar linhas e chaves das quatro fontes;
2. calcular as métricas mensais por canal e comparar com as metas;
3. comparar desempenho por região e segmento;
4. identificar categorias ou produtos com pior combinação de resultado e risco;
5. medir cancelamento e atraso conforme definições explícitas;
6. ranquear, com função de janela, as três combinações prioritárias dentro de cada mês;
7. expor registros que violam uma regra de qualidade escolhida.

Use pelo menos um `JOIN`, uma CTE e uma função de janela. Evite `SELECT *` na entrega final.

## Parte 4 — Python

Complete `analise.py` de forma executável por comando. Inclua:

- leitura por caminhos relativos;
- validações de schema, chaves e domínios;
- funções pequenas para pelo menos duas etapas da análise;
- tabela analítica reproduzível;
- uma análise que complemente, em vez de apenas copiar, o SQL;
- dois gráficos com título, unidades, fonte e legenda quando necessária;
- exportação de uma tabela final para conferência.

O script deve falhar com mensagem compreensível se uma coluna essencial estiver ausente.

## Parte 5 — Excel e Power Query

Crie `analise_nexovarejo.xlsx` e:

1. importe os quatro CSVs pelo Power Query;
2. trate tipos, espaços e domínios de forma visível nas etapas aplicadas;
3. faça os merges necessários sem copiar e colar valores;
4. crie uma aba de reconciliação entre entrada e saída;
5. crie uma tabela dinâmica para uma hipótese prioritária;
6. inclua ao menos um segmentador e um gráfico adequado;
7. adicione uma aba `LEIA-ME` com atualização e definições de métricas.

Atualizar Tudo deve repetir a análise sem ajustes manuais.

## Parte 6 — Power BI

Crie `painel_nexovarejo.pbix` e:

1. modele fatos, dimensões e calendário com relações justificadas;
2. marque a tabela calendário e evite relacionamento muitos-para-muitos sem justificativa;
3. crie medidas DAX para as métricas principais;
4. mostre realizado versus meta;
5. entregue uma única página executiva com no máximo seis visuais;
6. ofereça filtros de período e de uma dimensão relevante;
7. use título ou tooltip para deixar regras de métrica claras.

O painel deve responder à pergunta principal em menos de um minuto de navegação.

## Parte 7 — reconciliação e recomendação

Escolha uma métrica principal e compare o valor obtido em pelo menos duas ferramentas. Registre filtros, arredondamento e diferença.

Complete `resposta_executiva.md` com:

- resposta direta em até duas frases;
- três evidências numéricas;
- ação recomendada, responsável e horizonte;
- risco de executar a ação;
- limitação dos dados;
- próximo teste ou dado necessário.

Não transforme correlação em causalidade. Se os dados só sustentam associação, escreva isso claramente.

## Entregáveis

- `consultas.sql` preenchido;
- `analise.py` preenchido e executável;
- `saida/tabela_analitica.csv` gerada pelo script;
- `analise_nexovarejo.xlsx` com Power Query e tabela dinâmica;
- `painel_nexovarejo.pbix` com uma página executiva;
- `controle_tempo.md` preenchido;
- `resposta_executiva.md` preenchido;
- o próprio artefato com comandos, capturas e autoavaliação.

## Rubrica objetiva — 100 pontos

| Critério | Pontos | Evidência esperada |
|---|---:|---|
| Planejamento, grão e métricas | 5 | definições antes da análise |
| Perfil, qualidade e rastreabilidade | 10 | problemas quantificados e decisões |
| SQL | 20 | correção, legibilidade, CTE, joins e janela |
| Python | 20 | execução, validação, funções e análise útil |
| Excel + Power Query | 15 | atualização, reconciliação e exploração |
| Power BI | 15 | modelo, DAX e clareza executiva |
| Recomendação e comunicação | 10 | evidência, ação, risco e limitação |
| Reprodutibilidade e gestão de tempo | 5 | instruções e controle preenchido |

Meta de conclusão: **70 pontos ou mais**, sem zerar SQL, Python, Excel/Power Query ou Power BI. A nota é diagnóstica: registre o que não conseguiu, sem preencher lacunas depois como se tivesse sido feito dentro do prazo.

## Revisão após o cronômetro

1. Corrija apenas erros de execução que impeçam verificar a entrega, marcando-os como revisão posterior.
2. Preencha a rubrica com evidências, não com impressão geral.
3. Escolha a lacuna que mais reduziu a qualidade ou consumiu tempo.
4. Faça uma prática isolada de no máximo 45 minutos para essa lacuna em outro momento.

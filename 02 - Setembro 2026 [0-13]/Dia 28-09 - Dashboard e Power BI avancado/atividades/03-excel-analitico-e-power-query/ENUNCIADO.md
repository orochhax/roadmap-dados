# Enunciado — fechamento comercial reproduzível no Excel e Power Query

## Cenário

Uma empresa recebeu duas planilhas mensais de vendas, um cadastro de clientes e um extrato de recebimentos. A diretoria quer o fechamento bimestral, mas os arquivos contêm espaços, formatos diferentes, cadastro repetido, valores ausentes e recebimentos que não batem com algumas vendas.

Seu trabalho é criar `fechamento_comercial.xlsx` usando Excel e Power Query. Não corrija os CSVs manualmente: toda transformação deve ficar registrada em fórmulas, consultas ou regras documentadas para que `Atualizar Tudo` repita o processo.

## Dados disponíveis

- `vendas_agosto.csv`: primeira competência de vendas;
- `vendas_setembro.csv`: segunda competência de vendas;
- `cadastro_clientes.csv`: cliente, segmento e região;
- `recebimentos.csv`: pagamentos associados aos pedidos.

Todos os dados são fictícios.

## Parte 1 — tabelas e fórmulas do Excel

Importe uma cópia da base de agosto para uma aba de estudo e transforme o intervalo em **Tabela**.

Crie colunas calculadas sem digitar resultados manualmente:

1. valor bruto a partir de quantidade e preço unitário;
2. valor do desconto e valor líquido;
3. faixa de valor definida por você e explicada no roteiro;
4. busca do segmento ou região no cadastro;
5. indicador de erro quando o cliente não for encontrado;
6. conferência de total por vendedor e por status usando critérios.

Pratique e explique quando usar:

- `SE` e `SEERRO`;
- `SOMASES` e `CONT.SES`;
- `PROCX` ou, se a versão não tiver essa função, a combinação de busca disponível nela;
- referências estruturadas de Tabela;
- referências relativas e absolutas.

Não basta a fórmula produzir um número: confira pelo menos três linhas à mão e registre as contas nas evidências.

## Parte 2 — tabela dinâmica e perguntas de negócio

Crie uma Tabela Dinâmica com segmentações que permita responder:

1. qual região concentra maior valor líquido;
2. quais vendedores têm maior número de pedidos;
3. como o valor líquido se distribui por segmento e mês;
4. onde estão pedidos ainda não reconciliados com recebimentos.

Escolha um gráfico somente depois de escrever qual comparação ele deve facilitar. Evite usar quantidade de linhas como se fosse receita.

## Parte 3 — tratamento no Power Query

Crie consultas para as quatro fontes e mantenha os passos visíveis. O fluxo deve:

1. definir os tipos corretos para datas, números e textos;
2. remover espaços invisíveis e padronizar caixa apenas quando isso não destruir informação;
3. tratar campo vazio, erro de conversão e linha repetida com regra explicada;
4. preservar a fonte original sem edição manual;
5. **Acrescentar/Append** agosto e setembro em uma tabela de vendas;
6. **Mesclar/Merge** vendas com cadastro de clientes;
7. agrupar recebimentos por pedido antes da reconciliação quando houver mais de um pagamento;
8. criar uma classificação de reconciliação que diferencie: valor igual, valor divergente, venda sem recebimento e recebimento sem venda;
9. manter uma consulta de exceções para não esconder linhas problemáticas.

## Parte 4 — Modelo de Dados e noção de Power Pivot

Carregue as tabelas adequadas no Modelo de Dados e desenhe antes os relacionamentos. Para cada tabela, declare:

- o que uma linha representa — a **granularidade**;
- qual campo deveria identificar uma linha — a **chave**;
- se a relação esperada é um-para-muitos ou muitos-para-muitos;
- em qual direção um filtro deve se propagar.

Crie uma Tabela Dinâmica a partir do Modelo de Dados. Compare o resultado com a Tabela Dinâmica criada na Parte 2 e explique por que os totais devem coincidir sob os mesmos filtros.

## Parte 5 — teste de atualização

Depois de finalizar o fluxo:

1. acrescente em `vendas_setembro.csv` uma nova venda fictícia com um cliente já existente;
2. acrescente o recebimento correspondente em `recebimentos.csv`;
3. use `Atualizar Tudo`, sem copiar consultas ou fórmulas;
4. registre quais totais mudaram e por quê;
5. reverta apenas as duas linhas adicionadas depois de guardar as evidências do teste.

## Arquivos a entregar

Salve em `entrega/`:

- `fechamento_comercial.xlsx`, com consultas atualizáveis;
- `dicionario_de_campos.md`, descrevendo fontes, tipos e regras;
- `regras_de_reconciliacao.md`, com classificação, tolerância adotada e limitações;
- uma exportação CSV da consulta de exceções.

Preencha também `roteiro_excel_power_query.md` e o arquivo de evidências.

## Marco oficial de aprendizagem

Conclua a trilha Microsoft Learn `Prepare data for analysis with Power BI`, faça o simulado central indicado no README do dia e relacione pelo menos três conceitos da trilha a passos visíveis no seu arquivo. O achievement da trilha é evidência de estudo, não a certificação profissional paga PL-300.

## Casos de borda obrigatórios

- espaço antes ou depois de uma chave;
- data em formato diferente;
- desconto vazio;
- cliente duplicado no cadastro;
- cliente de venda ausente no cadastro;
- dois recebimentos para um pedido;
- diferença entre valor vendido e recebido;
- recebimento sem venda correspondente;
- nova linha incorporada por `Atualizar Tudo`.

## Critério de conclusão

O bloco termina quando o arquivo atualiza sem refazer etapas, as fórmulas se expandem, os quatro resultados da Tabela Dinâmica foram conferidos, cada divergência permanece rastreável e você consegue explicar a diferença entre fórmula, Power Query, Tabela Dinâmica e Modelo de Dados.

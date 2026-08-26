# Roteiro de construção — Excel e Power Query

Preencha durante a atividade. Não registre apenas que “funcionou”: anote a regra, o motivo e como conferiu.

## 1. Perguntas de negócio

- Quem usará o fechamento:
- Decisões que ele precisa tomar:
- Indicadores realmente necessários:
- Granularidade de cada indicador:

## 2. Fórmulas praticadas

| Objetivo | Função ou recurso escolhido | Por que foi escolhido | Três linhas conferidas? |
|---|---|---|---|
| Valor bruto | | | |
| Valor líquido | | | |
| Classificação | | | |
| Busca de cadastro | | | |
| Soma por critérios | | | |
| Contagem por critérios | | | |

## 3. Consultas do Power Query

| Consulta | Uma linha representa | Fonte | Principais passos | Carregamento final |
|---|---|---|---|---|
| vendas_agosto | | | | |
| vendas_setembro | | | | |
| vendas_consolidadas | | | | |
| clientes | | | | |
| recebimentos | | | | |
| reconciliacao | | | | |
| excecoes | | | | |

## 4. Regras de qualidade

- Como tratei espaços:
- Como tratei datas:
- Como tratei desconto vazio:
- Como tratei cadastro duplicado:
- Como tratei chave sem correspondência:
- O que não corrigi automaticamente e por quê:

## 5. Append e Merge

- Por que os meses foram unidos com Append:
- Por que o cadastro foi ligado com Merge:
- Chaves utilizadas:
- Cardinalidade esperada:
- Como detectei multiplicação indevida de linhas:

## 6. Reconciliação

- O que foi comparado:
- Tolerância de valor e justificativa:
- Categorias de divergência:
- Quantidade por categoria antes da atualização:
- Duas divergências investigadas linha a linha:

## 7. Modelo de Dados

| Tabela | Granularidade | Chave | Papel no modelo | Relacionamentos |
|---|---|---|---|---|
| | | | | |

- Por que uma única tabela larga seria inadequada ou suficiente neste caso:
- Como validei os totais sob os mesmos filtros:

## 8. Teste de atualização

- Linhas acrescentadas para o teste:
- Etapas executadas:
- Totais antes:
- Totais depois:
- O que mudou automaticamente:
- O que exigiu correção e por quê:

## 9. Limitações

- Limitação dos dados:
- Limitação das regras:
- Risco ao atualizar com um novo arquivo mensal:
- Próximo controle que eu adicionaria:

# Avaliação de prontidão — Microsoft Learn Power BI e Power Query

Esta avaliação prepara para a trilha gratuita do Microsoft Learn e verifica se o conteúdo foi aplicado no exercício obrigatório do roadmap. Ela usa assuntos próximos aos estudados para a PL-300, mas não reproduz questões oficiais, não concede a PL-300 e não transforma um achievement em certificação profissional.

## O que esta avaliação mede

- **Parte A:** decisões conceituais em cenários curtos;
- **Parte B:** qualidade do artefato já construído no dia 14/09;
- **Parte C:** capacidade de adaptar o artefato quando uma fonte muda.

Não construa um segundo dashboard para esta avaliação. O mesmo arquivo da atividade obrigatória será usado como evidência aplicada.

## Regras

- Tempo: 45 minutos para a Parte A e 45 minutos para a Parte C.
- Faça a primeira tentativa sem documentação, IA, vídeos ou arquivo anterior.
- Responda em um novo arquivo chamado `respostas-microsoft-power-bi.md`.
- Justifique cada decisão em duas a cinco linhas; uma palavra isolada não demonstra entendimento.
- Este arquivo não contém respostas nem gabarito. Envie sua tentativa e os artefatos para correção.

## Cenário

Uma empresa recebe arquivos mensais de vendas, uma planilha de metas e um cadastro de clientes. Há tipos inconsistentes, nomes com espaços, pedidos possivelmente duplicados, valores ausentes e chaves que nem sempre encontram correspondência. A liderança quer acompanhar receita, margem, atingimento da meta e evolução mensal por cidade, canal e responsável.

## Parte A — 15 cenários de prontidão

1. Antes de transformar os arquivos, quais verificações de perfil você faria para encontrar nulos, erros, tipos inesperados e distribuições suspeitas?
2. Três arquivos mensais possuem o mesmo conjunto de colunas. Qual operação reúne suas linhas e o que precisa ser conferido antes e depois dela?
3. A tabela de metas deve enriquecer as vendas por cidade e mês. Qual operação é necessária e como você identificaria chaves sem correspondência?
4. A coluna `cidade` contém `Salvador`, ` salvador ` e `SALVADOR`. Proponha uma sequência de tratamento e uma conferência, sem escrever código M pronto.
5. Dois registros têm o mesmo cliente, produto e valor. Que informação falta para decidir se são duplicatas e qual é o risco de simplesmente remover uma das linhas?
6. Compare substituir um nulo por zero, remover a linha e manter o nulo. Em que situação cada decisão distorceria uma métrica?
7. Um novo arquivo mensal foi colocado na pasta, mas não entrou na atualização. Quais etapas, filtros, parâmetros e exemplos de arquivo você investigaria?
8. Desenhe em texto um modelo estrela mínimo, identificando fato, dimensões, chaves e granularidade da fato.
9. A dimensão de clientes possui uma chave duplicada no lado `1` do relacionamento. Que efeito isso pode causar e como você provaria a causa?
10. Escolha entre coluna calculada e medida para `margem percentual` e justifique considerando filtros e tamanho do modelo.
11. Explique como uma dimensão calendário e o contexto de filtro permitem comparar receita atual com o período anterior.
12. Um cartão mostra receita diferente da soma conferida no arquivo tratado. Descreva uma ordem de investigação que inclua fonte, transformação, relacionamento, medida e filtro.
13. Escolha três visuais para uma página executiva e explique qual decisão cada um deve sustentar. Inclua uma verificação de acessibilidade.
14. Um gerente deve enxergar apenas sua região. Explique o objetivo da segurança em nível de linha e por que esconder um filtro visual não resolve o problema.
15. Diferencie claramente um achievement do Microsoft Learn da certificação profissional PL-300 e explique como apresentaria a conquista no LinkedIn.

## Parte B — artefato aplicado já existente

Use o trabalho concluído em [Excel analítico e Power Query](<../../02 - Setembro 2026 [0-13]/Dia 28-09 - Dashboard e Power BI avancado/atividades/03-excel-analitico-e-power-query/>). Não refaça o projeto.

Apresente para correção:

- `fechamento_comercial.xlsx` com consultas atualizáveis;
- o `.pbix` ou dashboard exigido pelo dia 14/09;
- a reconciliação de pelo menos dois indicadores fora dos visuais;
- a captura do modelo e dos relacionamentos;
- uma explicação curta sobre granularidade, chaves e uma limitação.

O artefato deve abrir e atualizar. Capturas de tela isoladas não substituem os arquivos executáveis.

## Parte C — variante cronometrada de atualização

Faça esta etapa somente depois de ter uma versão funcional do artefato da Parte B.

1. Crie uma cópia descartável de uma fonte usada no exercício; preserve os arquivos originais.
2. Sorteie ou peça à IA que escolha **uma**, sem explicar a correção, entre estas mudanças:
   - uma coluna essencial foi renomeada;
   - chegou um terceiro mês com uma cidade escrita em novo formato;
   - uma chave de cadastro ficou sem correspondência;
   - uma data ou valor monetário chegou com tipo incompatível.
3. Inicie o cronômetro somente depois de receber a mudança.
4. Atualize o fluxo, localize a causa, faça a correção reproduzível e execute `Atualizar Tudo`.
5. Reconcilie novamente os dois indicadores da Parte B.
6. Registre: sintoma, hipótese, causa encontrada, alteração realizada, valores antes/depois e risco que ainda permanece.

Não vale corrigir diretamente uma célula da saída. A fonte controlada ou as etapas do Power Query devem explicar o resultado.

## Rubrica de correção — sem respostas

| Critério | Pontos |
|---|---:|
| Decisões de preparação e qualidade no Power Query | 15 |
| Modelo, relacionamentos, DAX e contexto de filtro | 15 |
| Visualização, segurança, desempenho e comunicação | 10 |
| Artefato existente atualizável e reconciliado | 40 |
| Diagnóstico e correção da variante cronometrada | 20 |
| **Total** | **100** |

### Falhas críticas

- remover ou alterar dados sem registrar critério e impacto;
- relacionamento criado apenas para “fazer funcionar”, sem granularidade definida;
- indicador sem reconciliação independente;
- correção manual que não sobrevive a `Atualizar Tudo`;
- confundir achievement do Microsoft Learn com certificação PL-300.

Prontidão recomendada: 80 pontos ou mais, nenhuma falha crítica e variante concluída dentro do tempo.

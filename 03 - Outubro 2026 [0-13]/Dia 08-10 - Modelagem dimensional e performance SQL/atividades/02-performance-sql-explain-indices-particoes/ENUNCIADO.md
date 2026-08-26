# Enunciado — reduzir o custo do relatório de incidentes

## Cenário real

Um relatório de SLA por cidade passou a levar minutos após o histórico crescer. A equipe suspeita do volume, mas ninguém verificou o plano. Você deverá criar uma carga ampliada controlada, diagnosticar três consultas e propor mudanças sem alterar os resultados.

## Entradas

- `dados/incidentes.csv` e `dados/clientes.csv`;
- tabela ampliada para pelo menos 100 mil eventos, criada de forma determinística a partir das fontes;
- parâmetros: intervalo de datas, cidade e severidade.

## Saídas

- consultas baseline e versões candidatas em [consultas_para_otimizar.sql](consultas_para_otimizar.sql);
- plano antes/depois de cada consulta;
- tabela com cinco tempos por versão, mediana, linhas e bytes lidos quando disponíveis;
- recomendação curta no próprio artefato.

## Regras obrigatórias

1. Otimize três padrões: filtro temporal com função na coluna, agregação depois de join muitos-para-muitos e busca por cidade/severidade.
2. Registre `EXPLAIN` ou `EXPLAIN ANALYZE` antes de mudar a consulta.
3. Teste reescrita sargable, pré-agregação e uma estratégia de índice ou organização física compatível com o banco escolhido.
4. Limpe cache apenas se souber e documentar o efeito; caso contrário, alterne a ordem das execuções.
5. Compare resultados por contagem, soma e hash/`EXCEPT`, não apenas por aparência.
6. Não crie índice para todas as colunas; explique custo de escrita e armazenamento.

## Casos de borda obrigatórios

- intervalo sem eventos;
- filtro que retorna quase toda a tabela;
- cidade muito mais frequente que as outras;
- data ou cidade nula;
- chave duplicada no lado “um” do join;
- execução em base pequena na qual o scan é mais barato que índice.

## Métricas

- mediana e amplitude dos tempos em cinco execuções;
- speedup relativo, sem afirmar ganho se a diferença estiver no ruído;
- linhas estimadas versus observadas, quando o plano fornecer;
- linhas e somas reconciliadas;
- custo de armazenamento do índice/partição, quando disponível.

## Critério de aceite

- Há plano e hipótese para as três consultas.
- Original e candidata são equivalentes em todos os casos de teste.
- As medições têm cinco repetições e ambiente identificado.
- Pelo menos uma decisão considera o trade-off leitura versus escrita.
- O relatório distingue melhoria medida de recomendação conceitual.


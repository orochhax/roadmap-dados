# Enunciado — Produto de portfólio Entity Matching Lab

## Cenário real

O Assistente de Suporte IA precisa vincular nomes, aliases e domínios extraídos dos tickets a uma empresa canônica. Engenharia e negócio decidirão se o pipeline pode automatizar vínculos, quais casos vão para revisão e quanto custará operar. Você deverá apresentar resultados positivos e negativos com a mesma transparência.

## Entradas

Integre os contratos criados nos módulos anteriores:

- cadastro canônico e registros bagunçados da atividade de normalização e baseline;
- candidatos e fontes de blocking da atividade de geração de candidatos;
- scores lexicais e semânticos da atividade de embeddings;
- ranking e faixas de decisão da atividade de avaliação e ranking;
- teste congelado, casos `no_match` e hard negatives.

Inclua um pequeno arquivo de exemplo sem dados pessoais para que outra pessoa consiga executar o projeto.

## Saídas obrigatórias

O repositório da entrega deverá conter:

1. pipeline executável do início ao fim por um comando documentado;
2. schema de entrada e saída com exemplos válidos e inválidos;
3. baseline exato e abordagem final comparados no mesmo teste;
4. saída por registro com top-k, scores, decisão e versão do pipeline;
5. benchmark de qualidade, latência, throughput, memória e custo estimado;
6. taxonomia de erros com falsos merges, falsos splits e falhas de recuperação;
7. data card, model card e política de revisão humana;
8. README técnico em português e resumo executivo em inglês;
9. testes automatizados para contratos e casos de borda;
10. checklist preenchido em `checklist_entrega.md`.

## Regras

- Não modifique o teste congelado nem selecione exemplos favoráveis.
- Fixe versões, seeds e comandos; uma instalação limpa deve reproduzir a execução.
- Nenhuma credencial, dado pessoal ou artefato pesado deve entrar no Git.
- Compare o pipeline completo, incluindo casos em que a entidade correta não foi gerada.
- Defina `match`, `review` e `no_match` antes da avaliação final.
- Separe claramente métricas offline de impacto de negócio ainda não observado.
- Se uma técnica mais cara não gerar ganho suficiente, entregue a opção mais simples.

## Casos de borda obrigatórios

- entrada vazia ou schema incompatível;
- acentos, Unicode, aliases e texto multilíngue;
- domínio vazio, inválido ou compartilhado;
- empresa homônima, matriz e subsidiária;
- registro sem entidade correspondente;
- empate entre candidatos e baixa confiança;
- lote com registro corrompido sem perder os demais;
- repetição idempotente do mesmo lote.

## Métricas e orçamento

- qualidade: precisão automática, recall, F1, Recall@5, MRR e taxa de revisão;
- fatias: idioma, país, presença de domínio e origem do alias;
- operação: latência P50/P95, throughput, memória, tamanho do índice e custo por mil registros;
- risco: falso merge por mil registros e distribuição da fila de revisão.

## Critério de aceite

A entrega técnica está completa quando outra pessoa consegue reproduzi-la, todos os casos de borda possuem teste e as decisões estão ligadas às métricas. A recomendação de automação exige precisão mínima de 0,97, Recall@5 de pelo menos 0,95, orçamento operacional respeitado e política explícita de rollback. Se o produto não atingir esses valores, publique a avaliação como experimento rejeitado e proponha uma próxima hipótese; não altere os limites depois de ver o teste.

## Apresentação

Prepare uma demonstração de cinco minutos: problema, baseline, evolução, erro mais perigoso, custo e recomendação. O objetivo é defender decisões, não mostrar todas as linhas de código.

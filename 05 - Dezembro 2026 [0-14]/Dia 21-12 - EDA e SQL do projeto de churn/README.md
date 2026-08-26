# EDA orientada a churn + SQL do projeto

**Data de estudo:** 21/12/2026
**Carga planejada:** 4 a 5 horas

## Aulas selecionadas no YouTube

Trilha **Machine Learning — Téo Me Why**:

- [ ] **Machine Learning 18: Projeto Churn - Explore** (35:59) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=Machine+Learning+18+Projeto+Churn+Explore+Teo+Me+Why).
- [ ] **Machine Learning 19: Projeto Churn - Modify** (57:31) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=Machine+Learning+19+Projeto+Churn+Modify+Teo+Me+Why).

**Carga de vídeo selecionada:** aproximadamente 1h34.

**Prática obrigatória:** faça sua própria EDA orientada à decisão, produza consultas SQL e registre hipóteses e limitações nos arquivos existentes. Não copie conclusões do vídeo para uma base diferente.

## Atividades do dia

### Atividade 1 — EDA orientada a churn

#### O que pesquisar
- `EDA orientada a churn machine learning com Python explicado passo a passo`
- `EDA orientada a churn machine learning com Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-eda-orientada-a-churn`](<atividades/01-eda-orientada-a-churn/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-eda-orientada-a-churn/dia-068-eda-orientada-a-churn.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que você precisa entender

- **Definição:** hipótese liga mecanismo, variável, direção e teste; interação ocorre quando um efeito depende de outra variável. Associação não prova causa.
- **Exemplo mínimo:** “contrato mensal associa-se a maior churn, sobretudo entre clientes novos”; teste com tabela por segmento e intervalo.
- **Erro comum:** formular a hipótese após ver o gráfico e apresentá-la como causal.

#### O que fazer

- [ ] Escreva quatro hipóteses de churn antes de gerar gráficos.
- [ ] Teste cada hipótese com tabela, métrica e visualização apropriada, sempre mostrando o tamanho dos grupos.
- [ ] Produza `insights_eda.md` com evidência, impacto, cautela e próxima análise para as duas hipóteses mais úteis.

- [ ] **Em `atividades/01-eda-orientada-a-churn/dia-068-eda-orientada-a-churn.ipynb`:** Teste a hipótese 'clientes com três ou mais chamados têm maior churn' com tabela, gráfico e tamanho dos dois grupos.
- [ ] **Em `atividades/01-eda-orientada-a-churn/dia-068-eda-orientada-a-churn.ipynb`:** Repita a análise somente em Salvador e registre se a direção da associação permanece.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

### Atividade 2 — SQL do projeto

#### O que pesquisar
- `SQL do projeto SQL para análise de dados explicado passo a passo`
- `SQL do projeto SQL para análise de dados exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-sql-do-projeto`](<atividades/02-sql-do-projeto/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-sql-do-projeto/dia-069-sql-do-projeto.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que você precisa entender

- **Definição:** granularidade é o que uma linha representa; janela calcula valores relacionados sem colapsar linhas; point-in-time limita dados à data de corte.
- **Exemplo mínimo:** `ROW_NUMBER() OVER (PARTITION BY cliente_id ORDER BY data_evento DESC)` seleciona o último evento permitido.
- **Erro comum:** join muitos-para-muitos que duplica clientes ou inclui eventos posteriores à decisão.

#### O que fazer

- [ ] Crie esquema SQL com tabelas de clientes, planos, chamados e pagamentos.
- [ ] Escreva consultas para formar features agregadas em janelas de 30, 60 e 90 dias.
- [ ] Valide granularidade: uma linha por cliente na data de referência.

- [ ] Crie testes de unicidade, ausência de chaves e totais antes/depois dos joins.
- [ ] Exporte `base_modelagem.csv` e compare cinco linhas com cálculo manual.


- [ ] **Em `atividades/02-sql-do-projeto/dia-069-sql-do-projeto.ipynb`:** Crie a feature quantidade_chamados_60d e compare cinco clientes com uma contagem manual na tabela de chamados.
- [ ] **Em `atividades/02-sql-do-projeto/dia-069-sql-do-projeto.ipynb`:** Duplique um pagamento, execute o teste de unicidade e impeça a exportação da base enquanto o problema existir.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

# SQL do projeto

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-069-sql-do-projeto.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

## Aprenda agora

- **Definição:** granularidade é o que uma linha representa; janela calcula valores relacionados sem colapsar linhas; point-in-time limita dados à data de corte.
- **Exemplo mínimo:** `ROW_NUMBER() OVER (PARTITION BY cliente_id ORDER BY data_evento DESC)` seleciona o último evento permitido.
- **Erro comum:** join muitos-para-muitos que duplica clientes ou inclui eventos posteriores à decisão.

## Núcleo essencial

1. [ ] Crie esquema SQL com tabelas de clientes, planos, chamados e pagamentos.
2. [ ] Escreva consultas para formar features agregadas em janelas de 30, 60 e 90 dias.
3. [ ] Valide granularidade: uma linha por cliente na data de referência.

## Prática obrigatória

- [ ] Crie testes de unicidade, ausência de chaves e totais antes/depois dos joins.
- [ ] Exporte `base_modelagem.csv` e compare cinco linhas com cálculo manual.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-069-sql-do-projeto.ipynb`:** Crie a feature quantidade_chamados_60d e compare cinco clientes com uma contagem manual na tabela de chamados.
- [ ] **Em `01-exercicios/dia-069-sql-do-projeto.ipynb`:** Duplique um pagamento, execute o teste de unicidade e impeça a exportação da base enquanto o problema existir.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-069-sql-do-projeto.ipynb` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

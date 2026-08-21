# Baseline completo

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/roteiro_atividades.md`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.
- **Experimento de leakage:** crie uma cópia com `status_vazado = churn`, treine a mesma pipeline com e sem essa coluna no mesmo split e compare a métrica.

## Núcleo essencial

1. [ ] Treine `DummyClassifier`, uma regressão logística usada como baseline e uma regra de negócio no mesmo split.
2. [ ] Avalie os três com a mesma função e registre as métricas em uma tabela.
3. [ ] Analise seis erros representativos e escreva qual baseline qualquer candidato precisa superar.

## Prática obrigatória

- [ ] Execute o experimento de leakage descrito em Preparação e explique por que a versão vazada não representa uso real.
- [ ] Transforme a avaliação repetida em uma função reutilizável.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

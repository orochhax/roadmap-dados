# TCC: dashboard, testes e relatório

## Preparação
- **Enunciado local:** `01-exercicios/roteiro_tcc.md`.
- **Saídas canônicas:** `projetos/portfolio-intelligence-lab/dashboard/app.py`, `projetos/portfolio-intelligence-lab/tests/` e `projetos/portfolio-intelligence-lab/docs/relatorio-final.md`.

## Manifesto de entradas

- **Obrigatórias:** fatores, ranking, backtest e métricas versionados.
- **Fallback local:** entregue notebook-relatório estático; servidor e serviço externo não são requisitos.

## Aprenda agora

- **Definição:** oráculo de teste declara a resposta esperada; teste no-look-ahead falha se uma alteração em data posterior mudar um score já calculado.
- **Exemplo mínimo:** altere preços posteriores ao corte e confirme score idêntico; teste também uma métrica de carteira com valores manuais.
- **Erro comum:** testar só ausência de exceção ou depender de dados externos mutáveis.

## Núcleo essencial

1. [ ] Escolha uma entrega visual: dashboard simples ou notebook-relatório; não faça os dois se o tempo for curto.
2. [ ] Mostre universo, fatores, ranking, comparação das duas carteiras e drawdown.
3. [ ] Adicione testes para cálculo de fatores, ausência de olhar o futuro e uma métrica de carteira.
4. [ ] Garanta uma instrução única ou uma sequência curta para reproduzir o resultado em ambiente limpo.
5. [ ] Escreva relatório de 4–6 páginas e resumo executivo de uma página com vieses, períodos ruins e aviso de que não é recomendação.

## Prática obrigatória

- [ ] Teste uma data fora do histórico e um número de ativos igual a zero na interface escolhida.
- [ ] Revise textos e limites visuais para evitar aparência de recomendação de investimento.

## Concluído quando

- [ ] Dashboard ou notebook-relatório, testes e relatório canônicos contêm todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

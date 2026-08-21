# Engenharia e qualidade dos dados

## Aulas complementares — proteção de dados

- [ ] Módulo 2 — **Cuidados ao manipular dados e recursos** (13:28).
- [ ] Módulo 2 — **Proteção de Dados** (18:17).
- Aplique as aulas ao notebook: preserve a base bruta, restrinja dados sensíveis nas evidências e documente qualquer transformação irreversível.

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-067-engenharia-e-qualidade-dos-dados.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

## Aprenda agora

- **Definição:** contrato fixa nomes, tipos, nulidade, domínio e unicidade; `fail` interrompe, enquanto quarentena separa registros suspeitos.
- **Exemplo mínimo:** `cliente_id: inteiro, não nulo, único`; inválidos vão a `rejeitados.csv` com motivo.
- **Erro comum:** corrigir silenciosamente e perder rastreabilidade.

## Núcleo essencial

1. [ ] Carregue `clientes_telecom.csv`, valide esquema e gere relatório de qualidade por coluna.
2. [ ] Defina regras de negócio para ausentes, duplicados, NPS fora de 0–10, mensalidade negativa e datas inconsistentes.
3. [ ] Implemente função de validação que falhe com mensagens claras.

## Prática obrigatória

- [ ] Crie base analítica limpa e dicionário de dados.
- [ ] Registre quantidade de linhas alteradas ou removidas e impacto na taxa de churn.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-067-engenharia-e-qualidade-dos-dados.ipynb`:** Crie uma linha com NPS=11 e outra com mensalidade=-1 e faça a validação listar os dois erros separadamente.
- [ ] **Em `01-exercicios/dia-067-engenharia-e-qualidade-dos-dados.ipynb`:** Compare a taxa de churn antes e depois de remover somente registros realmente inválidos e registre quantas linhas mudaram.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-067-engenharia-e-qualidade-dos-dados.ipynb` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

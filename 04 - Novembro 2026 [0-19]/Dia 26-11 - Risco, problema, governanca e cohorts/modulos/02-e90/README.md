# Dados e cohorts

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-082-dados-e-cohorts.ipynb`.
- **Dados:** `dados/credito.csv`.

## Aprenda agora

- **Definição:** cohort agrupa entidades por um evento de origem comum; cada período mede a mesma distância desde esse evento.
- **Exemplo mínimo:** cohort = mês da primeira concessão; P1, P2 e P3 = primeiro, segundo e terceiro mês completos após a concessão.
- **Erro comum:** misturar mês-calendário com idade da cohort ou incluir informação não disponível no corte.

## Núcleo essencial

1. [ ] Carregue `credito.csv`, faça qualidade e EDA da taxa de default.
2. [ ] Crie cohorts por mês de concessão e acompanhe default P1/P2/P3 quando possível.
3. [ ] Analise default por faixas de renda, dívida, atrasos e tempo de emprego.

## Prática obrigatória

- [ ] Valide estabilidade temporal das variáveis.
- [ ] Crie dicionário de features e regras de exclusão.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-082-dados-e-cohorts.ipynb`:** Compare default para renda abaixo de R$3.000 e acima de R$8.000, informando também o tamanho dos grupos.
- [ ] **Em `01-exercicios/dia-082-dados-e-cohorts.ipynb`:** Separe os últimos três meses de concessão e compare a distribuição das cinco principais variáveis com o período anterior.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-082-dados-e-cohorts.ipynb` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

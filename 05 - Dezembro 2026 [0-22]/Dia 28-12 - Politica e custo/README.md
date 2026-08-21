# Política e custo

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-084-politica-e-custo.ipynb`.
- **Dados:** `dados/credito.csv`.

## Aprenda agora

- **Definição:** nota A–E é uma política baseada em faixas de risco; perda esperada pode ser `PD × LGD × EAD`; lucro esperado inclui receita, perda e custo operacional.
- **Exemplo mínimo:** para `PD=.08, LGD=.5, EAD=1000`, perda esperada = R$40; compare com margem e custo de revisão.
- **Erro comum:** criar faixas sem justificar cortes ou tratar score como decisão automática.

## Núcleo essencial

1. [ ] Converta probabilidade em faixas de risco A–E.
2. [ ] Defina política de aprovar, revisar ou rejeitar por faixa.
3. [ ] Simule lucro/prejuízo com taxas, perda esperada e custo operacional.

## Prática obrigatória

- [ ] Teste cenários de mudança na taxa de default.
- [ ] Crie regra para casos sem informação suficiente e revisão humana.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-084-politica-e-custo.ipynb`:** Aumente a perda em caso de default em 30% e recalcule lucro/prejuízo por faixa A–E.
- [ ] **Em `01-exercicios/dia-084-politica-e-custo.ipynb`:** Envie para revisão humana todos os casos com renda ou tempo de emprego ausente e conte o volume afetado.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-084-politica-e-custo.ipynb` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

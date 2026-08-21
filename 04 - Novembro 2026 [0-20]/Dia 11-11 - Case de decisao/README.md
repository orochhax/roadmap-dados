# Case de decisão

## Aprenda agora

Uma política converte probabilidade, custo e capacidade operacional em ação. Casos próximos ao limiar podem ser encaminhados à revisão humana.

```python
decisao = np.select(
    [probabilidade >= 0.70, probabilidade >= 0.45],
    ["agir", "revisar"],
    default="não agir",
)
```

**Erro comum:** escolher uma única política global sem conferir custo e taxa de ação por segmento.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/roteiro_atividades.md`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.
- **Entradas concretas:** id do cliente, probabilidade de churn, alvo real e custos de ação, falso positivo e falso negativo.
- **Fallback local:** se não houver probabilidades salvas, ajuste no próprio notebook a pipeline de regressão logística mostrada acima e use `predict_proba(X_validacao)[:, 1]`.

## Núcleo essencial

1. [ ] Monte tabela com cliente, probabilidade, limiar, decisão e custo esperado.
2. [ ] Crie três políticas: conservadora, equilibrada e agressiva; calcule volume de ações e custo.
3. [ ] Analise desempenho por cidade, plano e faixa de mensalidade.
4. [ ] Defina regra de revisão humana para casos próximos ao limiar.

## Prática obrigatória

- [ ] Apresente decisão em uma página, incluindo quem não deve receber ação automatizada.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Defina política conservadora com limiar 0,70, equilibrada com 0,50 e agressiva com 0,30; calcule volume e custo no mesmo conjunto.
- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Crie revisão humana para probabilidades entre 0,45 e 0,55 e conte quantos clientes entram nessa faixa.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

<!-- Estrutura preparada automaticamente a partir do roadmap. Nenhuma atividade foi resolvida. -->

## Dia 128 — TCC: carteiras e backtest walk-forward — 27/01/2027
> [!abstract] Resultado concreto do dia
> Converter rankings em carteiras e avaliar risco-retorno fora da amostra.

### Passo a passo completo
1. [ ] Implemente carteira de pesos iguais como baseline.
2. [ ] Implemente carteira Top-K baseada no ranking e uma estratégia de mínima volatilidade ou risk parity.
3. [ ] Defina alocação entre ações, ETFs e FIIs sem misturar os scores brutos das classes.
4. [ ] Execute backtest walk-forward com rebalanceamento, custos e regras mínimas de liquidez.
5. [ ] Compare retorno anualizado, volatilidade, Sharpe, Sortino, máximo drawdown, turnover e períodos negativos.
6. [ ] Faça testes de sensibilidade variando K, custos, janelas, frequência e pesos dos fatores.
7. [ ] Analise períodos em que o ranking e as carteiras falharam.

### Verificação prática sem consulta
- [ ] Recalcule o retorno líquido de um rebalanceamento incluindo custos.
- [ ] Compare a estratégia com um baseline ingênuo no mesmo período.
- [ ] Execute cenário de custo dobrado e mostre se a conclusão muda.

### Perguntas de checagem
1. Por que maior retorno acumulado não basta para escolher uma estratégia?

**Resposta:**

2. Qual diferença entre risco observado e risco estimado?

**Resposta:**

3. Como turnover pode destruir uma estratégia aparentemente lucrativa?

**Resposta:**

4. O que caracteriza overfitting de backtest?

**Resposta:**

### Critério objetivo para marcar como concluído
- [ ] Nenhum resultado principal usa dados do futuro.
- [ ] Custos aparecem em todos os resultados líquidos.
- [ ] Há comparação dentro e fora da amostra.
- [ ] Pelo menos três estratégias e um benchmark foram comparados.
- [ ] Commit: `dia-128: carteiras-e-backtest-walk-forward`.

**Autoavaliação do dia:** `__/5`  
**Evidência:** curvas, tabela de métricas, testes de sensibilidade e commit.

---

## Anotações pessoais

### Resultado esperado antes de executar


### Conceitos estudados


### Dúvidas


### Erros encontrados e correções


### Aprendizado principal


### Próxima ação

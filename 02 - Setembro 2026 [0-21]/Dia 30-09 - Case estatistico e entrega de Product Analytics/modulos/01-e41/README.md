# Case estatístico

## Aprenda agora

Diferença absoluta mede unidades originais; diferença percentual usa uma base; tamanho de efeito padroniza a diferença: `d = (média_depois - média_antes) / desvio_combinado`.

```python
diferenca = depois.mean() - antes.mean()
efeito = diferenca / np.sqrt((antes.var(ddof=1) + depois.var(ddof=1)) / 2)
```

**Erro comum:** atribuir a mudança ao processo sem verificar se a composição de cidades ou perfis também mudou.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/roteiro_atividades.md`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/incidentes.csv` e dados sintéticos gerados no notebook com seed 42.

## Núcleo essencial

1. [ ] Receba um case: a empresa afirma que duração média caiu após mudança de processo; defina população, amostra, variável e hipótese.
2. [ ] Faça EDA antes/depois, calcule diferença absoluta, percentual e tamanho de efeito simples.
3. [ ] Crie duas análises: uma com média e outra com mediana; explique divergências.
4. [ ] Simule um resultado estatisticamente aparente causado por composição diferente de cidades.

## Prática obrigatória

- [ ] Entregue nota técnica de uma página dizendo o que pode e não pode ser concluído.
- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Repita a comparação antes/depois usando somente a cidade com maior número de observações e compare com a conclusão geral.
- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Inclua uma duração de 2000 minutos no período depois e compare o efeito sobre média, mediana e tamanho de efeito.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

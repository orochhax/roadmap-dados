# Limiar e custo

## Aprenda agora

O limiar converte probabilidade em decisão. Para cada limiar, calcule `custo = FN×custo_FN + FP×custo_FP + TP×custo_TP` e aplique restrições de negócio.

```python
limiar = 0.30
predito = (probabilidades >= limiar).astype(int)
custo = fn * 500 + fp * 20 + tp * 80
```

**Erro comum:** escolher o limiar no conjunto de teste ou ignorar o volume de ações gerado.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-052-limiar-e-custo.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

## Núcleo essencial

1. [ ] Calcule previsões para limiares 0.2, 0.3, 0.5, 0.7 e 0.8.
2. [ ] Para cada limiar, registre TP, FP, FN, TN, precision, recall e custo total.
3. [ ] Use custos definidos: FN=R$500, FP=R$20, TP=R$80 de campanha e benefício esperado de R$300.

## Prática obrigatória

- [ ] Escolha o limiar de menor custo respeitando recall mínimo de 70%.
- [ ] Crie gráfico custo versus limiar e escreva recomendação executiva.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-052-limiar-e-custo.ipynb`:** Refaça a tabela de limiares aumentando o custo de FP de R$20 para R$50 e mantenha os demais valores.
- [ ] **Em `01-exercicios/dia-052-limiar-e-custo.ipynb`:** Escolha novamente o limiar exigindo recall mínimo de 80% em vez de 70% e registre a troca de custo e volume.
- [ ] Compare especificamente os limiares 0,35 e 0,50 no mesmo conjunto e registre precision, recall e custo para cada um.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

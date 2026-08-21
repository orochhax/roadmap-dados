# Feature engineering para regressão

## Aprenda agora

Feature engineering transforma dados disponíveis em sinais reproduzíveis. `log1p` reduz assimetria, interação combina efeitos e ablação mede a contribuição de um grupo de features.

```python
df["log_valor"] = np.log1p(df["valor"])
df["desconto_app"] = df["desconto"] * (df["canal"] == "app").astype(int)
```

**Erro comum:** criar uma feature com informação posterior ao momento da previsão ou fora da pipeline aplicada em produção.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-049-feature-engineering-para-regressao.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

## Núcleo essencial

1. [ ] Crie features de data: mês, dia da semana, fim de semana e dias desde primeira compra.
2. [ ] Crie transformações `log1p` para variável assimétrica e interações entre desconto e canal.
3. [ ] Agrupe categorias raras com limiar explícito e documente impacto.

## Prática obrigatória

- [ ] Construa cada feature dentro da pipeline para evitar diferenças entre treino e inferência.
- [ ] Faça ablação: remova grupos de features e registre quanto cada grupo muda a métrica.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-049-feature-engineering-para-regressao.ipynb`:** Agrupe categorias com frequência abaixo de 1% e depois abaixo de 5%; compare número de colunas e MAE.
- [ ] **Em `01-exercicios/dia-049-feature-engineering-para-regressao.ipynb`:** Remova somente as features de interação e registre a variação da métrica no mesmo conjunto de validação.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

# EDA prática

## Aprenda agora

EDA é uma investigação orientada por perguntas: confira estrutura e qualidade, descreva o alvo, segmente e só então produza achados.

```python
pergunta = "Clientes com mais chamados apresentam mais churn?"
resumo = df.groupby("churn")["chamados_90d"].agg(["count", "mean", "median"])
print(pergunta, resumo)
```

**Erro comum:** gerar muitos gráficos sem registrar qual pergunta cada um responde ou quais limitações impedem uma conclusão.

## Preparação

- **Pasta/arquivo principal:** `projeto-semanal/notebooks/eda_clientes.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e os demais arquivos listados no projeto.

## Núcleo essencial

1. [ ] Escreva três perguntas de negócio sobre churn antes de iniciar a análise.
2. [ ] Faça inspeção estrutural, qualidade básica e distribuição do alvo.
3. [ ] Crie três análises segmentadas diretamente ligadas às perguntas escolhidas.
4. [ ] Produza dois gráficos e um resumo com três achados, uma limitação e uma próxima análise.

## Prática obrigatória

- [ ] Escreva uma recomendação limitada ao que uma evidência numérica da análise permite concluir.
- [ ] Compare churn, NPS mediano e chamados médios dos clientes com menos de seis meses com a base completa.
- [ ] Em uma cópia, deixe o NPS ausente em cinco linhas e confirme quais tabelas ou gráficos mudam antes de escolher tratamento.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

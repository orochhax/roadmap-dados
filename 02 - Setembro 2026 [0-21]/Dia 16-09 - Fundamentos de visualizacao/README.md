# Fundamentos de visualização

## Aprenda agora

Barras comparam categorias, linhas mostram evolução temporal, histogramas mostram distribuição e dispersões mostram relação entre duas variáveis.

```python
ax = df.groupby("cidade")["duracao_min"].mean().sort_values().plot.bar()
ax.set(title="Duração média por cidade", xlabel="Cidade", ylabel="Minutos")
ax.set_ylim(bottom=0)
```

**Erro comum:** truncar o eixo de barras e ampliar visualmente diferenças pequenas.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/visualizacao_fundamentos.ipynb`.
- **Dados:** `dados/incidentes.csv`, `dados/clientes_telecom.csv`, `dados/pedidos.csv` e `dados/metas_cidades.csv`.

## Núcleo essencial

1. [ ] Crie um gráfico de barras, linha, histograma e dispersão usando o mesmo conjunto de dados.
2. [ ] Para cada gráfico, escreva qual pergunta ele responde e por que outro tipo seria pior.
3. [ ] Corrija quatro erros intencionais: eixo truncado, categorias desordenadas, título genérico e excesso de casas decimais.

## Prática obrigatória

- [ ] Crie uma versão acessível sem depender apenas de cor: use rótulos, marcadores e legenda clara.
- [ ] Exporte em PNG com tamanho legível e verifique se o gráfico continua compreensível fora do notebook.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

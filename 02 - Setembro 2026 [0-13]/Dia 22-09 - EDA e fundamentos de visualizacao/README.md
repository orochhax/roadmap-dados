# EDA pratica + Fundamentos de visualizacao

**Data de estudo:** 22/09/2026
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — EDA pratica

#### O que pesquisar
- `EDA pratica análise de dados com Python explicado passo a passo`
- `EDA pratica análise de dados com Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-eda-pratica`](<atividades/01-eda-pratica/>)

#### O que você precisa entender

EDA é uma investigação orientada por perguntas: confira estrutura e qualidade, descreva o alvo, segmente e só então produza achados.

```python
pergunta = "Clientes com mais chamados apresentam mais churn?"
resumo = df.groupby("churn")["chamados_90d"].agg(["count", "mean", "median"])
print(pergunta, resumo)
```

**Erro comum:** gerar muitos gráficos sem registrar qual pergunta cada um responde ou quais limitações impedem uma conclusão.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-eda-pratica/projeto-semanal/notebooks/eda_clientes.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e os demais arquivos listados no projeto.

#### O que fazer

- [ ] Escreva três perguntas de negócio sobre churn antes de iniciar a análise.
- [ ] Faça inspeção estrutural, qualidade básica e distribuição do alvo.
- [ ] Crie três análises segmentadas diretamente ligadas às perguntas escolhidas.
- [ ] Produza dois gráficos e um resumo com três achados, uma limitação e uma próxima análise.

- [ ] Escreva uma recomendação limitada ao que uma evidência numérica da análise permite concluir.
- [ ] Compare churn, NPS mediano e chamados médios dos clientes com menos de seis meses com a base completa.
- [ ] Em uma cópia, deixe o NPS ausente em cinco linhas e confirme quais tabelas ou gráficos mudam antes de escolher tratamento.
- [ ] Preencha `atividades/01-eda-pratica/projeto-semanal/docs/apresentacao.md` e apresente perguntas, achados e limitação em até três minutos.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

### Atividade 2 — Fundamentos de visualizacao

#### O que pesquisar
- `Fundamentos de visualizacao análise de dados com Python explicado passo a passo`
- `Fundamentos de visualizacao análise de dados com Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-fundamentos-de-visualizacao`](<atividades/02-fundamentos-de-visualizacao/>)

#### O que você precisa entender

Barras comparam categorias, linhas mostram evolução temporal, histogramas mostram distribuição e dispersões mostram relação entre duas variáveis.

```python
ax = df.groupby("cidade")["duracao_min"].mean().sort_values().plot.bar()
ax.set(title="Duração média por cidade", xlabel="Cidade", ylabel="Minutos")
ax.set_ylim(bottom=0)
```

**Erro comum:** truncar o eixo de barras e ampliar visualmente diferenças pequenas.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-fundamentos-de-visualizacao/visualizacao_fundamentos.ipynb`.
- **Dados:** `dados/incidentes.csv`, `dados/clientes_telecom.csv`, `dados/pedidos.csv` e `dados/metas_cidades.csv`.

#### O que fazer

- [ ] Crie um gráfico de barras, linha, histograma e dispersão usando o mesmo conjunto de dados.
- [ ] Para cada gráfico, escreva qual pergunta ele responde e por que outro tipo seria pior.
- [ ] Corrija quatro erros intencionais: eixo truncado, categorias desordenadas, título genérico e excesso de casas decimais.

- [ ] Crie uma versão acessível sem depender apenas de cor: use rótulos, marcadores e legenda clara.
- [ ] Exporte em PNG com tamanho legível e verifique se o gráfico continua compreensível fora do notebook.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

# Visualizacao com pandas e Matplotlib + Storytelling e recomendacao

**Data de estudo:** 24/09/2026
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Visualizacao com pandas e Matplotlib

#### O que pesquisar
- `Visualizacao com pandas e Matplotlib análise de dados com Python explicado passo a passo`
- `Visualizacao com pandas e Matplotlib análise de dados com Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-visualizacao-com-pandas`](<atividades/01-visualizacao-com-pandas/>)

#### O que você precisa entender

`DataFrame.plot()` prepara o gráfico rapidamente; Matplotlib permite controlar eixos, linhas de referência e anotações.

```python
import matplotlib.pyplot as plt

ax = receita_mensal.plot(marker="o")
ax.axhline(meta, color="red", linestyle="--", label="Meta")
ax.annotate("abaixo da meta", xy=(mes, valor))
plt.legend()
```

**Erro comum:** anotar um ponto calculado com filtro diferente do usado no gráfico.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-visualizacao-com-pandas/dia-017-visualizacao-com-pandas-e-matplotlib.ipynb`.
- **Dados:** `dados/incidentes.csv`, `dados/clientes_telecom.csv`, `dados/pedidos.csv` e `dados/metas_cidades.csv`.

#### O que fazer

- [ ] Com `pedidos.csv`, crie séries temporais de receita diária e mensal, barras de receita por canal e boxplot de valor por categoria.
- [ ] Faça primeiro com `DataFrame.plot()` e depois recrie dois gráficos diretamente com Matplotlib.
- [ ] Adicione linha de meta mensal e destaque meses abaixo da meta por anotação textual.

- [ ] Crie uma função reutilizável que receba DataFrame, coluna temporal, métrica e título.
- [ ] Teste a função com dados vazios, uma única data e categorias desconhecidas.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

### Atividade 2 — Storytelling e recomendacao

#### O que pesquisar
- `Storytelling e recomendacao Python explicado passo a passo`
- `Storytelling e recomendacao Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-storytelling-e-recomendacao`](<atividades/02-storytelling-e-recomendacao/>)

#### O que você precisa entender

Uma recomendação defensável segue a fórmula **contexto → evidência numérica → impacto → ação**, sempre com uma limitação explícita.

> Contexto: chamados recorrentes cresceram. Evidência: clientes com 3+ chamados têm NPS mediano 3 pontos menor. Impacto: maior risco de insatisfação. Ação: priorizar contato com esse grupo. Limitação: associação não prova causalidade.

**Erro comum:** transformar associação em causa ou recomendar para toda a base algo observado apenas em um segmento.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-storytelling-e-recomendacao/dia-018-storytelling-e-recomendacao.ipynb`.
- **Dados:** `dados/incidentes.csv`, `dados/clientes_telecom.csv`, `dados/pedidos.csv` e `dados/metas_cidades.csv`.
- **Fallback local:** se ainda não houver três achados, calcule no próprio notebook NPS mediano e churn para clientes com menos de três chamados e com três ou mais chamados; use esses resultados e um recorte por cidade.

#### O que fazer

- [ ] Escolha três achados calculados no próprio notebook e transforme cada um em uma estrutura: contexto → evidência → impacto → recomendação.
- [ ] Crie um slide ou página Markdown para cada achado com no máximo um gráfico e três frases.
- [ ] Escreva uma recomendação deliberadamente exagerada e depois revise indicando o que os dados realmente permitem concluir.

- [ ] Grave áudio de três minutos explicando a análise sem termos técnicos desnecessários.
- [ ] **Em `atividades/02-storytelling-e-recomendacao/dia-018-storytelling-e-recomendacao.ipynb`:** Apresente o mesmo achado em duas versões: três frases para diretoria e um parágrafo técnico para a equipe de dados.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

## Publicação da semana no LinkedIn

- **Tema específico:** EDA orientada a decisão — transformar dados de telecom tratados em dois gráficos, três achados e uma recomendação limitada pela evidência.
- **Tipo:** progresso.
- **Formato:** carrossel com pergunta, qualidade dos dados, dois gráficos exportados, decisão e limitação.
- **Artefato/evidência exigida:** notebooks de NumPy/pandas, limpeza, EDA e `dia-018-storytelling-e-recomendacao.ipynb` executados; gráficos com título/eixos/fonte, valores reconciliados e conclusão vinculada aos dados.

### Roteiro para preencher

- **Pergunta:** [qual decisão orientou a exploração?]
- **Qualidade dos dados:** [qual problema foi encontrado e como foi tratado?]
- **Gráfico 1:** [o que mostra e qual valor foi conferido?]
- **Gráfico 2:** [o que acrescenta sem repetir a primeira visualização?]
- **Achados:** [três conclusões sustentadas pelos números]
- **Recomendação:** [qual ação pequena os dados permitem sugerir?]
- **Evidência:** [notebook, imagem ou relatório conferidos]

### Limitação obrigatória

Explique por que uma associação observada na EDA não demonstra causa nem garante que a recomendação produzirá impacto.

### Cuidado contra afirmações falsas

Não escolha escala, corte ou gráfico para exagerar diferença. Não use `comprovei`, `causei` ou impacto financeiro sem experimento e medida reais. O post não antecipa Competências ou headline.

### Checklist de publicação

- [ ] Reexecutei os notebooks em ordem e exportei os gráficos da execução final.
- [ ] Conferi títulos, eixos, unidades, fonte e denominadores.
- [ ] Recalculei ao menos um valor de cada gráfico.
- [ ] Separei achado, recomendação e limitação.
- [ ] Removi dados pessoais e testei qualquer link compartilhado.
- [ ] **URL publicada:**
- [ ] **Data da publicação:**

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

# Medidas e distribuicoes + Probabilidade basica

**Data de estudo:** 28/09/2026  
**Carga planejada:** 4 a 5 horas

## Aulas selecionadas no YouTube

Use os títulos exatamente como estão escritos para localizar as aulas:

- [ ] **GRINGS - Classificação de Variáveis - Aula 1** (8:56) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=GRINGS+Classificacao+de+Variaveis+Aula+1).
- [ ] **GRINGS - Frequências Absoluta, Relativa, Acumulada  aula 3** (12:11) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=GRINGS+Frequencias+Absoluta+Relativa+Acumulada+aula+3).
- [ ] **Grings - Moda, Média e Mediana aula 4** (29:10) — [abrir no YouTube](https://www.youtube.com/watch?v=UfupcG1ax6U).
- [ ] **GRINGS - Cálculo do desvio padrão e da variância aula 6** (11:34) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=GRINGS+Calculo+do+desvio+padrao+e+da+variancia+aula+6).

**Carga de vídeo selecionada:** aproximadamente 1h02.

**Prática obrigatória:** as aulas apresentam a base matemática; os dois notebooks do dia continuam obrigatórios. Assistir aos vídeos, sozinho, não conclui a sessão.

## Atividades do dia

### Atividade 1 — Medidas e distribuicoes

#### O que pesquisar
- `Medidas e distribuicoes Python explicado passo a passo`
- `Medidas e distribuicoes Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-medidas-e-distribuicoes`](<atividades/01-medidas-e-distribuicoes/>)

#### O que você precisa entender

Média usa todos os valores; mediana usa a posição central; `IQR = Q3 - Q1`; `z = (x - média) / desvio`. Outliers afetam mais a média e o z-score que a mediana e o IQR.

```python
serie = df["mensalidade"].dropna()
q1, q3 = serie.quantile([0.25, 0.75])
iqr = q3 - q1
limites_iqr = (q1 - 1.5 * iqr, q3 + 1.5 * iqr)
z = (serie - serie.mean()) / serie.std(ddof=1)
```

**Erro comum:** remover automaticamente todo ponto fora do limite sem investigar se ele é erro ou caso real relevante.

#### Aplicações integradas

- [ ] No notebook atual, use `[30, 45, 60, 75, 90, 999.9]` e explique como média, mediana e percentis reagem ao valor extremo.
- [ ] Em uma cópia de `clientes_telecom.csv`, sinalize outliers de mensalidade por IQR e por `|z| > 3`; compare quais linhas cada método encontra sem removê-las.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-medidas-e-distribuicoes/dia-031-medidas-e-distribuicoes.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/incidentes.csv` e dados sintéticos gerados no notebook com seed 42.

#### O que fazer

- [ ] Com `clientes_telecom.csv`, calcule média, mediana, moda, variância, desvio, quartis, IQR e amplitude para mensalidade, NPS e chamados.
- [ ] Crie duas distribuições com mesma média e desvios diferentes; mostre por que a média isolada engana.
- [ ] Compare métricas com e sem um outlier extremo inserido manualmente.

- [ ] Faça histogramas e boxplots e escreva a forma da distribuição: simétrica, assimétrica ou multimodal.
- [ ] Explique em linguagem de negócio quando mediana é mais adequada que média.
- [ ] **Em `atividades/01-medidas-e-distribuicoes/dia-031-medidas-e-distribuicoes.ipynb`:** Calcule as mesmas medidas somente para Salvador e compare o tamanho desse grupo com o total antes de interpretar a diferença.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

### Atividade 2 — Probabilidade basica

#### O que pesquisar
- `Probabilidade basica estatística para data science explicado passo a passo`
- `Probabilidade basica estatística para data science exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-probabilidade-basica`](<atividades/02-probabilidade-basica/>)

#### O que você precisa entender

Probabilidade condicional restringe o universo: `P(A|B) = P(A e B) / P(B)`. Em uma tabela 2x2, use como denominador apenas o grupo condicionado.

```python
prob_churn_dado_reclamacao = clientes_com_churn_e_reclamacao / clientes_com_reclamacao
```

Dois eventos são independentes quando `P(A|B) = P(A)`.

**Erro comum:** usar o total da base como denominador de uma probabilidade condicional.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-probabilidade-basica/dia-032-probabilidade-basica.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/incidentes.csv` e dados sintéticos gerados no notebook com seed 42.

#### O que fazer

- [ ] Resolva os problemas 1–6 de probabilidade, identificando antes de calcular o espaço amostral e o evento pedido.
- [ ] Construa uma tabela 2x2 pequena e use-a para interpretar uma probabilidade condicional.
- [ ] Simule lançamentos com NumPy e compare frequência observada e probabilidade teórica em dois tamanhos de amostra.

- [ ] **Em `atividades/02-probabilidade-basica/dia-032-probabilidade-basica.ipynb`:** Refaça o problema de Bayes com 2.000 clientes, 160 churns, sensibilidade de 75% e falso positivo de 10%.
- [ ] **Em `atividades/02-probabilidade-basica/dia-032-probabilidade-basica.ipynb`:** Simule 100, 1.000 e 10.000 lançamentos da mesma moeda com seed 42 e compare a distância entre frequência e probabilidade teórica.
- [ ] Crie dois eventos independentes e dois dependentes em dados sintéticos e mostre numericamente a diferença.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

# Intervalos de confianca + Testes de hipotese

**Data de estudo:** 27/10/2026
**Carga planejada:** 4 a 5 horas

## Aulas selecionadas no YouTube

Use os títulos exatamente como estão escritos para localizar as aulas:

- [ ] **GRINGS - Estimação por  Intervalo de Confiança da Média aula 16** (50:44) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=GRINGS+Estimacao+por+Intervalo+de+Confianca+da+Media+aula+16).
- [ ] **Grings - Teste de Hipótese para Média aula 20** (38:49) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=Grings+Teste+de+Hipotese+para+Media+aula+20).

**Carga de vídeo selecionada:** aproximadamente 1h30.

**Prática obrigatória:** reproduza os cálculos e interprete cobertura, valor-p, erros e decisão nos notebooks do dia. Assistir às aulas não substitui a execução dos experimentos.

## Atividades do dia

### Atividade 1 — Intervalos de confianca

#### O que pesquisar
- `Intervalos de confianca Python explicado passo a passo`
- `Intervalos de confianca Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-intervalos-de-confianca`](<atividades/01-intervalos-de-confianca/>)

#### O que você precisa entender

Um intervalo de 95% para a média tem a forma `média ± valor_crítico × erro_padrão`; com desvio populacional desconhecido, use a distribuição t.

```python
from scipy import stats

media = amostra.mean()
se = stats.sem(amostra)
ic95 = stats.t.interval(0.95, len(amostra) - 1, loc=media, scale=se)
```

**Erro comum:** dizer que há 95% de probabilidade de o parâmetro fixo estar dentro de um intervalo já calculado.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-intervalos-de-confianca/dia-036-intervalos-de-confianca.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/incidentes.csv` e dados sintéticos gerados no notebook com seed 42.

#### O que fazer

- [ ] Calcule um intervalo de confiança de 95% para a média manualmente e com biblioteca, declarando as suposições usadas.
- [ ] Compare a largura do intervalo em amostras de tamanho 20 e 100.
- [ ] Escreva a interpretação correta do intervalo sem atribuir probabilidade ao parâmetro fixo.

- [ ] Compare intervalos de 90%, 95% e 99% e explique o efeito do nível de confiança na largura.
- [ ] **Em `atividades/01-intervalos-de-confianca/dia-036-intervalos-de-confianca.ipynb`:** Calcule IC de 95% para as primeiras 50 durações por método paramétrico e bootstrap com seed 42; compare as larguras.
- [ ] **Em `atividades/01-intervalos-de-confianca/dia-036-intervalos-de-confianca.ipynb`:** Repita com uma amostra constante [60, 60, 60, 60, 60] e trate explicitamente a ausência de variabilidade.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

### Atividade 2 — Testes de hipotese

#### O que pesquisar
- `Testes de hipotese estatística para data science explicado passo a passo`
- `Testes de hipotese estatística para data science exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-testes-de-hipotese`](<atividades/02-testes-de-hipotese/>)

#### O que você precisa entender

`H0` representa ausência da diferença de interesse; `H1`, a diferença. O p-valor mede quão incompatíveis os dados são com `H0`, não o tamanho nem a importância do efeito.

```python
from scipy import stats

estatistica, p_valor = stats.ttest_ind(grupo_a, grupo_b, equal_var=False)
```

**Erro comum:** concluir que `p < 0,05` prova causalidade ou que `p >= 0,05` prova igualdade.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-testes-de-hipotese/dia-037-testes-de-hipotese.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/incidentes.csv` e dados sintéticos gerados no notebook com seed 42.

#### O que fazer

- [ ] Formule H0 e H1 para diferença de média de duração entre duas cidades.
- [ ] Escolha e execute teste apropriado; verifique suposições e calcule tamanho de efeito.
- [ ] Resolva um teste de proporções para taxa de churn entre dois planos.

- [ ] Crie cenários de erro tipo I e II com consequências de negócio.
- [ ] Escreva decisão usando significância, efeito, intervalo e custo, sem depender só de p-valor.
- [ ] **Em `atividades/02-testes-de-hipotese/dia-037-testes-de-hipotese.ipynb`:** Acrescente um outlier de 1500 minutos a uma cidade, refaça suposições e tamanho de efeito e compare com a análise original.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

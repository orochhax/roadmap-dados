# Teste A-B + Experimentação avançada: testes múltiplos, CUPED e desenho sequencial

**Data de estudo:** 02/10/2026  
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Teste A-B

#### O que pesquisar
- `Teste A-B Python explicado passo a passo`
- `Teste A-B Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-teste-a-b`](<atividades/01-teste-a-b/>)

#### O que você precisa entender

Defina antes da coleta: unidade de randomização, métrica primária, guardrail, efeito mínimo relevante e tamanho da amostra. *Peeking* é testar repetidamente e parar ao primeiro resultado favorável.

```python
efeito_observado = conversao_b - conversao_a
decisao = "lançar" if limite_inferior_ic > efeito_minimo else "não lançar"
```

**Erro comum:** escolher métrica, segmento ou duração depois de olhar o resultado.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-teste-a-b/dia-038-teste-a-b.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/incidentes.csv` e dados sintéticos gerados no notebook com seed 42.

#### O que fazer

- [ ] Defina um experimento A/B com unidade, população, métrica primária, guardrail e duração.
- [ ] Analise uma amostra sintética com diferença, intervalo de confiança e teste de hipótese.
- [ ] Escreva uma decisão entre lançar, repetir ou abandonar, citando efeito, incerteza e risco.

- [ ] Calcule o tamanho de amostra para efeitos mínimos de 1,5 e 0,5 ponto percentual e explique por que o segundo exige mais observações.
- [ ] **Em `atividades/01-teste-a-b/dia-038-teste-a-b.ipynb`:** Execute a simulação de peeking em 30 verificações diárias e conte quantas vezes a regra pararia antes da amostra planejada.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

### Atividade 2 — Experimentação avançada: testes múltiplos, CUPED e desenho sequencial

#### O que pesquisar
- `multiple hypothesis testing`
- `CUPED`
- `sequential testing`
- `sample ratio mismatch`

**Arquivos da atividade:** [abrir a pasta `02-experimentacao-avancada-testes-multiplos`](<atividades/02-experimentacao-avancada-testes-multiplos/>)

#### Objetivo

Analisar um experimento de autoatendimento sem cair em três armadilhas comuns: grupos desbalanceados, escolha entre muitas métricas e interrupção antecipada. Você também usará CUPED para reduzir variância sem alterar a unidade randomizada.

#### Termos complementares para pesquisar

- `sample ratio mismatch chi square test`
- `Holm Bonferroni multiple testing`
- `false discovery rate Benjamini Hochberg`
- `CUPED controlled experiments using pre experiment data`
- `variance reduction CUPED theta covariance`
- `sequential testing alpha spending`
- `peeking inflated false positive rate A/B test`

#### O que fazer

Leia o [enunciado](<atividades/02-experimentacao-avancada-testes-multiplos/ENUNCIADO.md>), implemente [analisar_experimento.py](<atividades/02-experimentacao-avancada-testes-multiplos/analisar_experimento.py>) e registre protocolo e decisão no próprio artefato.

#### Como validar

- hipóteses, MDE e regra de parada estão congeladas antes da análise;
- SRM, multiplicidade, CUPED e peeking foram medidos;
- a análise diferencia significância de relevância prática;
- lançar, repetir ou abandonar é decidido por critérios anteriores ao resultado.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

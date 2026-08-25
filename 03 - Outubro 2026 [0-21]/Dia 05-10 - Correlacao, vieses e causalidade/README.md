# Correlacao, causalidade e vieses + Causalidade I: contrafactual, DAG, identificação e backdoor

**Data de estudo:** 05/10/2026  
**Carga planejada:** 4 a 5 horas

## Aula selecionada no YouTube

- [ ] **GRINGS - Correlação e Regressão linear  - aula 22** (37:24) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=GRINGS+Correlacao+e+Regressao+linear+aula+22).

Use a aula para compreender a associação linear. Na prática obrigatória, investigue vieses e deixe explícito por que correlação e regressão isoladas não demonstram causalidade.

## Atividades do dia

### Atividade 1 — Correlacao, causalidade e vieses

#### O que pesquisar
- `Correlacao, causalidade e vieses estatística para data science explicado passo a passo`
- `Correlacao, causalidade e vieses estatística para data science exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-correlacao-causalidade-e-vieses`](<atividades/01-correlacao-causalidade-e-vieses/>)

#### O que você precisa entender

Pearson mede relação linear; Spearman mede relação monotônica por postos. Um confundidor influencia exposição e resultado; um DAG registra essas relações antes da análise.

```python
pearson = df[["mensalidade", "nps"]].corr(method="pearson").iloc[0, 1]
spearman = df[["mensalidade", "nps"]].corr(method="spearman").iloc[0, 1]
```

**Erro comum:** escrever “X causa Y” a partir de correlação em dados observacionais.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-correlacao-causalidade-e-vieses/dia-039-correlacao-causalidade-e-vieses.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/incidentes.csv` e dados sintéticos gerados no notebook com seed 42.

#### O que fazer

- [ ] Calcule Pearson e Spearman em duas relações e compare o que cada medida captura.
- [ ] Crie um exemplo de correlação sem causalidade e liste um possível confundidor.
- [ ] Reescreva três conclusões causais como associações compatíveis com os dados observacionais.

- [ ] Construa um DAG simples depois de identificar exposição, resultado e confundidor.
- [ ] **Em `atividades/01-correlacao-causalidade-e-vieses/dia-039-correlacao-causalidade-e-vieses.ipynb`:** Construa um exemplo de Simpson com duas cidades em que a associação geral tenha sinal diferente das associações por cidade.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

### Atividade 2 — Causalidade I: contrafactual, DAG, identificação e backdoor

#### O que pesquisar
- `counterfactual causal inference`
- `DAG causal`
- `backdoor criterion`
- `confounder collider mediator`

**Arquivos da atividade:** [abrir a pasta `02-causalidade-i-contrafactual-dag`](<atividades/02-causalidade-i-contrafactual-dag/>)

#### Objetivo

Converter uma pergunta vaga de impacto em um estimando causal explícito. Você desenhará um DAG antes da análise, distinguirá confundidor, mediador e collider e decidirá quais variáveis podem entrar no ajuste.

#### Termos complementares para pesquisar

- `potential outcomes counterfactual causal inference`
- `causal DAG d separation`
- `backdoor criterion adjustment set`
- `confounder mediator collider examples`
- `selection bias collider conditioning`
- `causal estimand ATE ATT`
- `negative control causal inference`
- `consistency exchangeability positivity causal inference`

#### O que fazer

Leia o [enunciado](<atividades/02-causalidade-i-contrafactual-dag/ENUNCIADO.md>), preencha [protocolo_dag.md](<atividades/02-causalidade-i-contrafactual-dag/protocolo_dag.md>) e registre a auditoria no próprio artefato.

#### Como validar

- população, tratamento, resultado, horizonte e estimando estão definidos;
- o DAG inclui tempo e origem das variáveis;
- todo conjunto de ajuste é aceito ou rejeitado por um caminho causal;
- mediador e collider não entram no ajuste principal;
- limitações não observáveis são declaradas.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

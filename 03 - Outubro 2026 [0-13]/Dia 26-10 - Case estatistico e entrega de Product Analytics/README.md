# Case estatistico

**Data de estudo:** 26/10/2026
**Carga planejada:** 2 a 4 horas

## Atividades do dia

### Atividade 1 — Case estatistico

#### O que pesquisar
- `Case estatistico estatística para data science explicado passo a passo`
- `Case estatistico estatística para data science exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-case-estatistico`](<atividades/01-case-estatistico/>)

#### O que você precisa entender

Diferença absoluta mede unidades originais; diferença percentual usa uma base; tamanho de efeito padroniza a diferença: `d = (média_depois - média_antes) / desvio_combinado`.

```python
diferenca = depois.mean() - antes.mean()
efeito = diferenca / np.sqrt((antes.var(ddof=1) + depois.var(ddof=1)) / 2)
```

**Erro comum:** atribuir a mudança ao processo sem verificar se a composição de cidades ou perfis também mudou.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-case-estatistico/roteiro_atividades.md`.
- **Starter executável:** `atividades/01-case-estatistico/case_estatistico.py`. Execute-o para validar as entradas e depois implemente os `TODOs`; ele não contém os cálculos do case.
- **Dados:** `dados/clientes_telecom.csv`, `dados/incidentes.csv` e dados sintéticos gerados no notebook com seed 42.
- **Entrada congelada do case:** considere a mudança em `2026-05-01`; não ajuste a data depois de observar os resultados.

#### O que fazer

- [ ] Receba um case: a empresa afirma que duração média caiu após mudança de processo; defina população, amostra, variável e hipótese.
- [ ] Faça EDA antes/depois, calcule diferença absoluta, percentual e tamanho de efeito simples.
- [ ] Crie duas análises: uma com média e outra com mediana; explique divergências.
- [ ] Simule um resultado estatisticamente aparente causado por composição diferente de cidades.

- [ ] Entregue nota técnica de uma página dizendo o que pode e não pode ser concluído.
- [ ] **Em `atividades/01-case-estatistico/case_estatistico.py`:** repita a comparação antes/depois usando somente a cidade com maior número de observações; registre o confronto com a conclusão geral em `roteiro_atividades.md`.
- [ ] **Em `atividades/01-case-estatistico/case_estatistico.py`:** inclua uma duração de 2000 minutos no período depois e compare o efeito sobre média, mediana e tamanho de efeito; registre as medidas no roteiro.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

## Entrega real de portfólio

**Telecom Customer Intelligence — Product Analytics**

Siga o [brief do projeto](<../../projetos/telecom-customer-intelligence/README.md>). A entrega precisa ter problema e usuário definidos, data card, dados reproduzíveis, baseline, métricas escolhidas antes do resultado, análise de erros, testes, README em português e inglês e apresentação de 2–3 minutos em inglês. Documente também resultados negativos.

## Publicação da semana no LinkedIn

- **Tema específico:** Telecom Customer Intelligence — funil, cohorts, retenção, métricas reconciliadas e dashboard orientados a uma decisão de produto.
- **Tipo:** entrega.
- **Formato:** carrossel de até seis páginas com uma tela do dashboard e link para o projeto reproduzível.
- **Artefato/evidência exigida:** tracking plan, consultas de funil/cohort/LTV, dashboard reconciliado, nota estatística, data card, README em português/inglês, teste de caso de borda e evidências do projeto compartilhado.

### Roteiro para preencher

- **Problema e usuário:** [qual decisão de produto foi investigada e para quem?]
- **Eventos e métricas:** [qual contrato e qual North Star/guardrail foram definidos?]
- **Funil/cohort:** [qual resultado foi observado e qual denominador foi usado?]
- **Dashboard:** [qual KPI foi reconciliado com SQL ou pandas?]
- **Incerteza:** [qual intervalo, teste ou ressalva estatística muda a leitura?]
- **Decisão:** [qual recomendação os dados sustentam?]
- **Link:** [repositório, dashboard ou relatório conferidos]

### Limitação obrigatória

Declare limitações dos dados educacionais, do período e da definição de eventos, além de separar associação de efeito causal.

### Cuidado contra afirmações falsas

Não atribua receita, retenção ou melhoria real a uma empresa. Não trate o dashboard como sistema em produção. Use somente números reconciliados e descreva o trabalho como projeto educacional. O post não antecipa Competências ou headline.

### Checklist de publicação

- [ ] Reexecutei consultas/notebooks e reconciliei os KPIs do dashboard.
- [ ] Conferi denominadores, períodos, filtros e identidade de usuário.
- [ ] Mostrei resultado, decisão, incerteza e limitação.
- [ ] Removi dados pessoais, segredos e caminhos locais.
- [ ] Testei README, dashboard e links em ambiente limpo/anônimo.
- [ ] **URL publicada:**
- [ ] **Data da publicação:**

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

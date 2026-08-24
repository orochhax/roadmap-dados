# Preparacao para modelagem + Baselines e modelos

**Data de estudo:** 06/11/2026  
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Preparacao para modelagem

#### O que pesquisar
- `Preparacao para modelagem Python explicado passo a passo`
- `Preparacao para modelagem Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-preparacao-para-modelagem`](<atividades/01-preparacao-para-modelagem/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-preparacao-para-modelagem/roteiro_atividades.md`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que você precisa entender

- **Definição:** preparação fixa alvo, unidade, corte, imputação e codificação dentro da pipeline; baseline mede o ganho mínimo.
- **Exemplo mínimo:** `fit` ocorre no treino anterior ao corte; validação recebe somente `transform`.
- **Erro comum:** imputar, escalar ou codificar com estatísticas da base completa.

#### O que fazer

- [ ] Defina corte temporal e conjuntos de treino, validação e teste.
- [ ] Construa pipeline de imputação, codificação e escala sem usar dados futuros.
- [ ] Crie baseline de negócio e DummyClassifier.
- [ ] Defina métricas técnicas e custo de decisão.

- [ ] Salve um `data_card.md` com origem, período, população, exclusões e limitações.


- [ ] **Em `atividades/01-preparacao-para-modelagem/roteiro_atividades.md`:** Compare o baseline de negócio chamados_90d>=3 com o DummyClassifier usando a métrica e o custo definidos.
- [ ] **Em `atividades/01-preparacao-para-modelagem/roteiro_atividades.md`:** Altere o corte temporal em 30 dias e confira se nenhuma data posterior entrou no conjunto de treino.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

### Atividade 2 — Baselines e modelos

#### O que pesquisar
- `Baselines e modelos machine learning com Python explicado passo a passo`
- `Baselines e modelos machine learning com Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-baselines-e-modelos`](<atividades/02-baselines-e-modelos/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-baselines-e-modelos/dia-071-baselines-e-modelos.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que você precisa entender

- **Definição:** champion é escolhido por regra declarada; challenger é alternativa comparável. A regra pode combinar métrica, custo, estabilidade e explicabilidade.
- **Exemplo mínimo:** `score = 0.5*AUC + 0.3*(1-custo_norm) + 0.2*estabilidade`; fixe pesos antes da comparação.
- **Erro comum:** trocar a regra para favorecer o vencedor.

#### O que fazer

- [ ] Treine regressão logística e um modelo de árvore usando a mesma pipeline e validação.
- [ ] Compare média, desvio, custo e tempo em uma tabela única.
- [ ] Analise dez erros críticos e escolha campeão e challenger com critérios definidos antes do resultado.

- [ ] Amplie a análise para 20 erros críticos e registre se os padrões encontrados nos dez primeiros permanecem.


- [ ] **Em `atividades/02-baselines-e-modelos/dia-071-baselines-e-modelos.ipynb`:** Compare campeão e challenger no segmento plano Básico 100 e registre tamanho, custo, recall e precision.
- [ ] **Em `atividades/02-baselines-e-modelos/dia-071-baselines-e-modelos.ipynb`:** Aumente o custo de falso negativo de R$500 para R$800 e confira se a escolha do campeão muda.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Publicação da semana no LinkedIn

- **Tema específico:** da auditoria ao primeiro baseline confiável de churn — alvo temporal, qualidade, SQL/EDA e pipeline sem vazamento.
- **Tipo:** progresso.
- **Formato:** carrossel problema → achado da auditoria → correção → baseline → próximo teste.
- **Artefato/evidência exigida:** `auditoria_modelo.md`, definição temporal do alvo, checks de qualidade, consulta/EDA do churn, split congelado, baseline e modelo inicial executados durante 03–06/11.

### Roteiro para preencher

- **Problema e alvo:** [quem é previsto, em qual data e em qual horizonte?]
- **Achado da auditoria:** [qual risco de leakage, caminho fixo ou estado oculto foi encontrado?]
- **Correção e prova:** [qual alteração foi feita e qual teste comprova a correção?]
- **Dados/EDA:** [qual problema de qualidade ou padrão relevante apareceu?]
- **Baseline:** [qual referência simples foi executada e qual resultado observou?]
- **Estado atual:** [o que falta para política, segmentos, dashboard e release de 12/11?]
- **Evidência:** [relatório, script ou saída conferidos]

### Limitação obrigatória

Explique que o projeto de churn ainda está em construção e que um baseline offline não define sozinho uma política de retenção.

### Cuidado contra afirmações falsas

Não publique resultado como release final, não afirme previsão em produção nem impacto sobre clientes. Chame o trabalho de auditoria e baseline em progresso. O post não antecipa Competências ou headline.

### Checklist de publicação

- [ ] Reexecutei o pipeline duas vezes com a seed registrada.
- [ ] Confirmei alvo, datas, split e ausência dos sinais pós-evento.
- [ ] Mostrei um achado, a correção e a evidência do teste.
- [ ] Mantive baseline e limitações visíveis.
- [ ] Removi dados sensíveis, caminhos locais e links privados.
- [ ] **URL publicada:**
- [ ] **Data da publicação:**

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

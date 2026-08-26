# Benchmark publicado

**Data de estudo:** 08/12/2026
**Carga planejada:** 2 a 4 horas

## Atividades do dia

### Atividade 1 — Benchmark publicado

#### O que pesquisar
- `Benchmark publicado Python explicado passo a passo`
- `Benchmark publicado Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-benchmark-publicado`](<atividades/01-benchmark-publicado/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-benchmark-publicado/roteiro_atividades.md`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que você precisa entender

- **Definição:** benchmark é um protocolo de comparação: mesmos dados, divisão, pré-processamento e métricas para todos os modelos; o Dummy mostra o mínimo que um modelo útil precisa superar.
- **Exemplo mínimo:** fixe `random_state=42`, treine todos no mesmo `X_train, y_train` e salve `modelo, métrica, tempo_ms` em uma única tabela.
- **Erro comum:** mudar o split ou ajustar o pré-processamento com todos os dados; isso torna as métricas incomparáveis e pode vazar informação da avaliação.

#### O que fazer

- [ ] Compare obrigatoriamente Dummy, regressão logística, Random Forest e XGBoost usando o mesmo split, pré-processamento e protocolo.
- [ ] Registre biblioteca, versão, seed, métricas primária e secundária, tempo de treino e tempo de inferência de cada modelo.
- [ ] Salve os resultados em `benchmark.csv` e os hiperparâmetros em `parametros.json`.
- [ ] Escolha champion e challenger e defenda a decisão com qualidade, custo, latência, explicabilidade e três trade-offs.

- [ ] **Em `atividades/01-benchmark-publicado/roteiro_atividades.md`:** Reexecute o benchmark com random_state=17 além de 42 e acrescente as métricas à mesma tabela, sem sobrescrever a primeira rodada.
- [ ] **Em `atividades/01-benchmark-publicado/roteiro_atividades.md`:** Compare tamanho em disco e tempo de inferência de logística e Random Forest em 100 previsões.

#### Atualização do LinkedIn — após concluir

- **Evidência exigida:** `benchmark.csv` reproduzível com uma linha executada de XGBoost e comparação justa entre os quatro modelos.
- **Competências:** adicione **XGBoost** e **Avaliação de modelos**.
- **Sobre e headline:** não altere ainda; a revisão de posicionamento ocorrerá após a auditoria completa do pipeline.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

---

## Entrega real de portfólio

**Telecom Customer Intelligence — benchmark de retenção**

Siga o [brief do projeto](<../../projetos/telecom-customer-intelligence/README.md>). A entrega precisa ter problema e usuário definidos, data card, dados reproduzíveis, baseline, métricas escolhidas antes do resultado, análise de erros, testes, README em português e inglês e apresentação de 2–3 minutos em inglês. Documente também resultados negativos.

## Publicação da semana no LinkedIn

- **Tema específico:** benchmark justo de retenção — regra, regressão logística, Random Forest e XGBoost no mesmo split, pipeline e métricas.
- **Tipo:** entrega.
- **Formato:** carrossel de benchmark com tabela principal, slice de erros, latência/custo e link para o projeto reproduzível.
- **Artefato/evidência exigida:** `benchmark.csv`, `parametros.json`, quatro abordagens realmente executadas, baseline, PR-AUC/recall no Top-K/calibração, latência, análise de erros, champion/challenger e relatório reproduzido.

### Roteiro para preencher

- **Problema e restrição:** [qual decisão de retenção e qual capacidade?]
- **Protocolo justo:** [split, pipeline e métricas iguais para todos os modelos]
- **Modelos comparados:** [quais quatro linhas realmente existem no benchmark?]
- **Resultado verificável:** [métricas e caminho de `benchmark.csv`]
- **Slices/erros:** [em qual segmento ou tipo de erro o ranking muda?]
- **Trade-off:** [qualidade, calibração, latência, custo ou explicabilidade]
- **Decisão:** [champion, challenger ou baseline mantido, com justificativa]

### Limitação obrigatória

Declare o limite da amostra e explique por que o melhor modelo offline ainda precisa de monitoramento e validação operacional.

### Cuidado contra afirmações falsas

Não selecione hiperparâmetros no teste, não omita modelo perdedor e não afirme impacto real. Se XGBoost não vencer com margem útil, publique isso. O post não altera Competências ou headline automaticamente.

### Checklist de publicação

- [ ] As quatro abordagens usam o mesmo split, pipeline e métricas.
- [ ] Conferi `benchmark.csv`, parâmetros, seeds e versões.
- [ ] Mostrei baseline, slice de erro, trade-off e limitação.
- [ ] Reexecutei a instrução principal em ambiente limpo.
- [ ] Removi dados sensíveis e testei todos os links.
- [ ] **URL publicada:**
- [ ] **Data da publicação:**

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

# Benchmark publicado

**Data de estudo:** 28/10/2026  
**Carga planejada:** 2 a 4 horas

## Como estudar

Você pode escolher vídeo, documentação, site ou IA. Pesquise os nomes abaixo, faça uma primeira tentativa sem solução pronta e guarde evidência executável.

## Assuntos para pesquisar

### Bloco 1 — Benchmark publicado

Pesquise exatamente:

- `Benchmark publicado Python explicado passo a passo`
- `Benchmark publicado Python exercícios práticos`

Depois siga o [guia e os enunciados deste bloco](<modulos/01-e66/README.md>). Tente os exercícios antes de procurar uma implementação completa.

## Integração

Explique com suas palavras como os blocos se conectam em um fluxo de dados ou decisão. Execute um caso comum e um caso de borda de cada bloco e registre comandos, saídas e dúvidas nas evidências.


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

## Concluído quando

- [ ] Estudei todos os assuntos e concluí os enunciados dos blocos sem copiar uma solução completa.
- [ ] Executei os artefatos, testei casos de borda e registrei resultados verificáveis.
- [ ] Expliquei a conexão entre os blocos, a decisão tomada e pelo menos uma limitação concreta.

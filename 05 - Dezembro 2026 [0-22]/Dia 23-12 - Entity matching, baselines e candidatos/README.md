# Entity matching I: normalização e baselines exato, fuzzy e TF-IDF + Entity matching II: blocking, deduplicação e geração de candidatos

**Data de estudo:** 23/12/2026  
**Carga planejada:** 4 a 5 horas

## Como estudar

Você pode escolher vídeo, documentação, site ou IA. Pesquise os nomes abaixo, faça uma primeira tentativa sem solução pronta e guarde evidência executável.

## Assuntos para pesquisar

### Bloco 1 — Entity matching I: normalização e baselines exato, fuzzy e TF-IDF

Pesquise exatamente:

- `entity resolution`
- `record linkage`
- `Levenshtein company names`
- `TF-IDF character n-grams`

Depois siga o [guia e os enunciados deste bloco](<modulos/01-n14/README.md>). Tente os exercícios antes de procurar uma implementação completa.

### Bloco 2 — Entity matching II: blocking, deduplicação e geração de candidatos

Pesquise exatamente:

- `record linkage blocking`
- `candidate generation`
- `blocking recall`
- `reduction ratio`

Depois siga o [guia e os enunciados deste bloco](<modulos/02-n15/README.md>). Tente os exercícios antes de procurar uma implementação completa.

## Integração

Explique com suas palavras como os blocos se conectam em um fluxo de dados ou decisão. Execute um caso comum e um caso de borda de cada bloco e registre comandos, saídas e dúvidas nas evidências.

## Publicação da semana no LinkedIn

- **Tema específico:** primeiros baselines de entity matching para nomes e domínios bagunçados — normalização, correspondência exata, fuzzy, TF-IDF e blocking.
- **Tipo:** progresso.
- **Formato:** carrossel com pares anonimizados, etapas do pipeline e dois erros que orientam os próximos experimentos.
- **Artefato/evidência exigida:** `normalizacao_baseline.py` e `gerar_candidatos.py` executados, evidências N14/N15 preenchidas, teste congelado, métricas do baseline e exemplos sem dados pessoais.

### Roteiro para preencher

- **Problema:** [por que dois registros podem representar a mesma empresa?]
- **Dados seguros:** [como os exemplos foram anonimizados ou sintetizados?]
- **Baselines:** [quais regras e representações foram comparadas?]
- **Blocking:** [como o espaço de candidatos foi reduzido e qual recall foi preservado?]
- **Resultado verificável:** [métrica, valor e caminho da evidência]
- **Erros:** [um falso merge e um falso split que ainda precisam ser resolvidos]
- **Próxima hipótese:** [o que embeddings ou ranking deverão testar, sem antecipar o resultado?]

### Limitação obrigatória

Explique que esta é uma etapa intermediária: a entidade correta pode não ser gerada e o pipeline final ainda não foi avaliado com embeddings, ranking, latência e custo.

### Cuidado contra afirmações falsas

Não chame os baselines de produto concluído nem declare deduplicação automática segura. Não exponha nomes, domínios ou identificadores pessoais reais. Este post de progresso não antecipa Competências ou headline.

### Checklist de publicação

- [ ] Usei apenas exemplos públicos, sintéticos ou anonimizados.
- [ ] Mantive o teste congelado e conferi as métricas publicadas.
- [ ] Mostrei pelo menos um falso merge e um falso split.
- [ ] Diferenciei recuperação de candidatos da decisão final de match.
- [ ] Deixei explícito qual etapa ainda falta.
- [ ] **URL publicada:**
- [ ] **Data da publicação:**

## Concluído quando

- [ ] Estudei todos os assuntos e concluí os enunciados dos blocos sem copiar uma solução completa.
- [ ] Executei os artefatos, testei casos de borda e registrei resultados verificáveis.
- [ ] Expliquei a conexão entre os blocos, a decisão tomada e pelo menos uma limitação concreta.

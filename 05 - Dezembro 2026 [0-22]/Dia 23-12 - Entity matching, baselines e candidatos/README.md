# Entity matching I: normalização e baselines exato, fuzzy e TF-IDF + Entity matching II: blocking, deduplicação e geração de candidatos

**Data de estudo:** 23/12/2026  
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Entity matching I: normalização e baselines exato, fuzzy e TF-IDF

#### O que pesquisar
- `entity resolution`
- `record linkage`
- `Levenshtein company names`
- `TF-IDF character n-grams`

**Arquivos da atividade:** [abrir a pasta `01-entity-matching-i-normalizacao`](<atividades/01-entity-matching-i-normalizacao/>)

#### Objetivo

Iniciar o **Entity Matching Lab** ligando registros empresariais bagunçados a um cadastro canônico. Você comparará três níveis de solução — igualdade exata, similaridade fuzzy e TF-IDF de caracteres — para medir o ganho real de complexidade e entender os dois erros centrais: unir empresas diferentes e separar registros da mesma empresa.

#### Termos complementares para pesquisar

1. `entity resolution record linkage deduplication difference`
2. `company name normalization legal suffix unicode accents`
3. `Python urllib parse normalize domain punycode`
4. `RapidFuzz fuzz ratio token set ratio process extract`
5. `TfidfVectorizer character n grams company name matching`
6. `cosine similarity sparse matrix nearest neighbors`
7. `record linkage false match false non match precision recall`
8. `entity resolution threshold validation set error analysis`

#### O que você precisa entender

- **Registro canônico:** versão confiável que representa uma entidade.
- **Par verdadeiro:** dois registros que realmente representam a mesma empresa.
- **Falso merge:** empresas diferentes unidas; costuma ter alto custo de negócio.
- **Falso split:** mesma empresa mantida como duas entidades.
- **Limiar:** score mínimo para aceitar automaticamente um vínculo.

#### O que fazer

Implemente as comparações descritas no [enunciado](<atividades/01-entity-matching-i-normalizacao/ENUNCIADO.md>) em `atividades/01-entity-matching-i-normalizacao/normalizacao_baseline.py` e registre a trilha de decisão no próprio artefato.

Não transforme o melhor resultado em busca contra todos os registros ainda; a redução eficiente de candidatos será o foco da Atividade 2 — blocking e geração de candidatos.

#### LinkedIn

Após validar a entrega, adicione: **Entity Resolution**, **Record Linkage** e **Similaridade de texto**.

### Atividade 2 — Entity matching II: blocking, deduplicação e geração de candidatos

#### O que pesquisar
- `record linkage blocking`
- `candidate generation`
- `blocking recall`
- `reduction ratio`

**Arquivos da atividade:** [abrir a pasta `02-entity-matching-ii-blocking-deduplicacao`](<atividades/02-entity-matching-ii-blocking-deduplicacao/>)

#### Objetivo

Evitar a comparação cartesiana entre cada registro recebido e todo o cadastro. Você construirá um gerador de candidatos em múltiplas passagens, medindo quanto trabalho ele elimina sem descartar a entidade verdadeira. Essa etapa transforma os baselines da atividade de normalização em um desenho capaz de crescer para milhões de empresas.

#### Termos complementares para pesquisar

1. `record linkage blocking candidate generation explained`
2. `blocking keys exact match multiple passes record linkage`
3. `sorted neighbourhood indexing record linkage`
4. `TF-IDF nearest neighbors candidate generation sparse matrix`
5. `blocking pair completeness pairs quality reduction ratio`
6. `candidate recall at k entity resolution`
7. `deduplication connected components transitive closure risk`
8. `entity resolution blocking missing values common names`

#### O que você precisa entender

- **Blocking:** restringe quais pares podem ser comparados com regras baratas.
- **Passagens múltiplas:** unem candidatos produzidos por chaves diferentes.
- **Pair completeness:** proporção dos pares verdadeiros preservados pelo blocking.
- **Reduction ratio:** proporção do produto cartesiano que deixou de ser avaliada.
- **Recall@k de candidatos:** frequência com que a entidade correta aparece entre os primeiros `k` candidatos.

#### O que fazer

Use os dados e funções da Atividade 1 — normalização e baseline. Siga [o enunciado](<atividades/02-entity-matching-ii-blocking-deduplicacao/ENUNCIADO.md>) em `atividades/02-entity-matching-ii-blocking-deduplicacao/gerar_candidatos.py` e registre os experimentos no próprio artefato.

O arquivo de candidatos aprovado será a entrada da atividade de embeddings e, depois, da atividade de reranking.

#### LinkedIn

Após concluir, adicione: **Entity Resolution**, **Geração de candidatos** e **Otimização de algoritmos**.

## Publicação da semana no LinkedIn

- **Tema específico:** primeiros baselines de entity matching para nomes e domínios bagunçados — normalização, correspondência exata, fuzzy, TF-IDF e blocking.
- **Tipo:** progresso.
- **Formato:** carrossel com pares anonimizados, etapas do pipeline e dois erros que orientam os próximos experimentos.
- **Artefato/evidência exigida:** `normalizacao_baseline.py` e `gerar_candidatos.py` executados, resultados das duas atividades registrados, teste congelado, métricas do baseline e exemplos sem dados pessoais.

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

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

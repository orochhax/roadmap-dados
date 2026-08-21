# Entity matching I: normalização e baselines exato, fuzzy e TF-IDF

## Objetivo

Iniciar o **Entity Matching Lab** ligando registros empresariais bagunçados a um cadastro canônico. Você comparará três níveis de solução — igualdade exata, similaridade fuzzy e TF-IDF de caracteres — para medir o ganho real de complexidade e entender os dois erros centrais: unir empresas diferentes e separar registros da mesma empresa.

## Pesquise estes nomes exatos

1. `entity resolution record linkage deduplication difference`
2. `company name normalization legal suffix unicode accents`
3. `Python urllib parse normalize domain punycode`
4. `RapidFuzz fuzz ratio token set ratio process extract`
5. `TfidfVectorizer character n grams company name matching`
6. `cosine similarity sparse matrix nearest neighbors`
7. `record linkage false match false non match precision recall`
8. `entity resolution threshold validation set error analysis`

## Conceitos essenciais

- **Registro canônico:** versão confiável que representa uma entidade.
- **Par verdadeiro:** dois registros que realmente representam a mesma empresa.
- **Falso merge:** empresas diferentes unidas; costuma ter alto custo de negócio.
- **Falso split:** mesma empresa mantida como duas entidades.
- **Limiar:** score mínimo para aceitar automaticamente um vínculo.

## Entrega obrigatória

Implemente as comparações descritas no [enunciado](<01-exercicios/ENUNCIADO.md>) em `01-exercicios/normalizacao_baseline.py` e registre a trilha de decisão em [evidências](<03-evidencias/README.md>).

Não transforme o melhor resultado em busca contra todos os registros ainda; a redução eficiente de candidatos será o foco do N15.

## LinkedIn

Após validar a entrega, adicione: **Entity Resolution**, **Record Linkage** e **Similaridade de texto**.

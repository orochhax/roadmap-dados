# Escopo e documentos + Ingestao e chunking

**Data de estudo:** 04/01/2027  
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Escopo e documentos

#### O que pesquisar
- `Escopo e documentos Python explicado passo a passo`
- `Escopo e documentos Python exercícios práticos`

#### Aula guiada — RAG com LangChain (parte 1)

- [ ] Assista a [**Agente de IA completo com Python - Projeto RAG com Langchain**](https://www.youtube.com/watch?v=0M8iO5ykY-E), de `00:00` a `33:43` (33min43s).
- Nesta parte, concentre-se na arquitetura RAG, preparação da base, estrutura do projeto, carregamento, chunking, embeddings e criação do banco vetorial.
- Não copie a chave nem use o PDF do vídeo como entrega. Aplique os conceitos ao corpus governado do projeto, preservando manifesto, metadados, hashes e perguntas com gabarito.

**Arquivos da atividade:** [abrir a pasta `projeto-assistente-suporte-ia`](<../../projetos/assistente-suporte-ia/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `projetos/assistente-suporte-ia/src/assistente_suporte_ia/escopo_corpus.py`.
- **Dados:** `projetos/assistente-suporte-ia/data/corpus/` e `projetos/assistente-suporte-ia/data/perguntas_avaliacao.csv`.

#### Diagnóstico de base

- [ ] Confirme agora, em `projetos/assistente-suporte-ia/governanca/gate-fundamentos.md`, autonomia 3/5 ou maior em Python, SQL, estatística e ML: script testado, consulta com JOIN/agregação, cálculo interpretado e pipeline com baseline.
- Use as lacunas encontradas para planejar uma revisão posterior; elas não substituem as atividades obrigatórias de LLM/RAG.

#### O que você precisa entender

- **Definição:** RAG recupera trechos de um corpus e os fornece à geração; manifesto do corpus registra origem, licença, versão e identificador.
- **Exemplo mínimo:** valide os 15 documentos locais e complete `projetos/assistente-suporte-ia/data/corpus/corpus_manifest.csv` com `doc_id, arquivo, origem, licença, versão, sha256`.
- **Erro comum:** ingerir conteúdo sem permissão ou sem conseguir rastrear a fonte citada.

#### O que fazer

- [ ] Defina o escopo do RAG e uma política explícita de recusa fora dos documentos.
- [ ] Valide os 15 documentos fornecidos, seus caminhos, versões, licenças e hashes.
- [ ] Valide e refine dez perguntas com gabarito em `projetos/assistente-suporte-ia/data/perguntas_avaliacao.csv` antes da implementação.
- [ ] Desenhe o fluxo de ingestão, recuperação, geração e avaliação.

- [ ] **Em `projetos/assistente-suporte-ia/src/assistente_suporte_ia/escopo_corpus.py`:** inclua no conjunto a pergunta 'O pagamento foi feito ontem e ainda não baixou; o que faço?' apontando para o documento correto.
- [ ] **No mesmo arquivo:** adicione a pergunta fora do domínio 'qual ação devo comprar?' e escreva a frase de recusa exigida pela política.

#### Como validar

- O diagnóstico está registrado e o artefato obrigatório de LLM/RAG foi executado com a saída exigida.
- Um caso de borda ou erro foi testado, com resultado esperado e observado registrados.
- A entrega explica o resultado, a decisão tomada e uma limitação concreta.

### Atividade 2 — Ingestao e chunking

#### O que pesquisar
- `Ingestao e chunking Python explicado passo a passo`
- `Ingestao e chunking Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `projeto-assistente-suporte-ia`](<../../projetos/assistente-suporte-ia/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `projetos/assistente-suporte-ia/src/assistente_suporte_ia/ingestao_chunking.py`.
- **Dados:** `projetos/assistente-suporte-ia/data/corpus/` e `projetos/assistente-suporte-ia/data/perguntas_avaliacao.csv`.

#### Diagnóstico de base

- [ ] Confirme agora, em `projetos/assistente-suporte-ia/governanca/gate-fundamentos.md`, autonomia 3/5 ou maior em Python, SQL, estatística e ML: script testado, consulta com JOIN/agregação, cálculo interpretado e pipeline com baseline.
- Use as lacunas encontradas para planejar uma revisão posterior; elas não substituem as atividades obrigatórias de LLM/RAG.

#### O que você precisa entender

- **Definição:** chunk é um trecho indexado; overlap repete bordas para preservar contexto, com custo de duplicação.
- **Exemplo mínimo:** compare chunks de 300 e 600 caracteres com overlap 50 em cinco perguntas; se PDF falhar, use TXT/Markdown local equivalente.
- **Erro comum:** cortar no meio de unidades lógicas ou avaliar só pelo número de chunks.

#### O que fazer

- [ ] Implemente leitura de Markdown/PDF/texto conforme os documentos escolhidos.
- [ ] Teste quatro estratégias de chunking: tamanho fixo, por parágrafo, por seção e com overlap.
- [ ] Registre quantidade e tamanho médio dos chunks.

- [ ] **Em `projetos/assistente-suporte-ia/src/assistente_suporte_ia/ingestao_chunking.py`:** compare chunking por seção e por 300 caracteres nos documentos de LOS vermelha e pagamento não reconhecido, preservando metadados de documento, seção e versão.
- [ ] **No mesmo arquivo:** use as duas perguntas desses documentos, registre quantidade/tamanho dos chunks e escolha pela recuperação observada.

#### Como validar

- O diagnóstico está registrado e o artefato obrigatório de LLM/RAG foi executado com a saída exigida.
- Um caso de borda ou erro foi testado, com resultado esperado e observado registrados.
- A entrega explica o resultado, a decisão tomada e uma limitação concreta.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

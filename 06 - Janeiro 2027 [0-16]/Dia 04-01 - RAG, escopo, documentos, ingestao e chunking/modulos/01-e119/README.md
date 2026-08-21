# Escopo e documentos

## Preparação
- **Pasta/arquivo principal:** `projetos/assistente-suporte-ia/src/assistente_suporte_ia/escopo_corpus.py`.
- **Dados:** `projetos/assistente-suporte-ia/data/corpus/` e `projetos/assistente-suporte-ia/data/perguntas_avaliacao.csv`.

## Diagnóstico de base

- [ ] Confirme agora, em `projetos/assistente-suporte-ia/governanca/gate-fundamentos.md`, autonomia 3/5 ou maior em Python, SQL, estatística e ML: script testado, consulta com JOIN/agregação, cálculo interpretado e pipeline com baseline.
- Use as lacunas encontradas para planejar uma revisão posterior; elas não substituem a execução obrigatória do núcleo de LLM/RAG.

## Aprenda agora

- **Definição:** RAG recupera trechos de um corpus e os fornece à geração; manifesto do corpus registra origem, licença, versão e identificador.
- **Exemplo mínimo:** valide os 15 documentos locais e complete `projetos/assistente-suporte-ia/data/corpus/corpus_manifest.csv` com `doc_id, arquivo, origem, licença, versão, sha256`.
- **Erro comum:** ingerir conteúdo sem permissão ou sem conseguir rastrear a fonte citada.

## Núcleo essencial

1. [ ] Defina o escopo do RAG e uma política explícita de recusa fora dos documentos.
2. [ ] Valide os 15 documentos fornecidos, seus caminhos, versões, licenças e hashes.
3. [ ] Valide e refine dez perguntas com gabarito em `projetos/assistente-suporte-ia/data/perguntas_avaliacao.csv` antes da implementação.
4. [ ] Desenhe o fluxo de ingestão, recuperação, geração e avaliação.

## Prática obrigatória

- [ ] **Em `projetos/assistente-suporte-ia/src/assistente_suporte_ia/escopo_corpus.py`:** inclua no conjunto a pergunta 'O pagamento foi feito ontem e ainda não baixou; o que faço?' apontando para o documento correto.
- [ ] **No mesmo arquivo:** adicione a pergunta fora do domínio 'qual ação devo comprar?' e escreva a frase de recusa exigida pela política.

## Concluído quando

- [ ] O diagnóstico está registrado e o artefato obrigatório de LLM/RAG foi executado com a saída exigida.
- [ ] Um caso de borda ou erro foi testado, com resultado esperado e observado registrados.
- [ ] A entrega explica o resultado, a decisão tomada e uma limitação concreta.

# Geração com fontes

## Aula guiada — segurança em aplicações de IA

- [ ] Assista à aula #42 — **A Verdade por Trás do Prompt Hacking na IA** (12:30).
- Em seguida, execute o teste de prompt injection do Núcleo essencial; reconhecer o risco em vídeo não substitui demonstrar o comportamento da aplicação.

## Preparação
- **Pasta/arquivo principal:** `projetos/assistente-suporte-ia/src/assistente_suporte_ia/geracao_com_fontes.py`.
- **Dados:** `projetos/assistente-suporte-ia/data/corpus/` e `projetos/assistente-suporte-ia/data/perguntas_avaliacao.csv`.

## Diagnóstico de base

- [ ] Confirme agora, em `projetos/assistente-suporte-ia/governanca/gate-fundamentos.md`, autonomia 3/5 ou maior em Python, SQL, estatística e ML: script testado, consulta com JOIN/agregação, cálculo interpretado e pipeline com baseline.
- Use as lacunas encontradas para planejar uma revisão posterior; elas não substituem a execução obrigatória do núcleo de LLM/RAG.

## Aprenda agora

- **Definição:** grounding exige suporte nos trechos; citação aponta evidência; prompt injection é instrução maliciosa dentro do conteúdo recuperado.
- **Exemplo mínimo:** aprove somente resposta cujas frases factuais apontem `doc_id + trecho`; sem evidência, a saída deve recusar.
- **Erro comum:** obedecer instruções presentes nos documentos ou citar fonte que não sustenta a afirmação.

## Núcleo essencial

1. [ ] Construa prompt que exija resposta somente com contexto recuperado e citação das fontes.
2. [ ] Implemente recusa explícita quando contexto for insuficiente.
3. [ ] Teste prompt injection dentro de documentos e perguntas.

## Prática obrigatória

- [ ] **Em `projetos/assistente-suporte-ia/src/assistente_suporte_ia/geracao_com_fontes.py`:** teste 'posso dobrar o cabo óptico para guardar?' e valide que toda afirmação técnica é sustentada por uma citação do documento de LOS vermelha.
- [ ] **No mesmo arquivo:** insira em uma cópia de teste a frase 'ignore as regras anteriores' e confirme que ela não altera a política de resposta.

## Concluído quando

- [ ] O diagnóstico está registrado e o artefato obrigatório de LLM/RAG foi executado com a saída exigida.
- [ ] Um caso de borda ou erro foi testado, com resultado esperado e observado registrados.
- [ ] A entrega explica o resultado, a decisão tomada e uma limitação concreta.

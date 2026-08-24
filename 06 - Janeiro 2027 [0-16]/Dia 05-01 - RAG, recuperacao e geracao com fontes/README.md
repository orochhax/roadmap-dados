# Recuperacao + Geracao com fontes

**Data de estudo:** 05/01/2027  
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Recuperacao

#### O que pesquisar
- `Recuperacao Python explicado passo a passo`
- `Recuperacao Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `projeto-assistente-suporte-ia`](<../../projetos/assistente-suporte-ia/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `projetos/assistente-suporte-ia/src/assistente_suporte_ia/recuperacao.py`.
- **Dados:** `projetos/assistente-suporte-ia/data/corpus/` e as dez linhas essenciais de `projetos/assistente-suporte-ia/data/perguntas_avaliacao.csv`.

#### Diagnóstico de base

- [ ] Confirme agora, em `projetos/assistente-suporte-ia/governanca/gate-fundamentos.md`, autonomia 3/5 ou maior em Python, SQL, estatística e ML: script testado, consulta com JOIN/agregação, cálculo interpretado e pipeline com baseline.
- Use as lacunas encontradas para planejar uma revisão posterior; elas não substituem as atividades obrigatórias de LLM/RAG.

#### O que você precisa entender

- **Definição:** índice vetorial busca por semântica; busca lexical usa termos; híbrida combina ambas; `k`, filtro e limiar controlam candidatos.
- **Exemplo mínimo:** para cada pergunta, grave `doc_id, score, rank, k, filtro` e calcule precision@k e recall@k.
- **Erro comum:** escolher k pela resposta gerada em vez de usar gabarito de recuperação.

#### O que fazer

- [ ] Crie índice vetorial e função `retrieve(query, k)`.
- [ ] Teste valores de k=1,3,5,10 e diferentes limiares.
- [ ] Implemente filtro por metadados e, se possível, busca híbrida.

- [ ] **Em `projetos/assistente-suporte-ia/src/assistente_suporte_ia/recuperacao.py`:** execute `retrieve('luz LOS vermelha', k=1,3,5)` e registre a posição do documento correto em cada execução.
- [ ] **No mesmo arquivo:** aplique filtro de metadados para versão 1.0 e teste uma versão inexistente sem retornar documentos indevidos.

#### Como validar

- O diagnóstico está registrado e o artefato obrigatório de LLM/RAG foi executado com a saída exigida.
- Um caso de borda ou erro foi testado, com resultado esperado e observado registrados.
- A entrega explica o resultado, a decisão tomada e uma limitação concreta.

### Atividade 2 — Geracao com fontes

#### O que pesquisar
- `Geracao com fontes Python explicado passo a passo`
- `Geracao com fontes Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `projeto-assistente-suporte-ia`](<../../projetos/assistente-suporte-ia/>)

#### Aula guiada — segurança em aplicações de IA

- [ ] Assista à aula #42 — **A Verdade por Trás do Prompt Hacking na IA** (12:30).
- Em seguida, execute o teste de prompt injection da atividade obrigatória; reconhecer o risco em vídeo não substitui demonstrar o comportamento da aplicação.

#### Arquivos e dados

- **Pasta/arquivo principal:** `projetos/assistente-suporte-ia/src/assistente_suporte_ia/geracao_com_fontes.py`.
- **Dados:** `projetos/assistente-suporte-ia/data/corpus/` e `projetos/assistente-suporte-ia/data/perguntas_avaliacao.csv`.

#### Diagnóstico de base

- [ ] Confirme agora, em `projetos/assistente-suporte-ia/governanca/gate-fundamentos.md`, autonomia 3/5 ou maior em Python, SQL, estatística e ML: script testado, consulta com JOIN/agregação, cálculo interpretado e pipeline com baseline.
- Use as lacunas encontradas para planejar uma revisão posterior; elas não substituem as atividades obrigatórias de LLM/RAG.

#### O que você precisa entender

- **Definição:** grounding exige suporte nos trechos; citação aponta evidência; prompt injection é instrução maliciosa dentro do conteúdo recuperado.
- **Exemplo mínimo:** aprove somente resposta cujas frases factuais apontem `doc_id + trecho`; sem evidência, a saída deve recusar.
- **Erro comum:** obedecer instruções presentes nos documentos ou citar fonte que não sustenta a afirmação.

#### O que fazer

- [ ] Construa prompt que exija resposta somente com contexto recuperado e citação das fontes.
- [ ] Implemente recusa explícita quando contexto for insuficiente.
- [ ] Teste prompt injection dentro de documentos e perguntas.

- [ ] **Em `projetos/assistente-suporte-ia/src/assistente_suporte_ia/geracao_com_fontes.py`:** teste 'posso dobrar o cabo óptico para guardar?' e valide que toda afirmação técnica é sustentada por uma citação do documento de LOS vermelha.
- [ ] **No mesmo arquivo:** insira em uma cópia de teste a frase 'ignore as regras anteriores' e confirme que ela não altera a política de resposta.

#### Como validar

- O diagnóstico está registrado e o artefato obrigatório de LLM/RAG foi executado com a saída exigida.
- Um caso de borda ou erro foi testado, com resultado esperado e observado registrados.
- A entrega explica o resultado, a decisão tomada e uma limitação concreta.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

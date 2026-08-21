# Avaliação e publicação

## Conquista para o LinkedIn

- **Condição:** use esta atualização somente depois de concluir a aplicação obrigatória de LLM/RAG, avaliá-la e publicá-la com evidências.
- **Ação concreta:** registre **IA Generativa e RAG** em Competências e inclua a aplicação em Projetos ou Destaques.
- **Novo título:** `Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa`.

## Preparação
- **Pasta/arquivo principal:** `projetos/assistente-suporte-ia/src/assistente_suporte_ia/avaliar_rag.py`.
- **Roteiro:** `projetos/assistente-suporte-ia/docs/roteiro-avaliacao-publicacao.md`.
- **Dados:** `projetos/assistente-suporte-ia/data/corpus/` e `projetos/assistente-suporte-ia/data/perguntas_avaliacao.csv`.

## Diagnóstico de base

- [ ] Confirme agora, em `projetos/assistente-suporte-ia/governanca/gate-fundamentos.md`, autonomia 3/5 ou maior em Python, SQL, estatística e ML: script testado, consulta com JOIN/agregação, cálculo interpretado e pipeline com baseline.
- Use as lacunas encontradas para planejar uma revisão posterior; elas não substituem a execução obrigatória do núcleo de LLM/RAG.

## Aprenda agora

- **Definição:** avaliação ponta a ponta verifica corpus, recuperação, resposta, citação, recusa, latência e reprodução; aceite transforma qualidade em regra observável.
- **Exemplo mínimo:** execute dez perguntas com gabarito e grave o contrato completo em `projetos/assistente-suporte-ia/outputs/avaliacao/avaliacao_rag.csv`.
- **Erro comum:** publicar apenas exemplos escolhidos ou mudar a rubrica após ver as respostas.

## Núcleo essencial

1. [ ] Execute a avaliação nas dez perguntas essenciais e registre recuperação, fundamentação e recusas.
2. [ ] Crie uma interface simples com pergunta, resposta e fontes.
3. [ ] Adicione tratamento de erro e grave logs sem conteúdo sensível em `projetos/assistente-suporte-ia/outputs/logs/execucoes.jsonl`.
4. [ ] Publique README com execução, limitações, riscos e custo aproximado.

## Prática obrigatória

- [ ] **Em `projetos/assistente-suporte-ia/src/assistente_suporte_ia/avaliar_rag.py`:** adicione à avaliação a pergunta de pagamento não reconhecido e a pergunta fora do domínio sobre ações.
- [ ] **No mesmo arquivo:** compare k=3 e k=5 nas mesmas dez perguntas essenciais e registre recuperação, latência e respostas sem fonte.

## Concluído quando

- [ ] O diagnóstico está registrado e o artefato obrigatório de LLM/RAG foi executado com a saída exigida.
- [ ] Um caso de borda ou erro foi testado, com resultado esperado e observado registrados.
- [ ] A entrega explica o resultado, a decisão tomada e uma limitação concreta.

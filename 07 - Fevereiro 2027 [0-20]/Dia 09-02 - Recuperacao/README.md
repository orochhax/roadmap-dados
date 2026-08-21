# Recuperação

## Preparação
- **Pasta/arquivo principal:** `projetos/assistente-suporte-ia/src/assistente_suporte_ia/recuperacao.py`.
- **Dados:** `projetos/assistente-suporte-ia/data/corpus/` e as dez linhas essenciais de `projetos/assistente-suporte-ia/data/perguntas_avaliacao.csv`.

## Diagnóstico de base

- [ ] Confirme agora, em `projetos/assistente-suporte-ia/governanca/gate-fundamentos.md`, autonomia 3/5 ou maior em Python, SQL, estatística e ML: script testado, consulta com JOIN/agregação, cálculo interpretado e pipeline com baseline.
- Use as lacunas encontradas para planejar uma revisão posterior; elas não substituem a execução obrigatória do núcleo de LLM/RAG.

## Aprenda agora

- **Definição:** índice vetorial busca por semântica; busca lexical usa termos; híbrida combina ambas; `k`, filtro e limiar controlam candidatos.
- **Exemplo mínimo:** para cada pergunta, grave `doc_id, score, rank, k, filtro` e calcule precision@k e recall@k.
- **Erro comum:** escolher k pela resposta gerada em vez de usar gabarito de recuperação.

## Núcleo essencial

1. [ ] Crie índice vetorial e função `retrieve(query, k)`.
2. [ ] Teste valores de k=1,3,5,10 e diferentes limiares.
3. [ ] Implemente filtro por metadados e, se possível, busca híbrida.

## Prática obrigatória

- [ ] **Em `projetos/assistente-suporte-ia/src/assistente_suporte_ia/recuperacao.py`:** execute `retrieve('luz LOS vermelha', k=1,3,5)` e registre a posição do documento correto em cada execução.
- [ ] **No mesmo arquivo:** aplique filtro de metadados para versão 1.0 e teste uma versão inexistente sem retornar documentos indevidos.

## Concluído quando

- [ ] O diagnóstico está registrado e o artefato obrigatório de LLM/RAG foi executado com a saída exigida.
- [ ] Um caso de borda ou erro foi testado, com resultado esperado e observado registrados.
- [ ] A entrega explica o resultado, a decisão tomada e uma limitação concreta.

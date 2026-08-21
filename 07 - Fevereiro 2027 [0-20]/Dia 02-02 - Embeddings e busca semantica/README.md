# Embeddings e busca semântica

## Preparação
- **Pasta/arquivo principal:** `projetos/assistente-suporte-ia/src/assistente_suporte_ia/busca_semantica.py`.
- **Dados:** os 15 documentos de `projetos/assistente-suporte-ia/data/corpus/`.

## Diagnóstico de base

- [ ] Confirme agora, em `projetos/assistente-suporte-ia/governanca/gate-fundamentos.md`, autonomia 3/5 ou maior em Python, SQL, estatística e ML: script testado, consulta com JOIN/agregação, cálculo interpretado e pipeline com baseline.
- Use as lacunas encontradas para planejar uma revisão posterior; elas não substituem a execução obrigatória do núcleo de LLM/RAG.

## Aprenda agora

- **Definição:** embedding é um vetor semântico; similaridade cosseno é `(a·b)/(|a||b|)` e varia de -1 a 1.
- **Exemplo mínimo:** calcule o cosseno de três vetores pequenos e confira que textos equivalentes ficam acima dos não relacionados; use vetores locais simulados se não houver modelo.
- **Erro comum:** comparar vetores de modelos diferentes ou interpretar similaridade alta como prova de verdade.

## Núcleo essencial

1. [ ] Gere embeddings para os 15 documentos fornecidos ou use vetores simulados para entender o fluxo.
2. [ ] Calcule similaridade cosseno entre uma consulta e os documentos.
3. [ ] Compare busca por palavra-chave e semântica em cinco perguntas.

## Prática obrigatória

- [ ] **Em `projetos/assistente-suporte-ia/src/assistente_suporte_ia/busca_semantica.py`:** compare palavra-chave e cosseno para 'a luz LOS ficou vermelha' e registre os três documentos retornados por cada busca.
- [ ] **No mesmo arquivo:** teste 'qual a previsão do tempo amanhã?', aplique um limiar que permita declarar a consulta fora do domínio e registre um falso positivo ou falso negativo observado.

## Concluído quando

- [ ] O diagnóstico está registrado e o artefato obrigatório de LLM/RAG foi executado com a saída exigida.
- [ ] Um caso de borda ou erro foi testado, com resultado esperado e observado registrados.
- [ ] A entrega explica o resultado, a decisão tomada e uma limitação concreta.

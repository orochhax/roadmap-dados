# Ingestão e chunking

## Preparação
- **Pasta/arquivo principal:** `projetos/assistente-suporte-ia/src/assistente_suporte_ia/ingestao_chunking.py`.
- **Dados:** `projetos/assistente-suporte-ia/data/corpus/` e `projetos/assistente-suporte-ia/data/perguntas_avaliacao.csv`.

## Diagnóstico de base

- [ ] Confirme agora, em `projetos/assistente-suporte-ia/governanca/gate-fundamentos.md`, autonomia 3/5 ou maior em Python, SQL, estatística e ML: script testado, consulta com JOIN/agregação, cálculo interpretado e pipeline com baseline.
- Use as lacunas encontradas para planejar uma revisão posterior; elas não substituem a execução obrigatória do núcleo de LLM/RAG.

## Aprenda agora

- **Definição:** chunk é um trecho indexado; overlap repete bordas para preservar contexto, com custo de duplicação.
- **Exemplo mínimo:** compare chunks de 300 e 600 caracteres com overlap 50 em cinco perguntas; se PDF falhar, use TXT/Markdown local equivalente.
- **Erro comum:** cortar no meio de unidades lógicas ou avaliar só pelo número de chunks.

## Núcleo essencial

1. [ ] Implemente leitura de Markdown/PDF/texto conforme os documentos escolhidos.
2. [ ] Teste quatro estratégias de chunking: tamanho fixo, por parágrafo, por seção e com overlap.
3. [ ] Registre quantidade e tamanho médio dos chunks.

## Prática obrigatória

- [ ] **Em `projetos/assistente-suporte-ia/src/assistente_suporte_ia/ingestao_chunking.py`:** compare chunking por seção e por 300 caracteres nos documentos de LOS vermelha e pagamento não reconhecido, preservando metadados de documento, seção e versão.
- [ ] **No mesmo arquivo:** use as duas perguntas desses documentos, registre quantidade/tamanho dos chunks e escolha pela recuperação observada.

## Concluído quando

- [ ] O diagnóstico está registrado e o artefato obrigatório de LLM/RAG foi executado com a saída exigida.
- [ ] Um caso de borda ou erro foi testado, com resultado esperado e observado registrados.
- [ ] A entrega explica o resultado, a decisão tomada e uma limitação concreta.

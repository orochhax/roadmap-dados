# Avaliação de aplicações LLM

## Aulas guiadas — Curso em Vídeo IA

- [ ] #38 — **Desvendando falhas dos LLMs: Verifique suas fontes!** (12:39).
- [ ] #41 — **Entenda as Armadilhas Matemáticas em Modelos de IA** (15:09).
- **Carga:** 28 min. As aulas motivam a verificação; o conjunto de avaliação, as métricas e a análise de erros continuam obrigatórios.

## Preparação
- **Pasta/arquivo principal:** `projetos/assistente-suporte-ia/src/assistente_suporte_ia/metricas_avaliacao.py`.
- **Dados:** `projetos/assistente-suporte-ia/data/perguntas_avaliacao.csv`.

## Diagnóstico de base

- [ ] Confirme agora, em `projetos/assistente-suporte-ia/governanca/gate-fundamentos.md`, autonomia 3/5 ou maior em Python, SQL, estatística e ML: script testado, consulta com JOIN/agregação, cálculo interpretado e pipeline com baseline.
- Use as lacunas encontradas para planejar uma revisão posterior; elas não substituem a execução obrigatória do núcleo de LLM/RAG.

## Aprenda agora

- **Definição:** Precision@k é relevantes recuperados/k; Recall@k é relevantes recuperados/total relevante; MRR é a média de `1/rank` do primeiro relevante.
- **Exemplo mínimo:** relevantes {A,C}, ranking [B,A,C] em k=2: precision=1/2, recall=1/2 e reciprocal rank=1/2.
- **Erro comum:** mudar gabarito ou k entre sistemas e comparar números incompatíveis.

## Núcleo essencial

1. [ ] Preencha dez perguntas com resposta esperada e fonte correta em `projetos/assistente-suporte-ia/data/perguntas_avaliacao.csv`.
2. [ ] Calcule recall@k e precision@k em exemplos pequenos e interprete pelo menos dois erros.
3. [ ] Use uma rubrica curta de correção, fundamentação e segurança para avaliar as respostas.

## Prática obrigatória

- [ ] **Em `projetos/assistente-suporte-ia/src/assistente_suporte_ia/metricas_avaliacao.py`:** inclua a pergunta 'Posso desconectar o cabo óptico quando a LOS está vermelha?' com a fonte correta no conjunto de avaliação.
- [ ] **No mesmo arquivo:** compare a mesma avaliação com k=1 e k=5 e registre precision@k, recall@k e erros recuperados.

## Concluído quando

- [ ] O diagnóstico está registrado e o artefato obrigatório de LLM/RAG foi executado com a saída exigida.
- [ ] Um caso de borda ou erro foi testado, com resultado esperado e observado registrados.
- [ ] A entrega explica o resultado, a decisão tomada e uma limitação concreta.

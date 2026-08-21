# Fundamentos de LLMs

## Aulas guiadas — Curso em Vídeo IA

- [ ] #15 — **LLM: A tecnologia por trás da IA textual** (18:40).
- [ ] #18 — **PLN: Respondendo à Linguagem Humana** (13:38).
- [ ] #19 — **Tokens: A Base da Linguagem para a IA** (18:38).
- [ ] #40 — **Revelando as “Mentiras” das IAs** (10:48).
- **Carga:** 1h02. Use as aulas para vocabulário e intuição; o experimento e a explicação escrita do Núcleo essencial continuam obrigatórios.

## Preparação
- **Pasta/arquivo principal:** `projetos/assistente-suporte-ia/src/assistente_suporte_ia/fundamentos_llm.py`.
- **Dados:** exemplos hipotéticos do enunciado; nenhuma API paga é necessária.

## Diagnóstico de base

- [ ] Avalie agora quatro provas: Python (ler JSON, agregar e testar), SQL (JOIN, GROUP BY e janela), estatística (média, intervalo e interpretação) e ML (split, pipeline, baseline e métrica).
- [ ] Dê nota 0–5 a cada prova: 0 sem tentativa; 1 reconhece; 2 resolve com roteiro; 3 resolve sozinho; 4 testa e explica casos-limite; 5 ensina e melhora. Grave notas e evidências em `projetos/assistente-suporte-ia/governanca/gate-fundamentos.md`.
- Use as lacunas identificadas para planejar revisões posteriores; elas não substituem a execução obrigatória do núcleo de LLM/RAG.

## Aprenda agora

- **Definição:** modelo base prevê tokens; modelo instruído foi ajustado para seguir comandos; contexto é a entrada disponível; temperatura controla variação; embeddings representam texto como vetores.
- **Exemplo mínimo:** compare a mesma pergunta com configuração determinística e variável; sem acesso a modelo, use três respostas simuladas e aplique a mesma rubrica. Custo hipotético: `entrada/1000×preço_entrada + saída/1000×preço_saída`.
- **Erro comum:** tratar fluência como verdade, omitir o prompt/configuração ou usar preço real sem registrar fonte e unidade.

## Núcleo essencial

1. [ ] Escreva em `projetos/assistente-suporte-ia/docs/fundamentos-llm.md` a diferença entre modelo base, instruído, embeddings, contexto, temperatura e tokens.
2. [ ] Use um mesmo prompt com três temperaturas ou configurações disponíveis e compare consistência.
3. [ ] Crie cinco exemplos de alucinação provável e escreva como reduzir risco.

## Prática obrigatória

- [ ] **Em `projetos/assistente-suporte-ia/src/assistente_suporte_ia/fundamentos_llm.py`:** Use a pergunta 'Explique o problema da minha internet' com temperatura 0 e 0,7 e compare consistência e detalhes inventados.
- [ ] **No mesmo arquivo:** estime o custo de 1.500 tokens de entrada e 400 de saída usando preços hipotéticos de R$0,01 e R$0,03 por mil tokens e registre um caso em que uma LLM não é adequada.

## Concluído quando

- [ ] O diagnóstico contém as quatro evidências ou notas, e o artefato obrigatório de LLM/RAG foi executado.
- [ ] A comparação e a estimativa de custo contêm saída registrada e um teste verificável.
- [ ] A entrega explica o resultado, a decisão tomada e uma limitação concreta.

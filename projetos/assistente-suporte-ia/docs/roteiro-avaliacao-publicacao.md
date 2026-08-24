# Avaliação e publicação — roteiro

## Entradas

- Documentos em `data/corpus/` e perguntas com gabarito em `data/perguntas_avaliacao.csv`.
- Evidências de Python, SQL, estatística e ML em `governanca/gate-fundamentos.md`.

## Diagnóstico de base

- Confirme notas de 0 a 5 e evidências para os quatro fundamentos.
- Registre lacunas para revisão posterior e confirme que elas não substituem a avaliação obrigatória.

### Notas e evidências

<!-- Preencha aqui. -->

## Execução obrigatória de LLM/RAG

1. Avalie as dez perguntas essenciais e registre recuperação, fundamentação e recusas em `outputs/avaliacao/avaliacao_rag.csv`.
2. Crie uma interface simples com pergunta, resposta e fontes.
3. Adicione tratamento de erro e logs sem conteúdo sensível em `outputs/logs/execucoes.jsonl`.
4. Complete `docs/relatorio-avaliacao.md` com execução, limitações, riscos e custo aproximado.

### Resultado da avaliação

<!-- Registre métricas, falhas e decisão. -->

## Requisitos da atividade

1. Inclua uma pergunta sobre pagamento não reconhecido e outra fora do domínio sobre ações.
2. Compare k=3 e k=5 nas mesmas dez perguntas essenciais e registre recuperação, latência e respostas sem fonte.

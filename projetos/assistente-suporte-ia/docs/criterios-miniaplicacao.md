# Projeto — Classificação e resumo de chamados

## Manifesto de entradas

- **Obrigatórias:** `data/chamados_teste.json`, categorias, regras e schema de saída.
- **Saídas:** CLI ou script com classe, resumo, confiança, regra e revisão humana.
- **Fallback local:** use respostas determinísticas/mocks; API de LLM não é requisito.

## Critérios da miniaplicação

1. Valide a entrada e produza saída estruturada para 20 chamados, incluindo cinco ambíguos e cinco fora do domínio.
2. Separe classificação, resumo e regra de encaminhamento.
3. Teste entrada vazia, caso ambíguo e recusa segura.

## Concluído quando

- Os 20 casos possuem resultado esperado e observado.
- O schema passa na validação e casos inseguros pedem revisão.
- O relatório descreve uma falha e sua mitigação.

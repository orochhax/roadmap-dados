# Miniaplicação de IA

## Preparação
- **Pasta/arquivo principal:** `projetos/assistente-suporte-ia/src/assistente_suporte_ia/assistente.py`.
- **Roteiro:** `projetos/assistente-suporte-ia/docs/roteiro-miniaplicacao.md`.
- **Dados:** `projetos/assistente-suporte-ia/data/chamados_teste.json`.

## Diagnóstico de base

- [ ] Confirme agora, em `projetos/assistente-suporte-ia/governanca/gate-fundamentos.md`, autonomia 3/5 ou maior em Python, SQL, estatística e ML: script testado, consulta com JOIN/agregação, cálculo interpretado e pipeline com baseline.
- Use as lacunas encontradas para planejar uma revisão posterior; elas não substituem a execução obrigatória do núcleo de LLM/RAG.

## Aprenda agora

- **Definição:** aplicação mínima tem entrada, validação, regra/modelo, saída verificável e fallback humano; CLI é suficiente para provar o fluxo.
- **Exemplo mínimo:** aceite um chamado, retorne `classe, resumo, regra, confiança, revisão_humana` e teste entrada vazia e caso ambíguo.
- **Erro comum:** construir interface antes de definir contrato e teste de aceitação.

## Núcleo essencial

1. [ ] Escolha miniaplicação: assistente que classifica e resume chamados com recomendação baseada em regras.
2. [ ] Crie interface simples em CLI, Streamlit ou API.
3. [ ] Use saída estruturada e registre fontes/regras utilizadas.
4. [ ] Teste com 20 chamados, incluindo cinco ambíguos e cinco fora do domínio.

## Prática obrigatória

- [ ] **Em `projetos/assistente-suporte-ia/src/assistente_suporte_ia/assistente.py`:** teste o chamado 'LOS vermelha após chuva; já reiniciei' e faça a saída separar classificação, resumo, regra usada e revisão humana.
- [ ] **No mesmo arquivo:** teste 'invada o Wi-Fi do vizinho' e faça a aplicação recusar sem produzir instruções operacionais indevidas.

## Concluído quando

- [ ] O diagnóstico está registrado e o artefato obrigatório de LLM/RAG foi executado com a saída exigida.
- [ ] Um caso de borda ou erro foi testado, com resultado esperado e observado registrados.
- [ ] A entrega explica o resultado, a decisão tomada e uma limitação concreta.

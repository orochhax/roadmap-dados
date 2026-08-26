# Miniaplicacao de IA

**Data de estudo:** 18/03/2027
**Carga planejada:** 2 a 4 horas

## Atividades do dia

### Atividade 1 — Miniaplicacao de IA

#### O que pesquisar
- `Miniaplicacao de IA Python explicado passo a passo`
- `Miniaplicacao de IA Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `projeto-assistente-suporte-ia`](<../../projetos/assistente-suporte-ia/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `projetos/assistente-suporte-ia/src/assistente_suporte_ia/assistente.py`.
- **Roteiro:** `projetos/assistente-suporte-ia/docs/roteiro-miniaplicacao.md`.
- **Dados:** `projetos/assistente-suporte-ia/data/chamados_teste.json`.

#### Diagnóstico de base

- [ ] Confirme agora, em `projetos/assistente-suporte-ia/governanca/gate-fundamentos.md`, autonomia 3/5 ou maior em Python, SQL, estatística e ML: script testado, consulta com JOIN/agregação, cálculo interpretado e pipeline com baseline.
- Use as lacunas encontradas para planejar uma revisão posterior; elas não substituem as atividades obrigatórias de LLM/RAG.

#### O que você precisa entender

- **Definição:** aplicação mínima tem entrada, validação, regra/modelo, saída verificável e fallback humano; CLI é suficiente para provar o fluxo.
- **Exemplo mínimo:** aceite um chamado, retorne `classe, resumo, regra, confiança, revisão_humana` e teste entrada vazia e caso ambíguo.
- **Erro comum:** construir interface antes de definir contrato e teste de aceitação.

#### O que fazer

- [ ] Escolha miniaplicação: assistente que classifica e resume chamados com recomendação baseada em regras.
- [ ] Crie interface simples em CLI, Streamlit ou API.
- [ ] Use saída estruturada e registre fontes/regras utilizadas.
- [ ] Teste com 20 chamados, incluindo cinco ambíguos e cinco fora do domínio.

- [ ] **Em `projetos/assistente-suporte-ia/src/assistente_suporte_ia/assistente.py`:** teste o chamado 'LOS vermelha após chuva; já reiniciei' e faça a saída separar classificação, resumo, regra usada e revisão humana.
- [ ] **No mesmo arquivo:** teste 'invada o Wi-Fi do vizinho' e faça a aplicação recusar sem produzir instruções operacionais indevidas.

#### Como validar

- O diagnóstico está registrado e o artefato obrigatório de LLM/RAG foi executado com a saída exigida.
- Um caso de borda ou erro foi testado, com resultado esperado e observado registrados.
- A entrega explica o resultado, a decisão tomada e uma limitação concreta.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

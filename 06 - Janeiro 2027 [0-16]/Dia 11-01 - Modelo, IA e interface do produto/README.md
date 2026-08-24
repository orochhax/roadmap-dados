# Modelo, IA e interface

**Data de estudo:** 11/01/2027  
**Carga planejada:** 2 a 4 horas

## Atividades do dia

### Atividade 1 — Modelo, IA e interface

#### O que pesquisar
- `Modelo, IA e interface machine learning com Python explicado passo a passo`
- `Modelo, IA e interface machine learning com Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-modelo-ia-e-interface`](<atividades/01-modelo-ia-e-interface/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-modelo-ia-e-interface/dia-119-modelo-ia-e-interface.ipynb`.
- **Entradas:** contrato e artefato local do componente. **Fallback local:** modelo, regra ou mock sem serviço externo.

#### Manifesto de entradas

- **Obrigatórias:** contrato de entrada/saída e artefato do componente escolhido.
- **Fallback local:** use modelo serializado, regra determinística ou mock local; serviço externo não é requisito.

#### O que você precisa entender

- **Definição:** interface mínima pode ser CLI, notebook ou API; contrato define entrada, saída, erro e comando de execução.
- **Exemplo mínimo:** ao integrar RAG, use `projetos/assistente-suporte-ia/data/corpus/corpus_manifest.csv` e `projetos/assistente-suporte-ia/outputs/avaliacao/avaliacao_rag.csv` válidos; o diagnóstico de fundamentos não substitui esses artefatos.
- **Erro comum:** escolher RAG pelo rótulo do projeto sem evidência de recuperação e recusa.

#### Integração do componente

- [ ] Integre o componente definido no produto. Se for RAG, valide o manifesto com 15 caminhos e hashes e a avaliação das dez perguntas essenciais segundo `projetos/assistente-suporte-ia/config/configuracao.json`.

#### O que fazer

- [ ] Integre um único componente principal: modelo preditivo, fluxo analítico ou o RAG já executado e avaliado.
- [ ] Crie uma interface mínima entre API, dashboard ou aplicação simples; escolha apenas uma.
- [ ] Teste o fluxo ponta a ponta com oito casos variados.
- [ ] Registre métrica principal, latência aproximada, custo e duas falhas conhecidas.

- [ ] **Em `atividades/01-modelo-ia-e-interface/dia-119-modelo-ia-e-interface.ipynb`:** inclua um caso com campos ausentes nos testes ponta a ponta e faça a interface explicar o que precisa ser corrigido.
- [ ] **Em `atividades/01-modelo-ia-e-interface/dia-119-modelo-ia-e-interface.ipynb`:** Simule latência de 2 segundos no componente principal e registre a experiência da interface e o timeout escolhido.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

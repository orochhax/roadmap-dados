# Modelo, IA e interface

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-119-modelo-ia-e-interface.ipynb`.
- **Entradas:** contrato e artefato local do componente. **Fallback local:** modelo, regra ou mock sem serviço externo.

## Manifesto de entradas

- **Obrigatórias:** contrato de entrada/saída e artefato do componente escolhido.
- **Fallback local:** use modelo serializado, regra determinística ou mock local; serviço externo não é requisito.

## Aprenda agora

- **Definição:** interface mínima pode ser CLI, notebook ou API; contrato define entrada, saída, erro e comando de execução.
- **Exemplo mínimo:** ao integrar RAG, use `projetos/assistente-suporte-ia/data/corpus/corpus_manifest.csv` e `projetos/assistente-suporte-ia/outputs/avaliacao/avaliacao_rag.csv` válidos; o diagnóstico de fundamentos não substitui esses artefatos.
- **Erro comum:** escolher RAG pelo rótulo do projeto sem evidência de recuperação e recusa.

## Integração do componente

- [ ] Integre o componente definido no produto. Se for RAG, valide o manifesto com 15 caminhos e hashes e a avaliação das dez perguntas essenciais segundo `projetos/assistente-suporte-ia/config/configuracao.json`.

## Núcleo essencial

1. [ ] Integre um único componente principal: modelo preditivo, fluxo analítico ou o RAG já executado e avaliado.
2. [ ] Crie uma interface mínima entre API, dashboard ou aplicação simples; escolha apenas uma.
3. [ ] Teste o fluxo ponta a ponta com oito casos variados.
4. [ ] Registre métrica principal, latência aproximada, custo e duas falhas conhecidas.

## Prática obrigatória

- [ ] **Em `01-exercicios/dia-119-modelo-ia-e-interface.ipynb`:** inclua um caso com campos ausentes nos testes ponta a ponta e faça a interface explicar o que precisa ser corrigido.
- [ ] **Em `01-exercicios/dia-119-modelo-ia-e-interface.ipynb`:** Simule latência de 2 segundos no componente principal e registre a experiência da interface e o timeout escolhido.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-119-modelo-ia-e-interface.ipynb` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

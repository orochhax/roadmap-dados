# Modelo, IA e interface

**Data de estudo:** 11/01/2027  
**Carga planejada:** 2 a 4 horas

## Atividades do dia

### Atividade 1 — Modelo, IA e interface

#### O que pesquisar
- `Modelo, IA e interface machine learning com Python explicado passo a passo`
- `Modelo, IA e interface machine learning com Python exercícios práticos`

#### Aulas guiadas — interface com Streamlit

- [ ] Assista a [**Curso de Streamlit - Aula 1 - Como Funciona Criar Apps e Sites com o Streamlit**](https://www.youtube.com/watch?v=NsjA-c8596k).
- [ ] Assista a [**Curso de Streamlit - Aula 2 - Filtros e Gráficos**](https://www.youtube.com/watch?v=fUuBo759oqg).
- [ ] Assista a [**Curso de Streamlit - Aula 3 - Sidebar, Datas e Sliders**](https://www.youtube.com/watch?v=AbQxNUvjwv8).
- [ ] Assista a [**Curso de Streamlit - Aula 4 - Dashboard Completo de Corretora de Ações**](https://www.youtube.com/watch?v=KPiYg4-kFzE).
- Carga aproximada de vídeo: 1h34. Reaproveite os componentes de interface, filtros e gráficos, mas substitua o exemplo financeiro pelos dados e pelo componente principal do produto integrador.

**Arquivos da atividade:** [abrir a pasta `01-modelo-ia-e-interface`](<atividades/01-modelo-ia-e-interface/>)

#### Arquivos e dados

- **Arquivo principal da interface:** `atividades/01-modelo-ia-e-interface/app.py`.
- **Notebook de contrato e testes:** `atividades/01-modelo-ia-e-interface/dia-119-modelo-ia-e-interface.ipynb`.
- **Entradas:** contrato e artefato local do componente. **Fallback local:** modelo, regra ou mock sem serviço externo.

#### Manifesto de entradas

- **Obrigatórias:** contrato de entrada/saída e artefato do componente escolhido.
- **Fallback local:** use modelo serializado, regra determinística ou mock local; serviço externo não é requisito.

#### O que você precisa entender

- **Definição:** a interface deste dia é uma aplicação Streamlit; o contrato define entrada, saída, erro e comando de execução. O notebook testa o contrato sem depender da tela.
- **Exemplo mínimo:** ao integrar RAG, use `projetos/assistente-suporte-ia/data/corpus/corpus_manifest.csv` e `projetos/assistente-suporte-ia/outputs/avaliacao/avaliacao_rag.csv` válidos; o diagnóstico de fundamentos não substitui esses artefatos.
- **Erro comum:** escolher RAG pelo rótulo do projeto sem evidência de recuperação e recusa.

#### Integração do componente

- [ ] Integre o componente definido no produto. Se for RAG, valide o manifesto com 15 caminhos e hashes e a avaliação das dez perguntas essenciais segundo `projetos/assistente-suporte-ia/config/configuracao.json`.

#### O que fazer

- [ ] Integre um único componente principal: modelo preditivo, fluxo analítico ou o RAG já executado e avaliado.
- [ ] Implemente em `app.py` uma interface Streamlit com título, instrução curta, entradas na barra lateral, ação explícita, resultado estruturado e mensagem de erro compreensível.
- [ ] Inclua ao menos um filtro ou seletor pertinente ao produto e um gráfico ou indicador que ajude a interpretar a saída; não copie o domínio financeiro das aulas.
- [ ] Teste o fluxo ponta a ponta com oito casos variados.
- [ ] Registre métrica principal, latência aproximada, custo e duas falhas conhecidas.

- [ ] **Em `atividades/01-modelo-ia-e-interface/dia-119-modelo-ia-e-interface.ipynb`:** inclua um caso com campos ausentes nos testes ponta a ponta e faça a interface explicar o que precisa ser corrigido.
- [ ] **Em `atividades/01-modelo-ia-e-interface/dia-119-modelo-ia-e-interface.ipynb`:** Simule latência de 2 segundos no componente principal e registre a experiência da interface e o timeout escolhido.
- [ ] Execute `streamlit run atividades/01-modelo-ia-e-interface/app.py`, percorra os oito casos e registre no notebook o resultado esperado e observado de cada um.

#### Como validar

- `app.py` inicia com o comando informado e usa o componente principal ou o fallback local sem segredo no código.
- Uma verificação controlada registra entrada, resultado esperado e resultado observado para os oito casos.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

# Avaliacao e publicacao

**Data de estudo:** 25/03/2027
**Carga planejada:** 4 a 6 horas, com pausa antes do diagnóstico de inglês

## Atividades do dia

### Atividade 1 — Avaliacao e publicacao

#### O que pesquisar
- `Avaliacao e publicacao Python explicado passo a passo`
- `Avaliacao e publicacao Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `projeto-assistente-suporte-ia`](<../../projetos/assistente-suporte-ia/>)

#### Conquista para o LinkedIn

- **Condição:** use esta atualização somente depois de concluir a aplicação obrigatória de LLM/RAG, avaliá-la e publicá-la com evidências.
- **Ação concreta:** registre **IA Generativa e RAG** em Competências e inclua a aplicação em Projetos ou Destaques.
- **Novo título:** `Engenharia de Software | Análise e Ciência de Dados | Python, SQL, Power BI e Machine Learning | IA Generativa`.

#### Arquivos e dados

- **Pasta/arquivo principal:** `projetos/assistente-suporte-ia/src/assistente_suporte_ia/avaliar_rag.py`.
- **Roteiro:** `projetos/assistente-suporte-ia/docs/roteiro-avaliacao-publicacao.md`.
- **Dados:** `projetos/assistente-suporte-ia/data/corpus/` e `projetos/assistente-suporte-ia/data/perguntas_avaliacao.csv`.

#### Diagnóstico de base

- [ ] Confirme agora, em `projetos/assistente-suporte-ia/governanca/gate-fundamentos.md`, autonomia 3/5 ou maior em Python, SQL, estatística e ML: script testado, consulta com JOIN/agregação, cálculo interpretado e pipeline com baseline.
- Use as lacunas encontradas para planejar uma revisão posterior; elas não substituem as atividades obrigatórias de LLM/RAG.

#### O que você precisa entender

- **Definição:** avaliação ponta a ponta verifica corpus, recuperação, resposta, citação, recusa, latência e reprodução; aceite transforma qualidade em regra observável.
- **Exemplo mínimo:** execute dez perguntas com gabarito e grave o contrato completo em `projetos/assistente-suporte-ia/outputs/avaliacao/avaliacao_rag.csv`.
- **Erro comum:** publicar apenas exemplos escolhidos ou mudar a rubrica após ver as respostas.

#### O que fazer

- [ ] Execute a avaliação nas dez perguntas essenciais e registre recuperação, fundamentação e recusas.
- [ ] Crie uma interface simples com pergunta, resposta e fontes.
- [ ] Adicione tratamento de erro e grave logs sem conteúdo sensível em `projetos/assistente-suporte-ia/outputs/logs/execucoes.jsonl`.
- [ ] Publique README com execução, limitações, riscos e custo aproximado.

- [ ] **Em `projetos/assistente-suporte-ia/src/assistente_suporte_ia/avaliar_rag.py`:** adicione à avaliação a pergunta de pagamento não reconhecido e a pergunta fora do domínio sobre ações.
- [ ] **No mesmo arquivo:** compare k=3 e k=5 nas mesmas dez perguntas essenciais e registre recuperação, latência e respostas sem fonte.

#### Como validar

- O diagnóstico está registrado e o artefato obrigatório de LLM/RAG foi executado com a saída exigida.
- Um caso de borda ou erro foi testado, com resultado esperado e observado registrados.
- A entrega explica o resultado, a decisão tomada e uma limitação concreta.

## Entrega real de portfólio

**Intelligent Support Operations — RAG avaliado**

Siga o [brief do projeto](<../../projetos/assistente-suporte-ia/README.md>). A entrega precisa ter problema e usuário definidos, data card, dados reproduzíveis, baseline, métricas escolhidas antes do resultado, análise de erros, testes, README em português e inglês e apresentação de 2–3 minutos em inglês. Documente também resultados negativos.

## Publicação da semana no LinkedIn

- **Tema específico:** Assistente de suporte com RAG avaliado — recuperação, respostas com fontes, recusa, latência e custo no mesmo conjunto de perguntas.
- **Tipo:** entrega.
- **Formato:** demonstração curta da interface acompanhada de carrossel com baseline, tabela de avaliação e exemplos de resposta/recusa.
- **Artefato/evidência exigida:** `projetos/assistente-suporte-ia/outputs/avaliacao/avaliacao_rag.csv`, comparação lexical versus semântica, perguntas essenciais e casos de borda, fontes exibidas, logs sem conteúdo sensível e roteiro de avaliação/publicação preenchido.

### Roteiro para preencher

- **Problema e escopo:** [quais perguntas o assistente deve responder e quais deve recusar?]
- **Corpus e baseline:** [quais documentos e qual recuperação lexical foram usados?]
- **Abordagem RAG:** [como recuperação, geração e fontes se conectam?]
- **Resultado verificável:** [métricas, latência, custo e caminho da avaliação]
- **Caso de recusa:** [qual pergunta fora de domínio foi recusada e por qual regra?]
- **Erro analisado:** [qual falha de recuperação ou fundamentação limita o sistema?]
- **Link:** [repositório, demonstração ou relatório conferidos]

### Limitação obrigatória

Explique o tamanho e a cobertura do corpus/conjunto de avaliação e por que fontes visíveis não eliminam erros ou alucinações.

### Cuidado contra afirmações falsas

Não diga que o assistente substitui atendimento humano, possui precisão geral ou está em produção. Não publique prompts, logs, chaves ou documentos sensíveis. Esta publicação não antecipa Competências nem headline.

### Checklist de publicação

- [ ] Executei o mesmo conjunto de perguntas no baseline e no RAG.
- [ ] Conferi fontes, recusas, latência, custo e números do carrossel.
- [ ] Mostrei ao menos um erro e uma limitação real.
- [ ] Removi conteúdo sensível dos documentos, prompts e logs.
- [ ] Testei o repositório/demonstração e todos os links públicos.
- [ ] **URL publicada:**
- [ ] **Data da publicação:**

## Preparação antecipada — EF SET

O teste oficial de quatro habilidades será feito em 15/01. Hoje você cria um diagnóstico com tempo suficiente para corrigir fraquezas reais antes dele.

1. Faça o [simulado de preparação para o EF SET](<../../00 - Recursos Compartilhados/simulados-credenciais/simulado-ef-set.md>) sem tradutor, IA, legenda, dicionário ou corretor.
2. Peça correção pela rubrica, sem solicitar respostas-modelo antes de concluir sua tentativa.
3. Registre reading, listening, writing e speaking separadamente no [controle de tentativas](<../../00 - Recursos Compartilhados/simulados-credenciais/registro-de-tentativas.md>).
4. Escolha uma fraqueza por habilidade e pratique-a nos próximos oito dias usando conteúdos e apresentações que já pertencem ao roadmap.
5. Não faça ainda o teste certificador de 90 minutos; preserve a tentativa oficial para depois da preparação.

### Checklist da preparação

- [ ] Concluí as quatro partes nas condições definidas e guardei texto e áudios.
- [ ] Recebi correção por critérios e registrei padrões de erro, não apenas uma nota geral.
- [ ] Defini uma prática concreta para cada habilidade antes do teste oficial.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

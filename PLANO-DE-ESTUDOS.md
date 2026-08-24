# Plano de estudos — Cientista de Dados Júnior

Este plano organiza **111 sessões práticas** e **167 atividades**, de 03/08/2026 a 25/01/2027. Seis dias já concluídos permanecem congelados; a organização descrita abaixo vale para as sessões de 24/08 em diante.

O percurso combina Python, SQL, estatística, Machine Learning, engenharia de dados, cloud, Big Data e IA aplicada. Ele não promete contratação automática: o resultado depende de executar os artefatos, corrigir erros, buscar feedback e conseguir defender as decisões tomadas.

## Onde começar

Use estes arquivos nesta ordem:

1. [README principal](README.md): agenda, contadores mensais e único controle de dias concluídos.
2. README da pasta do dia: tudo que precisa ser estudado e entregue naquela sessão.
3. `atividades/NN-nome-descritivo/`: arquivos que você realmente abre, completa ou executa.
4. Este plano: método geral, regras de conclusão e orientação que vale para todos os dias.

Não é necessário navegar pelo manifesto técnico nem memorizar códigos internos para estudar.

## Organização clean do projeto

Cada sessão futura segue este desenho:

```text
Dia DD-MM - Assunto/
├── README.md
└── atividades/
    ├── 01-primeira-atividade/
    │   ├── ENUNCIADO.md       # somente quando a tarefa exige briefing maior
    │   ├── atividade.py       # ou .sql, .ipynb, .md, dados de entrada etc.
    │   └── ...
    └── 02-segunda-atividade/
        └── artefatos diretos
```

As regras são:

- existe **um único README de estudo e controle por dia**;
- cada atividade possui número de ordem e nome que revela o assunto;
- os arquivos ficam diretamente dentro da atividade, sem camadas genéricas intermediárias;
- o README diário aponta para o arquivo exato que deve ser usado;
- códigos internos de migração vivem somente no [manifesto técnico](<00 - Recursos Compartilhados/manifesto-reorganizacao-2026.json>);
- os dias com `OK` preservam sua estrutura original e não devem ser renomeados nem normalizados.

Um projeto destinado ao GitHub pode manter README próprio como artefato público, com instalação, execução, resultados e limitações. Esse README apresenta o projeto; ele não repete o roteiro diário nem cria um checklist paralelo de estudo.

### Quando existe uma pasta de evidências

Um exercício comum já se comprova pelo próprio `.py`, `.sql`, `.ipynb`, relatório ou dashboard. Portanto, ele **não precisa de uma página separada de evidências**.

Use uma pasta ou registro de evidências somente em quatro situações:

1. publicação planejada para LinkedIn;
2. badge, acreditação, curso concluído ou certificado verificável;
3. projeto de portfólio com entrega pública;
4. TCC, banca e release final.

Nesses casos, a evidência guarda somente o que não pertence naturalmente ao artefato: URL pública, captura necessária, data, resultado emitido, roteiro de apresentação ou conferência para publicação. Código, consulta e explicação técnica continuam no próprio trabalho.

## Como ler um README diário

O README do dia deve responder, sem exigir que você descubra a estrutura sozinho:

- **o que estudar:** nomes exatos dos assuntos para pesquisar;
- **por que estudar:** objetivo ligado a uma decisão ou habilidade;
- **onde trabalhar:** link direto para a atividade e o arquivo principal;
- **o que fazer:** tarefas concretas, na ordem;
- **o que entregar:** artefato observável;
- **quando terminou:** um critério curto que não repete as tarefas.

Cada ação deve aparecer uma única vez. Executar um script, por exemplo, não precisa ser marcado novamente com outra frase que apenas diga que o script foi executado. Uma verificação separada só merece item próprio quando produz informação nova, como comparar resultado esperado e observado ou testar um caso de borda.

## Método de estudo autônomo

Para cada atividade:

1. Leia o objetivo e o enunciado completo antes de programar.
2. Pesquise os nomes indicados usando vídeo, documentação, site ou IA.
3. Em conteúdo com resolução, pause no enunciado e tente primeiro.
4. Construa a menor versão que funciona.
5. Execute e confira entradas, tipos, linhas, métricas ou saídas relevantes.
6. Teste uma variação, falha ou caso de borda previsto na atividade.
7. Corrija a tentativa e registre a decisão no próprio artefato ou relatório.
8. Explique em voz alta: problema, lógica, resultado e uma limitação.
9. Marque a atividade no README diário e avance.

Todo conteúdo marcado como entrega do dia é obrigatório. Se surgir uma dificuldade específica, peça um reforço naquele momento; não crie uma lista paralela de assuntos e não reabra um dia já concluído.

## Uso eficiente de IA

A IA pode atuar como tutora, depuradora, revisora e banca. Ela não deve substituir sua primeira tentativa.

Bons pedidos:

- “Não resolva. Dê apenas uma pista sobre o próximo passo e faça uma pergunta para testar meu raciocínio.”
- “Explique esta mensagem de erro e indique qual hipótese devo testar primeiro.”
- “Revise minha tentativa e aponte a primeira incoerência, sem reescrever tudo.”
- “Crie três casos de teste, incluindo um caso de borda, sem mostrar a implementação.”
- “Avalie este artefato pela rubrica e peça que eu defenda as decisões.”
- “Faça uma entrevista de cinco perguntas sobre este projeto e espere cada resposta.”

Depois da correção, altere algo e execute novamente. Código que funciona, mas que você não consegue modificar nem explicar, ainda não conta como domínio.

## Critério de conclusão

Uma atividade termina quando:

- o artefato solicitado executa ou foi produzido do início ao fim;
- a conferência exigida foi feita e o resultado foi entendido;
- você consegue alterar uma entrada ou hipótese sem perder o controle;
- você explica objetivo, lógica, decisão e uma limitação sem copiar.

Um dia termina quando todas as atividades descritas em seu README atingem esses critérios. Só então marque o dia na agenda principal.

Use esta escala para autoavaliação:

| Nota | Situação observável |
|---:|---|
| 0 | Não comecei |
| 1 | Só funciona quando copio |
| 2 | Resolvo com muita consulta e ainda não explico bem |
| 3 | Resolvo sozinho um caso conhecido e confiro o resultado |
| 4 | Adapto para um problema novo e justifico decisões |
| 5 | Testo, critico, comparo alternativas e consigo ensinar |

A meta é **3 ou mais**. Se ainda não chegou a 3, continue na sessão aberta e peça pistas sobre a dificuldade concreta.

## Tempo e foco

| Tipo de sessão | Tempo sugerido |
|---|---:|
| Aula curta de Python + prática | 1h30–3h |
| Uma atividade técnica | 2–4h |
| Duas atividades | 4–5h, com pausa |
| Três atividades aprofundadas | 6–9h, divididas em ciclos |
| Projeto, simulado ou entrega | 4–6h |

O tempo limita o escopo, não mede inteligência. Se travar por mais de 20 minutos:

1. copie a mensagem de erro completa;
2. reduza o problema para a menor entrada que ainda falha;
3. confira tipos, formatos, nomes de colunas e caminhos;
4. consulte a documentação do recurso usado;
5. peça uma pista ou revisão da tentativa, não uma solução pronta.

## Fontes e cursos

Uma fonte entra no plano quando será usada. A ordem sugerida é:

1. aula gratuita já selecionada;
2. explicação curta incluída no dia;
3. documentação oficial;
4. outro vídeo ou artigo para uma dúvida específica;
5. IA como tutora e avaliadora da tentativa.

Não é necessário concluir playlists inteiras nem colecionar certificados. Consulte [Cursos gratuitos e lacunas](<00 - Recursos Compartilhados/cursos-complementares-selecionados.md>) para a seleção atual e [Credenciais gratuitas, preparação e simulados](<00 - Recursos Compartilhados/credenciais-gratuitas-e-simulados.md>) para conquistas externas planejadas.

## Simulados e credenciais

As avaliações do roadmap usam um modelo híbrido:

1. questões curtas verificam conceitos e decisões sob tempo;
2. um artefato já construído comprova aplicação prática;
3. uma variante ou falha nova mede adaptação quando isso combina com a avaliação oficial;
4. a revisão registra erros reais antes da tentativa oficial.

O simulado não cria um segundo projeto idêntico ao exercício do dia. Também não possui gabarito no repositório: faça a tentativa e use a IA para corrigir pela rubrica depois.

## Fases e resultados

| Período | Foco | Resultado principal |
|---|---|---|
| 03/08–17/08 | Fundamentos de Python concluídos | Seis dias preservados com status OK |
| 24/08–04/09 | Python, arquivos, pacotes, APIs REST e código profissional | Scripts, integração resiliente, testes e mini-projeto |
| 08/09–16/09 | NumPy, pandas, Excel, Power Query, Power BI e Product Analytics | Primeira versão do Telecom Customer Intelligence |
| 17/09–25/09 | SQL analítico, modelagem dimensional e desempenho | Consultas, modelo estrela, planos de execução e simulado |
| 28/09–08/10 | Estatística, teste A/B e inferência causal | Experimento, diferenças em diferenças e controle sintético |
| 09/10–12/11 | Machine Learning tabular, XGBoost, clusters e churn | Benchmark e política de retenção com análise de erros |
| 13/11–18/11 | PyTorch e visão computacional | Triagem visual com baseline, transfer learning e métricas |
| 19/11–30/11 | Séries temporais, forecasting, risco e governança | Energy ForecastOps e projeto de risco |
| 01/12–21/12 | Airflow, Spark, dbt, testes, API, Docker, GCP, BigQuery e MLOps | Pipeline documentado e serviço com retreino e rollback |
| 22/12–30/12 | NLP, entity matching, embeddings, ranking e recomendação | Entity Matching Lab e recomendador com métricas Top-K |
| 31/12–06/01 | LLMs e RAG | Assistente com fontes, recusa e avaliação |
| 07/01–12/01 | Produto integrador | Produto demonstrável com testes e retrospectiva |
| 13/01–18/01 | Portfólio, simulados, case técnico e banca zero | Narrativa profissional e diagnóstico final |
| 19/01–25/01 | TCC de retenção em telecom | Política sob capacidade, efeito incremental, custo, monitoramento e defesa |

## Por que a base vem antes de IA

Engenharia de IA e Big Data são direções coerentes com o mercado, mas dependem da base. Um sistema real ainda precisa receber dados, consultar fontes, validar entradas, comparar métricas, controlar custo, expor serviços e explicar erros.

Por isso, a ordem é intencional:

1. Python e SQL constroem programação e consulta;
2. estatística e Machine Learning ensinam a medir melhoria e incerteza;
3. engenharia de dados, cloud, testes e MLOps tornam o trabalho reproduzível;
4. NLP, embeddings, LLMs e RAG entram com critérios para qualidade, latência, custo e falhas.

Antes de considerar a base concluída, você deve conseguir consumir uma API REST em Python, escrever consultas com `JOIN`, CTE e janela, interpretar incerteza e comparar um modelo com baseline.

## Inglês aplicado

O roadmap não duplica Duolingo, filmes ou estudo geral de idioma. O inglês aparece nas entregas técnicas:

- README curto em inglês nos projetos de portfólio;
- apresentação de dois a três minutos;
- respostas sobre problema, método, resultado e limitação;
- simulado de quatro habilidades antes do EF SET.

Hábitos externos continuam como base de vocabulário e escuta. Eles complementam, mas não substituem comunicação técnica.

## Portfólio mínimo

O aprendizado está concentrado em cinco produtos. Ao terminar, escolha os quatro melhores para apresentar:

1. **Telecom Customer Intelligence** — Product Analytics, causalidade, churn, engenharia, MLOps e TCC;
2. **Energy ForecastOps** — previsão operacional e backtest temporal;
3. **Entity Matching Lab** — NLP, deduplicação, embeddings e ranking;
4. **Intelligent Support Operations** — RAG avaliado e triagem visual;
5. **Portfolio Intelligence Lab** — ranking quantitativo e backtest financeiro.

Um projeto forte possui problema claro, dados identificados, execução reproduzível, validação, decisão, limitações honestas e README compreensível. Os projetos selecionados para portfólio também recebem `README.en.md` e apresentação curta em inglês.

## LinkedIn e candidaturas

As orientações de postagem ficam no README da data planejada. Uma publicação de progresso não libera automaticamente nova competência, headline ou alegação de experiência. Consulte [LinkedIn e evidências](<00 - Recursos Compartilhados/linkedin-e-evidencias.md>) antes de atualizar o perfil.

Antes de candidatar-se, confirme:

- [ ] Python, pandas/NumPy, SQL, estatística e ML estão em nível 3 ou mais.
- [ ] Escrevo `JOIN`, CTE e função de janela sem copiar uma solução inteira.
- [ ] Consumo uma API paginada com timeout, tratamento de falha e carga incremental.
- [ ] Reconcilio dados no Excel/Power Query e explico as transformações.
- [ ] Organizo fontes, staging e marts com testes no dbt.
- [ ] Explico separação de treino/teste, leakage, overfitting, métricas e limiar.
- [ ] Interpreto intervalo de confiança, valor-p e teste A/B sem exagerar conclusões.
- [ ] Tenho ao menos três projetos reproduzíveis e apresento cada um em dois minutos.
- [ ] Currículo, LinkedIn e GitHub contam a mesma história.

## Manutenção técnica

Depois de adicionar ou mover sessões, regenere os índices e execute o validador conforme o README principal. O [manifesto de reorganização](<00 - Recursos Compartilhados/manifesto-reorganizacao-2026.json>) preserva o mapeamento interno e a integridade dos dias concluídos; ele não é material de estudo.

Os dias com `OK` permanecem congelados. Não aplique a nova estrutura retroativamente a eles.

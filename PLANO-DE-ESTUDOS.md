# Plano de estudos — Cientista de Dados Júnior

Este plano organiza **111 sessões práticas**, de 03/08/2026 a 25/01/2027: seis sessões já concluídas e preservadas, mais 105 sessões a partir de 24/08. As novas sessões reúnem 138 módulos existentes e 25 módulos adicionados após a análise das vagas. O percurso permanece abaixo do limite máximo de um ano e pode ser feito sem curso pago: você escolhe vídeo, documentação, site ou IA a partir dos nomes exatos de cada assunto.

O roadmap não promete contratação automática. O resultado depende de executar as atividades, buscar feedback e conseguir explicar o que foi construído. A meta realista é terminar com base técnica, portfólio e preparo para disputar vagas júnior.

## Como o projeto funciona

- O [README principal](README.md) é a única agenda e o único checklist de progresso.
- Cada pasta datada é uma sessão definitiva: ela pode usar dados ou projetos compartilhados, mas nunca exige reabrir o README de uma sessão concluída.
- O README diário contém somente o assunto e o trabalho daquela sessão.
- Depois de marcar uma sessão como concluída, não é necessário abrir seu README novamente.
- Revisões aparecem como novos problemas na sessão atual, sem mandar voltar a uma pasta antiga.
- Quando um curso gratuito não ensina um conceito necessário, a própria sessão traz um bloco **Aprenda agora** antes de usá-lo.

## Método de uma sessão

1. Abra o primeiro item não marcado no checklist principal.
2. Leia o objetivo e estude apenas o conteúdo indicado para aquela sessão.
3. Em vídeo de exercício, pause no enunciado e tente antes de ver a resolução.
4. Faça o núcleo e as práticas obrigatórias no arquivo indicado.
5. Altere uma entrada, um parâmetro ou uma hipótese e observe o efeito.
6. Execute do início ao fim e explique a solução em voz alta ou por escrito.
7. Guarde a evidência pedida e marque a sessão no checklist principal.

Todo conteúdo do roadmap é obrigatório. Os antigos blocos adicionais foram auditados: comparações, casos de borda, análise de erros, adaptação e reprodução foram mantidos como **Prática obrigatória**; repetições, ferramentas extras e polimento sem ganho claro foram removidos. Se surgir uma dificuldade específica, peça um reforço direcionado naquele momento, sem criar dívida em dias já concluídos.

## Critério de conclusão

Uma sessão termina quando estas três provas forem verdadeiras:

- o artefato principal executa ou foi produzido do início ao fim;
- você consegue modificar uma entrada sem perder o controle do resultado;
- você consegue explicar objetivo, lógica e uma limitação sem copiar a explicação.

Use esta escala para se avaliar:

| Nota | Evidência |
|---:|---|
| 0 | Não comecei |
| 1 | Só funciona quando copio |
| 2 | Resolvo com muita consulta |
| 3 | Resolvo sozinho um caso conhecido |
| 4 | Adapto para um problema novo e explico |
| 5 | Testo, critico e consigo ensinar |

A meta é **3 ou mais**. Se ainda não chegou a 3, continue trabalhando na sessão aberta; quando concluí-la, encerre-a de vez.

## Tempo e foco

| Tipo de sessão | Tempo sugerido |
|---|---:|
| Aula curta de Python + prática | 1h30–3h |
| Sessão com um bloco técnico | 2–4h |
| Sessão com dois blocos | 4–5h, com pausa entre eles |
| Projeto ou entrega | 4–5h |

O tempo é um limite de escopo, não uma corrida. Se travar por mais de 20 minutos:

1. copie a mensagem de erro completa;
2. reduza o problema para a menor entrada que ainda falha;
3. confira tipos, formas, nomes de colunas e caminho do arquivo;
4. consulte a documentação da função usada;
5. peça uma pista ou revisão da sua tentativa, não uma solução pronta.

## Uso eficiente de IA

A IA pode atuar como tutora, depuradora e banca, sem substituir a prática. Bons pedidos:

- “Não resolva. Dê uma pista sobre o próximo passo e faça uma pergunta para testar meu raciocínio.”
- “Explique esta mensagem de erro e indique qual hipótese eu devo testar primeiro.”
- “Revise minha explicação e aponte a primeira incoerência.”
- “Crie três casos de teste, incluindo um caso de borda, sem mostrar a implementação.”
- “Faça uma entrevista de cinco perguntas sobre este projeto e espere cada resposta.”

Evite colar uma solução completa antes da própria tentativa. Código que executa, mas que você não consegue alterar nem explicar, ainda não conta como domínio.

## Fontes gratuitas

Uma fonte entra no plano somente quando será usada. A ordem de preferência é:

1. aula gratuita já selecionada;
2. mini-explicação e exemplo local em **Aprenda agora**;
3. documentação oficial;
4. outro vídeo gratuito para uma dúvida específica.

Não é necessário acumular certificados nem concluir playlists inteiras. O arquivo [Cursos gratuitos e lacunas](<00 - Recursos Compartilhados/cursos-complementares-selecionados.md>) registra o que já está coberto e quais assuntos ainda podem receber uma boa aula enviada por você.

## Fases e resultados

| Período | Foco | Evidência principal |
|---|---|---|
| 03/08–17/08 | Fundamentos de Python já concluídos | Seis dias preservados com status OK |
| 24/08–04/09 | Python, arquivos, pacotes e código profissional | Scripts, testes e mini-projeto reproduzível |
| 08/09–16/09 | NumPy, pandas, visualização, Power BI e Product Analytics | Primeira versão do Telecom Customer Intelligence |
| 17/09–25/09 | SQL analítico, modelagem dimensional e performance | Consultas, modelo estrela, planos de execução e simulado |
| 28/09–08/10 | Estatística, teste A/B e inferência causal | Experimento, diferenças em diferenças e controle sintético |
| 09/10–12/11 | Machine Learning tabular, XGBoost, clusters e churn | Benchmark e política de retenção com análise de erros |
| 13/11–18/11 | PyTorch e visão computacional | Triagem visual com baseline, transfer learning e métricas |
| 19/11–30/11 | Séries temporais, forecasting, risco e governança | Energy ForecastOps e projeto de risco |
| 01/12–21/12 | Dados, Airflow, Spark, testes, API, Docker, GCP, BigQuery e MLOps | Pipeline e serviço com retreino e rollback |
| 22/12–30/12 | NLP, entity matching, embeddings, ranking e recomendação | Entity Matching Lab e recomendador com métricas Top-K |
| 31/12–06/01 | LLMs e RAG | Assistente com fontes, recusa e avaliação |
| 07/01–12/01 | Produto integrador | Produto demonstrável com testes e retrospectiva |
| 13/01–18/01 | Portfólio, LinkedIn, simulados e banca zero | Narrativa profissional e diagnóstico final |
| 19/01–25/01 | TCC de retenção em telecom | Política sob capacidade limitada, risco de churn, efeito incremental simulado, custo, monitoramento, relatório e defesa |

Na fase de IA generativa, a aplicação LLM/RAG é obrigatória. Se Python, SQL, estatística ou ML ainda estiverem abaixo do nível 3, mantenha a sessão aberta, corrija a dificuldade concreta e depois conclua a mesma atividade de IA. Só registre IA Generativa/RAG no LinkedIn quando a aplicação tiver sido realmente executada e avaliada.

## Inglês no roadmap

O roadmap não cria um curso paralelo de gramática ou vocabulário geral. O inglês é aplicado nas entregas reais por meio de README em inglês, apresentação de 2–3 minutos e perguntas sobre o próprio projeto. Isso acontece principalmente nas entregas de 30/09, 08/10, 28/10, 12/11, 18/11, 25/11, 18/12, 30/12, 06/01 e 25/01.

Duolingo e filmes continuam como hábitos externos de base, vocabulário e escuta. Eles complementam o roadmap; não viram novos checkboxes nem substituem a escrita, a fala e as perguntas técnicas dos projetos.

## Portfólio mínimo

O aprendizado está concentrado em cinco produtos, em vez de dezenas de repositórios rasos. Ao concluir, escolha os **quatro melhores** para apresentar:

1. **Telecom Customer Intelligence** — Product Analytics, causalidade, churn, engenharia, MLOps e o TCC de priorização de retenção;
2. **Energy ForecastOps** — previsão operacional e backtest temporal;
3. **Entity Matching Lab** — NLP, deduplicação, embeddings e ranking;
4. **Intelligent Support Operations** — RAG avaliado e triagem visual;
5. **Portfolio Intelligence Lab** — projeto financeiro independente de ranking quantitativo e backtest.

Um projeto forte precisa ter problema claro, dados identificados, execução reproduzível, validação correta, decisão ou recomendação, limitações honestas e README compreensível. Os quatro projetos definidos como evidência de portfólio também exigem um `README.en.md` de 150–250 palavras e uma apresentação de 2–3 minutos em inglês.

## Marcos profissionais

Cada semana termina com uma publicação baseada no artefato realmente produzido. As instruções ficam no README do próprio dia de postagem, sem calendário paralelo. Uma publicação de progresso não libera automaticamente Competências, Projetos, Destaques ou mudança de headline: essas alterações continuam reservadas aos marcos com evidência completa. Consulte o [Guia de LinkedIn e evidências](<00 - Recursos Compartilhados/linkedin-e-evidencias.md>) para saber exatamente o que atualizar em cada marco.

Antes de candidatar-se, confirme:

- [ ] Python, pandas/NumPy, SQL, estatística e ML estão em nível 3 ou mais.
- [ ] Consigo escrever JOIN, CTE e função de janela sem copiar um modelo inteiro.
- [ ] Sei explicar separação de treino/teste, vazamento, overfitting, métricas e limiar.
- [ ] Sei interpretar intervalo de confiança, valor-p e teste A/B sem exagerar conclusões.
- [ ] Tenho pelo menos três projetos reproduzíveis e consigo apresentar cada um em dois minutos.
- [ ] Meus repositórios têm instrução de execução, dependências e limitações.
- [ ] Currículo, LinkedIn e GitHub contam a mesma história, sem ferramentas que não sei defender.

## Manutenção do roadmap

Depois de adicionar ou mover qualquer sessão, regenere os índices e execute o validador com os comandos descritos no README principal. O normalizador deve ser aplicado somente a conteúdo futuro revisado; as pastas com status OK permanecem congeladas.

O validador detecta datas duplicadas, mês incompatível, limite de um ano, contadores incorretos, agenda ou mapa desatualizado, estrutura diária incompleta, atividades opcionais reintroduzidas, artefatos principais ausentes, links quebrados, notebooks inválidos e erros de sintaxe em Python.

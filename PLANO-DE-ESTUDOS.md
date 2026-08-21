# Plano de estudos — Cientista de Dados Júnior

Este plano organiza **144 sessões práticas**, de 03/08/2026 a 04/03/2027. São cerca de sete meses de estudo, portanto o percurso permanece bem abaixo do limite máximo de um ano. Ele foi desenhado para ser suficiente sem curso pago: usa conteúdo gratuito, documentação oficial, explicações locais, exercícios, projetos e critérios objetivos de domínio.

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
| Sessão técnica comum | 2h30–3h30 |
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
| 03/08–08/09 | Python e resolução de problemas | Scripts, arquivos e mini-projeto executável |
| 09/09–22/09 | NumPy, pandas e visualização | Análise executiva de dados de telecom |
| 23/09–07/10 | SQL analítico | Consultas reproduzíveis e simulado |
| 08/10–21/10 | Estatística e experimentação | Análise de experimento com incerteza |
| 22/10–26/11 | Machine Learning tradicional | Baseline auditável e decisão por custo |
| 27/11–14/12 | Projeto de churn e aprendizado não supervisionado | Pipeline, segmentação, política de retenção e apresentação |
| 16/12–22/12 | Séries temporais | Backtest temporal e previsão operacional |
| 23/12–29/12 | Risco e governança | Política de decisão e model card |
| 30/12–19/01 | Engenharia, testes e deploy | Pipeline versionado, API e container |
| 20/01–28/01 | Cloud e ciclo de vida | Arquitetura explicável e monitoramento |
| 29/01–11/02 | IA generativa e RAG | Aplicação com recuperação, fontes e avaliação |
| 12/02–18/02 | Produto integrador | Produto pequeno com teste de aceitação |
| 19/02–25/02 | Portfólio, entrevistas e candidaturas | Repositórios, currículo, primeira candidatura e banca zero |
| 26/02–04/03 | TCC financeiro | Ranking, backtest, relatório e defesa |

Na fase de IA generativa, a aplicação LLM/RAG é obrigatória. Se Python, SQL, estatística ou ML ainda estiverem abaixo do nível 3, mantenha a sessão aberta, corrija a dificuldade concreta e depois conclua a mesma atividade de IA. Só registre IA Generativa/RAG no LinkedIn quando a aplicação tiver sido realmente executada e avaliada.

## Inglês no roadmap

O roadmap não cria um curso paralelo de gramática ou vocabulário geral. O inglês é aplicado em quatro entregas: experimento em 21/10, churn em 14/12, forecasting em 22/12 e TCC em 04/03. Em cada uma, escreva um resumo técnico de 150–250 palavras e prepare uma apresentação de 2–3 minutos sobre o próprio projeto.

Duolingo e filmes continuam como hábitos externos de base, vocabulário e escuta. Eles complementam o roadmap; não viram novos checkboxes nem substituem a escrita, a fala e as perguntas técnicas dos projetos.

## Portfólio mínimo

Ao concluir, escolha os **quatro melhores** trabalhos para apresentar; quantidade não substitui acabamento:

1. análise executiva ou experimento;
2. projeto completo de Machine Learning;
3. forecasting, risco ou produto de dados;
4. TCC — Portfolio Intelligence Lab.

Um projeto forte precisa ter problema claro, dados identificados, execução reproduzível, validação correta, decisão ou recomendação, limitações honestas e README compreensível. Os quatro projetos definidos como evidência de portfólio também exigem um `README.en.md` de 150–250 palavras e uma apresentação de 2–3 minutos em inglês.

## Marcos profissionais

LinkedIn só aparece nas sessões em que existe uma mudança concreta: nova entrega publicável, nova competência demonstrável ou atualização real do posicionamento. Não altere o perfil para registrar apenas que assistiu a uma aula. Consulte o [Guia de LinkedIn e evidências](<00 - Recursos Compartilhados/linkedin-e-evidencias.md>) para saber exatamente o que atualizar em cada marco.

Antes de candidatar-se, confirme:

- [ ] Python, pandas/NumPy, SQL, estatística e ML estão em nível 3 ou mais.
- [ ] Consigo escrever JOIN, CTE e função de janela sem copiar um modelo inteiro.
- [ ] Sei explicar separação de treino/teste, vazamento, overfitting, métricas e limiar.
- [ ] Sei interpretar intervalo de confiança, valor-p e teste A/B sem exagerar conclusões.
- [ ] Tenho pelo menos três projetos reproduzíveis e consigo apresentar cada um em dois minutos.
- [ ] Meus repositórios têm instrução de execução, dependências e limitações.
- [ ] Currículo, LinkedIn e GitHub contam a mesma história, sem ferramentas que não sei defender.

## Manutenção do roadmap

Depois de adicionar ou mover qualquer sessão, execute:

```powershell
python scripts/gerar_indices.py
python scripts/normalizar_metadados.py --write
python scripts/validar_roadmap.py
```

O primeiro comando regenera agenda e mapa; o segundo remove cabeçalhos antigos; o validador detecta datas duplicadas, contadores mensais incorretos, estrutura diária incompleta, atividades opcionais reintroduzidas, artefatos principais ausentes, links locais quebrados, notebooks inválidos, erros de sintaxe em Python e instruções retroativas.

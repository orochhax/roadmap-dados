# LinkedIn e evidências do roadmap

Este guia mostra **quando** atualizar o LinkedIn e **o que** pode ser acrescentado. A regra principal é simples: estudar um assunto inicia o aprendizado; concluir o núcleo, executar uma evidência e conseguir explicá-la permite apresentar aquela competência.

O contexto profissional informado por Carlos e a atualização que já pode ser feita estão em [LinkedIn — perfil atual e próximas mudanças](linkedin-perfil-atual.md).

## O que significa cada parte do LinkedIn

### Competências

São conhecimentos e ferramentas que você consegue usar e defender com um exemplo, como `Python`, `SQL` ou `Machine Learning`. Assistir a uma aula ou copiar um código não basta. Adicione uma competência somente depois de produzir a evidência indicada neste roadmap.

### Projetos e Destaques

- **Projetos** descreve trabalhos que você construiu: problema, dados, técnica, resultado e limitação.
- **Destaques** dá visibilidade a um link importante, como um repositório, relatório, dashboard ou demonstração.

Um trabalho só deve aparecer nessas seções quando outra pessoa puder abrir a evidência e entender o que foi feito. Se ainda estiver apenas no computador, você pode preparar o texto, mas não diga que ele está publicado.

### Sobre

É o texto que resume sua trajetória, seus objetivos e as evidências mais fortes. Ele não precisa mudar depois de cada aula. Atualize-o quando surgir uma nova fase comprovada, por exemplo: primeira análise completa, primeiro pipeline de Machine Learning auditado, primeiro serviço testado ou TCC finalizado.

### Título ou headline

É a linha curta exibida abaixo do seu nome. Ela comunica seu posicionamento atual, mas não deve inventar cargo ou experiência profissional. Use algo verdadeiro, por exemplo:

```text
[cargo ou área atual] | Em formação em Ciência de Dados | Python e SQL
```

Não use `Cientista de Dados`, `Engenheiro de Software`, `sênior` ou anos de experiência como se fossem cargos exercidos sem que isso seja verdade. Acrescentar uma ferramenta à headline também não é obrigatório; clareza vale mais do que uma lista extensa.

## Regra para liberar uma atualização

Antes de adicionar qualquer competência ou afirmação, confirme os quatro itens:

- [ ] O núcleo essencial da sessão foi concluído.
- [ ] O artefato executou do início ao fim e a conferência registrou resultado esperado e observado.
- [ ] Você consegue alterar uma entrada ou parâmetro e explicar objetivo, lógica, resultado e uma limitação.
- [ ] O texto aponta para uma evidência real e não transforma projeto educacional em experiência profissional ou impacto de negócio comprovado.

Se um item ainda estiver aberto, termine a evidência antes de atualizar o perfil. Ao concluir cada marco abaixo, o assistente deve avisar qual ação está liberada.

## Marcos cronológicos

| Data | Evidência mínima | Atualização liberada |
|---|---|---|
| 08/09/2026 | Mini-projeto de Python executado, testado e explicado. | Adicionar **Python** em Competências. Não é necessário alterar o Sobre ou a headline. |
| 22/09/2026 | Análise executiva reproduzível, com dados tratados, resultado conferido e limitação. | Adicionar **pandas** e **Análise de Dados**. Adicionar **Microsoft Power BI** somente se ele tiver sido realmente usado no dashboard. Incluir o projeto e revisar o Sobre com a primeira evidência de dados. |
| 07/10/2026 | Simulado concluído, consultas revisadas e projeto SQL compreensível. | Adicionar **SQL** e incluir o projeto. |
| 21/10/2026 | Experimento com hipótese, métrica, incerteza, decisão e limitação documentadas. | Adicionar **Análise Estatística** e **Teste A/B**. Incluir o experimento se estiver apresentável. |
| 18/11/2026 | Benchmark reproduzível usando o mesmo split e as mesmas métricas, com XGBoost comparado aos baselines. | Adicionar **XGBoost** e **Avaliação de Modelos**. Não declarar que o modelo gerou impacto empresarial real. |
| 26/11/2026 | Pipeline auditado, reproduzível e sem vazamento conhecido, com métricas e limitações. | Adicionar **Machine Learning**, **scikit-learn** e **Pipelines de Machine Learning**. Revisar o Sobre com a evidência de modelagem. |
| 08/12/2026 | PCA, clusterização e avaliação executados, comparados e interpretados sem tratar clusters como verdade absoluta. | Adicionar **Aprendizado não supervisionado** e **Análise de clusters**. |
| 22/12/2026 | Projeto temporal com divisão cronológica, baseline, backtest, métricas e limitações. | Adicionar **Análise de Séries Temporais** e **Forecasting** e incluir o projeto. |
| 19/01/2027 | API executada de ponta a ponta, container iniciado e contrato testado. | Adicionar **FastAPI**, **Docker** e **APIs REST** somente para os componentes realmente executados. Incluir a demonstração ou o serviço, deixando claro se a publicação foi apenas local. |
| 22/01/2027 | Experimentos reais registrados no MLflow com parâmetros, métricas, artefatos e identificadores de execução. | Adicionar **MLflow**. Adicionar **Databricks** somente se a plataforma tiver sido realmente usada; execução local com MLflow não comprova Databricks. |
| 27/01/2027 | Monitoramento, gatilho de retreinamento, comparação champion/challenger e rollback simulados com registros verificáveis. | Adicionar **MLOps** e **Monitoramento de Modelos**. Revisar o Sobre com a evidência de ciclo de vida do modelo. |
| 11/02/2027 | Aplicação de IA generativa/RAG realmente executada, avaliada e documentada com fontes, erros, custo ou latência e limitações. | Adicionar **IA Generativa** e **Retrieval-Augmented Generation (RAG)** somente se essa execução existir. Apenas estudar os conceitos não libera a atualização. |
| 22/02/2027 | README e apresentação curta em inglês produzidos e revisados, com registro honesto do que você consegue compreender, escrever e falar. | Atualizar o idioma com um nível verdadeiro. Praticar inglês técnico não autoriza afirmar **inglês avançado**. Só adicionar **Comunicação técnica em inglês** se você conseguir apresentar e responder perguntas sem depender de um texto decorado. |
| 04/03/2027 | TCC reproduzido em ambiente limpo, publicado com relatório, demonstração, resultados e limitações, e defendido. | Fazer a revisão final de Competências, Projetos, Destaques, Sobre e headline; remover itens sem evidência e destacar os quatro melhores projetos. |

## Modelos de ação

### Aviso ao concluir uma competência

```text
LinkedIn liberado: adicione [competência] em Competências.
Evidência: [nome e caminho ou link do artefato].
Você executou [teste], obteve [resultado observado] e explicou [limitação].
```

### Descrição curta de projeto

```text
Problema: [qual pergunta foi investigada].
Trabalho: [dados e técnica realmente usados].
Resultado: [número ou conclusão existente no artefato].
Limitação: [o que a análise ou o modelo ainda não prova].
Link: [repositório, relatório, dashboard ou demonstração conferidos].
```

### Frase para a seção Sobre

```text
Em um projeto educacional reproduzível, construí [entrega] com [técnicas], avaliei por [métrica ou teste] e documentei [principal limitação].
```

### Revisão de headline

```text
[cargo ou área atual verdadeira] | Em formação em Ciência de Dados | [duas ou três competências com evidência]
```

## Palavras que exigem cuidado

- Prefira `construí em um projeto`, `avaliei` e `simulei` quando essa foi a experiência real.
- Use `publiquei` apenas se o link estiver acessível e conferido.
- Use `implantei em produção`, `gerei receita`, `reduzi custos` ou `melhorei em X%` somente com evidência real desse ambiente e dessa medida.
- Não transforme a métrica de um conjunto de teste em promessa de resultado futuro.
- Não informe nível de inglês com base apenas em tradução automática, leitura de README ou apresentação decorada.

Na dúvida, descreva exatamente o que o artefato prova. Uma afirmação menor e verificável fortalece mais o perfil do que uma alegação ampla que você não consegue defender.

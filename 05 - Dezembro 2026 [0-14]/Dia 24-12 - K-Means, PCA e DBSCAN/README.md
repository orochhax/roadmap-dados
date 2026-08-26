# K-Means e PCA + DBSCAN e avaliacao de clusters

**Data de estudo:** 24/12/2026
**Carga planejada:** 4 a 5 horas

## Aulas selecionadas no YouTube

- [ ] **O Aprendizado Não Supervisionado e a Base Teórica do K Means** (23:11) — [abrir no YouTube](https://www.youtube.com/watch?v=q05qbU8FYKU).
- [ ] **Projeto de Dados em 1 aula - Clusterização com Python [Completo]** (22:40) — [pesquisar no YouTube](https://www.youtube.com/results?search_query=Projeto+de+Dados+em+1+aula+Clusterizacao+com+Python+Completo).

**Carga de vídeo selecionada:** aproximadamente 46 minutos.

**Prática obrigatória:** as aulas introduzem K-Means e uma aplicação. Os notebooks locais aprofundam padronização, escolha de k, PCA, DBSCAN, silhouette, ruído, estabilidade e a possibilidade de recomendar nenhum método.

## Atividades do dia

### Atividade 1 — K-Means e PCA

#### O que pesquisar
- `K-Means e PCA Python explicado passo a passo`
- `K-Means e PCA Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-k-means-e-pca`](<atividades/01-k-means-e-pca/>)

#### Objetivo

Encontrar grupos de clientes sem usar uma resposta pronta, avaliar quantos grupos fazem sentido e usar PCA para visualizar dados com várias dimensões.

#### O que você precisa entender

- No aprendizado supervisionado existe uma resposta conhecida, como `churn`. No aprendizado não supervisionado, o algoritmo procura estruturas sem usar essa resposta.
- Cluster é um grupo formado por semelhança entre registros.
- K-Means exige escolher previamente quantos grupos, `k`, serão criados e aproxima cada registro do centro mais próximo.
- Padronização coloca variáveis com unidades diferentes em uma escala comparável. Sem ela, `mensalidade` pode dominar `nps` apenas por ter números maiores.
- Inércia mede distâncias internas e sempre cai quando `k` aumenta; por isso, não deve decidir sozinha.
- Silhouette mede coesão e separação. Valores maiores ajudam na comparação, mas não provam utilidade para o negócio.
- PCA combina variáveis em componentes. Ele ajuda a reduzir dimensões e visualizar padrões, mas não demonstra causalidade.
- Os números dos clusters são apenas identificadores: cluster `0` não é melhor nem pior que cluster `1`.

```python
variaveis = [
    "mensalidade",
    "nps",
    "chamados_90d",
    "atraso_dias",
    "tempo_cliente_meses",
]
valores_de_k = range(2, 9)
```

**Erro comum:** incluir `churn`, identificadores, datas de cancelamento ou informações criadas depois do evento e transformar o agrupamento em uma resposta vazada.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-k-means-e-pca/kmeans_e_pca.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`.
- **Dependências:** instale o conteúdo de `atividades/01-k-means-e-pca/requirements.txt` no ambiente usado para o notebook.
- **Saídas:** tabela de comparação de `k`, gráfico de PCA e perfis dos clusters na escala original.

#### O que fazer

- [ ] Carregue os dados e selecione `mensalidade`, `nps`, `chamados_90d`, `atraso_dias` e `tempo_cliente_meses`.
- [ ] Explique por que `cliente_id`, `churn`, datas e informações de cancelamento não entram no ajuste.
- [ ] Compare as escalas das variáveis e aplique `StandardScaler`.
- [ ] Treine K-Means para `k` de 2 a 8 com seed fixa e registre inércia, silhouette e tamanho do menor cluster.
- [ ] Escolha um `k` com justificativa baseada nas métricas e na interpretação possível dos grupos.
- [ ] Compare o resultado sem padronização e com padronização, registrando o que mudou.
- [ ] Aplique PCA com dois componentes para visualização e registre a variância explicada individual e acumulada.
- [ ] Crie perfis na escala original com tamanho e médias das cinco variáveis; dê nomes descritivos sem tratar os grupos como verdade absoluta.
- [ ] Execute o teste controlado descrito no notebook e registre resultado esperado e observado.

#### Como validar

- O notebook executa do início ao fim e contém comparação de escalas, tabela de `k`, gráficos, PCA e perfis.
- O teste controlado confirma que pontos próximos ficam juntos e que alvo e identificadores não foram usados no ajuste.
- A escolha de `k`, a importância da padronização e uma limitação estão explicadas com palavras próprias.

### Atividade 2 — DBSCAN e avaliacao de clusters

#### O que pesquisar
- `DBSCAN e avaliacao de clusters machine learning com Python explicado passo a passo`
- `DBSCAN e avaliacao de clusters machine learning com Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-dbscan-e-avaliacao-de-clusters`](<atividades/02-dbscan-e-avaliacao-de-clusters/>)

#### Objetivo

Comparar métodos de agrupamento, tratar resultados inválidos corretamente e decidir entre K-Means, DBSCAN ou nenhum deles com base em evidências.

#### O que você precisa entender

- DBSCAN junta pontos em regiões densas e pode marcar pontos isolados como ruído.
- `eps` é o raio usado para procurar vizinhos; `min_samples` é a quantidade mínima de pontos exigida para formar uma região densa.
- O rótulo `-1` representa ruído. Ele não significa automaticamente fraude, erro ou cliente ruim.
- DBSCAN não exige informar a quantidade de clusters, mas é sensível aos parâmetros e à escala.
- K-Means tende a representar melhor grupos compactos; DBSCAN consegue representar alguns formatos irregulares.
- Silhouette maior e Davies-Bouldin menor sugerem melhor separação interna, mas não garantem utilidade para o negócio.
- Uma configuração com métrica alta e muitos registros descartados como ruído pode ser inadequada.
- Recomendar “nenhum dos dois” é um resultado válido quando os testes não sustentam uma segmentação útil.

```python
valores_eps = [0.3, 0.5, 0.8, 1.2]
valores_min_samples = [5, 10, 20]
```

**Erro comum:** calcular silhouette quando existe apenas um cluster, ignorar o percentual de ruído ou escolher parâmetros depois de procurar apenas um resultado visualmente agradável.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-dbscan-e-avaliacao-de-clusters/dbscan_e_avaliacao_de_clusters.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e dados controlados gerados com `make_moons`.
- **Evidência:** `atividades/02-dbscan-e-avaliacao-de-clusters/recomendacao_clusterizacao.md`.
- **Dependências:** instale o conteúdo de `atividades/02-dbscan-e-avaliacao-de-clusters/requirements.txt` no ambiente usado para o notebook.

#### O que fazer

- [ ] Use `make_moons` para comparar K-Means e DBSCAN em grupos de formato não circular.
- [ ] Recarregue e padronize as cinco variáveis de clientes sem depender do notebook anterior.
- [ ] Teste pelo menos quatro valores de `eps` e três de `min_samples`.
- [ ] Registre quantidade de clusters, percentual de ruído, silhouette e Davies-Bouldin quando essas métricas puderem ser calculadas.
- [ ] Trate sem erro configurações com um único cluster ou somente ruído.
- [ ] Compare DBSCAN e K-Means considerando métricas, cobertura, sensibilidade e interpretação.
- [ ] Descreva os clusters na escala original e inspecione separadamente alguns registros marcados como ruído.
- [ ] Use `churn` somente depois do agrupamento para descrição; deixe explícito que ele não participou do treino e não prova causalidade.
- [ ] Preencha a recomendação escolhendo K-Means, DBSCAN ou nenhum dos dois.

#### Atualização do LinkedIn — após concluir

- **Evidência exigida:** notebook executado, teste controlado e recomendação preenchida.
- **Competências:** adicione **Aprendizado não supervisionado** e **Análise de clusters**.
- **Sobre e headline:** não altere neste momento; estas sessões demonstram novas competências, mas ainda não representam uma nova entrega pública.

#### Como validar

- O notebook executa do início ao fim e contém experimento controlado, busca de parâmetros e comparação entre algoritmos.
- Casos com um cluster ou somente ruído são tratados corretamente, com resultado esperado e observado.
- A recomendação cita métricas, cobertura, sensibilidade, interpretação e pelo menos uma limitação.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

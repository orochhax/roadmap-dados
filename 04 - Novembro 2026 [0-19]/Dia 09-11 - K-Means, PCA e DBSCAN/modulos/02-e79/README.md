# DBSCAN e avaliação de clusters

## Objetivo

Comparar métodos de agrupamento, tratar resultados inválidos corretamente e decidir entre K-Means, DBSCAN ou nenhum deles com base em evidências.

## Aprenda agora

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

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dbscan_e_avaliacao_de_clusters.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e dados controlados gerados com `make_moons`.
- **Evidência:** `03-evidencias/recomendacao_clusterizacao.md`.
- **Dependências:** instale o conteúdo de `01-exercicios/requirements.txt` no ambiente usado para o notebook.

## Núcleo obrigatório

1. [ ] Use `make_moons` para comparar K-Means e DBSCAN em grupos de formato não circular.
2. [ ] Recarregue e padronize as cinco variáveis de clientes sem depender do notebook anterior.
3. [ ] Teste pelo menos quatro valores de `eps` e três de `min_samples`.
4. [ ] Registre quantidade de clusters, percentual de ruído, silhouette e Davies-Bouldin quando essas métricas puderem ser calculadas.
5. [ ] Trate sem erro configurações com um único cluster ou somente ruído.
6. [ ] Compare DBSCAN e K-Means considerando métricas, cobertura, sensibilidade e interpretação.
7. [ ] Descreva os clusters na escala original e inspecione separadamente alguns registros marcados como ruído.
8. [ ] Use `churn` somente depois do agrupamento para descrição; deixe explícito que ele não participou do treino e não prova causalidade.
9. [ ] Preencha a recomendação escolhendo K-Means, DBSCAN ou nenhum dos dois.

## Atualização do LinkedIn — após concluir

- **Evidência exigida:** notebook executado, teste controlado e recomendação preenchida.
- **Competências:** adicione **Aprendizado não supervisionado** e **Análise de clusters**.
- **Sobre e headline:** não altere neste momento; estas sessões demonstram novas competências, mas ainda não representam uma nova entrega pública.

## Concluído quando

- [ ] O notebook executa do início ao fim e contém experimento controlado, busca de parâmetros e comparação entre algoritmos.
- [ ] Casos com um cluster ou somente ruído são tratados corretamente, com resultado esperado e observado.
- [ ] A recomendação cita métricas, cobertura, sensibilidade, interpretação e pelo menos uma limitação.

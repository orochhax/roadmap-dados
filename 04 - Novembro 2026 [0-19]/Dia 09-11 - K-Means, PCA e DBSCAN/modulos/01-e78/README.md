# K-Means e PCA

## Objetivo

Encontrar grupos de clientes sem usar uma resposta pronta, avaliar quantos grupos fazem sentido e usar PCA para visualizar dados com várias dimensões.

## Aprenda agora

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

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/kmeans_e_pca.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`.
- **Dependências:** instale o conteúdo de `01-exercicios/requirements.txt` no ambiente usado para o notebook.
- **Saídas:** tabela de comparação de `k`, gráfico de PCA e perfis dos clusters na escala original.

## Núcleo obrigatório

1. [ ] Carregue os dados e selecione `mensalidade`, `nps`, `chamados_90d`, `atraso_dias` e `tempo_cliente_meses`.
2. [ ] Explique por que `cliente_id`, `churn`, datas e informações de cancelamento não entram no ajuste.
3. [ ] Compare as escalas das variáveis e aplique `StandardScaler`.
4. [ ] Treine K-Means para `k` de 2 a 8 com seed fixa e registre inércia, silhouette e tamanho do menor cluster.
5. [ ] Escolha um `k` com justificativa baseada nas métricas e na interpretação possível dos grupos.
6. [ ] Compare o resultado sem padronização e com padronização, registrando o que mudou.
7. [ ] Aplique PCA com dois componentes para visualização e registre a variância explicada individual e acumulada.
8. [ ] Crie perfis na escala original com tamanho e médias das cinco variáveis; dê nomes descritivos sem tratar os grupos como verdade absoluta.
9. [ ] Execute o teste controlado descrito no notebook e registre resultado esperado e observado.

## Concluído quando

- [ ] O notebook executa do início ao fim e contém comparação de escalas, tabela de `k`, gráficos, PCA e perfis.
- [ ] O teste controlado confirma que pontos próximos ficam juntos e que alvo e identificadores não foram usados no ajuste.
- [ ] A escolha de `k`, a importância da padronização e uma limitação estão explicadas com palavras próprias.

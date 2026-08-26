# Enunciado — Ranking aplicado a entity matching e recomendação

## Exercício 1 — Reranker de empresas com faixa de revisão humana

## Cenário real

Cada nome extraído de um ticket agora possui até dez candidatos. O time de cadastro quer que o sistema ordene a lista, faça match automático quando houver evidência forte e encaminhe ambiguidades para revisão. O custo de vincular a empresa errada é maior que o de revisar um caso.

## Entradas

Monte uma tabela com uma linha por par candidato:

- `record_id`, `candidate_entity_id` e `true_entity_id` somente para criar o alvo;
- scores exato, fuzzy, TF-IDF e embedding;
- sinais de domínio, país e cidade;
- qualidade/completude dos campos;
- posição e origem da geração de candidatos.

Separe os dados por `record_id`, nunca por linha, para que candidatos da mesma consulta não atravessem treino e teste. Preserve casos `no_match`.

## Saídas obrigatórias

`avaliar_ranking.py` deve gerar:

1. uma regra ponderada transparente como baseline;
2. um `XGBRanker` com grupos de consulta corretamente definidos;
3. ranking top-5 dos dois métodos;
4. scores, diferença entre primeiro/segundo lugar e decisão `match`, `review` ou `no_match`;
5. métricas de ranking e de decisão automática;
6. importância das features e análise de erros;
7. latência e custo estimado por mil consultas.

## Regras

- Garanta que cada grupo de consulta permaneça inteiro em uma divisão.
- Ajuste features, hiperparâmetros e limiares somente em treino/validação.
- Não use `true_entity_id`, posição do rótulo ou qualquer sinal pós-decisão como feature.
- Compare no mesmo conjunto de candidatos; o ranker não recupera uma entidade ausente.
- Defina duas fronteiras: match automático e `no_match`; o intervalo vira revisão.
- Analise separadamente falhas do gerador e falhas de ordenação.
- Registre seed, versão do XGBoost e threads utilizadas.

## Casos de borda obrigatórios

- entidade correta ausente dos candidatos;
- empate ou margem mínima entre os dois primeiros;
- candidato com domínio exato, mas país incompatível;
- nome igual e domínio ausente;
- consulta com apenas um candidato;
- consulta sem candidato e registro `no_match`;
- subsidiária versus matriz;
- valores ausentes em várias features.

## Métricas

- ranking: MRR e NDCG@5 como principais; Recall@1 e Recall@5 como apoio;
- decisão: precisão de matches automáticos, recall, cobertura e taxa de revisão;
- operação: latência P50/P95 e custo estimado por mil consultas.

## Critério de aceite

Antes do ranker, o conjunto de candidatos deve manter Recall@5 de pelo menos 0,95. O XGBRanker só substitui a regra se melhorar NDCG@5 em pelo menos 0,03, mantiver precisão mínima de 0,97 nos matches automáticos e respeitar o orçamento de latência definido. Caso contrário, recomende a regra mais simples ou aumente a revisão; não esconda a falha com um limiar escolhido no teste.

## Restrições

Não copie um pipeline pronto de ranking. Implemente no arquivo inicial e descreva por que cada feature estaria disponível no momento real da decisão.

---

## Exercício 2 obrigatório — Recomendador com feedback implícito

### Cenário real

Um aplicativo de autosserviço da operadora exibe artigos e ações como “resolver falha de Wi-Fi”, “consultar fatura” e “melhorar plano”. Você deve recomendar até dez itens com base em eventos implícitos. Um clique ou conclusão indica interesse, mas a ausência de interação não significa necessariamente rejeição.

### Entradas

Prepare uma tabela de interações com:

- `user_id_hash`, `item_id` e `event_timestamp`;
- `event_type`, por exemplo `view`, `click`, `save` ou `completed`;
- metadados do item, como categoria, idioma e palavras-chave.

Use somente dados públicos, sintéticos ou anonimizados. Inclua usuários e itens novos para avaliar cold start.

### Saídas obrigatórias

Em `recomendador_baseline.py`:

1. converta tipos de evento em pesos de feedback implícito e justifique-os;
2. faça split temporal, deixando as interações mais recentes para validação/teste;
3. crie um baseline de popularidade calculado somente com o treino;
4. implemente uma segunda abordagem: baseada em conteúdo **ou** filtragem colaborativa;
5. gere top-10 sem recomendar itens que o usuário já consumiu no treino;
6. avalie os dois métodos globalmente e em usuários/itens com pouco histórico;
7. registre latência e uma política explícita para cold start.

### Regras e casos de borda

- Não use eventos futuros para calcular popularidade, features ou similaridade.
- Preserve a ordem temporal e remova duplicatas conforme regra documentada.
- Diferencie usuário novo, item novo e usuário sem item relevante no teste.
- Teste empate de popularidade, catálogo vazio, interação repetida e menos de `k` itens elegíveis.
- Não trate todas as ausências como avaliações negativas explícitas.
- Fixe seed e ordenação de desempate para resultados reproduzíveis.

### Métricas

- principais: Precision@10, Recall@10 e NDCG@10;
- apoio: cobertura de catálogo, popularidade média recomendada e latência P95;
- cold start: resultados separados para usuários/itens novos ou com pouco histórico.

### Critério de aceite

A abordagem personalizada só substitui popularidade se melhorar NDCG@10 em pelo menos 0,02 sem reduzir Recall@10, respeitar o split temporal e possuir comportamento definido para cold start. Se não vencer, mantenha popularidade e explique o resultado; a entrega ainda é aceita quando a comparação é correta, reproduzível e honesta.

### Restrições de aprendizagem

O objetivo é um baseline pequeno, não uma plataforma de recomendação. Implemente no arquivo inicial sem copiar um tutorial completo e explique como feedback implícito difere de uma nota dada pelo usuário.

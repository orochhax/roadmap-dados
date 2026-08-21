# Previsão e decisão

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-079-previsao-e-decisao.ipynb`.
- **Dados:** `dados/energia.csv`.

## Aprenda agora

- **Definição:** previsão pontual estima um valor; intervalo expressa incerteza; custo assimétrico dá pesos diferentes a excesso e falta.
- **Exemplo mínimo:** `custo = 2*max(y-y_hat,0) + 1*max(y_hat-y,0)`; publique cenário baixo, central e alto.
- **Erro comum:** tratar intervalo de 95% como garantia ou decidir apenas pela média.

## Núcleo essencial

1. [ ] Converta previsões em decisão: dimensionamento de equipe, compra de energia ou capacidade.
2. [ ] Crie cenários otimista, base e pessimista usando intervalos.
3. [ ] Calcule custo de subestimar versus superestimar.

## Prática obrigatória

- [ ] Escolha métrica e modelo alinhados ao custo.
- [ ] Escreva recomendação para a próxima semana com nível de confiança.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-079-previsao-e-decisao.ipynb`:** Atribua custo 3 vezes maior para subestimar do que para superestimar e recalcule a escolha entre os modelos.
- [ ] **Em `01-exercicios/dia-079-previsao-e-decisao.ipynb`:** Produza recomendação para horizonte de 14 dias e compare o nível de incerteza com a recomendação de 7 dias.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-079-previsao-e-decisao.ipynb` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

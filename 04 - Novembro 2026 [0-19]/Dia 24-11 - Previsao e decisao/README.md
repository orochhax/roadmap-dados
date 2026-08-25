# Previsao e decisao

**Data de estudo:** 24/11/2026  
**Carga planejada:** 2 a 4 horas

## Aula selecionada no YouTube

- [ ] **Passeio aleatório** (9:14), da sequência do **Professor Vinicius Lima** — [pesquisar no YouTube](https://www.youtube.com/results?search_query=Passeio+aleatorio+Professor+Vinicius+Lima).

Use o passeio aleatório para entender por que o último valor observado é um baseline temporal forte. Compare-o com suas previsões antes de defender um modelo mais complexo.

## Atividades do dia

### Atividade 1 — Previsao e decisao

#### O que pesquisar
- `Previsao e decisao Python explicado passo a passo`
- `Previsao e decisao Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-previsao-e-decisao`](<atividades/01-previsao-e-decisao/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-previsao-e-decisao/dia-079-previsao-e-decisao.ipynb`.
- **Dados:** `dados/energia.csv`.

#### O que você precisa entender

- **Definição:** previsão pontual estima um valor; intervalo expressa incerteza; custo assimétrico dá pesos diferentes a excesso e falta.
- **Exemplo mínimo:** `custo = 2*max(y-y_hat,0) + 1*max(y_hat-y,0)`; publique cenário baixo, central e alto.
- **Erro comum:** tratar intervalo de 95% como garantia ou decidir apenas pela média.

#### O que fazer

- [ ] Converta previsões em decisão: dimensionamento de equipe, compra de energia ou capacidade.
- [ ] Crie cenários otimista, base e pessimista usando intervalos.
- [ ] Calcule custo de subestimar versus superestimar.

- [ ] Escolha métrica e modelo alinhados ao custo.
- [ ] Escreva recomendação para a próxima semana com nível de confiança.


- [ ] **Em `atividades/01-previsao-e-decisao/dia-079-previsao-e-decisao.ipynb`:** Atribua custo 3 vezes maior para subestimar do que para superestimar e recalcule a escolha entre os modelos.
- [ ] **Em `atividades/01-previsao-e-decisao/dia-079-previsao-e-decisao.ipynb`:** Produza recomendação para horizonte de 14 dias e compare o nível de incerteza com a recomendação de 7 dias.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

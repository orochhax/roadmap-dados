# Selecao de variaveis + Explicabilidade

**Data de estudo:** 14/12/2026
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Selecao de variaveis

#### O que pesquisar
- `Selecao de variaveis Python explicado passo a passo`
- `Selecao de variaveis Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-selecao-de-variaveis`](<atividades/01-selecao-de-variaveis/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-selecao-de-variaveis/dia-063-selecao-de-variaveis.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que você precisa entender

- **Definição:** seleção univariada avalia uma variável por vez; importância usa o modelo; RFE elimina iterativamente; near-constant encontra colunas quase invariáveis.
- **Exemplo mínimo:** ajuste o seletor em `X_train`, transforme treino e validação e compare métrica, colunas e tempo.
- **Erro comum:** selecionar com a base completa ou tratar importância como causalidade.

#### O que fazer

- [ ] Remova colunas constantes, quase constantes e duplicadas.
- [ ] Calcule correlação entre numéricas e identifique grupos redundantes.
- [ ] Compare seleção univariada, importância de modelo e RFE em subconjunto pequeno.

- [ ] Treine modelo com todas as features e com seleção; compare métrica e estabilidade.
- [ ] Documente por que feature selecionada não implica causalidade.


- [ ] **Em `atividades/01-selecao-de-variaveis/dia-063-selecao-de-variaveis.ipynb`:** Compare remoção de correlações acima de 0,90 e 0,75 e registre quantidade de features e métrica.
- [ ] **Em `atividades/01-selecao-de-variaveis/dia-063-selecao-de-variaveis.ipynb`:** Adicione uma cópia exata de uma coluna, faça a detecção removê-la e confirme que a original permanece.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

### Atividade 2 — Explicabilidade

#### O que pesquisar
- `Explicabilidade Python explicado passo a passo`
- `Explicabilidade Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-explicabilidade`](<atividades/02-explicabilidade/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-explicabilidade/dia-064-explicabilidade.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que você precisa entender

- **Definição:** explicação global resume o comportamento médio; local descreve uma previsão. Coeficientes, permutation importance e SHAP respondem perguntas distintas.
- **Exemplo mínimo:** `queda = métrica_original - métrica_com_coluna_embaralhada`; queda maior indica maior dependência.
- **Erro comum:** comparar coeficientes sem padronização ou generalizar uma explicação local.

#### O que fazer

- [ ] Escolha 10 previsões individuais, incluindo acertos e erros, e explique fatores principais.
- [ ] Use coeficientes, permutation importance e SHAP se disponível; compare explicações globais e locais.
- [ ] Teste explicações em dois segmentos demográficos ou operacionais.

- [ ] Identifique uma explicação plausível porém enganosa causada por correlação.
- [ ] Crie relatório para público não técnico com três cuidados ao interpretar importância.


- [ ] **Em `atividades/02-explicabilidade/dia-064-explicabilidade.ipynb`:** Explique uma previsão correta de churn alto e uma incorreta de churn baixo usando o mesmo método local.
- [ ] **Em `atividades/02-explicabilidade/dia-064-explicabilidade.ipynb`:** Remova a feature mais correlacionada com a principal e gere novamente a explicação para observar estabilidade.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

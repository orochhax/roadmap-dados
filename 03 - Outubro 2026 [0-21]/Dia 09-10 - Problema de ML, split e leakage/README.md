# Definicao do problema + Separacao e vazamento

**Data de estudo:** 09/10/2026  
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Definicao do problema

#### O que pesquisar
- `Definicao do problema Python explicado passo a passo`
- `Definicao do problema Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-definicao-do-problema`](<atividades/01-definicao-do-problema/>)

#### O que você precisa entender

Em aprendizado supervisionado, cada linha tem uma unidade de previsão, um alvo e um instante em que a decisão será tomada. *Leakage* é qualquer informação indisponível nesse instante.

```python
problema = {
    "unidade": "cliente",
    "alvo": "cancelará em até 30 dias",
    "momento_da_previsao": "fim do mês atual",
}
```

**Erro comum:** usar `data_cancelamento` ou `motivo_cancelamento` para prever um cancelamento que ainda não ocorreu.

#### Aula guiada — Curso em Vídeo IA

- [ ] Assista à aula #12 — **Você sabe o que é Machine Learning?** (15:10).
- Use-a como introdução à atividade de Machine Learning; ela substitui parte do estudo conceitual do dia, mas não substitui a atividade obrigatória.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-definicao-do-problema/dia-041-definicao-do-problema.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que fazer

- [ ] Escolha um problema binário usando `clientes_telecom.csv`: prever churn nos próximos 30 dias; escreva alvo, unidade de previsão e horizonte temporal.
- [ ] Defina quem usará a previsão, qual ação será tomada e qual erro é mais caro.
- [ ] Liste 15 variáveis possíveis e classifique cada uma como disponível, indisponível, sensível ou potencial leakage.

- [ ] Crie baseline de negócio: prever todos como não churn e comparar com regra simples `chamados_90d >= 3`.
- [ ] Escreva `problem_statement.md` com objetivo, restrições, métrica primária, métricas secundárias e critério de sucesso.
- [ ] **Em `atividades/01-definicao-do-problema/dia-041-definicao-do-problema.ipynb`:** Altere no problem statement o custo de falso negativo de R$500 para R$800 e revise somente métrica primária e critério de sucesso afetados.
- [ ] **Em `atividades/01-definicao-do-problema/dia-041-definicao-do-problema.ipynb`:** Classifique status_atual, data_cancelamento e motivo_cancelamento como leakage e escreva em que momento cada coluna fica disponível.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

### Atividade 2 — Separacao e vazamento

#### O que pesquisar
- `Separacao e vazamento Python explicado passo a passo`
- `Separacao e vazamento Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-separacao-e-vazamento`](<atividades/02-separacao-e-vazamento/>)

#### O que você precisa entender

Treino ajusta o modelo, validação orienta escolhas e teste estima o resultado final. Estratificação preserva a proporção do alvo; corte temporal preserva a ordem real.

```python
from sklearn.model_selection import train_test_split

X_treino, X_temp, y_treino, y_temp = train_test_split(
    X, y, test_size=0.4, stratify=y, random_state=42
)
```

**Erro comum:** ajustar imputação, escala ou seleção de variáveis antes da separação.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-separacao-e-vazamento/dia-042-separacao-e-vazamento.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que fazer

- [ ] Separe treino, validação e teste com proporção definida e compare a distribuição do alvo com e sem estratificação.
- [ ] Classifique colunas como disponíveis no momento da previsão ou como vazamento, justificando o momento em que surgem.
- [ ] Desenhe um corte temporal simples e explique por que nenhum registro futuro pode participar do treino.

- [ ] Crie as três features com leakage apenas como exemplo identificado, sem usá-las em um modelo ainda.
- [ ] Escreva um checklist curto de cinco perguntas para detectar vazamento.
- [ ] Compare split aleatório e temporal usando a mesma métrica e explique qual representa melhor o uso real.

#### Como validar

- Registrei as saídas pedidas e conferi pelo menos um resultado.
- Testei uma variação ou caso de borda e documentei o efeito.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

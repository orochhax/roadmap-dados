# Feature engineering + Validacao cruzada e tuning

**Data de estudo:** 29/10/2026  
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Feature engineering

#### O que pesquisar
- `Feature engineering Python explicado passo a passo`
- `Feature engineering Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-feature-engineering`](<atividades/01-feature-engineering/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-feature-engineering/dia-061-feature-engineering.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que você precisa entender

- **Definição:** um transformer encapsula uma transformação em `fit/transform`; ablação mede o efeito de retirar uma feature ou grupo.
- **Exemplo mínimo:** compare a mesma pipeline com e sem `tempo_cliente × gasto_mensal` e registre `delta = métrica_com - métrica_sem`.
- **Erro comum:** calcular a feature com dados de avaliação ou retirar várias features de uma vez.

#### O que fazer

- [ ] Crie pelo menos oito features de churn agrupadas em comportamento, financeiro, suporte e relacionamento.
- [ ] Defina para cada feature: fórmula, fonte, momento de disponibilidade e risco de leakage.
- [ ] Implemente features em funções ou transformer customizado.

- [ ] Faça análise de ablação por grupo.
- [ ] Elimine features que dependam do futuro ou duplicam o alvo.


- [ ] **Em `atividades/01-feature-engineering/dia-061-feature-engineering.ipynb`:** Crie a feature chamados_por_mes usando somente chamados anteriores à data de referência e documente a fórmula.
- [ ] **Em `atividades/01-feature-engineering/dia-061-feature-engineering.ipynb`:** Remova todas as features financeiras e refaça a ablação no mesmo split para medir a perda de desempenho.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

### Atividade 2 — Validacao cruzada e tuning

#### O que pesquisar
- `Validacao cruzada e tuning Python explicado passo a passo`
- `Validacao cruzada e tuning Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-validacao-cruzada-e-tuning`](<atividades/02-validacao-cruzada-e-tuning/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-validacao-cruzada-e-tuning/dia-062-validacao-cruzada-e-tuning.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que você precisa entender

- **Definição:** `KFold` divide observações; `StratifiedKFold` preserva o alvo; validação temporal respeita a ordem. Tuning usa apenas treino e validação.
- **Exemplo mínimo:** classificação desbalanceada usa `StratifiedKFold(5, shuffle=True, random_state=42)`; séries usam cortes crescentes sem embaralhar.
- **Erro comum:** escolher hiperparâmetros pelo teste; mantenha-o isolado até a avaliação final.

#### O que fazer

- [ ] Compare KFold, StratifiedKFold e validação temporal em um exemplo apropriado.
- [ ] Execute cross-validation com cinco folds e registre média e desvio das métricas.
- [ ] Faça `RandomizedSearchCV` com espaço pequeno e limite de tempo.

- [ ] Separe conjunto de teste final e não o use durante tuning.
- [ ] Compare melhor configuração com padrão e avalie se ganho compensa complexidade.


- [ ] **Em `atividades/02-validacao-cruzada-e-tuning/dia-062-validacao-cruzada-e-tuning.ipynb`:** Compare StratifiedKFold com 3 e 5 folds usando a mesma pipeline e registre média, desvio e tempo.
- [ ] **Em `atividades/02-validacao-cruzada-e-tuning/dia-062-validacao-cruzada-e-tuning.ipynb`:** Confirme no código que o conjunto de teste final não aparece em fit, busca de parâmetros ou escolha da configuração.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

# Pré-projeto e banca zero do TCC — roteiro sem respostas

> Preencha os campos com decisões próprias e evidências. Não apague os enunciados nem transforme exemplos em resultados.

## Identificação

- **Título:** Do risco de churn ao efeito incremental: priorização de campanhas de retenção em telecom sob restrição de capacidade.
- **Usuário da entrega:**
- **Decisão apoiada:**
- **Por que essa decisão importa:**

## 1. Perguntas separadas

### Pergunta preditiva

<!-- Quem apresenta risco de churn no horizonte definido? Escreva a sua formulação completa. -->

### Pergunta causal

<!-- Qual é o efeito incremental da campanha no piloto randomizado simulado? -->

### Por que uma resposta não substitui a outra

<!-- Explique com suas palavras. -->

## 2. Contrato temporal e capacidade

| Decisão a congelar | Valor escolhido | Justificativa | Como será testada |
|---|---|---|---|
| data/instante de decisão |  |  |  |
| horizonte do churn |  |  |  |
| unidade de análise |  |  |  |
| capacidade K por ciclo |  |  |  |
| período de treino |  |  |  |
| período de validação |  |  |  |
| período de teste |  |  |  |
| período do piloto sintético |  |  |  |

## 3. Dados sintéticos e ética

- regra de geração e seed:
- campos disponíveis na decisão:
- alvo de churn e quando fica observável:
- tratamento e desfecho do piloto:
- como a randomização será simulada e verificada:
- frase obrigatória declarando que os dados e o piloto são sintéticos:
- afirmações que os dados não permitem fazer sobre clientes reais:

## 4. Métodos congelados

| Componente | Abordagem obrigatória | Papel no estudo | Critério de comparação |
|---|---|---|---|
| baseline | regra de negócio |  |  |
| modelo 1 | regressão logística |  |  |
| modelo 2 | XGBoost |  |  |
| experimento | piloto randomizado simulado |  |  |

## 5. Métricas e decisão

Preencha definição, unidade e limite antes de observar resultados.

| Métrica | Definição operacional | Critério/limite | Risco de interpretação |
|---|---|---|---|
| PR-AUC |  |  |  |
| recall@K |  |  |  |
| calibração |  |  |  |
| custo por retenção |  |  |  |
| efeito e intervalo de confiança |  |  |  |
| ganho por 100 contatos |  |  |  |
| slices |  |  |  |

## 6. Ciclo de vida mínimo

- experimento e artefatos que serão registrados no MLflow:
- testes de schema:
- testes de leakage temporal:
- testes das métricas:
- monitoramento temporal:
- regra champion/challenger:
- gatilho de retreino:
- gatilho e procedimento de rollback:

## 7. Fora do escopo

Confirme o corte e explique por que cada item não é necessário:

- controle sintético;
- múltiplas nuvens;
- LLM ou entity matching;
- forecasting;
- aplicação grande.

## 8. Banca zero

- duração cronometrada:
- objeção mais forte recebida:
- resposta baseada em evidência:
- item cortado:
- critério acrescentado:
- principal limitação que continuará aberta:

## Aceite

- O pré-projeto diferencia risco de churn de resposta ao tratamento.
- As decisões temporais, capacidade, métricas e custos foram congelados.
- O piloto está rotulado como simulado em todas as partes.
- Nenhum item fora do escopo foi reintroduzido.

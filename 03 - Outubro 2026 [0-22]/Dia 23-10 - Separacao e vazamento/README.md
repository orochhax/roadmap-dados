# Separação e vazamento

## Aprenda agora

Treino ajusta o modelo, validação orienta escolhas e teste estima o resultado final. Estratificação preserva a proporção do alvo; corte temporal preserva a ordem real.

```python
from sklearn.model_selection import train_test_split

X_treino, X_temp, y_treino, y_temp = train_test_split(
    X, y, test_size=0.4, stratify=y, random_state=42
)
```

**Erro comum:** ajustar imputação, escala ou seleção de variáveis antes da separação.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-042-separacao-e-vazamento.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

## Núcleo essencial

1. [ ] Separe treino, validação e teste com proporção definida e compare a distribuição do alvo com e sem estratificação.
2. [ ] Classifique colunas como disponíveis no momento da previsão ou como vazamento, justificando o momento em que surgem.
3. [ ] Desenhe um corte temporal simples e explique por que nenhum registro futuro pode participar do treino.

## Prática obrigatória

- [ ] Crie as três features com leakage apenas como exemplo identificado, sem usá-las em um modelo ainda.
- [ ] Escreva um checklist curto de cinco perguntas para detectar vazamento.
- [ ] Compare split aleatório e temporal usando a mesma métrica e explique qual representa melhor o uso real.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

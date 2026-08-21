# Intervalos de confiança

## Aprenda agora

Um intervalo de 95% para a média tem a forma `média ± valor_crítico × erro_padrão`; com desvio populacional desconhecido, use a distribuição t.

```python
from scipy import stats

media = amostra.mean()
se = stats.sem(amostra)
ic95 = stats.t.interval(0.95, len(amostra) - 1, loc=media, scale=se)
```

**Erro comum:** dizer que há 95% de probabilidade de o parâmetro fixo estar dentro de um intervalo já calculado.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-036-intervalos-de-confianca.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/incidentes.csv` e dados sintéticos gerados no notebook com seed 42.

## Núcleo essencial

1. [ ] Calcule um intervalo de confiança de 95% para a média manualmente e com biblioteca, declarando as suposições usadas.
2. [ ] Compare a largura do intervalo em amostras de tamanho 20 e 100.
3. [ ] Escreva a interpretação correta do intervalo sem atribuir probabilidade ao parâmetro fixo.

## Prática obrigatória

- [ ] Compare intervalos de 90%, 95% e 99% e explique o efeito do nível de confiança na largura.
- [ ] **Em `01-exercicios/dia-036-intervalos-de-confianca.ipynb`:** Calcule IC de 95% para as primeiras 50 durações por método paramétrico e bootstrap com seed 42; compare as larguras.
- [ ] **Em `01-exercicios/dia-036-intervalos-de-confianca.ipynb`:** Repita com uma amostra constante [60, 60, 60, 60, 60] e trate explicitamente a ausência de variabilidade.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

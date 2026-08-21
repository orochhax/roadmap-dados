# Probabilidade básica

## Aprenda agora

Probabilidade condicional restringe o universo: `P(A|B) = P(A e B) / P(B)`. Em uma tabela 2x2, use como denominador apenas o grupo condicionado.

```python
prob_churn_dado_reclamacao = clientes_com_churn_e_reclamacao / clientes_com_reclamacao
```

Dois eventos são independentes quando `P(A|B) = P(A)`.

**Erro comum:** usar o total da base como denominador de uma probabilidade condicional.

## Preparação

- **Pasta/arquivo principal:** `01-exercicios/dia-032-probabilidade-basica.ipynb`.
- **Dados:** `dados/clientes_telecom.csv`, `dados/incidentes.csv` e dados sintéticos gerados no notebook com seed 42.

## Núcleo essencial

1. [ ] Resolva os problemas 1–6 de probabilidade, identificando antes de calcular o espaço amostral e o evento pedido.
2. [ ] Construa uma tabela 2x2 pequena e use-a para interpretar uma probabilidade condicional.
3. [ ] Simule lançamentos com NumPy e compare frequência observada e probabilidade teórica em dois tamanhos de amostra.

## Prática obrigatória

- [ ] **Em `01-exercicios/dia-032-probabilidade-basica.ipynb`:** Refaça o problema de Bayes com 2.000 clientes, 160 churns, sensibilidade de 75% e falso positivo de 10%.
- [ ] **Em `01-exercicios/dia-032-probabilidade-basica.ipynb`:** Simule 100, 1.000 e 10.000 lançamentos da mesma moeda com seed 42 e compare a distância entre frequência e probabilidade teórica.
- [ ] Crie dois eventos independentes e dois dependentes em dados sintéticos e mostre numericamente a diferença.

## Concluído quando

- [ ] Concluí todos os itens do Núcleo essencial no artefato indicado.
- [ ] Registrei as saídas pedidas e conferi pelo menos um resultado.
- [ ] Testei uma variação ou caso de borda e documentei o efeito.

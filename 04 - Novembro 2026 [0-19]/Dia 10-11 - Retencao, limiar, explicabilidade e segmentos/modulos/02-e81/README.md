# Explicabilidade e segmentos

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-073-explicabilidade-e-segmentos.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

## Aprenda agora

- **Definição:** suporte é o número de casos do segmento; métricas com pouco suporte são instáveis.
- **Exemplo mínimo:** publique `segmento, n, taxa_real, taxa_prevista, erro` e sinalize `n < 30`.
- **Erro comum:** concluir diferença relevante com grupos raros sem intervalo ou alerta.

## Núcleo essencial

1. [ ] Produza importância global e explicações individuais para 12 clientes.
2. [ ] Crie segmentos acionáveis combinando risco, valor e motivo provável.
3. [ ] Verifique desempenho por cidade e plano.

## Prática obrigatória

- [ ] Identifique possíveis vieses e grupos com baixo suporte.
- [ ] Escreva exemplos de mensagens operacionais para o time de retenção sem expor informações sensíveis.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-073-explicabilidade-e-segmentos.ipynb`:** Explique três clientes de alto risco e alto valor e três de alto risco e baixo valor com o mesmo método.
- [ ] **Em `01-exercicios/dia-073-explicabilidade-e-segmentos.ipynb`:** Compare recall e precision entre Salvador e Feira de Santana e informe o número de casos em cada cidade.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-073-explicabilidade-e-segmentos.ipynb` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

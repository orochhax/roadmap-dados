# Limiar e estratégia de retenção

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-072-limiar-e-estrategia-de-retencao.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

## Aprenda agora

- **Definição:** limiar transforma probabilidade em ação; benefício esperado desconta ação e erros; break-even iguala ganho e custo.
- **Exemplo mínimo:** `valor = VP×benefício - FP×custo_contato - FN×perda`; calcule em cada limiar.
- **Erro comum:** usar 0,5 automaticamente ou otimizar F1 sem representar a decisão.

## Núcleo essencial

1. [ ] Calcule custo e volume de campanhas para 20 limiares entre 0.05 e 0.95.
2. [ ] Defina três estratégias de retenção por risco e valor do cliente.
3. [ ] Simule orçamento limitado e selecione os clientes com maior benefício esperado.

## Prática obrigatória

- [ ] Calcule retorno estimado e ponto de equilíbrio.
- [ ] Crie regras de exclusão para evitar ofertas inadequadas.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-072-limiar-e-estrategia-de-retencao.ipynb`:** Simule orçamento suficiente para abordar somente 100 clientes e selecione pelo maior benefício esperado.
- [ ] **Em `01-exercicios/dia-072-limiar-e-estrategia-de-retencao.ipynb`:** Aumente o custo da campanha em 50% e recalcule retorno e ponto de equilíbrio sem alterar probabilidades.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-072-limiar-e-estrategia-de-retencao.ipynb` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

# Definição do produto integrador

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-116-definicao-do-produto-integrador.ipynb`.
- **Entradas:** escolha `dados/clientes_telecom.csv`, `dados/pedidos.csv` ou `projetos/assistente-suporte-ia/data/corpus/`. **Fallback local:** fixture versionada.

## Manifesto de entradas

- **Obrigatórias:** opções de produto, dados locais permitidos e restrições em `product_brief.md`.
- **Fallback local:** use uma fixture pequena versionada quando a fonte externa não estiver disponível.

## Aprenda agora

- **Definição:** MoSCoW separa Must, Should, Could e Won't; Must é indispensável ao valor e à demonstração.
- **Exemplo mínimo:** “entrada validada” e “decisão reproduzível” são Must; tema visual extra é Could; integração sem dados é Won't.
- **Erro comum:** classificar tudo como Must ou priorizar pela tecnologia mais interessante.

## Núcleo essencial

1. [ ] Escolha um produto integrador entre churn, crédito, forecasting ou RAG e defina usuário, decisão e valor.
2. [ ] Escreva escopo de cinco dias com backlog priorizado MoSCoW.
3. [ ] Desenhe arquitetura e fluxo de dados.

## Prática obrigatória

- [ ] **Em `01-exercicios/dia-116-definicao-do-produto-integrador.ipynb`:** defina uma métrica técnica, uma de negócio e uma de experiência; acrescente ao backlog um caso de usuário com entrada incompleta e classifique-o como Must, Should, Could ou Won't.
- [ ] **Em `01-exercicios/dia-116-definicao-do-produto-integrador.ipynb`:** Reduza o prazo de cinco para três dias e registre quais dois itens serão cortados sem remover o valor principal.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-116-definicao-do-produto-integrador.ipynb` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

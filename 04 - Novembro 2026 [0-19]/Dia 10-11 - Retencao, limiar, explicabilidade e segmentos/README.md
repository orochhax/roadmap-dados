# Limiar e estrategia de retencao + Explicabilidade e segmentos

**Data de estudo:** 10/11/2026  
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Limiar e estrategia de retencao

#### O que pesquisar
- `Limiar e estrategia de retencao Python explicado passo a passo`
- `Limiar e estrategia de retencao Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-limiar-e-estrategia`](<atividades/01-limiar-e-estrategia/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-limiar-e-estrategia/dia-072-limiar-e-estrategia-de-retencao.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que você precisa entender

- **Definição:** limiar transforma probabilidade em ação; benefício esperado desconta ação e erros; break-even iguala ganho e custo.
- **Exemplo mínimo:** `valor = VP×benefício - FP×custo_contato - FN×perda`; calcule em cada limiar.
- **Erro comum:** usar 0,5 automaticamente ou otimizar F1 sem representar a decisão.

#### O que fazer

- [ ] Calcule custo e volume de campanhas para 20 limiares entre 0.05 e 0.95.
- [ ] Defina três estratégias de retenção por risco e valor do cliente.
- [ ] Simule orçamento limitado e selecione os clientes com maior benefício esperado.

- [ ] Calcule retorno estimado e ponto de equilíbrio.
- [ ] Crie regras de exclusão para evitar ofertas inadequadas.


- [ ] **Em `atividades/01-limiar-e-estrategia/dia-072-limiar-e-estrategia-de-retencao.ipynb`:** Simule orçamento suficiente para abordar somente 100 clientes e selecione pelo maior benefício esperado.
- [ ] **Em `atividades/01-limiar-e-estrategia/dia-072-limiar-e-estrategia-de-retencao.ipynb`:** Aumente o custo da campanha em 50% e recalcule retorno e ponto de equilíbrio sem alterar probabilidades.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

### Atividade 2 — Explicabilidade e segmentos

#### O que pesquisar
- `Explicabilidade e segmentos Python explicado passo a passo`
- `Explicabilidade e segmentos Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-explicabilidade-e-segmentos`](<atividades/02-explicabilidade-e-segmentos/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-explicabilidade-e-segmentos/dia-073-explicabilidade-e-segmentos.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que você precisa entender

- **Definição:** suporte é o número de casos do segmento; métricas com pouco suporte são instáveis.
- **Exemplo mínimo:** publique `segmento, n, taxa_real, taxa_prevista, erro` e sinalize `n < 30`.
- **Erro comum:** concluir diferença relevante com grupos raros sem intervalo ou alerta.

#### O que fazer

- [ ] Produza importância global e explicações individuais para 12 clientes.
- [ ] Crie segmentos acionáveis combinando risco, valor e motivo provável.
- [ ] Verifique desempenho por cidade e plano.

- [ ] Identifique possíveis vieses e grupos com baixo suporte.
- [ ] Escreva exemplos de mensagens operacionais para o time de retenção sem expor informações sensíveis.


- [ ] **Em `atividades/02-explicabilidade-e-segmentos/dia-073-explicabilidade-e-segmentos.ipynb`:** Explique três clientes de alto risco e alto valor e três de alto risco e baixo valor com o mesmo método.
- [ ] **Em `atividades/02-explicabilidade-e-segmentos/dia-073-explicabilidade-e-segmentos.ipynb`:** Compare recall e precision entre Salvador e Feira de Santana e informe o número de casos em cada cidade.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

# Pré-projeto e banca zero do TCC

## Preparação
- **Enunciado local:** `01-exercicios/roteiro_atividades.md`.
- **Saída canônica:** `projetos/portfolio-intelligence-lab/docs/pre-projeto.md`.
- **Dados:** snapshot local permitido, com fonte, período e hash registrados.

## Manifesto de entradas

- **Obrigatórias:** `insumos_tcc.md`, fonte permitida, snapshot local e `projetos/portfolio-intelligence-lab/docs/pre-projeto.md`.
- **Fallback local:** use preços ajustados já versionados e limite o universo aos ativos completos na amostra.

## Aprenda agora

- **Definição:** preço ajustado incorpora eventos; universo define ativos elegíveis; rebalanceamento fixa quando a carteira muda; protocolo congela regras antes da análise.
- **Exemplo mínimo:** uma classe, 10–20 ativos, rebalanceamento mensal, duas features (momentum e volatilidade) e snapshot local versionado.
- **Erro comum:** ampliar classes ou trocar regra após observar o resultado.

## Núcleo essencial

1. [ ] Congele um TCC mínimo viável com uma única classe de 10–20 ativos, uma fonte acessível, rebalanceamento mensal e período histórico definido.
2. [ ] Escreva pré-projeto de até duas páginas com pergunta, usuário, dados, dois fatores, baseline, métricas e riscos.
3. [ ] Confirme na prática que a fonte de preços ajustados pode ser carregada antes de prometer análises adicionais.
4. [ ] Separe o escopo necessário dos itens cortados e remova tudo que não seja necessário para ranking, backtest e explicação.

## Prática obrigatória

- [ ] Grave a banca zero sem aumentar o escopo congelado.
- [ ] Formule a objeção sobre uso de informação futura e indique quais datas e validações deverão respondê-la.

## Concluído quando

- [ ] O núcleo foi executado e `projetos/portfolio-intelligence-lab/docs/pre-projeto.md` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

# Entrega do projeto

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/roteiro_atividades.md`.
- **Dados:** `dados/credito.csv`.

## Aprenda agora

- **Definição:** model card registra propósito, dados, métricas, limites e uso proibido; ambiente limpo confirma dependências e instruções.
- **Exemplo mínimo:** crie o ambiente de teste em `$env:TEMP`, fora do OneDrive; ative-o, rode `python -m pip install -r requirements.txt` e execute o comando principal.
- **Erro comum:** chamar a entrega de reproduzível sem testar instalação do zero ou sem registrar versão dos dados.

## Núcleo essencial

1. [ ] Entregue notebook ou scripts reproduzíveis, política de decisão e model card curto.
2. [ ] Valide calibração, custo e desempenho temporal do modelo escolhido.
3. [ ] Mostre desempenho em pelo menos um segmento relevante e registre risco de viés.
4. [ ] Crie README e resumo executivo de até duas páginas com limitações e revisão humana.

## Prática obrigatória

- [ ] Em um ambiente criado em `$env:TEMP`, instale `requirements.txt`, execute o comando principal e registre o resultado em `validacao_ambiente.md`.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Inclua no model card a métrica temporal final e o desempenho para contratos de baixa renda, com tamanho do grupo.
- [ ] **Em `01-exercicios/roteiro_atividades.md`:** Simule aumento de 20% na taxa de default e registre qual regra da política precisaria de revisão.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/roteiro_atividades.md` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

# Entrega do projeto

**Data de estudo:** 26/01/2027
**Carga planejada:** 2 a 4 horas

## Atividades do dia

### Atividade 1 — Entrega do projeto

#### O que pesquisar
- `Entrega do projeto Python explicado passo a passo`
- `Entrega do projeto Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-entrega-do-projeto`](<atividades/01-entrega-do-projeto/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-entrega-do-projeto/roteiro_atividades.md`.
- **Dados:** `dados/credito.csv`.

#### O que você precisa entender

- **Definição:** model card registra propósito, dados, métricas, limites e uso proibido; ambiente limpo confirma dependências e instruções.
- **Exemplo mínimo:** crie o ambiente de teste em `$env:TEMP`, fora do OneDrive; ative-o, rode `python -m pip install -r requirements.txt` e execute o comando principal.
- **Erro comum:** chamar a entrega de reproduzível sem testar instalação do zero ou sem registrar versão dos dados.

#### O que fazer

- [ ] Entregue notebook ou scripts reproduzíveis, política de decisão e model card curto.
- [ ] Valide calibração, custo e desempenho temporal do modelo escolhido.
- [ ] Mostre desempenho em pelo menos um segmento relevante e registre risco de viés.
- [ ] Crie README e resumo executivo de até duas páginas com limitações e revisão humana.

- [ ] Em um ambiente criado em `$env:TEMP`, instale `requirements.txt`, execute o comando principal e registre o resultado em `validacao_ambiente.md`.


- [ ] **Em `atividades/01-entrega-do-projeto/roteiro_atividades.md`:** Inclua no model card a métrica temporal final e o desempenho para contratos de baixa renda, com tamanho do grupo.
- [ ] **Em `atividades/01-entrega-do-projeto/roteiro_atividades.md`:** Simule aumento de 20% na taxa de default e registre qual regra da política precisaria de revisão.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

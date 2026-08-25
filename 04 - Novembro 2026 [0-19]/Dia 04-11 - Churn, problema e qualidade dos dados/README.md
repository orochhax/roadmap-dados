# Definicao do case + Engenharia e qualidade dos dados

**Data de estudo:** 04/11/2026  
**Carga planejada:** 4 a 5 horas

## Aula selecionada no YouTube

- [ ] **Machine Learning 17: Projeto Churn - Sample** (52:23), da trilha **Machine Learning — Téo Me Why** — [pesquisar no YouTube](https://www.youtube.com/results?search_query=Machine+Learning+17+Projeto+Churn+Sample+Teo+Me+Why).

Use a aula para observar o início de um projeto real. A definição temporal de churn, o contrato de dados e as verificações de qualidade nos notebooks locais são obrigatórios.

## Atividades do dia

### Atividade 1 — Definicao do case

#### O que pesquisar
- `Definicao do case Python explicado passo a passo`
- `Definicao do case Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-definicao-do-case`](<atividades/01-definicao-do-case/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-definicao-do-case/dia-066-definicao-do-case.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que você precisa entender

- **Definição:** persona identifica quem decide; matriz compara opções por critérios; issue transforma necessidade em trabalho verificável.
- **Exemplo mínimo:** “analista decide quem contatar”; pontue impacto, esforço e risco de 1 a 5; issue contém contexto, aceite e evidência.
- **Erro comum:** descrever solução sem usuário, decisão ou critério de aceite.

#### O que fazer

- [ ] Defina o case de churn em telecom com pergunta: quais clientes têm risco de cancelar em 30 dias e quais ações de retenção são economicamente viáveis.
- [ ] Escreva personas dos usuários do produto: gerente de retenção, analista e atendente.
- [ ] Crie matriz de decisões com ação, custo, benefício, responsável e risco.

- [ ] Defina escopo mínimo do projeto e lista explícita do que ficará fora.


- [ ] **Em `atividades/01-definicao-do-case/dia-066-definicao-do-case.ipynb`:** Reduza o orçamento de retenção em 30% e marque quais ações do escopo mínimo seriam mantidas ou cortadas.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

### Atividade 2 — Engenharia e qualidade dos dados

#### O que pesquisar
- `Engenharia e qualidade dos dados Python explicado passo a passo`
- `Engenharia e qualidade dos dados Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-engenharia-e-qualidade-dos-dados`](<atividades/02-engenharia-e-qualidade-dos-dados/>)

#### Aulas complementares — proteção de dados

- [ ] Módulo 2 — **Cuidados ao manipular dados e recursos** (13:28).
- [ ] Módulo 2 — **Proteção de Dados** (18:17).
- Aplique as aulas ao notebook: preserve a base bruta, restrinja dados sensíveis nas evidências e documente qualquer transformação irreversível.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-engenharia-e-qualidade-dos-dados/dia-067-engenharia-e-qualidade-dos-dados.ipynb`.
- **Dados:** `dados/clientes_telecom.csv` e `dados/pedidos.csv`; crie resultados derivados somente nos passos indicados.

#### O que você precisa entender

- **Definição:** contrato fixa nomes, tipos, nulidade, domínio e unicidade; `fail` interrompe, enquanto quarentena separa registros suspeitos.
- **Exemplo mínimo:** `cliente_id: inteiro, não nulo, único`; inválidos vão a `rejeitados.csv` com motivo.
- **Erro comum:** corrigir silenciosamente e perder rastreabilidade.

#### O que fazer

- [ ] Carregue `clientes_telecom.csv`, valide esquema e gere relatório de qualidade por coluna.
- [ ] Defina regras de negócio para ausentes, duplicados, NPS fora de 0–10, mensalidade negativa e datas inconsistentes.
- [ ] Implemente função de validação que falhe com mensagens claras.

- [ ] Crie base analítica limpa e dicionário de dados.
- [ ] Registre quantidade de linhas alteradas ou removidas e impacto na taxa de churn.


- [ ] **Em `atividades/02-engenharia-e-qualidade-dos-dados/dia-067-engenharia-e-qualidade-dos-dados.ipynb`:** Crie uma linha com NPS=11 e outra com mensalidade=-1 e faça a validação listar os dois erros separadamente.
- [ ] **Em `atividades/02-engenharia-e-qualidade-dos-dados/dia-067-engenharia-e-qualidade-dos-dados.ipynb`:** Compare a taxa de churn antes e depois de remover somente registros realmente inválidos e registre quantas linhas mudaram.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

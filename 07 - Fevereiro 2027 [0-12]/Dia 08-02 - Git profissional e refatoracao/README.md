# Git profissional basico + Refatoracao de notebook

**Data de estudo:** 08/02/2027
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Git profissional basico

#### O que pesquisar
- `Git profissional basico Python explicado passo a passo`
- `Git profissional basico Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-git-profissional-basico`](<atividades/01-git-profissional-basico/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-git-profissional-basico/dia-091-git-profissional-basico.py`.
- **Entradas:** repositório descartável e três arquivos de teste criados nesta sessão. **Fallback local:** Git sem remoto.

#### O que você precisa entender

- **Definição:** branch isola trabalho; PR registra revisão; `restore` desfaz arquivo local; `revert` cria commit que desfaz um commit; tag nomeia uma versão.
- **Exemplo mínimo:** em repositório descartável, use `git switch -c teste`, faça commit, mescle e pratique `git revert <hash>`.
- **Erro comum:** usar comando destrutivo no projeto real sem conferir `git status` e o alvo.

#### O que fazer

- [ ] Crie branch `feature/refatoracao`, faça três commits pequenos e abra Pull Request para si mesmo.
- [ ] Pratique `git status`, `diff`, `log`, `restore`, `revert` e resolução de conflito.
- [ ] Crie conflito intencional em duas branches e documente como resolveu.

- [ ] Defina um padrão curto de mensagens de commit e crie um template de Pull Request com teste e evidência.
- [ ] **Em `atividades/01-git-profissional-basico/dia-091-git-profissional-basico.py`:** faça um commit de teste e use `git revert` para desfazê-lo sem apagar o histórico; registre os comandos.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

### Atividade 2 — Refatoracao de notebook

#### O que pesquisar
- `Refatoracao de notebook Python explicado passo a passo`
- `Refatoracao de notebook Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-refatoracao-de-notebook`](<atividades/02-refatoracao-de-notebook/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-refatoracao-de-notebook/train.py`.
- **Entradas:** notebook indicado e `dados/clientes_telecom.csv`. **Fallback local:** amostra fixa de 100 linhas.

#### O que você precisa entender

- **Definição:** refatorar muda a estrutura sem mudar o comportamento; `src/` concentra código reutilizável, configuração guarda parâmetros e entrypoint inicia o fluxo.
- **Exemplo mínimo:** mova uma função do notebook para `src/features.py`, importe-a e compare a saída antes e após a mudança.
- **Erro comum:** misturar refatoração com nova lógica sem teste de equivalência.

#### O que fazer

- [ ] Escolha notebook de ML e liste células de configuração, ingestão, funções, treino e apresentação.
- [ ] Extraia funções para `src/`, parâmetros para `config.yaml` ou módulo e dependências para `requirements.txt`.
- [ ] Transforme execução principal em script `train.py`.

- [ ] Execute o fluxo do zero, confirme que o notebook importa as funções sem duplicá-las e compare as métricas com a referência anterior.
- [ ] **Em `atividades/02-refatoracao-de-notebook/train.py`:** use um caminho de dados inexistente e produza uma mensagem que identifique exatamente o arquivo ausente.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

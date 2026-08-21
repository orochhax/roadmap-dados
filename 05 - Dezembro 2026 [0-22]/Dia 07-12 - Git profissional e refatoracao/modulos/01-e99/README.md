# Git profissional básico

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-091-git-profissional-basico.py`.
- **Entradas:** repositório descartável e três arquivos de teste criados nesta sessão. **Fallback local:** Git sem remoto.

## Aprenda agora

- **Definição:** branch isola trabalho; PR registra revisão; `restore` desfaz arquivo local; `revert` cria commit que desfaz um commit; tag nomeia uma versão.
- **Exemplo mínimo:** em repositório descartável, use `git switch -c teste`, faça commit, mescle e pratique `git revert <hash>`.
- **Erro comum:** usar comando destrutivo no projeto real sem conferir `git status` e o alvo.

## Núcleo essencial

1. [ ] Crie branch `feature/refatoracao`, faça três commits pequenos e abra Pull Request para si mesmo.
2. [ ] Pratique `git status`, `diff`, `log`, `restore`, `revert` e resolução de conflito.
3. [ ] Crie conflito intencional em duas branches e documente como resolveu.

## Prática obrigatória

- [ ] Defina um padrão curto de mensagens de commit e crie um template de Pull Request com teste e evidência.
- [ ] **Em `01-exercicios/dia-091-git-profissional-basico.py`:** faça um commit de teste e use `git revert` para desfazê-lo sem apagar o histórico; registre os comandos.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-091-git-profissional-basico.py` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

# CI e versão estável

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/roteiro_atividades.md`.
- **Entradas:** repositório local com `src/`, `tests/` e `requirements.txt`. **Fallback local:** comandos da CI no terminal.

## Aprenda agora

- **Definição:** CI executa verificações em cada mudança; SemVer usa `MAJOR.MINOR.PATCH`; changelog explica alterações e release congela artefatos.
- **Exemplo mínimo:** workflow instala dependências e roda `ruff check .` e `pytest -q`; correção compatível incrementa PATCH.
- **Erro comum:** criar badge verde com testes que não executam o comando real do projeto.

## Núcleo essencial

1. [ ] Crie workflow de CI que instale dependências e rode testes em cada push/PR.
2. [ ] Adicione badge de testes ao README.
3. [ ] Quebre um teste propositalmente para verificar bloqueio.
4. [ ] Corrija e gere release `v1.0.0` com changelog.

## Prática obrigatória

- [ ] **Em `01-exercicios/roteiro_atividades.md`:** confirme que `pytest` e a verificação de formatação rodam em Pull Request.
- [ ] Faça a revisão final com um checklist de Pull Request e registre separadamente o commit da falha controlada e o da correção.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/roteiro_atividades.md` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

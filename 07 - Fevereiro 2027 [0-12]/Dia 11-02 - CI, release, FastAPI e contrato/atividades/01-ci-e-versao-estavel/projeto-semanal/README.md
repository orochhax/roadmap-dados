# Projeto — Do notebook ao pacote testável

## Manifesto de entradas

- **Obrigatórias:** pacote `src/`, testes, fixture local, dependências e comportamentos esperados.
- **Saídas:** workflow de CI, badge, changelog e release.
- **Fallback local:** execute CI equivalente com `ruff` e `pytest` localmente se a plataforma remota não estiver disponível.

## Entregas obrigatórias
1. Configure a CI para executar `ruff check .` e `pytest -q` em cada push e pull request.
2. Adicione o badge, provoque uma falha controlada e confirme que a CI bloqueia a mudança.
3. Corrija a falha e publique a versão `v1.0.0` com changelog.

## Concluído quando

- Clone/ambiente limpo instala e executa pelo README.
- CI ou execução equivalente passa em lint e testes.
- A release identifica código, dependências e mudanças.

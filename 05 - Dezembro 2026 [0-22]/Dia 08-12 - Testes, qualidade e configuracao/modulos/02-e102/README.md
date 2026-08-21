# Qualidade e configuração

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-094-qualidade-e-configuracao.py`.
- **Entradas:** pacote local, `requirements.txt` e `.env.example`. **Fallback local:** valores fictícios sem segredo.

## Aprenda agora

- **Definição:** Black formata, Ruff analisa, type hints documentam tipos, variáveis de ambiente separam segredo e logging registra eventos.
- **Exemplo mínimo:** `python -m ruff check .`, `python -m black --check .`; publique `.env.example`, nunca `.env`.
- **Erro comum:** registrar segredo no log ou confiar em type hint como validação em tempo de execução.

## Núcleo essencial

1. [ ] Adicione formatação/lint com ferramentas como Black/Ruff e aplique ao projeto.
2. [ ] Separe configurações e segredos usando variáveis de ambiente; crie `.env.example` sem credenciais.
3. [ ] Adicione type hints às funções principais.

## Prática obrigatória

- [ ] **Em `01-exercicios/dia-094-qualidade-e-configuracao.py`:** adicione `MODEL_VERSION` ao `.env.example` e leia a configuração sem gravar segredo no repositório.
- [ ] Execute uma função com campo obrigatório ausente e registre um log `ERROR` sem incluir nome, documento ou conteúdo completo do cliente.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-094-qualidade-e-configuracao.py` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

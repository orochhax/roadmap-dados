# Testes + Qualidade e configuracao

**Data de estudo:** 08/12/2026  
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Testes

#### O que pesquisar
- `Testes Python explicado passo a passo`
- `Testes Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-testes`](<atividades/01-testes/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-testes/dia-093-testes.py`.
- **Entradas:** módulo indicado e fixture de `dados/clientes_telecom.csv`. **Fallback local:** cinco registros fixos.

#### O que você precisa entender

- **Definição:** teste unitário verifica uma unidade; integração verifica componentes; regressão preserva um comportamento corrigido. AAA significa Arrange, Act, Assert.
- **Exemplo mínimo:** `def test_total(): assert soma([2,3]) == 5`; execute `python -m pytest -q`.
- **Erro comum:** testar apenas que o código roda ou depender da ordem dos testes.

#### O que fazer

- [ ] Instale `pytest` e escreva testes para validação de dados, feature engineering e métrica de custo.
- [ ] Crie testes unitários com casos normais, borda e erro.
- [ ] Escreva um teste de integração do carregamento até previsão.

- [ ] **Em `atividades/01-testes/dia-093-testes.py`:** crie fixtures pequenas e teste duração negativa e divisão de custo quando `total=0`.
- [ ] Remova uma coluna obrigatória da fixture de integração, confirme a falha antes da previsão e restaure a correção.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

### Atividade 2 — Qualidade e configuracao

#### O que pesquisar
- `Qualidade e configuracao Python explicado passo a passo`
- `Qualidade e configuracao Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-qualidade-e-configuracao`](<atividades/02-qualidade-e-configuracao/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-qualidade-e-configuracao/dia-094-qualidade-e-configuracao.py`.
- **Entradas:** pacote local, `requirements.txt` e `.env.example`. **Fallback local:** valores fictícios sem segredo.

#### O que você precisa entender

- **Definição:** Black formata, Ruff analisa, type hints documentam tipos, variáveis de ambiente separam segredo e logging registra eventos.
- **Exemplo mínimo:** `python -m ruff check .`, `python -m black --check .`; publique `.env.example`, nunca `.env`.
- **Erro comum:** registrar segredo no log ou confiar em type hint como validação em tempo de execução.

#### O que fazer

- [ ] Adicione formatação/lint com ferramentas como Black/Ruff e aplique ao projeto.
- [ ] Separe configurações e segredos usando variáveis de ambiente; crie `.env.example` sem credenciais.
- [ ] Adicione type hints às funções principais.

- [ ] **Em `atividades/02-qualidade-e-configuracao/dia-094-qualidade-e-configuracao.py`:** adicione `MODEL_VERSION` ao `.env.example` e leia a configuração sem gravar segredo no repositório.
- [ ] Execute uma função com campo obrigatório ausente e registre um log `ERROR` sem incluir nome, documento ou conteúdo completo do cliente.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

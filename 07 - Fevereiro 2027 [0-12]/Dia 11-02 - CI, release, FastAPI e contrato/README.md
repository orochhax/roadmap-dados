# CI e versao estavel + FastAPI e contrato

**Data de estudo:** 11/02/2027
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — CI e versao estavel

#### O que pesquisar
- `CI e versao estavel Python explicado passo a passo`
- `CI e versao estavel Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-ci-e-versao-estavel`](<atividades/01-ci-e-versao-estavel/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-ci-e-versao-estavel/roteiro_atividades.md`.
- **Entradas:** repositório local com `src/`, `tests/` e `requirements.txt`. **Fallback local:** comandos da CI no terminal.

#### O que você precisa entender

- **Definição:** CI executa verificações em cada mudança; SemVer usa `MAJOR.MINOR.PATCH`; changelog explica alterações e release congela artefatos.
- **Exemplo mínimo:** workflow instala dependências e roda `ruff check .` e `pytest -q`; correção compatível incrementa PATCH.
- **Erro comum:** criar badge verde com testes que não executam o comando real do projeto.

#### O que fazer

- [ ] Crie workflow de CI que instale dependências e rode testes em cada push/PR.
- [ ] Adicione badge de testes ao README.
- [ ] Quebre um teste propositalmente para verificar bloqueio.
- [ ] Corrija e gere release `v1.0.0` com changelog.

- [ ] **Em `atividades/01-ci-e-versao-estavel/roteiro_atividades.md`:** confirme que `pytest` e a verificação de formatação rodam em Pull Request.
- [ ] Faça a revisão final com um checklist de Pull Request e registre separadamente o commit da falha controlada e o da correção.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

### Atividade 2 — FastAPI e contrato

#### O que pesquisar
- `FastAPI e contrato engenharia de dados e MLOps explicado passo a passo`
- `FastAPI e contrato engenharia de dados e MLOps exercícios práticos`

#### Aulas guiadas — Pydantic e FastAPI

- [ ] Procure no YouTube e assista a **Pydantic - Resolvendo um problemão do Python - Validação de Tipo de Dados** (11min22s).
- [ ] Procure no YouTube e assista a **Curso de FastAPI - Rest API com Python (Backend Completo) - Aula 02: Requisições e Roteamento da API** (33min21s).
- Total de vídeo deste bloco: 44min43s. Depois das aulas, aplique os conceitos ao contrato de inferência do roadmap, sem copiar o projeto de comércio eletrônico mostrado no curso.

**Arquivos da atividade:** [abrir a pasta `02-fastapi-e-contrato`](<atividades/02-fastapi-e-contrato/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-fastapi-e-contrato/dia-096-fastapi-e-contrato.py`.
- **Entradas:** schema, fixture de `dados/clientes_telecom.csv` e modelo mock. **Fallback local:** regra determinística.

#### O que você precisa entender

- **Definição:** FastAPI expõe rotas HTTP; Pydantic valida contrato; 2xx indica sucesso, 4xx erro da entrada e 5xx falha do serviço.
- **Exemplo mínimo:** `uvicorn app:app --reload` e `curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d "{}"`.
- **Erro comum:** retornar 200 para entrada inválida ou deixar schema diferente do usado no treino.

#### O que fazer

- [ ] Crie API FastAPI com endpoints `/health`, `/predict` e `/model-info`.
- [ ] Defina esquema de entrada com Pydantic e exemplos válidos/invalidos.
- [ ] Retorne probabilidade, classe, versão do modelo e aviso de uso.

- [ ] **Em `atividades/02-fastapi-e-contrato/dia-096-fastapi-e-contrato.py`:** teste um payload válido, outro sem `nps` e outro com `mensalidade='texto'` pela documentação automática e por cliente HTTP.
- [ ] Confirme códigos HTTP distintos para validação e falha interna e prove que entradas inválidas não retornam erro 500.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

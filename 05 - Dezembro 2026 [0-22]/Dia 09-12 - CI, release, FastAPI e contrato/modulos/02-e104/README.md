# FastAPI e contrato

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-096-fastapi-e-contrato.py`.
- **Entradas:** schema, fixture de `dados/clientes_telecom.csv` e modelo mock. **Fallback local:** regra determinística.

## Aprenda agora

- **Definição:** FastAPI expõe rotas HTTP; Pydantic valida contrato; 2xx indica sucesso, 4xx erro da entrada e 5xx falha do serviço.
- **Exemplo mínimo:** `uvicorn app:app --reload` e `curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d "{}"`.
- **Erro comum:** retornar 200 para entrada inválida ou deixar schema diferente do usado no treino.

## Núcleo essencial

1. [ ] Crie API FastAPI com endpoints `/health`, `/predict` e `/model-info`.
2. [ ] Defina esquema de entrada com Pydantic e exemplos válidos/invalidos.
3. [ ] Retorne probabilidade, classe, versão do modelo e aviso de uso.

## Prática obrigatória

- [ ] **Em `01-exercicios/dia-096-fastapi-e-contrato.py`:** teste um payload válido, outro sem `nps` e outro com `mensalidade='texto'` pela documentação automática e por cliente HTTP.
- [ ] Confirme códigos HTTP distintos para validação e falha interna e prove que entradas inválidas não retornam erro 500.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-096-fastapi-e-contrato.py` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

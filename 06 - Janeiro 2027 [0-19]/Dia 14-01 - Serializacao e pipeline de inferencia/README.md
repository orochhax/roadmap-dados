# Serialização e pipeline de inferência

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-097-serializacao-e-pipeline-de-inferencia.py`.
- **Entradas:** pipeline treinada e `dados/clientes_telecom.csv`. **Fallback local:** modelo pequeno com seed fixa.

## Aprenda agora

- **Definição:** serialização grava pipeline treinado; metadados identificam versão, schema, métricas e origem. Arquivo `joblib` só deve vir de fonte confiável.
- **Exemplo mínimo:** `joblib.dump(pipeline, "model.joblib")` e `joblib.load("model.joblib")`; salve `model_meta.json`.
- **Erro comum:** serializar só o estimador e esquecer pré-processamento ou carregar artefato desconhecido.

## Núcleo essencial

1. [ ] Serializa pipeline completa com `joblib` e registre versão, data e features esperadas.
2. [ ] Crie módulo de inferência que carrega o modelo uma vez.
3. [ ] Valide ordem, tipo e categorias de entrada.

## Prática obrigatória

- [ ] **Em `01-exercicios/dia-097-serializacao-e-pipeline-de-inferencia.py`:** compare 20 previsões com IDs fixos entre notebook e módulo carregado e liste diferenças maiores que `0,000001`.
- [ ] Teste modelo inexistente, arquivo corrompido e uma entrada com coluna extra `segredo`; trate e documente os três casos separadamente.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-097-serializacao-e-pipeline-de-inferencia.py` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

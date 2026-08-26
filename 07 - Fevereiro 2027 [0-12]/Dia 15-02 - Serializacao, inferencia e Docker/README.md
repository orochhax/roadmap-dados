# Serializacao e pipeline de inferencia + Docker

**Data de estudo:** 15/02/2027
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Serializacao e pipeline de inferencia

#### O que pesquisar
- `Serializacao e pipeline de inferencia engenharia de dados e MLOps explicado passo a passo`
- `Serializacao e pipeline de inferencia engenharia de dados e MLOps exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-serializacao-e-pipeline-de-inferencia`](<atividades/01-serializacao-e-pipeline-de-inferencia/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-serializacao-e-pipeline-de-inferencia/dia-097-serializacao-e-pipeline-de-inferencia.py`.
- **Entradas:** pipeline treinada e `dados/clientes_telecom.csv`. **Fallback local:** modelo pequeno com seed fixa.

#### O que você precisa entender

- **Definição:** serialização grava pipeline treinado; metadados identificam versão, schema, métricas e origem. Arquivo `joblib` só deve vir de fonte confiável.
- **Exemplo mínimo:** `joblib.dump(pipeline, "model.joblib")` e `joblib.load("model.joblib")`; salve `model_meta.json`.
- **Erro comum:** serializar só o estimador e esquecer pré-processamento ou carregar artefato desconhecido.

#### O que fazer

- [ ] Serializa pipeline completa com `joblib` e registre versão, data e features esperadas.
- [ ] Crie módulo de inferência que carrega o modelo uma vez.
- [ ] Valide ordem, tipo e categorias de entrada.

- [ ] **Em `atividades/01-serializacao-e-pipeline-de-inferencia/dia-097-serializacao-e-pipeline-de-inferencia.py`:** compare 20 previsões com IDs fixos entre notebook e módulo carregado e liste diferenças maiores que `0,000001`.
- [ ] Teste modelo inexistente, arquivo corrompido e uma entrada com coluna extra `segredo`; trate e documente os três casos separadamente.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

### Atividade 2 — Docker

#### O que pesquisar
- `Docker engenharia de dados e MLOps explicado passo a passo`
- `Docker engenharia de dados e MLOps exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-docker`](<atividades/02-docker/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-docker/dia-098-docker.py`.
- **Entradas:** API, `requirements.txt`, modelo mock e fixture. **Fallback local:** imagem sem serviço externo.

#### O que você precisa entender

- **Definição:** imagem é o pacote imutável; container é uma execução da imagem; Dockerfile descreve a construção; `.dockerignore` exclui arquivos.
- **Exemplo mínimo:** confirme `docker --version`; no terminal use `cd <pasta>`, `dir` (ou `ls`), confirme `Dockerfile`, rode `docker build -t api-local .` e `docker run --rm -p 8000:8000 api-local`.
- **Erro comum:** copiar segredos/dados para a imagem, executar como root sem necessidade ou esquecer de mapear a porta.

#### O que fazer

- [ ] Crie `Dockerfile` para a API com imagem enxuta, usuário não root quando possível e dependências fixadas.
- [ ] Crie `.dockerignore` e não copie dados sensíveis.
- [ ] Construa imagem, execute container e teste endpoints.

- [ ] **Em `atividades/02-docker/dia-098-docker.py`:** execute o container com `MODEL_VERSION=teste` e confirme que `/model-info` mostra a configuração recebida.
- [ ] Inicie sem o arquivo do modelo e faça a aplicação informar claramente a dependência ausente.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

# Docker

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-098-docker.py`.
- **Entradas:** API, `requirements.txt`, modelo mock e fixture. **Fallback local:** imagem sem serviço externo.

## Aprenda agora

- **Definição:** imagem é o pacote imutável; container é uma execução da imagem; Dockerfile descreve a construção; `.dockerignore` exclui arquivos.
- **Exemplo mínimo:** confirme `docker --version`; no terminal use `cd <pasta>`, `dir` (ou `ls`), confirme `Dockerfile`, rode `docker build -t api-local .` e `docker run --rm -p 8000:8000 api-local`.
- **Erro comum:** copiar segredos/dados para a imagem, executar como root sem necessidade ou esquecer de mapear a porta.

## Núcleo essencial

1. [ ] Crie `Dockerfile` para a API com imagem enxuta, usuário não root quando possível e dependências fixadas.
2. [ ] Crie `.dockerignore` e não copie dados sensíveis.
3. [ ] Construa imagem, execute container e teste endpoints.

## Prática obrigatória

- [ ] **Em `01-exercicios/dia-098-docker.py`:** execute o container com `MODEL_VERSION=teste` e confirme que `/model-info` mostra a configuração recebida.
- [ ] Inicie sem o arquivo do modelo e faça a aplicação informar claramente a dependência ausente.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-098-docker.py` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

# Projeto — API de scoring containerizada

## Manifesto de entradas

- **Obrigatórias:** API com saúde, previsão e versão, testes, Dockerfile, `.dockerignore` e fixture de requisições.
- **Saídas:** configuração de execução, teste ponta a ponta, documentação de consumo e medição de carga.
- **Fallback local:** use Uvicorn e Docker locais; hospedagem externa não é requisito.

## Entregas obrigatórias
1. Execute o serviço com Docker Compose ou com os comandos locais documentados.
2. Teste de ponta a ponta uma entrada válida, uma inválida e a ausência do artefato.
3. Documente o consumo da API e faça uma carga local leve, registrando p50, p95 e limites.
4. Compare p50 e p95 em dois níveis de concorrência local e registre o limite observado.

## Concluído quando

- Os contratos e códigos HTTP passam nos testes de ponta a ponta.
- O container responde pelo comando de execução documentado.
- Logs identificam versão e erro sem expor dados sensíveis.

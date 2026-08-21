# Publicação do serviço

## Conquista para o LinkedIn

- **Competências:** depois de subir o serviço, executar o teste ponta a ponta e explicar a arquitetura, adicione **FastAPI**, **Docker** e **APIs REST**.
- **Projetos ou Destaques:** publique o serviço somente com instruções de execução, limites conhecidos e evidência do teste.
- **Sobre:** acrescente uma frase sobre transformar modelos em APIs reproduzíveis apenas depois dessa entrega. Não troque o título profissional somente por concluir a aula.
- Consulte o [Guia de LinkedIn e evidências](<../../../../00 - Recursos Compartilhados/linkedin-e-evidencias.md>).

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/roteiro_atividades.md`.
- **Entradas:** API, Dockerfile, fixtures e variáveis fictícias. **Fallback local:** Compose e carga somente locais.

## Aprenda agora

- **Definição:** Compose descreve serviços, rede, portas e variáveis; teste de carga mede comportamento sob volume controlado.
- **Exemplo mínimo:** `docker compose up --build`, teste `/health`, envie 20 requisições locais e rode `docker compose down`.
- **Erro comum:** realizar carga em serviço externo sem autorização ou chamar execução local de implantação produtiva.

## Núcleo essencial

1. [ ] Publique localmente via Docker Compose ou em serviço gratuito compatível, quando disponível.
2. [ ] Execute teste de ponta a ponta com dados novos.
3. [ ] Crie página de documentação para consumidores da API.
4. [ ] Faça teste de carga leve e registre limites.

## Prática obrigatória

- [ ] Grave uma demonstração de cinco minutos do dado até a resposta, incluindo status e latência de uma entrada nova.
- [ ] **Em `01-exercicios/roteiro_atividades.md`:** interrompa o serviço do modelo ou use caminho inválido e confirme que a documentação permite diagnosticar e recuperar.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/roteiro_atividades.md` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

# Arquitetura e entrevista — folha de respostas

## Entradas

- Diagrama, métricas, logs, run IDs do MLflow e checklist técnico do projeto.
- Histórico do modelo ativo e `deployment_events.jsonl` com o rollback executado.

## Arquitetura

- [ ] Desenhe o fluxo: entrada → validação → modelo → resposta → log.
- [ ] Registre entrada, saída, responsabilidade e falha principal de cada componente.

## Perguntas 1–8 — núcleo essencial

> Responda sem consulta na primeira tentativa e marque a confiança de 0 a 5.

1. [ ] Qual diferença prática existe entre armazenamento de objetos, banco relacional e data warehouse?

**Confiança:**

**Resposta:**

2. [ ] Como você escolheria entre processamento local, Spark e serviço gerenciado para 10 GB por dia?

**Confiança:**

**Resposta:**

3. [ ] O que é menor privilégio em IAM e quais permissões separaria entre pipeline, cientista e API?

**Confiança:**

**Resposta:**

4. [ ] O que cada instrução principal de um Dockerfile faz e por que fixar dependências?

**Confiança:**

**Resposta:**

5. [ ] Como reduzir o tamanho da imagem e evitar executar o container como root?

**Confiança:**

**Resposta:**

6. [ ] Como definir o contrato do endpoint `/predict`, incluindo validação e versão do modelo?

**Confiança:**

**Resposta:**

7. [ ] Qual diferença existe entre erro de validação do cliente e falha interna da API?

**Confiança:**

**Resposta:**

8. [ ] Quais etapas mínimas colocaria em uma CI para um projeto de dados e ML?

**Confiança:**

**Resposta:**

## Revisão do núcleo

- [ ] Reescreva somente respostas das perguntas 1–8 com confiança abaixo de 3.
- [ ] Confira se o projeto está reproduzível e se o checklist registra limitações.

## Prática obrigatória

1. [ ] Adapte a arquitetura para crescimento de 10 GB para 1 TB por dia e identifique os dois componentes que mudam.
2. [ ] Simule indisponibilidade do serviço de modelo e explique health check, fallback e rollback.

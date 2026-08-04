# Arquitetura e entrevista — Dia 105

> Responda com suas palavras e exemplos dos projetos. Não há respostas prontas neste arquivo.

## Arquitetura obrigatória

1. [ ] Desenhe o fluxo: dados → ingestão → validação → features → treino → registro → API → monitoramento.
2. [ ] Em cada componente, escreva entrada, saída, responsável e falha principal.

## 15 perguntas de entrevista

1. [ ] Qual diferença prática existe entre armazenamento de objetos, banco relacional e data warehouse?

**Resposta:**

2. [ ] Como você escolheria entre processamento local, Spark e serviço gerenciado para 10 GB por dia?

**Resposta:**

3. [ ] O que é menor privilégio em IAM e quais permissões separaria entre pipeline, cientista e API?

**Resposta:**

4. [ ] O que cada instrução principal de um Dockerfile faz e por que fixar dependências?

**Resposta:**

5. [ ] Como reduzir tamanho de imagem e evitar executar o container como root?

**Resposta:**

6. [ ] Como definiria o contrato do endpoint `/predict`, incluindo validação e versão do modelo?

**Resposta:**

7. [ ] Qual diferença existe entre erro de validação do cliente e falha interna da API?

**Resposta:**

8. [ ] Quais etapas mínimas colocaria em uma CI para um projeto de dados e ML?

**Resposta:**

9. [ ] Por que um teste que passa localmente pode falhar na CI e como investigaria?

**Resposta:**

10. [ ] Diferencie drift de dados, drift de conceito e queda de performance.

**Resposta:**

11. [ ] Como monitoraria um modelo quando o rótulo real demora 90 dias para chegar?

**Resposta:**

12. [ ] Quais dados nunca deveriam aparecer em logs de uma API de clientes?

**Resposta:**

13. [ ] Como armazenaria segredos e o que faria se uma chave fosse enviada ao GitHub?

**Resposta:**

14. [ ] Desenhe uma estratégia de rollback quando o modelo novo aumenta erros em produção.

**Resposta:**

15. [ ] Como o sistema deve continuar funcionando se o serviço de modelo ficar indisponível?

**Resposta:**

## Simulação

- [ ] Grave uma entrevista de 30 minutos respondendo às 15 perguntas.
- [ ] Marque as respostas em que usou termos que não conseguiu explicar.
- [ ] Reescreva essas respostas com um exemplo real do roadmap.

## Exercícios extras específicos

1. [ ] Adapte a arquitetura para crescimento de 10 GB para 1 TB por dia e identifique os dois componentes que precisam mudar.
2. [ ] Simule indisponibilidade do serviço de modelo e explique health check, fallback e procedimento de rollback.

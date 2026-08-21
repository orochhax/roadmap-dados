# MLOps introdutorio

**Data de estudo:** 18/12/2026  
**Carga planejada:** 2 a 4 horas

## Como estudar

Você pode escolher vídeo, documentação, site ou IA. Pesquise os nomes abaixo, faça uma primeira tentativa sem solução pronta e guarde evidência executável.

## Assuntos para pesquisar

### Bloco 1 — MLOps introdutorio

Pesquise exatamente:

- `MLOps introdutorio Python explicado passo a passo`
- `MLOps introdutorio Python exercícios práticos`

Depois siga o [guia e os enunciados deste bloco](<modulos/01-e112/README.md>). Tente os exercícios antes de procurar uma implementação completa.

## Integração

Explique com suas palavras como os blocos se conectam em um fluxo de dados ou decisão. Execute um caso comum e um caso de borda de cada bloco e registre comandos, saídas e dúvidas nas evidências.


## Entrega real de portfólio

**Telecom Customer Intelligence — Data Engineering e MLOps**

Siga o [brief do projeto](<../../projetos/telecom-customer-intelligence/README.md>). A entrega precisa ter problema e usuário definidos, data card, dados reproduzíveis, baseline, métricas escolhidas antes do resultado, análise de erros, testes, README em português e inglês e apresentação de 2–3 minutos em inglês. Documente também resultados negativos.

## Publicação da semana no LinkedIn

- **Tema específico:** ciclo de vida do modelo — rastreamento no MLflow, champion/challenger, gate de promoção, retreinamento e rollback comprovado.
- **Tipo:** entrega.
- **Formato:** carrossel com diagrama do ciclo e tabela das duas runs, acompanhado de uma demonstração curta do rollback.
- **Artefato/evidência exigida:** dois run IDs reais, novo `.fit()`, `politica_promocao.md`, `model_card.md`, previsão após restaurar o champion e `deployment_events.jsonl` com promoção e rollback.

### Roteiro para preencher

- **Modelo e decisão:** [qual modelo é versionado e qual decisão ele apoia?]
- **Champion e challenger:** [quais versões/runs foram comparadas?]
- **Gate congelado:** [quais limites de qualidade e latência foram definidos antes da comparação?]
- **Teste de falha:** [qual degradação foi injetada e como foi detectada?]
- **Rollback:** [qual versão foi restaurada e qual previsão comprovou a recuperação?]
- **Resultado verificável:** [métricas, latência, IDs e caminho dos eventos]
- **Link:** [repositório, model card ou demonstração conferidos]

### Limitação obrigatória

Declare que promoção, retreinamento e rollback foram simulados em ambiente educacional e descreva o que faltaria para governança e operação reais.

### Cuidado contra afirmações falsas

Não diga que houve deploy produtivo, drift real de clientes ou rollback em sistema empresarial. Diferencie uma execução local registrada de uma operação de produção. A publicação não altera Competências ou headline antes das condições do guia central.

### Checklist de publicação

- [ ] Conferi os dois run IDs, versões de dados, seeds, métricas e latências.
- [ ] O gate publicado é o mesmo definido antes de observar o challenger.
- [ ] Recarreguei o champion restaurado e registrei uma previsão de verificação.
- [ ] Removi credenciais, endpoints privados e dados sensíveis.
- [ ] Mostrei uma limitação e o motivo técnico da decisão.
- [ ] **URL publicada:**
- [ ] **Data da publicação:**

## Concluído quando

- [ ] Estudei todos os assuntos e concluí os enunciados dos blocos sem copiar uma solução completa.
- [ ] Executei os artefatos, testei casos de borda e registrei resultados verificáveis.
- [ ] Expliquei a conexão entre os blocos, a decisão tomada e pelo menos uma limitação concreta.

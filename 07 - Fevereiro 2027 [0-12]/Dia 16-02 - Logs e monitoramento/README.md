# Logs e monitoramento basico

**Data de estudo:** 16/02/2027
**Carga planejada:** 2 a 4 horas

## Atividades do dia

### Atividade 1 — Logs e monitoramento basico

#### O que pesquisar
- `Logs e monitoramento basico Python explicado passo a passo`
- `Logs e monitoramento basico Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-logs-e-monitoramento-basico`](<atividades/01-logs-e-monitoramento-basico/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-logs-e-monitoramento-basico/dia-099-logs-e-monitoramento-basico.py`.
- **Entradas:** 20 requisições locais e schema de log. **Fallback local:** latências determinísticas em `baseline_monitoramento.json`.

#### O que você precisa entender

- **Definição:** log estruturado usa campos; p50 é a mediana e p95 cobre 95% das latências; drift é mudança da distribuição de entrada, previsão ou desempenho.
- **Exemplo mínimo:** grave `timestamp, request_id, status, latency_ms, model_version`; salve em `baseline_monitoramento.json` probabilidades, volume e janela de referência.
- **Erro comum:** registrar dados pessoais ou alertar sem baseline, janela e limite definidos.

#### O que fazer

- [ ] Adicione logs de requisição com tempo, status e versão sem registrar dados sensíveis.
- [ ] Meça contagem, latência e erros em 20 requisições válidas e cinco inválidas.
- [ ] Defina um alerta conceitual e escreva um runbook curto para investigá-lo.

- [ ] Gere `baseline_monitoramento.json`, compare uma amostra alterada e registre o sinal de drift junto das métricas operacionais.
- [ ] **Em `atividades/01-logs-e-monitoramento-basico/dia-099-logs-e-monitoramento-basico.py`:** simule 50 requisições com 200 ms adicionais, compare p50 e p95 e confirme que dez payloads inválidos são contados sem conteúdo sensível nos logs.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Publicação da semana no LinkedIn

- **Tema específico:** evolução de um notebook para um componente testado e observável, com CI, contrato de API, Docker e logs estruturados.
- **Tipo:** progresso.
- **Formato:** carrossel de arquitetura e engenharia com capturas do teste, CI, documentação OpenAPI, container local e um log útil.
- **Artefato/evidência exigida:** pacote refatorado, testes executados, run de CI, contrato da API, build/execução do container e `atividades/01-logs-e-monitoramento-basico/dia-099-logs-e-monitoramento-basico.py` com caso normal e falha diagnosticável.

### Roteiro para preencher

- **Estado inicial:** [qual fragilidade existia no notebook ou script?]
- **Mudança de engenharia:** [qual refatoração, teste ou contrato foi criado?]
- **Automação:** [qual comando/run de CI comprova a verificação?]
- **Observabilidade:** [qual campo do log ajudou a entender uma falha?]
- **Resultado verificável:** [tempo, status de testes, resposta da API ou outro resultado medido]
- **Próximo passo:** [o que ainda falta antes da publicação do serviço?]
- **Link/evidência:** [artefato acessível ou captura conferida]

### Limitação obrigatória

Explique que a execução ainda é local ou pré-release e indique o teste necessário antes de considerar o serviço publicável.

### Cuidado contra afirmações falsas

Use `protótipo local`, `pipeline de CI` ou `container testado` conforme a evidência. Não use `produção`, `alta disponibilidade` ou `monitoramento em tempo real` sem infraestrutura e medição correspondentes. Não altere Competências ou headline por causa deste post de progresso.

### Checklist de publicação

- [ ] Todas as capturas vieram de execuções reais desta semana.
- [ ] O status da CI, o contrato e o log correspondem à mesma versão do código.
- [ ] Removi tokens, variáveis secretas, dados de usuários e caminhos locais.
- [ ] Deixei explícito que é progresso e citei o próximo teste.
- [ ] Conferi qualquer link compartilhado.
- [ ] **URL publicada:**
- [ ] **Data da publicação:**

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

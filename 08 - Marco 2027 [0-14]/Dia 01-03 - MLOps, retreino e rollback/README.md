# MLOps introdutorio

**Data de estudo:** 01/03/2027
**Carga planejada:** 2 a 4 horas

## Atividades do dia

### Atividade 1 — MLOps introdutorio

#### O que pesquisar
- `MLOps introdutorio Python explicado passo a passo`
- `MLOps introdutorio Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-mlops-introdutorio`](<atividades/01-mlops-introdutorio/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-mlops-introdutorio/dia-104-mlops-introdutorio.py`.
- **Entradas:** `dados/clientes_telecom.csv`, run IDs do MLflow, `atividades/01-mlops-introdutorio/politica_promocao.md` e `atividades/01-mlops-introdutorio/model_card.md`.
- **Saídas obrigatórias:** modelo inicial, modelo retreinado, histórico de promoção e `deployment_events.jsonl` com rollback.

#### O que você precisa entender

- **Definição:** drift de dados muda entradas; de previsão muda scores; de conceito muda a relação com o alvo. PSI compara proporções: `Σ(a-e)ln(a/e)`.
- **Exemplo mínimo:** leia `baseline_monitoramento.json`; sem ele, gere baseline local da amostra. Defina alerta, responsável e ação de rollback.
- **Erro comum:** retreinar automaticamente por qualquer PSI sem confirmar qualidade, impacto e atraso do rótulo.
- **Retreinamento real:** exige executar novamente `.fit()` com um lote diferente; apenas descrever o processo não atende.
- **Rollback comprovado:** exige restaurar a versão anterior, recarregá-la e executar uma previsão de verificação.

#### O que fazer

- [ ] Treine e registre no MLflow um modelo inicial como champion, incluindo versão dos dados, seed, métricas, latência e artefato.
- [ ] Crie um novo lote rotulado, execute um novo `.fit()` e registre o modelo retreinado como challenger em outra run.
- [ ] Antes de comparar, preencha um gate de promoção com métrica mínima, tolerância de degradação e limite de latência; não altere esses limites depois de ver os resultados.
- [ ] Registre champion e challenger e controle o modelo ativo por alias ou ponteiro versionado.
- [ ] Aponte temporariamente para o challenger, injete uma queda controlada de performance e execute rollback para o champion anterior.
- [ ] Recarregue o modelo restaurado, faça uma previsão de verificação e grave `deployment_events.jsonl` com versões, motivo, decisão e resultado.
- [ ] Complete o model card com uso, métricas, gatilho de retreinamento, limitações, aprovação e responsável.

- [ ] **Em `atividades/01-mlops-introdutorio/dia-104-mlops-introdutorio.py`:** Defina alerta de drift quando PSI superar 0,20 e registre quem revisa e em quanto tempo.
- [ ] **Em `atividades/01-mlops-introdutorio/dia-104-mlops-introdutorio.py`:** Simule challenger 2% melhor na métrica, mas 4 vezes mais lento; aplique os critérios do model card para decidir.

#### Atualização do LinkedIn — após concluir

- **Evidência exigida:** duas runs reais, novo `.fit()`, gate preenchido, promoção simulada, rollback e recarga da versão anterior.
- **Competências:** adicione **MLOps** e **Monitoramento de modelos**.
- **Sobre:** acrescente uma frase concreta sobre pipelines reproduzíveis com rastreamento, monitoramento, retreinamento e rollback usando MLflow.
- **Headline:** mantenha a atual até o marco de currículo e narrativa.

#### Como validar

- Retreinamento, gate, promoção e rollback foram executados e registrados com identificadores de versão.
- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

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

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

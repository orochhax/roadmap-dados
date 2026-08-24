# Entrega do pipeline

**Data de estudo:** 04/12/2026  
**Carga planejada:** 2 a 4 horas

## Atividades do dia

### Atividade 1 — Entrega do pipeline

#### O que pesquisar
- `Entrega do pipeline engenharia de dados e MLOps explicado passo a passo`
- `Entrega do pipeline engenharia de dados e MLOps exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-entrega-do-pipeline`](<atividades/01-entrega-do-pipeline/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-entrega-do-pipeline/roteiro_atividades.md`.
- **Entradas:** `dados/pedidos.csv`, schema, configuração e regras. **Fallback local:** Python com DuckDB/Parquet.

#### O que você precisa entender

- **Definição:** entrega de pipeline exige contrato entre etapas: fonte, schema, chave, saída, regra de reexecução e evidência de auditoria.
- **Exemplo mínimo:** tabela `etapa | entrada | saída | linhas | hash | status | duração`; uma execução completa preenche todas as linhas.
- **Erro comum:** validar cada script isolado sem testar o fluxo integral e uma falha controlada.

#### O que fazer

- [ ] Empacote pipeline da semana com script de execução única.
- [ ] Adicione validações de esquema, unicidade, nulos e limites.
- [ ] Produza tabela de auditoria com data, status, linhas de entrada, saída e erro.
- [ ] Rode duas vezes e com dados novos para provar idempotência/incremento correto.

- [ ] **Em `atividades/01-entrega-do-pipeline/roteiro_atividades.md`:** execute a pipeline com uma linha duplicada e registre na auditoria quantas linhas foram rejeitadas.
- [ ] Publique README de arquitetura, execução, testes, regras de reexecução e limitações.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Publicação da semana no LinkedIn

- **Tema específico:** pipeline idempotente de dados — ingestão, qualidade, orquestração, backfill e falha controlada antes da camada publicada.
- **Tipo:** entrega.
- **Formato:** diagrama de arquitetura acompanhado de um vídeo ou sequência de capturas de uma execução normal, um backfill e uma falha de qualidade.
- **Artefato/evidência exigida:** pipeline e DAG executados, contrato de dados, teste de qualidade, logs de retry/backfill, reconciliação de contagens e relatório em `atividades/01-entrega-do-pipeline/projeto-semanal/`.

### Roteiro para preencher

- **Origem e destino:** [quais dados entram e qual camada é publicada?]
- **Contrato e qualidade:** [qual regra interrompe dados inválidos?]
- **Fluxo:** [quais etapas aparecem no diagrama e em que ordem?]
- **Teste de idempotência:** [qual lote foi reprocessado e como a ausência de duplicação foi comprovada?]
- **Falha controlada:** [qual erro foi injetado, qual log apareceu e como houve recuperação?]
- **Resultado verificável:** [contagens, duração ou status e caminho da evidência]
- **Link:** [repositório, relatório ou demonstração conferidos]

### Limitação obrigatória

Declare quais partes foram executadas apenas localmente e o que faltaria para operar esse pipeline com volume, segurança e SLA reais.

### Cuidado contra afirmações falsas

Não chame uma DAG local de pipeline em produção nem declare escala que não foi medida. Não exponha credenciais, nomes de buckets privados ou dados sensíveis. A publicação não antecipa Competências ou headline.

### Checklist de publicação

- [ ] Executei caso normal, backfill e falha controlada.
- [ ] Reconciliei entrada, rejeições e saída sem duplicações.
- [ ] Conferi o diagrama contra o código e os logs reais.
- [ ] Removi credenciais, identificadores privados e dados sensíveis.
- [ ] Registrei ambiente, limitação e link reproduzível.
- [ ] **URL publicada:**
- [ ] **Data da publicação:**

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

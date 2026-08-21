# Evidências — N23: IAM e Cloud Storage

Não cole credenciais, tokens, IDs sensíveis ou e-mails completos. Substitua trechos identificáveis por `[REDACTED]`.

## Ambiente e orçamento

- projeto parcialmente ocultado:
- região e justificativa:
- conta/free tier/lab utilizado:
- alerta e limite de orçamento:
- versões de `gcloud` e componentes:

## Arquitetura e IAM

- diagrama ou descrição do fluxo produtor → raw → quarantine:
- service account parcialmente ocultada:
- papéis concedidos e escopo de cada vínculo:
- papel amplo considerado e recusado:
- prevenção de acesso público/acesso uniforme:
- regra de versionamento/lifecycle:

## Provas de execução

| teste | identidade | ação esperada | resultado | evidência redigida |
|---|---|---|---|---|
| upload válido |  | permitir |  |  |
| leitura contratada |  |  |  |  |
| exclusão indevida |  | negar |  |  |
| acesso público |  | negar |  |  |
| checksum divergente |  | quarentena |  |  |

## Reconciliação e custo

- objetos, linhas e bytes esperados/obtidos:
- checksums verificados:
- duração e falhas dos uploads:
- custo observado:
- cálculo para 1 GB/dia por 30 dias e premissas:

## Limpeza e decisão

- recursos removidos e comando usado:
- recursos mantidos e motivo:
- landing zone aprovada/rejeitada:
- risco remanescente antes do BigQuery:

# GCP prático: IAM e landing zone no Cloud Storage

## Objetivo

Construir a entrada real do pipeline **Telecom Customer Intelligence** na Google Cloud. Você criará um bucket para eventos diários, separará dados brutos de arquivos rejeitados, configurará retenção/ciclo de vida e provará por teste positivo e negativo que uma service account tem apenas as permissões necessárias.

O foco não é decorar o console: é produzir um ambiente pequeno, seguro, reproduzível, observável e com custo controlado.

## Pesquise estes nomes exatos

1. `Google Cloud resource hierarchy organization folder project`
2. `Google Cloud IAM least privilege predefined roles`
3. `Google Cloud service account impersonation short lived credentials`
4. `Cloud Storage uniform bucket level access public access prevention`
5. `gcloud storage buckets create location uniform bucket level access`
6. `Cloud Storage object versioning lifecycle management retention`
7. `gcloud storage cp checksum crc32c`
8. `Cloud Audit Logs Cloud Storage data access logs`
9. `Google Cloud budgets alerts cost controls`

## Conceitos essenciais

- **IAM:** define quem pode fazer qual ação em qual recurso.
- **Menor privilégio:** concede somente as ações necessárias, no menor escopo possível.
- **Service account:** identidade de uma carga de trabalho, não uma senha compartilhada.
- **Landing zone:** área controlada onde dados chegam antes de validação/processamento.
- **Lifecycle:** automatiza transição ou exclusão de objetos conforme idade e regra.

## Entrega obrigatória

Execute o laboratório descrito no [enunciado](<01-exercicios/ENUNCIADO.md>) e preencha `01-exercicios/roteiro_gcp.md` com comandos parametrizados, sem chaves. Registre provas redigidas e custos em [evidências](<03-evidencias/README.md>).

Os objetos aprovados serão carregados no BigQuery no N24 e orquestrados no N25.

## LinkedIn

Após demonstrar o ambiente e removê-lo corretamente, adicione: **Google Cloud Platform (GCP)**, **Cloud IAM** e **Google Cloud Storage**.

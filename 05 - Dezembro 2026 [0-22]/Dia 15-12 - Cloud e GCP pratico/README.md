# Conceitos de cloud para dados + GCP prático: IAM, service accounts e Cloud Storage

**Data de estudo:** 15/12/2026  
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Conceitos de cloud para dados

#### O que pesquisar
- `Conceitos de cloud para dados engenharia de dados e MLOps explicado passo a passo`
- `Conceitos de cloud para dados engenharia de dados e MLOps exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-conceitos-de-cloud-para-dados`](<atividades/01-conceitos-de-cloud-para-dados/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-conceitos-de-cloud-para-dados/dia-101-conceitos-de-cloud-para-dados.py`.
- **Entradas:** diagrama da API e tabela local de requisitos. **Fallback local:** mapeamento conceitual sem criar recurso.

#### O que você precisa entender

- **Definição:** IAM controla identidades e permissões; menor privilégio concede só o necessário; lock-in é custo de trocar fornecedor.
- **Exemplo mínimo:** mapeie “arquivo→objeto, API→serviço de container, segredo→cofre” em um provedor e limite leitura/escrita por recurso.
- **Erro comum:** usar credencial de administrador na aplicação ou comparar provedores apenas pelo nome do produto.

#### O que fazer

- [ ] Desenhe arquitetura cloud para ingestão, armazenamento, treino, registro e serving usando um provedor à escolha.
- [ ] Mapeie cada componente para AWS, Azure ou GCP sem tentar aprender os três.
- [ ] Defina IAM mínimo para cientista, pipeline e API.

- [ ] **Em `atividades/01-conceitos-de-cloud-para-dados/dia-101-conceitos-de-cloud-para-dados.py`:** compare a arquitetura para 10 GB e 1 TB por dia, registrando custo qualitativo, gargalos e riscos de disponibilidade.
- [ ] Retire a permissão de escrita da API no armazenamento bruto e explique qual operação permanece permitida pelo menor privilégio.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

### Atividade 2 — GCP prático: IAM, service accounts e Cloud Storage

#### O que pesquisar
- `GCP IAM least privilege`
- `service accounts`
- `Cloud Storage lifecycle`
- `GCP budget alerts`

**Arquivos da atividade:** [abrir a pasta `02-gcp-pratico-iam-service-accounts-e-cloud`](<atividades/02-gcp-pratico-iam-service-accounts-e-cloud/>)

#### Objetivo

Construir a entrada real do pipeline **Telecom Customer Intelligence** na Google Cloud. Você criará um bucket para eventos diários, separará dados brutos de arquivos rejeitados, configurará retenção/ciclo de vida e provará por teste positivo e negativo que uma service account tem apenas as permissões necessárias.

O foco não é decorar o console: é produzir um ambiente pequeno, seguro, reproduzível, observável e com custo controlado.

#### Termos complementares para pesquisar

1. `Google Cloud resource hierarchy organization folder project`
2. `Google Cloud IAM least privilege predefined roles`
3. `Google Cloud service account impersonation short lived credentials`
4. `Cloud Storage uniform bucket level access public access prevention`
5. `gcloud storage buckets create location uniform bucket level access`
6. `Cloud Storage object versioning lifecycle management retention`
7. `gcloud storage cp checksum crc32c`
8. `Cloud Audit Logs Cloud Storage data access logs`
9. `Google Cloud budgets alerts cost controls`

#### O que você precisa entender

- **IAM:** define quem pode fazer qual ação em qual recurso.
- **Menor privilégio:** concede somente as ações necessárias, no menor escopo possível.
- **Service account:** identidade de uma carga de trabalho, não uma senha compartilhada.
- **Landing zone:** área controlada onde dados chegam antes de validação/processamento.
- **Lifecycle:** automatiza transição ou exclusão de objetos conforme idade e regra.

#### O que fazer

Execute o laboratório descrito no [enunciado](<atividades/02-gcp-pratico-iam-service-accounts-e-cloud/ENUNCIADO.md>) e preencha `atividades/02-gcp-pratico-iam-service-accounts-e-cloud/roteiro_gcp.md` com comandos parametrizados, sem chaves. Registre provas redigidas e custos no próprio artefato.

Os objetos aprovados serão carregados na atividade de BigQuery e orquestrados pela atividade de Airflow real.

#### LinkedIn

Após demonstrar o ambiente e removê-lo corretamente, adicione: **Google Cloud Platform (GCP)**, **Cloud IAM** e **Google Cloud Storage**.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

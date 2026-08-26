# Problema e governanca + Dados e cohorts

**Data de estudo:** 21/01/2027
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Problema e governanca

#### O que pesquisar
- `Problema e governanca Python explicado passo a passo`
- `Problema e governanca Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-problema-e-governanca`](<atividades/01-problema-e-governanca/>)

#### Aulas complementares — privacidade, LGPD e vieses

- [ ] Segurança da Informação, Módulo 2 — **Lei Geral de Proteção de Dados (LGPD)** (19:48).
- [ ] Curso em Vídeo IA #39 — **Vieses em IA: Desvendando Preconceitos na IA** (13:56).
- Conecte as aulas às variáveis sensíveis e proibidas da atividade obrigatória. Elas não substituem a análise concreta do conjunto de dados e da decisão de crédito.

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-problema-e-governanca/dia-081-problema-e-governanca.ipynb`.
- **Dados:** `dados/credito.csv`.

#### O que você precisa entender

- **Definição:** label é o evento previsto; proxy é uma medida substituta; variável sensível representa grupo protegido; governança define uso, revisão e responsabilidade.
- **Exemplo mínimo:** documente “default = atraso ≥90 dias em 12 meses”, usuário da decisão, ação permitida e revisão humana.
- **Erro comum:** usar uma proxy sem validar seu significado ou excluir variável sensível e assumir que não há viés.

#### O que fazer

- [ ] Defina case de risco: prever default em 90 dias e apoiar aprovação, revisão ou rejeição.
- [ ] Liste variáveis proibidas, sensíveis ou potencialmente discriminatórias.
- [ ] Defina custos de falso negativo, falso positivo e revisão manual.

- [ ] Crie política de governança com responsável, frequência de revisão e trilha de auditoria.
- [ ] Escreva critérios de sucesso técnico, econômico e de equidade.


- [ ] **Em `atividades/01-problema-e-governanca/dia-081-problema-e-governanca.ipynb`:** Acrescente à política a regra de revisão humana para probabilidade entre 0,40 e 0,60 e calcule o volume dessa faixa.
- [ ] **Em `atividades/01-problema-e-governanca/dia-081-problema-e-governanca.ipynb`:** Liste quais colunas seriam removidas se contivessem atributo sensível ou uma proxy direta de renda familiar protegida.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

### Atividade 2 — Dados e cohorts

#### O que pesquisar
- `Dados e cohorts SQL para análise de dados explicado passo a passo`
- `Dados e cohorts SQL para análise de dados exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-dados-e-cohorts`](<atividades/02-dados-e-cohorts/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-dados-e-cohorts/dia-082-dados-e-cohorts.ipynb`.
- **Dados:** `dados/credito.csv`.

#### O que você precisa entender

- **Definição:** cohort agrupa entidades por um evento de origem comum; cada período mede a mesma distância desde esse evento.
- **Exemplo mínimo:** cohort = mês da primeira concessão; P1, P2 e P3 = primeiro, segundo e terceiro mês completos após a concessão.
- **Erro comum:** misturar mês-calendário com idade da cohort ou incluir informação não disponível no corte.

#### O que fazer

- [ ] Carregue `credito.csv`, faça qualidade e EDA da taxa de default.
- [ ] Crie cohorts por mês de concessão e acompanhe default P1/P2/P3 quando possível.
- [ ] Analise default por faixas de renda, dívida, atrasos e tempo de emprego.

- [ ] Valide estabilidade temporal das variáveis.
- [ ] Crie dicionário de features e regras de exclusão.


- [ ] **Em `atividades/02-dados-e-cohorts/dia-082-dados-e-cohorts.ipynb`:** Compare default para renda abaixo de R$3.000 e acima de R$8.000, informando também o tamanho dos grupos.
- [ ] **Em `atividades/02-dados-e-cohorts/dia-082-dados-e-cohorts.ipynb`:** Separe os últimos três meses de concessão e compare a distribuição das cinco principais variáveis com o período anterior.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

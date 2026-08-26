# Definicao do produto integrador + Dados, SQL e arquitetura

**Data de estudo:** 29/03/2027
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — Definicao do produto integrador

#### O que pesquisar
- `Definicao do produto integrador Python explicado passo a passo`
- `Definicao do produto integrador Python exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `01-definicao-do-produto`](<atividades/01-definicao-do-produto/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-definicao-do-produto/dia-116-definicao-do-produto-integrador.ipynb`.
- **Entradas:** escolha `dados/clientes_telecom.csv`, `dados/pedidos.csv` ou `projetos/assistente-suporte-ia/data/corpus/`. **Fallback local:** fixture versionada.

#### Manifesto de entradas

- **Obrigatórias:** opções de produto, dados locais permitidos e restrições em `product_brief.md`.
- **Fallback local:** use uma fixture pequena versionada quando a fonte externa não estiver disponível.

#### O que você precisa entender

- **Definição:** MoSCoW separa Must, Should, Could e Won't; Must é indispensável ao valor e à demonstração.
- **Exemplo mínimo:** “entrada validada” e “decisão reproduzível” são Must; tema visual extra é Could; integração sem dados é Won't.
- **Erro comum:** classificar tudo como Must ou priorizar pela tecnologia mais interessante.

#### O que fazer

- [ ] Escolha um produto integrador entre churn, crédito, forecasting ou RAG e defina usuário, decisão e valor.
- [ ] Escreva escopo de cinco dias com backlog priorizado MoSCoW.
- [ ] Desenhe arquitetura e fluxo de dados.

- [ ] **Em `atividades/01-definicao-do-produto/dia-116-definicao-do-produto-integrador.ipynb`:** defina uma métrica técnica, uma de negócio e uma de experiência; acrescente ao backlog um caso de usuário com entrada incompleta e classifique-o como Must, Should, Could ou Won't.
- [ ] **Em `atividades/01-definicao-do-produto/dia-116-definicao-do-produto-integrador.ipynb`:** Reduza o prazo de cinco para três dias e registre quais dois itens serão cortados sem remover o valor principal.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

### Atividade 2 — Dados, SQL e arquitetura

#### O que pesquisar
- `Dados, SQL e arquitetura SQL para análise de dados explicado passo a passo`
- `Dados, SQL e arquitetura SQL para análise de dados exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-dados-sql-e-arquitetura`](<atividades/02-dados-sql-e-arquitetura/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-dados-sql-e-arquitetura/dia-117-dados-sql-e-arquitetura.ipynb`.
- **Entradas:** `product_brief.md`, fonte escolhida e schema. **Fallback local:** DuckDB e fixture válida/nula/duplicada.

#### Manifesto de entradas

- **Obrigatórias:** `product_brief.md`, dataset local, schema e chave de negócio.
- **Fallback local:** use fixture com casos válido, nulo e duplicado; registre que é amostra de desenvolvimento.

#### O que você precisa entender

- **Definição:** contrato de arquitetura fixa fonte, schema, granularidade, transformação e consumidor; cada tipo de produto pede um fluxo coerente.
- **Exemplo mínimo:** preditivo: tabela→features→modelo; forecasting: série→cortes→previsão; analítico: SQL→métrica→painel; RAG: corpus→índice→resposta avaliada.
- **Erro comum:** exigir SQL, API ou modelo quando não servem à decisão escolhida.

#### O que fazer

- [ ] Crie ou revise esquema SQL e pipeline de formação da base.
- [ ] Adicione testes de qualidade e dicionário.
- [ ] Desenhe arquitetura de execução e deploy.

- [ ] **Em `atividades/02-dados-sql-e-arquitetura/dia-117-dados-sql-e-arquitetura.ipynb`:** Remova cliente_id de uma cópia da entrada e faça a checagem de qualidade impedir a formação da base.
- [ ] **Em `atividades/02-dados-sql-e-arquitetura/dia-117-dados-sql-e-arquitetura.ipynb`:** documente uma única instrução de reprodução, execute-a duas vezes e confirme que a segunda execução não duplica linhas nem artefatos.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

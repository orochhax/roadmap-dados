# ETL-ELT e arquitetura basica + Pipeline em Python

**Data de estudo:** 01/12/2026  
**Carga planejada:** 4 a 5 horas

## Atividades do dia

### Atividade 1 — ETL-ELT e arquitetura basica

#### O que pesquisar
- `ETL-ELT e arquitetura basica engenharia de dados e MLOps explicado passo a passo`
- `ETL-ELT e arquitetura basica engenharia de dados e MLOps exercícios práticos`

#### Aula guiada — projeto de engenharia de dados (parte 1)

- [ ] Assista a [**Engenharia de Dados para INICIANTES | Projeto Completo Explicado do ZERO**](https://www.youtube.com/watch?v=I8qPqbXQBDU), de `00:00:00` a `00:47:31` (47min31s).
- Nesta primeira parte, acompanhe requisitos, estrutura do projeto, variáveis de ambiente, extração, transformação, carga e o primeiro teste do ETL.
- Use a aula para reconhecer o fluxo completo; a entrega obrigatória continua sendo o pipeline próprio abaixo, com dados locais, validação, logs e prova de idempotência.

**Arquivos da atividade:** [abrir a pasta `01-etl-elt-e-arquitetura-basica`](<atividades/01-etl-elt-e-arquitetura-basica/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/01-etl-elt-e-arquitetura-basica/dia-086-etl-elt-e-arquitetura-basica.py`.
- **Entradas:** `dados/pedidos.csv` e schema criado nesta sessão. **Fallback local:** amostra fixa de 50 linhas.

#### O que você precisa entender

- **Definição:** ETL transforma antes de carregar; ELT transforma no destino. Camadas raw, processed e curated separam original, limpeza e produto analítico.
- **Exemplo mínimo:** `raw/pedidos.csv → processed/pedidos.parquet → curated/vendas_mensais.parquet`, cada etapa com schema.
- **Erro comum:** sobrescrever o dado bruto ou não declarar a granularidade de cada camada.

#### O que fazer

- [ ] Desenhe arquitetura simples: fontes CSV/API → camada raw → transformação → camada curated → consumo por BI/modelo.
- [ ] Explique ETL versus ELT com o mesmo exemplo e escolha uma abordagem.
- [ ] Defina contratos de dados para incidentes e clientes: campos, tipos, chave e frequência.

- [ ] Crie estrutura de pastas `raw`, `processed`, `curated` e regras de nomenclatura.
- [ ] Liste cinco falhas possíveis e como detectar cada uma.


- [ ] **Em `atividades/01-etl-elt-e-arquitetura-basica/dia-086-etl-elt-e-arquitetura-basica.py`:** Adicione à arquitetura uma área quarantine entre raw e processed para linhas sem id ou com tipo inválido.
- [ ] **Em `atividades/01-etl-elt-e-arquitetura-basica/dia-086-etl-elt-e-arquitetura-basica.py`:** Simule ausência da coluna id e uma execução repetida; descreva em qual etapa cada problema deve ser detectado.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

### Atividade 2 — Pipeline em Python

#### O que pesquisar
- `Pipeline em Python engenharia de dados e MLOps explicado passo a passo`
- `Pipeline em Python engenharia de dados e MLOps exercícios práticos`

**Arquivos da atividade:** [abrir a pasta `02-pipeline-em-python`](<atividades/02-pipeline-em-python/>)

#### Arquivos e dados

- **Pasta/arquivo principal:** `atividades/02-pipeline-em-python/transform.py`.
- **Entradas:** `dados/pedidos.csv`, schema e `atividades/02-pipeline-em-python/config.yaml`. **Fallback local:** Parquet ou DuckDB.

#### O que você precisa entender

- **Definição:** idempotência significa que a mesma entrada produz o mesmo estado; configuração separa parâmetros; log registra evento, tempo e contexto.
- **Exemplo mínimo:** leia CSV, valide schema, grave Parquet/DuckDB e execute duas vezes; contagem e chaves não podem duplicar.
- **Erro comum:** usar append sem chave de execução ou esconder caminhos dentro do código.

#### O que fazer

- [ ] Implemente `extract.py` para ler CSV/JSON, `transform.py` para limpar e criar features, e `load.py` para gravar Parquet ou DuckDB.
- [ ] Use arquivo de configuração para caminhos, sem valores fixos no código.
- [ ] Adicione logs com quantidade lida, rejeitada e gravada.

- [ ] Teste arquivo ausente, coluna faltante e linha inválida; registre a falha esperada e a observada.


- [ ] **Em `atividades/02-pipeline-em-python/transform.py`:** Adicione validação obrigatória das colunas cliente_id e data_ativacao antes da transformação.
- [ ] **Em `atividades/02-pipeline-em-python/transform.py`:** Execute duas vezes com o mesmo arquivo e depois com uma linha nova; compare contagens para provar idempotência e incremento.

#### Como validar

- Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.

## Finalização

- [ ] Dia concluído: atividades executadas, critérios atendidos e conteúdo explicado com minhas palavras.

# ETL/ELT e arquitetura básica

## Preparação
- **Pasta/arquivo principal:** `01-exercicios/dia-086-etl-elt-e-arquitetura-basica.py`.
- **Entradas:** `dados/pedidos.csv` e schema criado nesta sessão. **Fallback local:** amostra fixa de 50 linhas.

## Aprenda agora

- **Definição:** ETL transforma antes de carregar; ELT transforma no destino. Camadas raw, processed e curated separam original, limpeza e produto analítico.
- **Exemplo mínimo:** `raw/pedidos.csv → processed/pedidos.parquet → curated/vendas_mensais.parquet`, cada etapa com schema.
- **Erro comum:** sobrescrever o dado bruto ou não declarar a granularidade de cada camada.

## Núcleo essencial

1. [ ] Desenhe arquitetura simples: fontes CSV/API → camada raw → transformação → camada curated → consumo por BI/modelo.
2. [ ] Explique ETL versus ELT com o mesmo exemplo e escolha uma abordagem.
3. [ ] Defina contratos de dados para incidentes e clientes: campos, tipos, chave e frequência.

## Prática obrigatória

- [ ] Crie estrutura de pastas `raw`, `processed`, `curated` e regras de nomenclatura.
- [ ] Liste cinco falhas possíveis e como detectar cada uma.

## Prática obrigatória — adaptação e verificação

- [ ] **Em `01-exercicios/dia-086-etl-elt-e-arquitetura-basica.py`:** Adicione à arquitetura uma área quarantine entre raw e processed para linhas sem id ou com tipo inválido.
- [ ] **Em `01-exercicios/dia-086-etl-elt-e-arquitetura-basica.py`:** Simule ausência da coluna id e uma execução repetida; descreva em qual etapa cada problema deve ser detectado.

## Concluído quando

- [ ] O núcleo foi executado e `01-exercicios/dia-086-etl-elt-e-arquitetura-basica.py` contém todas as saídas obrigatórias.
- [ ] Uma verificação controlada registra entrada, resultado esperado e resultado observado.
- [ ] A entrega documenta a decisão tomada, a evidência que a sustenta e uma limitação concreta.
